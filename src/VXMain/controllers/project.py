'''
Created on Jul 23, 2011

@author: ravenoak
'''

from VXMain.lib.base import BaseController
from VXMain.model import DBSession
from VXMain.model.project import Project
from VXMain.widgets.Forms import createProjectForm, updateProjectForm, updateProjectFiller
from datetime import datetime
from pylons.i18n import ugettext as _, lazy_ugettext as l_
from repoze.what import predicates
from sprox.fillerbase import TableFiller, EditFormFiller
from sprox.formbase import EditableForm, AddRecordForm
from sprox.tablebase import TableBase
from sqlalchemy.orm.exc import NoResultFound
from tg import expose, flash, require, url, request, redirect, tmpl_context, validate
from tgext.crud import CrudRestController


class RestProjectController(CrudRestController):
    model = Project

    class new_form_type(AddRecordForm):
        __model__ = Project

    class edit_form_type(EditableForm):
        __model__ = Project

    class edit_filler_type(EditFormFiller):
        __model__ = Project

    class table_type(TableBase):
        __model__ = Project

    class table_filler_type(TableFiller):
        __model__ = Project

    @expose('VXMain.templates.rest_get_one')
    def get_one(self, *args, **kw):
        return super(RestProjectController, self).get_one(*args, **kw)


class ProjectController(BaseController):
    """
    """

    #rest = RestProjectController()

    @expose()
    def index(self):
        redirect(url('/project/listByName'))

    @expose()
    def add(self, label = u'New Project'):
        redirect(url('/project/new?label=' + label))

    @expose()
    def create(self, label = u'New Project'):
        redirect(url('/project/new?label=' + label))

    @expose('VXMain.templates.projectUpdate')
    def edit(self, id):
        tmpl_context.updateProjectForm = updateProjectForm
        value = updateProjectFiller.get_value(values = {'id' : id, })
        return dict(pageRole = 'u', value = value)

    @expose('VXMain.templates.projectRead')
    def get(self, id = None):
        if not id:
            redirect(url('/project/list'))
        try:
            id = int(id)
        except ValueError:
            redirect(url('/project/list'))
        return self._r(id)

    @expose()
    def getAll(self):
        redirect(url('/project/get'))

    @expose('VXMain.templates.projectRead')
    def getByName(self, name):
        try:
            project = DBSession.query(Project).filter_by(name = unicode(name)).one()
        except NoResultFound:
            flash(l_(''))
            redirect(url('/project/new'))
        return dict(project = project)

    @expose()
    def list(self):
        redirect(url('/project/listByID'))

    @expose('VXMain.templates.projectList')
    def listByID(self):
        projects = DBSession.query(Project).order_by(Project.id)
        return dict(projects = projects)

    @expose('VXMain.templates.projectList')
    def listByUpdated(self):
        projects = DBSession.query(Project).order_by(Project.updated)
        return dict(projects = projects)

    @expose('VXMain.templates.projectUpdate')
    def new(self, name = u'NewProject'):
        name = unicode(name)
        tmpl_context.createProjectForm = createProjectForm
        return dict(pageRole = 'c', projectName = name, value = {'name': name})

    @expose('VXMain.templates.projectList')
    def search(self, **kw):
        projects = DBSession.query(Project).filter_by(kw)
        return dict(projects = projects)

    @expose()
    @validate(form = createProjectForm, error_handler = new)
    @require(predicates.has_permission('editor', msg = l_('Only for Editors')))
    def _c(self, name, confirmed = False, **kw):
        if confirmed:
            project = Project()
            project.created = datetime.now()
            project.updated = datetime.now()
            project.name = unicode(name)
            if kw['title']:
                project.title = unicode(kw['title'])
            if kw['body']:
                project.body = unicode(kw['body'])
            if kw['collection']:
                project.collection = DBSession.query(Collection).get(kw['collection'])
            if kw['tags']:
                for I in kw['tags']:
                    project.tags.append(DBSession.query(Tag).get(I))
            try:
                DBSession.add(project)
                DBSession.flush()
            except:
                flash (u'Could not add project: %s' % (project.name), 'error')
            flash(u'Added project: %s' % (project.name))
            redirect(url('/project/' + project.name))
        redirect(url('/project/'))

    @expose()
    def _r(self, projectID):
        project = DBSession.query(Project).get(projectID)
        return dict(project = project)

    @expose()
    @validate(form = updateProjectForm)
    @require(predicates.has_permission('editor', msg = l_('Only for Editors')))
    def _u(self, name, confirmed = False, **kw):
        if (confirmed == True):
            project = DBSession.query(Project).filter_by(name = unicode(name)).one()
            if kw['title']:
                project.title = unicode(kw['title'])
            if kw['body']:
                project.body = unicode(kw['body'])
            if kw['collection']:
                project.collection = DBSession.query(Collection).get(kw['collection'])
            if kw['tags']:
                for I in kw['tags']:
                    project.tags.append(DBSession.query(Tag).get(I))
            project.updated = datetime.now()
            DBSession.flush()
        redirect(url('/project/' + project.name))

    @expose()
    #@validate(form = deleteProjectForm)
    @require(predicates.has_permission('editor', msg = l_('Only for Editors')))
    def _d(self, name, confirmed = False):
        if (confirmed == True):
            DBSession.query(Project).filter_by(name = unicode(name)).delete()
            DBSession.flush()
            flash(_("Deleted Project: $s") % name, 'warning')
        redirect(url('/project/list'))

    @expose('VXMain.templates.projectRead')
    def _default(self, project):
        return self.get(project)
