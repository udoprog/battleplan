import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from battleplan.lib.base import BaseController, render
from battleplan import model as m

log = logging.getLogger(__name__)

class HashesController(BaseController):
    """REST Controller styled on the Atom Publishing Protocol"""
    # To properly map this controller, ensure your config/routing.py
    # file has a resource setup:
    #     map.resource('hash', 'hashes')

    def index(self, format='html'):
        """GET /hashes: All items in the collection"""
        # url('hashes')

    def create(self):
        """POST /hashes: Create a new item"""
        # url('hashes')

    def new(self, format='html'):
        """GET /hashes/new: Form to create a new item"""
        # url('new_hash')

    def update(self, id):
        """PUT /hashes/id: Update an existing item"""
        # Forms posted to this method should contain a hidden field:
        #    <input type="hidden" name="_method" value="PUT" />
        # Or using helpers:
        #    h.form(url('hash', id=ID),
        #           method='put')
        # url('hash', id=ID)

    def delete(self, id):
        """DELETE /hashes/id: Delete an existing item"""
        # Forms posted to this method should contain a hidden field:
        #    <input type="hidden" name="_method" value="DELETE" />
        # Or using helpers:
        #    h.form(url('hash', id=ID),
        #           method='delete')
        # url('hash', id=ID)

    def show(self, id, format='html'):
        """GET /hashes/id: Show a specific item"""
        # url('hash', id=ID)
        c.hash = m.Hash.get(id).first()
        if not c.hash:
            c.hash = m.Hash.by_name(id).first()
        if not c.hash:
            return abort(404)

        return render('/hashes/show.mako')

    def edit(self, id, format='html'):
        """GET /hashes/id/edit: Form to edit an existing item"""
        # url('edit_hash', id=ID)
