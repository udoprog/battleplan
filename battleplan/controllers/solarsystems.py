import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
from webhelpers import paginate

from battleplan.lib.base import BaseController, render
from battleplan import model as m
from battleplan.lib.decorators import validate
from battleplan.lib.validator import Integer, String

log = logging.getLogger(__name__)

class SolarsystemsController(BaseController):
    """REST Controller styled on the Atom Publishing Protocol"""
    # To properly map this controller, ensure your config/routing.py
    # file has a resource setup:
    #     map.resource('solarsystem', 'solarsystems')

    @validate(
        "page", Integer(default=0, max=None),
        "c", Integer(default=25, min=10, max=100),
        "q", String(optional=True)
    )
    def index(self, format='html'):
        """GET /solarsystems: All items in the collection"""
        # url('solarsystems')
        c.solarsystems = m.Session.query(m.SolarSystem).order_by(m.SolarSystem.solarSystemName)
        if c.q:
            c.solarsystems = c.solarsystems.filter(m.SolarSystem.solarSystemName.like(c.q + "%"))
        c.page = paginate.Page(c.solarsystems, page=c.page, items_per_page=c.c, c=c.c, q=c.q)
        return render("/solarsystems/index.mako")

    @validate("q", String())
    def filter_solarsystems(self):
        if not c.q:
            return redirect(url.current(action="index"))
        return redirect(url.current(action="index", q=c.q))

    def create(self):
        """POST /solarsystems: Create a new item"""
        # url('solarsystems')

    def new(self, format='html'):
        """GET /solarsystems/new: Form to create a new item"""
        # url('new_solarsystem')

    def update(self, id):
        """PUT /solarsystems/id: Update an existing item"""
        # Forms posted to this method should contain a hidden field:
        #    <input type="hidden" name="_method" value="PUT" />
        # Or using helpers:
        #    h.form(url('solarsystem', id=ID),
        #           method='put')
        # url('solarsystem', id=ID)

    def delete(self, id):
        """DELETE /solarsystems/id: Delete an existing item"""
        # Forms posted to this method should contain a hidden field:
        #    <input type="hidden" name="_method" value="DELETE" />
        # Or using helpers:
        #    h.form(url('solarsystem', id=ID),
        #           method='delete')
        # url('solarsystem', id=ID)

    def show(self, id, format='html'):
        """GET /solarsystems/id: Show a specific item"""
        if id == "current" and c.eve.trusted:
            c.solarsystem = m.SolarSystem.by_name(c.eve.solarsystem_name).first()
            if c.solarsystem:
                return redirect(url.current(id=c.solarsystem.solarSystemID))
        
        c.solarsystem = m.SolarSystem.get(id).first()
        
        if not c.solarsystem:
            abort(404)
        
        c.reports = m.Report.by_solarsystem(c.solarsystem).all()
        return render('/solarsystems/show.mako')
        # url('solarsystem', id=ID)

    def edit(self, id, format='html'):
        """GET /solarsystems/id/edit: Form to edit an existing item"""
        # url('edit_solarsystem', id=ID)
