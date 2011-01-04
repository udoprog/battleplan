from pylons import request, response, session
from pylons.controllers.util import abort, redirect

def get(required=[]):
    def inner(func):
        def wrapper(self, *args, **kw):
            for r in required:
                if r not in request.GET:
                    abort(400)
            return func(self, *args)
        return wrapper
    return inner

def params(required=[]):
    def inner(func):
        def wrapper(self, *args, **kw):
            for r in required:
                if r not in request.params:
                    abort(400)
            return func(self, *args)
        return wrapper
    return inner
