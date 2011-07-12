'''
Created on Jul 9, 2011

@author: ravenoak
'''

from datetime import datetime
from sprox.fillerbase import TableFiller, EditFormFiller
from sprox.formbase import EditableForm, AddRecordForm
from sprox.tablebase import TableBase
from sqlalchemy.orm.exc import NoResultFound
from pylons.i18n import ugettext as _, lazy_ugettext as l_
from repoze.what import predicates
from tg import expose, flash, require, url, request, redirect, tmpl_context, validate
from tgext.crud import CrudRestController
from VXMain.lib.base import BaseController
from VXMain.model import DBSession
from VXMain.model.page import Page
from VXMain.model.auth import User
from VXMain.widgets.PageForms import createPageForm, updatePageForm


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
    def index(self):
        redirect('/page/list')

    @expose('VXMain.templates.pageUpdate')
    def add(self, name):
        tmpl_context.createPageForm = createPageForm
        page = Page()
        return dict(pageRole = 'c', page = page)

    @expose('VXMain.templates.pageUpdate')
    def edit(self, name):
        tmpl_context.updatePageForm = updatePageForm
        page = DBSession.query(Page).filter_by(name = name)
        return dict(pageRole = 'u', page = page)

    @expose('VXMain.templates.pageList')
    def list(self):
        pageNames = [page.name for page in DBSession.query(Page)]
        return dict(pageNames = pageNames)

    @expose('VXMain.templates.pageRead')
    def by_name(self, name):
        return self._r(name)

    @expose()
    @validate(form = createPageForm, error_handler = add)
    @require(predicates.has_permission('editor', msg = l_('Only for Editors')))
    def _c(self, name, title, body, tags = [], categories = []):
        author = DBSession.query(User).filter_by(user_name = request.identity['repoze.who.userid'])
        new = Page(
            name = name,
            title = title,
            body = body,
            author = author,
            created = datetime.now(),
            updated = datetime.now(),
            tags = tags,
            categories = categories,
        )
        DBSession.add(new)
        flash(u'Added page: %s' % (new.title))
        redirect('./list')

    @expose('VXMain.templates.pageRead')
    def _r(self, search, **kw):
        if (search == u'search'):
            # moment for try
            page = DBSession.query(Page).filter_by(kw).one()
        else:
            # moment for try
            page = DBSession.query(Page).filter_by(name = search).one()
        return dict(page = page)

    @validate(form = updatePageForm)
    @require(predicates.has_permission('editor', msg = l_('Only for Editors')))
    @expose('VXMain.templates.pageUpdate')
    def _u(self, name, title = None, body = None, tags = [], categories = []):
        page = DBSession.query(Page).filter_by(name = name).one()
        for I in ("name", "title", "body", "tags", "categories"):
            page.I = I
        return dict(page = page, pageRole = 'u')

    #@validate(form = deletePageForm)
    @require(predicates.has_permission('editor', msg = l_('Only for Editors')))
    @expose('VXMain.templates.pageDelete')
    def _d(self, name, confirmed = False):
        if (confirmed == True):
            DBSession.query(Page).filter_by(name = name).delete()
            flash(_("Deleted Page: $s") % name, 'warning')
        redirect('./list')

    @expose('VXMain.templates.pageRead')
    def default(self, name):
        pass
        return self.by_name(name)
