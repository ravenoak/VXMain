'''
Created on Jul 9, 2011

@author: ravenoak
'''

from VXMain.lib.base import BaseController
from VXMain.model import DBSession
#from VXMain.model.auth import User
from VXMain.model.primitives import Page
#from VXMain.widgets.Forms import create_page_form, update_page_form, update_page_filler
from VXMain.widgets.renderers import bodyMarkup
#from datetime import datetime
#from pylons.i18n import ugettext as _, lazy_ugettext as l_
#from repoze.what import predicates
#from sprox.fillerbase import TableFiller, EditFormFiller
#from sprox.formbase import EditableForm, AddRecordForm
#from sprox.tablebase import TableBase
from sqlalchemy.orm.exc import NoResultFound
from tg import expose, flash, require, url, request, redirect, tmpl_context, validate
#from tgext.crud import CrudRestController



class PageController(BaseController):
    """
    """

    @expose()
    def index(self):
        redirect(url('/page/list_by_label'))

    @expose('VXMain.templates.page.read')
    def get(self, page = None):
        if not page:
            redirect(url('/page/list_by_label'))
        try:
            page = int(page)
        except ValueError:
            if type(page) == str:
                return self.get_by_label(unicode(page))
        return self._r(page)

    @expose()
    def get_all(self):
        redirect(url('/page/get'))

    @expose('VXMain.templates.page.read')
    def get_by_label(self, label):
        try:
            page = DBSession.query(Page).filter_by(label = unicode(label)).one()
        except NoResultFound:
            flash(u'Page "%s" not found' % (label))
            redirect(url('/page/new/' + label))
        render = bodyMarkup
        return dict(page = page, render = render)

    @expose()
    def list(self):
        redirect(url('/page/list_by_label'))

    @expose('VXMain.templates.page.list')
    def list_by_label(self):
        pages = DBSession.query(Page).order_by(Page.label)
        return dict(pages = pages)

    @expose('VXMain.templates.page.list')
    def list_by_updated(self):
        pages = DBSession.query(Page)
        #pages = DBSession.query(Page).order_by(Page.updated)
        return dict(pages = pages)

    @expose('VXMain.templates.page.list')
    def search(self, **kw):
        pages = DBSession.query(Page).filter_by(kw)
        return dict(pages = pages)

    @expose()
    def _r(self, page_id):
        page = DBSession.query(Page).get(page_id)
        render = bodyMarkup
        return dict(page = page, render = render)

    @expose('VXMain.templates.page.read')
    def _default(self, page):
        return self.get(page)
