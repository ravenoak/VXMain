'''
Created on Jul 10, 2011

@author: ravenoak
'''

from sprox.formbase import EditableForm
from sprox.fillerbase import EditFormFiller
from tw2.forms import TextField, CheckBox, HiddenField
from vxmain.model import DBSession, Page, Project

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


create_page_form = CreatePage(DBSession)
update_page_form = UpdatePage(DBSession)
update_page_filler = PageFiller(DBSession)

create_project_form = ProjectForm(DBSession)
update_project_form = ProjectForm(DBSession)
update_project_filler = ProjectFiller(DBSession)
