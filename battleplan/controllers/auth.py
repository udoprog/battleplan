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
        session.pop("user", None)
        session.pop("corp", None)
        session.save()
        return redirect(url(self.default_path))
    
    @validate('name', String(),
        'api_userid', String(),
        'api_key', String())
    def do_signin(self):
        path_before_login = session.pop("path_before_login", self.default_path)
        
#        api = eveapi.EVEAPIConnection()
#        auth = api.auth(userID=c.api_userid, apiKey=c.api_key)
#        
#        def check_character(name):
#            try:
#                result = auth.account.Characters()
#            except eveapi.Error, e:
#                c.errors.add(e.args[0])
#                return None
#
#            for char in result.characters:
#                if char.name == name:
#                    return char
#            return None
#        
#        def get_corp(char):
#            try:
#                result = auth.corp.CorporationSheet(characterID=char.characterID)
#            except eveapi.Error, e:
#                c.errors.add(e.args[0])
#                return None
#            
#            return result
#        
#        char = check_character(c.name);
#
#        if not char:
#            return self.signin()
#        
#        corp = get_corp(char)
#        
#        if not corp:
#            return self.signin()
#        
#        g = self._py_object.app_globals
#
#        if corp.allianceName not in g.alliances:
#            return self.signin()
#        
        session["user"] = c.name
        session["corp"] = "NOALL"
        session.save()
        return redirect(url(path_before_login))

    @validate(
        'name', String(default=""),
        'api_userid', String(default=""),
        'api_key', String(default=""))
    def signin(self):
        c.alliances = self._py_object.app_globals.alliances
        if not c.name: c.name = c.eve.char_name;
        c.path_before_login = session.get("path_before_login", self.default_path)
        return render('/auth/signin.mako')
