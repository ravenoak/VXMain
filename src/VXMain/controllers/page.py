'''
Created on Jul 9, 2011

@author: ravenoak
'''

from sprox.fillerbase import TableFiller, EditFormFiller
from sprox.formbase import EditableForm, AddRecordForm
from sprox.tablebase import TableBase
from sqlalchemy.orm.exc import NoResultFound
from pylons.i18n import ugettext as _, lazy_ugettext as l_
from repoze.what import predicates
from tg import expose, flash, require, url, request, redirect
from tgext.crud import CrudRestController
from VXMain.lib.base import BaseController
from VXMain.model import DBSession, metadata
from VXMain.model.page import *

class RestPageController(CrudRestController):
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
        return super(RestPageController, self).get_one(*args, **kw)

class PageController(BaseController):
    """
    """

    @expose()
    def c(self, name):
        exist = DBSession.query(Page).filter_by(name = name).count()
        if (exist > 0):
            redirect("/page/r/name")
        else:
            redirect("/page/u/name?mode=create")

    @expose('VXMain.templates.pageRead')
    def r(self, name):
        page = DBSession.query(Page).filter_by(name = name).one()
        return dict()

    @expose('VXMain.templates.pageUpdate')
    def u(self, name, mode = 'update'):
        if (mode == 'update'):
            page = DBSession.query(Page).filter_by(name = name).one()
        elif (mode == 'create'):
            page = Page(name = name)
            DBSession.add(page)

        return dict()

    @expose('VXMain.templates.pageDelete')
    def d(self, name, confimed = False):
        pass

    @expose()
    def index(self):
        redirect('/pages/list')

    @expose('VXMain.templates.pageList')
    def list(self):
        pages = [page.pagename for page in DBSession.query(Page)]
        return dict(pages = pages)
