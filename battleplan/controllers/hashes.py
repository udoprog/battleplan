import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
from webhelpers import paginate

from battleplan.lib.base import BaseController, render
from battleplan import model as m
from battleplan.lib.decorators import validate
from battleplan.lib.validator import Integer, String

log = logging.getLogger(__name__)

class HashesController(BaseController):
    auth_required = True
    """REST Controller styled on the Atom Publishing Protocol"""
    # To properly map this controller, ensure your config/routing.py
    # file has a resource setup:
    #     map.resource('hash', 'hashes')

    @validate(
        "page", Integer(default=0, max=None),
        "c", Integer(default=25, min=10, max=100),
        "q", String(optional=True)
    )
    def index(self, format='html'):
        """GET /hashes: All items in the collection"""
        # url('hashes')
        c.hashes = m.Session.query(m.Hash)
        if c.q:
            c.hashes = c.hashes.filter(m.Hash.name.like(c.q + "%"))
        c.page = paginate.Page(c.hashes, page=c.page, items_per_page=c.c, c=c.c)
        return render("/hashes/index.mako")

    @validate("q", String())
    def filter_hashes(self):
        return redirect(url.current(action="index", q=c.q))

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
        hash = m.Hash.get(id).first()
        if not hash:
            return redirect(url('hashes'))
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
