import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from battleplan.lib.base import BaseController, render
from battleplan.lib import find_route, system_names
from battleplan.lib.decorators import get
from battleplan import model as m

log = logging.getLogger(__name__)

class TravelController(BaseController):
    def _get_system(self, system_name):
        q = m.Session.query(m.SolarSystem);
        return q.filter_by(solarSystemName=system_name).first()
    
    def index(self):
        return render('/travel/index.mako')

    @get(required=["to", "fr"])
    def plot(self):
        c.from_system = self._get_system(request.GET.get("fr"))
        c.to_system = self._get_system(request.GET.get("to"))
        c.avoid = list()
        c.systems = system_names
        
        for a in request.GET.get("avoid", "").split(","):
            s = self._get_system(a)
            if not s: continue
            c.avoid.append(s.solarSystemID)

        c.sec_low = None
        c.sec_high = None

        if "lowest" in request.GET:
            try:
                c.sec_low = float(request.GET.get("lowest"))
            finally:
                pass
        
        if "highest" in request.GET:
            try:
                c.sec_high = float(request.GET.get("highest"))
            finally:
                pass
        
        if c.from_system and c.to_system:
            c.route = list(find_route(c.from_system, c.to_system, c.avoid, c.sec_low, c.sec_high))
            c.no_route = (len(c.route) == 0)
        else:
            c.route = []
            c.no_route = True

        return render('/travel/plot.mako')
