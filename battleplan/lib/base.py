"""The base Controller API

Provides the BaseController class for subclassing.
"""
from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers import WSGIController
from pylons.controllers.util import abort, redirect
from pylons.templating import render_mako as render

from battleplan.model.meta import Session
from battleplan.lib.error import ErrorDict

class BaseController(WSGIController):
    required_auth = True

    def __before__(self):
        c.user = None

        if self.required_auth:
            if 'user' not in session:
                session['path_before_login'] = request.path_info
                session.save()
                return redirect(url("auth_signin"))
        
        if "user" in session:
            c.user = session["user"]

    def __call__(self, environ, start_response):
        """Invoke the Controller"""
        # WSGIController.__call__ dispatches to the Controller method
        # the request is routed to. This routing information is
        # available in environ['pylons.routes_dict']
        py_object = environ['pylons.pylons']
        py_object.tmpl_context.errors = ErrorDict();
        py_object.tmpl_context.eve = environ["eve"]
        
        try:
            return WSGIController.__call__(self, environ, start_response)
        finally:
            Session.remove()
