'''
Created on Jul 23, 2011

@author: ravenoak
'''

from VXMain.lib.base import BaseController
from VXMain.model import DBSession
from VXMain.model.project import Project
from VXMain.widgets.ProjectForms import createProjectForm, updateProjectForm
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

    @expose()
    def index(self):
        redirect('/project/list')

    @expose('VXMain.templates.projectUpdate')
    def add(self, name):
        tmpl_context.createProjectForm = createProjectForm
        project = Project()
        return dict(pageRole = 'c', project = project)

    @expose('VXMain.templates.projectUpdate')
    def edit(self, name):
        tmpl_context.updateProjectForm = updateProjectForm
        project = DBSession.query(Project).filter_by(name = name)
        return dict(pageRole = 'u', project = project)

    @expose('VXMain.templates.projectList')
    def list(self):
        projectNames = [project.name for project in DBSession.query(Project)]
        return dict(projectNames = projectNames)

    @expose('VXMain.templates.projectRead')
    def by_name(self, name):
        return self._r(name)

    @expose()
    @validate(form = createProjectForm, error_handler = add)
    @require(predicates.has_permission('editor', msg = l_('Only for Editors')))
    def _c(self, name, title, body, tags = []):
        new = Project(
            name = name,
            title = title,
            body = body,
            author = request.identity['repoze.who.userid'],
            created = datetime.now(),
            updated = datetime.now(),
            tags = tags,
        )
        DBSession.add(new)
        flash(u'Added Project: %s' % (new.label))
        redirect('./list')

    @expose('VXMain.templates.projectRead')
    def _r(self, search, **kw):
        if (search == u'search'):
            # moment for try
            project = DBSession.query(Project).filter_by(kw).one()
        else:
            # moment for try
            project = DBSession.query(Project).filter_by(name = search).one()
        return dict(project = project)

    @validate(form = updateProjectForm)
    @require(predicates.has_permission('editor', msg = l_('Only for Editors')))
    @expose('VXMain.templates.projectUpdate')
    def _u(self, name, title = None, body = None, tags = []):
        project = DBSession.query(Project).filter_by(name = name).one()
        for I in ("name", "title", "body", "tags"):
            project.I = I
        return dict(project = project, pageRole = 'u')

    #@validate(form = deleteProjectForm)
    @require(predicates.has_permission('editor', msg = l_('Only for Editors')))
    @expose('VXMain.templates.projectDelete')
    def _d(self, name, confirmed = False):
        if (confirmed == True):
            DBSession.query(Project).filter_by(name = name).delete()
            flash(_("Deleted Project: $s") % name, 'warning')
        redirect('./list')

    @expose('VXMain.templates.projectRead')
    def _default(self, name):
        pass
        return self.by_name(name)
