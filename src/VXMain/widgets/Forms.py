'''
Created on Jul 10, 2011

@author: ravenoak
'''

from sprox.formbase import EditableForm
from sprox.fillerbase import EditFormFiller
from tw.forms import TextField, CheckBox, HiddenField
from VXMain.model import DBSession, Page, Project

class PageForm(EditableForm):
    __model__ = Page
    __omit_fields__ = [
        'id', 'author_id', 'updated', 'created', 'author',
    ]
    __dropdown_field_names__ = ['label', ]
    #__dropdown_field_names__ = {'tags': 'label', 'resources': 'label', 'collection': 'label'}
    __require_fields__ = ['confirmed', ]
    title = TextField('title', size = 64, maxlength = 128)
    confirmed = CheckBox('confirmed')

class UpdatePage(PageForm):
    name = HiddenField

class CreatePage(PageForm):
    __require_fields__ = ['confirmed', 'name']

class PageFiller(EditFormFiller):
    __model__ = Page

class ProjectForm(EditableForm):
    __model__ = Project
    __require_fields__ = ['confirmed', ]
    id = HiddenField
    label = TextField('label', size = 64, maxlength = 128)
    confirmed = CheckBox('confirmed')

class CreateProject(ProjectForm):
    pass

class UpdateProject(ProjectForm):
    pass

class ProjectFiller(EditFormFiller):
    __model__ = Project


createPageForm = CreatePage(DBSession)
updatePageForm = UpdatePage(DBSession)
updatePageFiller = PageFiller(DBSession)

createProjectForm = ProjectForm(DBSession)
updateProjectForm = ProjectForm(DBSession)
updateProjectFiller = ProjectFiller(DBSession)
