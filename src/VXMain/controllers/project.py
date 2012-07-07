'''
Created on Jul 23, 2011

@author: ravenoak
'''

from VXMain.lib.base import BaseController
from VXMain.model import DBSession
from VXMain.model.project import Project
from VXMain.widgets.Forms import create_project_form, update_project_form, update_project_filler
from datetime import datetime
from pylons.i18n import ugettext as _, lazy_ugettext as l_
from repoze.what import predicates
from sqlalchemy.orm.exc import NoResultFound
from tg import expose, flash, require, url, request, redirect, tmpl_context, validate


class ProjectController(BaseController):
    """
    """

    @expose()
    def index(self):
        redirect(url('/project/list_by_name'))

    @expose()
    def add(self, label = u'New Project'):
        redirect(url('/project/new?label=' + label))

    @expose()
    def create(self, label = u'New Project'):
        redirect(url('/project/new?label=' + label))

    @expose('VXMain.templates.project.update')
    def edit(self, proj_id):
        tmpl_context.update_project_form = update_project_form
        value = update_project_filler.get_value(values = {'id' : proj_id, })
        return dict(pageRole = 'u', value = value)

    @expose('VXMain.templates.project.read')
    def get(self, proj_id = None):
        if not proj_id:
            redirect(url('/project/list'))
        try:
            proj_id = int(proj_id)
        except ValueError:
            redirect(url('/project/list'))
        return self._r(proj_id)

    @expose()
    def get_all(self):
        redirect(url('/project/get'))

    @expose()
    def list(self):
        redirect(url('/project/list_by_id'))

    @expose('VXMain.templates.project.list')
    def list_by_id(self):
        projects = DBSession.query(Project).order_by(Project.id)
        return dict(projects = projects)

#    @expose('VXMain.templates.project.list')
#    def list_by_updated(self):
#        projects = DBSession.query(Project).order_by(Project.updated)
#        return dict(projects = projects)

    @expose('VXMain.templates.project.update')
    def new(self, label = u'New Project'):
        label = unicode(label)
        tmpl_context.create_project_form = create_project_form
        return dict(pageRole = 'c', value = {'label': label})

    @expose('VXMain.templates.project.list')
    def search(self, **kw):
        projects = DBSession.query(Project).filter_by(kw)
        return dict(projects = projects)

    @expose()
    @validate(form = create_project_form, error_handler = new)
    @require(predicates.has_permission('editor', msg = l_('Only for Editors')))
    def _c(self, confirmed = False, **kw):
        if confirmed:
            project = Project()
            try:
                DBSession.add(project)
                DBSession.flush()
            except:
                flash(u'Could not add Project: "%s"' % (project.label), 'error')
            flash(u'Added Project: "%s"' % (project.label))
            redirect(url('/project/' + project.id))
        redirect(url('/project/'))

    @expose()
    def _r(self, proj_id):
        project = DBSession.query(Project).get(proj_id)
        return dict(project = project)

    @expose()
    @validate(form = update_project_form)
    @require(predicates.has_permission('editor', msg = l_('Only for Editors')))
    def _u(self, proj_id, confirmed = False, **kw):
        if (confirmed == True):
            project = DBSession.query(Project).get(proj_id)
            DBSession.flush()
        redirect(url('/project/' + project.id))

    @expose()
    #@validate(form = delete_project_form)
    @require(predicates.has_permission('editor', msg = l_('Only for Editors')))
    def _d(self, proj_id, confirmed = False):
        if (confirmed == True):
            proj = DBSession.query(Project).get(proj_id)
            label = proj.label
            proj.delete()
            DBSession.flush()
            flash(u'Deleted Project: "$s"' % label, 'warning')
        redirect(url('/project/list'))

    @expose('VXMain.templates.project.read')
    def _default(self, project):
        return self.get(project)
