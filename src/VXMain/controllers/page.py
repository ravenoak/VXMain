'''
Created on Jul 9, 2011

@author: ravenoak
'''

from VXMain.lib.base import BaseController
from VXMain.model import DBSession
#from VXMain.model.auth import User
from VXMain.model.primitives import Page
#from VXMain.widgets.Forms import create_page_form, update_page_form, update_page_filler
#from datetime import datetime
#from pylons.i18n import ugettext as _, lazy_ugettext as l_
from repoze.what import predicates
#from sprox.fillerbase import TableFiller, EditFormFiller
#from sprox.formbase import EditableForm, AddRecordForm
#from sprox.tablebase import TableBase
from sqlalchemy.orm.exc import NoResultFound
from tg import expose, flash, require, url, request, redirect, tmpl_context, validate
from tgext.crud import CrudRestController
from markdown import Markdown
from genshi.core import Markup


#class RestPageController(CrudRestController):
#    model = Page
#
#    class new_form_type(AddRecordForm):
#        __model__ = Page
#
#    class edit_form_type(EditableForm):
#        __model__ = Page
#
#    class edit_filler_type(EditFormFiller):
#        __model__ = Page
#
#    class table_type(TableBase):
#        __model__ = Page
#
#    class table_filler_type(TableFiller):
#        __model__ = Page
#
#    @expose('VXMain.templates.rest_get_one')
#    def get_one(self, *args, **kw):
#        return super(RestPageController, self).get_one(*args, **kw)


class PageController(BaseController):
    """
    """

    #rest = RestPageController()

    @expose()
    def index(self):
        redirect(url('/page/list_by_label'))

#    @expose()
#    def add(self, label = u'NewPage'):
#        redirect(url('/page/new/' + label))

#    @expose()
#    def create(self, label = u'NewPage'):
#        redirect(url('/page/new/' + label))

#    @expose('VXMain.templates.page.update')
#    def edit(self, label):
#        tmpl_context.update_page_form = update_page_form
#        page_id, page_label = DBSession.query(Page.id, Page.label).filter_by(label = unicode(label)).one()
#        value = update_page_filler.get_value(values = {'id' : page_id, })
#        return dict(page_role = 'u', value = value, page_label = page_label)

    @expose('VXMain.templates.page.read')
    def get(self, page = None):
        if not page:
            redirect(url('/page/list_by_label'))
        tmpl_context.markup = Markup
        tmpl_context.markdown = Markdown()
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
        tmpl_context.markup = Markup
        tmpl_context.markdown = Markdown()
        return dict(page = page)

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

#    @expose('VXMain.templates.page.update')
#    def new(self, label = u'NewPage'):
#        label = unicode(label)
#        tmpl_context.create_page_form = create_page_form
#        return dict(page_role = 'c', page_label = label, value = {'label': label})

    @expose('VXMain.templates.page.list')
    def search(self, **kw):
        pages = DBSession.query(Page).filter_by(kw)
        return dict(pages = pages)

#    @expose()
#    @validate(form = create_page_form, error_handler = new)
#    @require(predicates.has_permission('administrators', msg = l_('Only for Admins')))
#    def _c(self, label, confirmed = False, **kw):
#        if confirmed:
#            page = Page()
#            page.created = datetime.now()
#            page.updated = datetime.now()
#            page.label = unicode(label)
#            if kw['title']:
#                page.title = unicode(kw['title'])
#            if kw['body']:
#                page.body = unicode(kw['body'])
#            try:
#                DBSession.add(page)
#                DBSession.flush()
#            except:
#                flash (u'Could not add Page: "%s"' % (page.label), 'error')
#                redirect(url('/page/'))
#            flash(u'Added Page: "%s"' % (page.label))
#            redirect(url('/page/' + page.label))
#        redirect(url('/page/'))

    @expose()
    def _r(self, page_id):
        page = DBSession.query(Page).get(page_id)
        return dict(page = page)

#    @expose()
#    @validate(form = update_page_form)
#    @require(predicates.has_permission('administrators', msg = l_('Only for Admins')))
#    def _u(self, label, confirmed = False, **kw):
#        if (confirmed == True):
#            page = DBSession.query(Page).filter_by(label = unicode(label)).one()
#            if kw['title']:
#                page.title = unicode(kw['title'])
#            if kw['body']:
#                page.body = unicode(kw['body'])
#            if kw['collection']:
#                page.collection = DBSession.query(Collection).get(kw['collection'])
#            if kw['tags']:
#                for I in kw['tags']:
#                    page.tags.append(DBSession.query(Tag).get(I))
#            page.updated = datetime.now()
#            DBSession.flush()
#        redirect(url('/page/' + page.label))

#    @expose()
#    #@validate(form = delete_page_form)
#    @require(predicates.has_permission('administrators', msg = l_('Only for Admins')))
#    def _d(self, label, confirmed = False):
#        if (confirmed == True):
#            DBSession.query(Page).filter_by(label = unicode(label)).delete()
#            DBSession.flush()
#            flash(u'Deleted Page: "$s"' % label, 'warning')
#        redirect(url('/page/list'))

    @expose('VXMain.templates.page.read')
    def _default(self, page):
        return self.get(page)
