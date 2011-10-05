# -*- coding: utf-8 -*-
"""Main Controller"""

from VXMain.controllers.admin import adminController
from VXMain.controllers.error import ErrorController
from VXMain.controllers.page import PageController
from VXMain.controllers.project import ProjectController
from VXMain.controllers.secure import SecureController
from VXMain.lib.base import BaseController
from VXMain.model import DBSession
from VXMain.model.page import Page
from VXMain.model import DBSession
from pylons.i18n import ugettext as _, lazy_ugettext as l_
from repoze.what import predicates
from tg import expose, flash, require, url, request, redirect
from tgext.tagging import TaggingController

__all__ = ['RootController']


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
    admin = adminController
    error = ErrorController()
    page = PageController()
    pages = page
    project = ProjectController()
    projects = project
    secc = SecureController()
    PageTagging = TaggingController(model = Page, session = DBSession, allow_edit = None)

    @expose()
    def index(self):
        """Handle the front-page."""
        redirect(url('/page/Welcome'))

    @expose()
    def about(self):
        """Handle the 'about' page."""
        redirect(url('/page/About'))

    @expose()
    def contact(self):
        """Handle the 'contact' page."""
        redirect(url('/page/Contact'))

#    @expose('VXMain.templates.data')
#    @expose('json')
#    def data(self, **kw):
#        """This method showcases how you can use the same controller for a data page and a display page"""
#        return dict(params = kw)

    @expose('VXMain.templates.login')
    def login(self, came_from = url('/')):
        """Start the user login."""
        login_counter = request.environ['repoze.who.logins']
        if login_counter > 0:
            flash(u'Wrong credentials', 'warning')
        return dict(page = 'login', login_counter = str(login_counter),
                    came_from = came_from)

    @expose()
    def post_login(self, came_from = url('/')):
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

