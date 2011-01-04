systems=dict()
system_names=list()
jumps=dict()

def rec_find_route(fr, to, avoid, sec_low, sec_high):
    if fr in avoid or to in avoid: return
    if fr == to: return
    
    queue = list([fr])
    visited = set()
    prev = dict()
    
    while len(queue) > 0:
        f = queue.pop()
        visited.add(f)
        
        if f == to:
            res=list()
            while prev[f] != fr:
                yield((prev[f], f))
                f = prev[f]
            yield((fr, f))
            return
        
        for s in jumps[f]:
            if s in visited: continue
            if s in avoid: continue
            if sec_low is not None and systems[s].security < sec_low: continue
            if sec_high is not None and systems[s].security > sec_high: continue
            prev[s] = f
            queue.insert(0, s)

def find_route(fr, to, avoid=[], sec_low=None, sec_high=None):
    stack = list(rec_find_route(fr.solarSystemID, to.solarSystemID, set(avoid), sec_low, sec_high))
    stack.reverse()
    
    if len(stack) == 0:
        return
    
    for fr, to in stack:
        yield((systems[fr], systems[to]))
