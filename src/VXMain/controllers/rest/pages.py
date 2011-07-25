import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from VXMain.lib.base import BaseController, render

log = logging.getLogger(__name__)

class PagesController(BaseController):
    """REST Controller styled on the Atom Publishing Protocol"""
    # To properly map this controller, ensure your config/routing.py
    # file has a resource setup:
    #     map.resource('page', 'pages', controller='rest/pages', 
    #         path_prefix='/rest', name_prefix='rest_')

    def index(self, format='html'):
        """GET /rest/pages: All items in the collection"""
        # url('rest_pages')

    def create(self):
        """POST /rest/pages: Create a new item"""
        # url('rest_pages')

    def new(self, format='html'):
        """GET /rest/pages/new: Form to create a new item"""
        # url('rest_new_page')

    def update(self, id):
        """PUT /rest/pages/id: Update an existing item"""
        # Forms posted to this method should contain a hidden field:
        #    <input type="hidden" name="_method" value="PUT" />
        # Or using helpers:
        #    h.form(url('rest_page', id=ID),
        #           method='put')
        # url('rest_page', id=ID)

    def delete(self, id):
        """DELETE /rest/pages/id: Delete an existing item"""
        # Forms posted to this method should contain a hidden field:
        #    <input type="hidden" name="_method" value="DELETE" />
        # Or using helpers:
        #    h.form(url('rest_page', id=ID),
        #           method='delete')
        # url('rest_page', id=ID)

    def show(self, id, format='html'):
        """GET /rest/pages/id: Show a specific item"""
        # url('rest_page', id=ID)

    def edit(self, id, format='html'):
        """GET /rest/pages/id/edit: Form to edit an existing item"""
        # url('rest_edit_page', id=ID)
