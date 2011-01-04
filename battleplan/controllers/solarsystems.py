import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from battleplan.lib.base import BaseController, render
from battleplan import model as m

log = logging.getLogger(__name__)

class SolarsystemsController(BaseController):
    """REST Controller styled on the Atom Publishing Protocol"""
    # To properly map this controller, ensure your config/routing.py
    # file has a resource setup:
    #     map.resource('solarsystem', 'solarsystems')

    def index(self, format='html'):
        """GET /solarsystems: All items in the collection"""
        # url('solarsystems')

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
        c.solarsystem = m.SolarSystem.get(id).first()
        if not c.solarsystem:
            abort(404)
        
        c.reports = m.Report.by_solarsystem(c.solarsystem).all()
        return render('/solarsystems/show.mako')
        # url('solarsystem', id=ID)

    def edit(self, id, format='html'):
        """GET /solarsystems/id/edit: Form to edit an existing item"""
        # url('edit_solarsystem', id=ID)
