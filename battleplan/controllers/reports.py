import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
from pylons.decorators import jsonify

from battleplan.lib import helpers as h
from battleplan.lib.base import BaseController, render
from battleplan.lib.decorators import validate
from battleplan.lib.validator import String, Integer
from battleplan.lib import reports
from battleplan import model as m

log = logging.getLogger(__name__)

class SolarSystem:
    def __init__(self, optional=False, by_id=False):
        self.optional = optional
        self.by_id = by_id

    def _handle_missing(self):
        if self.optional: return None
        raise ValueError
    
    def __call__(self, value):
        if value is None: return self._handle_missing()
        if self.by_id: solarSystem = m.SolarSystem.get(value).first()
        else: solarSystem = m.SolarSystem.by_name(value).first()
        if not solarSystem: raise ValueError, "No such solar system '" + value + "'"
        return solarSystem

class Hash:
    def __init__(self, optional=False):
        self.optional = optional

    def _handle_missing(self):
        if self.optional: return None
        raise ValueError
    
    def __call__(self, value):
        if value is None: return self._handle_missing()
        hash = m.Hash.get(value).first()
        if not hash: raise ValueError, "No such hash '" + value + "'"
        return hash

class ReportsController(BaseController):
    required_auth = True
    
    def index(self):
        c.reports = m.Report.by_created().limit(25).all()
        return render('/reports/index.mako')

    def _bad_param(self, keys):
        return {'error': "Missing/invalid parameters '" + ",".join(keys) + "'", 'result': []}
    
    @jsonify
    @validate(
        "limit", Integer(0, 25),
        "offset", Integer(0, optional=True),
        "hash", Hash(optional=True),
        "solarsystem", SolarSystem(optional=True, by_id=True),
        error=_bad_param)
    def latest_reports(self):
        q = m.Report.by_created()
        
        if c.hash:
            q = q.filter(m.Report.hashes.contains(c.hash))

        if c.solarsystem:
            q = q.filter(m.Report.solarSystem == c.solarsystem)
        
        q = q.limit(c.limit).offset(c.offset)
        return {'result': [r.to_json() for r in q.all()], 'error': ""}

    @jsonify
    @validate(
        "latest_id", String(optional=True),
        "hash", Hash(optional=True),
        "solarsystem", SolarSystem(optional=True, by_id=True),
        error=_bad_param)
    def latest_check(self):
        q = m.Report.by_created()
        
        if c.hash:
            q = q.filter(m.Report.hashes.contains(c.hash))
        
        if c.solarsystem:
            q = q.filter(m.Report.solarSystem == c.solarsystem)
        
        r = q.first()

        if r is None:
            return {'result': False, 'error': ""}
        
        if c.latest_id:
            return {'result': r.id.hex != c.latest_id, 'error': ""}
        else:
            return {'result': True, 'error': ""}
    
    def show(self, id):
        c.report = m.Report.get(id).first();

        if not c.report:
            return abort(404)

        c.text = ""
        
        for t,p in reports.tokenize_report(c.report.text):
            if t == reports.Map:
                s = m.SolarSystem.by_name(p).first()
                if not s:
                    c.text += "[no such system '" + p + "']"
                else:
                    c.text += h.link_to(s.solarSystemName, url('solarsystem',id=s.solarSystemID))
            elif t == reports.Hash:
                c.text += h.link_to("#" + p, url('hash', id=p))
            else:
                c.text += p
        
        return render('/reports/show.mako')
    
    @validate(
        "solarSystem", SolarSystem(optional=True),
        "text", String(default=""),
        "title", String(default=""),
        "priority", Integer(default=0)
    )
    def new(self):
        if not c.solarSystem:
            c.solarSystem = ""
        else:
            c.solarSystem = c.solarSystem.solarSystemName

        return render('/reports/new.mako')

    def _create_error(self, keys):
        if not c.solarSystem:
            c.solarSystem = ""
        if isinstance(c.solarSystem, m.SolarSystem):
            c.solarSystem = c.solarSystem.solarSystemName
        
        return render('/reports/new.mako')
        
    def _strip_uc(s):
        import re
        s = re.sub("[^\w &]", "", s)
        return re.sub("\s+", " ", s).strip().upper()

    #just checking to see if I can see this
    
    @validate(
        "solarSystem", SolarSystem(),
        "text", String(empty=False),
        "title", String(empty=False, filter=_strip_uc),
        "priority", Integer(0,5),
    error=_create_error)
    def create(self):
        report = m.Report()
        
        for t,p in reports.tokenize_report(c.text):
            if t == reports.Map:
                # just ignore this for now, it will resolve itself up there ^
                pass
            elif t == reports.Hash:
                hash = m.Hash.by_name(p).first()
                if not hash:
                    hash = m.Hash()
                    hash.name = p
                    m.Session.add(hash)
                hash.reports.append(report)
        
        report.solarSystemID=c.solarSystem.solarSystemID
        
        report.title=c.title
        report.text=c.text
        report.priority=c.priority
        
        m.Session.add(report)
        m.Session.commit()
        
        return redirect(url.current())
