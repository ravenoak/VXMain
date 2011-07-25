import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from VXMain.lib.base import BaseController, render

log = logging.getLogger(__name__)

class TagsController(BaseController):
    """REST Controller styled on the Atom Publishing Protocol"""
    # To properly map this controller, ensure your config/routing.py
    # file has a resource setup:
    #     map.resource('tag', 'tags', controller='rest/tags', 
    #         path_prefix='/rest', name_prefix='rest_')

    def index(self, format='html'):
        """GET /rest/tags: All items in the collection"""
        # url('rest_tags')

    def create(self):
        """POST /rest/tags: Create a new item"""
        # url('rest_tags')

    def new(self, format='html'):
        """GET /rest/tags/new: Form to create a new item"""
        # url('rest_new_tag')

    def update(self, id):
        """PUT /rest/tags/id: Update an existing item"""
        # Forms posted to this method should contain a hidden field:
        #    <input type="hidden" name="_method" value="PUT" />
        # Or using helpers:
        #    h.form(url('rest_tag', id=ID),
        #           method='put')
        # url('rest_tag', id=ID)

    def delete(self, id):
        """DELETE /rest/tags/id: Delete an existing item"""
        # Forms posted to this method should contain a hidden field:
        #    <input type="hidden" name="_method" value="DELETE" />
        # Or using helpers:
        #    h.form(url('rest_tag', id=ID),
        #           method='delete')
        # url('rest_tag', id=ID)

    def show(self, id, format='html'):
        """GET /rest/tags/id: Show a specific item"""
        # url('rest_tag', id=ID)

    def edit(self, id, format='html'):
        """GET /rest/tags/id/edit: Form to edit an existing item"""
        # url('rest_edit_tag', id=ID)
