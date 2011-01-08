from pylons.controllers.util import abort, redirect

import logging

log = logging.getLogger(__name__)

def get(required=[]):
    def inner(func):
        def wrapper(self, *args, **kw):
            request = self._py_object.request;
            
            for r in required:
                if r not in request.GET:
                    abort(400)
            return func(self, *args)
        return wrapper
    return inner

def params(required=[]):
    def inner(func):
        def wrapper(self, *args, **kw):
            request = self._py_object.request;
            
            for r in required:
                if r not in request.params:
                    abort(400)
            return func(self, *args)
        return wrapper
    return inner


def validate(*vals, **kw):
    if len(vals) % 2 != 0: raise ValueError, "All validators must come in a key, callable pair"
    if len(vals) == 0: raise ValueError, "No validators defined"

    for i in range(0, len(vals), 2):
        key, val = vals[i], vals[i+1]
        if not hasattr(val, "__call__"): raise ValueError, i + ": validator must be callable"
    
    error = kw.get("error", None)
    
    def inner(func):
        def wrapper(self, *args, **kw):
            request = self._py_object.request;
            c = self._py_object.tmpl_context;

            verr = False
            vkeys = list()

            for i in range(0, len(vals), 2):
                key, val = vals[i], vals[i+1]
                try: setattr(c, key, val.__call__(request.params.get(key, None)))
                except ValueError, e:
                    setattr(c.errors, key, str(e))
                    setattr(c, key, request.params.get(key, None))
                    verr = True
                    vkeys.append(key)
            
            if verr:
                if error: return error(self, vkeys)
                else: return abort(404)
            
            return func(self, *args)
        return wrapper
    return inner
