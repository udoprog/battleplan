import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from battleplan.lib.base import BaseController, render
from battleplan.lib import eveapi
from battleplan.lib.decorators import validate
from battleplan.lib.validator import String

log = logging.getLogger(__name__)

class AuthController(BaseController):
    required_auth = False
    default_path = "index"

    def signout(self):
        del session["user"]
        session.save()
        return redirect(url(self.default_path))
    
    @validate('name', String(),
        'api_userid', String(),
        'api_key', String())
    def do_signin(self):
        path_before_login = session.pop("path_before_login", self.default_path)
        
        api = eveapi.EVEAPIConnection()
        auth = api.auth(userID=c.api_userid, apiKey=c.api_key)
        
        def check_character():
            try:
                result = auth.account.Characters()
            except eveapi.Error, e:
                c.errors.add(e.args[0])
                return False

            for char in result.characters:
                if char.name == c.name:
                    return True
            return False

        if not check_character():
            return self.signin()
        
        session["user"] = "test"
        session.save()
        return redirect(url(path_before_login))

    @validate(
        'name', String(default=""),
        'api_userid', String(default=""),
        'api_key', String(default=""))
    def signin(self):
        if not c.name: c.name = c.eve.char_name;
        c.path_before_login = session.get("path_before_login", self.default_path)
        return render('/auth/signin.mako')
