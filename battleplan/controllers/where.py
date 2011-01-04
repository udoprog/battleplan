import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from battleplan.lib.base import BaseController, render
from battleplan.lib import find_route, systems
from battleplan import model

log = logging.getLogger(__name__)

class WhereController(BaseController):
    def __before__(self):
        if c.eve.trusted:
            c.ss = model.Session.query(model.SolarSystem).filter_by(solarSystemName=c.eve.solarsystem_name).first()
        else:
            c.ss = model.Session.query(model.SolarSystem).filter_by(solarSystemName=c.eve.solarsystem_name).first()
        
        if not c.ss:
            abort(400)

    def index(self):
        # Return a rendered template
        #return render('/where.mako')
        # or, return a string
        return render('/where.mako')

    def travel(self):
        query = request.GET.get("q", "None")

        try:
            c.ts = model.Session.query(model.SolarSystem).filter(solarSystemID=int(query)).first()
        except:
            pass
        
        if not hasattr(c, "ts"):
            c.ts = model.Session.query(model.SolarSystem).filter(model.SolarSystem.solarSystemName.like(query + "%")).first()
        
        if c.ts:
            c.route = list(find_route(c.ss, c.ts))
            c.systems = systems
            return render('/travel.mako')
        
        return "Travel to " + str(c.ts);
