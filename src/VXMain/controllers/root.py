# -*- coding: utf-8 -*-
"""Main Controller"""

from tg import expose, flash, require, url, request, redirect
from pylons.i18n import ugettext as _, lazy_ugettext as l_
from tgext.admin.tgadminconfig import TGAdminConfig
from tgext.admin.controller import AdminController
from repoze.what import predicates
from tgext.crud import CrudRestController
from sprox.tablebase import TableBase
from sprox.formbase import EditableForm, AddRecordForm
from sprox.fillerbase import TableFiller, EditFormFiller


from VXMain.lib.base import BaseController
from VXMain.model import DBSession, metadata
from VXMain.model.page import *
from VXMain.model.project import *
from VXMain import model
from VXMain.controllers.secure import SecureController

from VXMain.controllers.error import ErrorController

__all__ = ['RootController']


class PageController(CrudRestController):
    model = Page

    class new_form_type(AddRecordForm):
        __model__ = Page

    class edit_form_type(EditableForm):
        __model__ = Page

    class edit_filler_type(EditFormFiller):
        __model__ = Page

    class table_type(TableBase):
        __model__ = Page

    class table_filler_type(TableFiller):
        __model__ = Page

    @expose('VXMain.templates.rest_get_one')
    def get_one(self, *args, **kw):
        return super(PageController, self).get_one(*args, **kw)



class RootController(BaseController):
    """
    The root controller for the VXMain application.

    All the other controllers and WSGI applications should be mounted on this
    controller. For example::

        panel = ControlPanelController()
        another_app = AnotherWSGIApplication()

    Keep in mind that WSGI applications shouldn't be mounted directly: They
    must be wrapped around with :class:`tg.controllers.WSGIAppController`.

    """
    secc = SecureController()

    admin = AdminController(model, DBSession, config_type = TGAdminConfig)
    #catwalk = Catwalk(model, DBSession)

    error = ErrorController()

    page = PageController(DBSession)

    @expose('VXMain.templates.index')
    def index(self):
        """Handle the front-page."""
        return dict(page = 'index')

    @expose('VXMain.templates.about')
    def about(self):
        """Handle the 'about' page."""
        return dict(page = 'about')

    @expose('VXMain.templates.environ')
    def environ(self):
        """This method showcases TG's access to the wsgi environment."""
        return dict(environment = request.environ)

    @expose('VXMain.templates.data')
    @expose('json')
    def data(self, **kw):
        """This method showcases how you can use the same controller for a data page and a display page"""
        return dict(params = kw)

    @expose('VXMain.templates.authentication')
    def auth(self):
        """Display some information about auth* on this application."""
        return dict(page = 'auth')

    @expose('VXMain.templates.index')
    @require(predicates.has_permission('manage', msg = l_('Only for managers')))
    def manage_permission_only(self, **kw):
        """Illustrate how a page for managers only works."""
        return dict(page = 'managers stuff')

    @expose('VXMain.templates.index')
    @require(predicates.is_user('editor', msg = l_('Only for the editor')))
    def editor_user_only(self, **kw):
        """Illustrate how a page exclusive for the editor works."""
        return dict(page = 'editor stuff')

    @expose('VXMain.templates.login')
    def login(self, came_from = url('/')):
        """Start the user login."""
        login_counter = request.environ['repoze.who.logins']
        if login_counter > 0:
            flash(_('Wrong credentials'), 'warning')
        return dict(page = 'login', login_counter = str(login_counter),
                    came_from = came_from)

    @expose()
    def post_login(self, came_from = '/'):
        """
        Redirect the user to the initially requested page on successful
        authentication or redirect her back to the login page if login failed.

        """
        if not request.identity:
            login_counter = request.environ['repoze.who.logins'] + 1
            redirect('/login', came_from = came_from, __logins = login_counter)
        userid = request.identity['repoze.who.userid']
        flash(_('Welcome back, %s!') % userid)
        redirect(came_from)

    @expose()
    def post_logout(self, came_from = url('/')):
        """
        Redirect the user to the initially requested page on logout and say
        goodbye as well.

        """
        flash(_('We hope to see you soon!'))
        redirect(came_from)
