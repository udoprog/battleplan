import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from battleplan.lib.base import BaseController, render

log = logging.getLogger(__name__)

class MainController(BaseController):
    required_auth = False

    def index(self):
        return render('/main/index.mako')

    def help(self):
        return render('/main/help.mako')
