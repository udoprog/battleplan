import Queue as queue
import logging
import types

import threading
import time

log = logging.getLogger("scheduler")

class CallBase:
    def __init__(self):
        self.callbacks = list()
    
    def callback(self, callback):
        self.callbacks.append(callback)
        return self
    
    def _give_all(self, r):
        for c in self.callbacks: c.__call__(r)

class CallTask(CallBase):
    def __init__(self, target, *args):
        CallBase.__init__(self)
        if not hasattr(target, '__call__'): raise ValueError, "target must be callable"
        self.target = target
        self.args = args
    
    def run(self):
        r = self.target.__call__(*self.args)
        self._give_all(r)
        return False
    
    def exit(self):
        log.info("Terminating task " + str(self))

class GenTask(CallBase):
    def __init__(self, target, *args):
        CallBase.__init__(self)
        if not hasattr(target, '__call__'): raise ValueError, "target must be callable"
        target = target.__call__(*args)
        if not isinstance(target, types.GeneratorType): raise ValueError, "target callable must be a generator"
        self.target = target
        self.sendval = None
    
    def run(self):
        try:
            r = self.target.send(self.sendval)
        except StopIteration:
            return False
        self._give_all(r)
        return True
    
    def exit(self):
        log.info("Terminating task " + str(self))

class Scheduler:
    def __init__(self):
        self.queue = queue.Queue()
        self.running = True
    
    def schedule(self, task):
        self.queue.put(task)

    def shutdown(self):
        self.running = False

    def _run(self):
        if not self.running:
            if self.queue.empty(): return False
        
        t = self.queue.get()
        log.info("Running task " + str(t))
        
        if not t.run():
            t.exit()
        else:
            #re-schedule the task
            self.schedule(t)
        
        return True
    
    def mainloop(self):
        log.info("Entering mainloop")
        while self._run(): pass
        log.info("Exiting mainloop")

class ThreadedScheduler(threading.Thread, Scheduler):
    def __init__(self):
        threading.Thread.__init__(self)
        Scheduler.__init__(self)

    def run(self):
        self.mainloop()

#logging.basicConfig(level=logging.DEBUG)

ts = ThreadedScheduler()

def test(start):
    for i in xrange(start):
        yield i 

def test2(ret):
    return ret

def result(r):
    print(r)

ts.schedule(GenTask(test, 100000).callback(result))
ts.schedule(CallTask(test2, 13).callback(result))

ts.start()
ts.shutdown()
ts.join()
