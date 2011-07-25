'''
Created on Jul 9, 2011

@author: ravenoak
'''

from VXMain.lib.base import BaseController
from VXMain.model import DBSession
from VXMain.model.auth import User
from VXMain.model.page import Page, Tag, Collection
from VXMain.widgets.PageForms import updatePageForm, updatePageFiller
from datetime import datetime
from pylons.i18n import ugettext as _, lazy_ugettext as l_
from repoze.what import predicates
from sprox.fillerbase import TableFiller, EditFormFiller
from sprox.formbase import EditableForm, AddRecordForm
from sprox.tablebase import TableBase
from sqlalchemy.orm.exc import NoResultFound
from tg import expose, flash, require, url, request, redirect, tmpl_context, validate
from tgext.crud import CrudRestController
from markdown import Markdown
from genshi.core import Markup


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

    #rest = RestPageController()

    @expose()
    def index(self):
        redirect(url('/page/listByName'))

    @expose()
    def add(self, name = u'NewPage'):
        redirect(url('/page/new/' + name))

    @expose()
    def create(self, name = u'NewPage'):
        redirect(url('/page/new/' + name))

    @expose('VXMain.templates.pageUpdate')
    def edit(self, name):
        tmpl_context.updatePageForm = updatePageForm
        pageID, pageName = DBSession.query(Page.id, Page.name).filter_by(name = unicode(name)).one()
        value = updatePageFiller.get_value(values = {'id' : pageID, })
        return dict(pageRole = 'u', value = value, pageName = pageName)

    @expose('VXMain.templates.pageRead')
    def get(self, page = None):
        if not page:
            redirect(url('/page/listByName'))
        tmpl_context.markup = Markup
        tmpl_context.markdown = Markdown()
        try:
            page = int(page)
        except ValueError:
            if type(page) == str:
                return self.getByName(unicode(page))
        return self._r(page)

    @expose()
    def getAll(self):
        redirect(url())

    @expose('VXMain.templates.pageRead')
    def getByName(self, name):
        try:
            page = DBSession.query(Page).filter_by(name = unicode(name)).one()
        except NoResultFound:
            flash(l_(''))
            redirect()
        tmpl_context.markup = Markup
        tmpl_context.markdown = Markdown()
        return dict(page = page)

    @expose()
    def list(self):
        redirect(url('/page/listByName'))

    @expose('VXMain.templates.pageList')
    def listByName(self):
        pages = DBSession.query(Page).order_by(Page.name)
        return dict(pages = pages)

    @expose('VXMain.templates.pageList')
    def listByUpdated(self):
        pages = DBSession.query(Page).order_by(Page.updated)
        return dict(pages = pages)

    @expose('VXMain.templates.pageUpdate')
    def new(self, name = u'NewPage'):
        name = unicode(name)
        tmpl_context.updatePageForm = updatePageForm
        return dict(pageRole = 'c', pageName = name, value = {'name': name})

    @expose('VXMain.templates.pageList')
    def search(self, **kw):
        pages = DBSession.query(Page).filter_by(kw)
        return dict(pages = pages)

    @expose()
    @validate(form = updatePageForm, error_handler = add)
    @require(predicates.has_permission('editor', msg = l_('Only for Editors')))
    def _c(self, name, confirmed = False, **kw):
        if confirmed:
            page = Page()
            page.name = unicode(name)
            if kw['title']:
                page.title = unicode(kw['title'])
            if kw['body']:
                page.body = unicode(kw['body'])
            if kw['collection']:
                page.collection = DBSession.query(Collection).get(kw['collection'])
            if kw['tags']:
                for I in kw['tags']:
                    page.tags.append(DBSession.query(Tag).get(I))
            page.created = datetime.now()
            page.updated = datetime.now()
            DBSession.add(page)
            DBSession.flush()
            flash(u'Added page: %s' % (page.name))
            redirect(url('/page/' + page.name))
        redirect(url('/page/'))

    @expose()
    def _r(self, pageID):
        page = DBSession.query(Page).get(pageID)
        return dict(page = page)

    @expose()
    @validate(form = updatePageForm)
    @require(predicates.has_permission('editor', msg = l_('Only for Editors')))
    def _u(self, name, confirmed = False, **kw):
        if (confirmed == True):
            page = DBSession.query(Page).filter_by(name = unicode(name)).one()
            if kw['title']:
                page.title = unicode(kw['title'])
            if kw['body']:
                page.body = unicode(kw['body'])
            if kw['collection']:
                page.collection = DBSession.query(Collection).get(kw['collection'])
            if kw['tags']:
                for I in kw['tags']:
                    page.tags.append(DBSession.query(Tag).get(I))
            page.updated = datetime.now()
            DBSession.flush()
        redirect(url('/page/' + page.name))

    @expose()
    #@validate(form = deletePageForm)
    @require(predicates.has_permission('editor', msg = l_('Only for Editors')))
    def _d(self, name, confirmed = False):
        if (confirmed == True):
            DBSession.query(Page).filter_by(name = unicode(name)).delete()
            DBSession.flush()
            flash(_("Deleted Page: $s") % name, 'warning')
        redirect(url('/page/list'))

    @expose('VXMain.templates.pageRead')
    def _default(self, page):
        return self.get(page)
