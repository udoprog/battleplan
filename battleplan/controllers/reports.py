import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from battleplan.lib.base import BaseController, render
from battleplan.lib.decorators import params
from battleplan import model as m

log = logging.getLogger(__name__)

class ReportsController(BaseController):
    def __before__(self):
        if not session.has_key("user"):
            session["user"] = "Udo Prog"

    def index(self):
        c.reports = m.Session.query(m.Report).order_by(m.Report.created.desc()).limit(10).all()
        return render('/reports/index.mako')

    def new(self):
        # Return a rendered template
        #return render('/intel.mako')
        # or, return a string
        return render('/reports/new.mako')

    @params(required=["text", "solarSystemName"])
    def create(self):
        text = request.params.get("text")
        solarSystemName = request.params.get("solarSystemName")
        
        solarSystem = m.SolarSystem.by_name(solarSystemName).first()
        
        if not solarSystem:
            abort(400)
        
        report = m.Report()
        report.solarSystemID=solarSystem.solarSystemID
        report.text=text
        
        m.Session.add(report)
        m.Session.commit()
        
        return redirect(url.current())
