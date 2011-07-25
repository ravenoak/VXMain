'''
Created on Jul 10, 2011

@author: ravenoak
'''

from sprox.formbase import EditableForm, AddRecordForm
from sprox.fillerbase import EditFormFiller
from tw.forms import TextField, CheckBox
from VXMain.model import DBSession
from VXMain.model.page import Page

class UpdatePage(EditableForm):
    __model__ = Page
    __omit_fields__ = [
        'id', 'author_id', 'updated', 'created', 'author'
    ]
    __require_fields__ = ['confirmed', 'name']
    __dropdown_field_names__ = ['label', ]
    #__dropdown_field_names__ = {'tags': 'label', 'resources': 'label', 'collection': 'label'}
    title = TextField
    confirmed = CheckBox('confirmed')

class PageFiller(EditFormFiller):
    __model__ = Page


#createPageForm = CreatePage(DBSession)
updatePageForm = UpdatePage(DBSession)
updatePageFiller = PageFiller(DBSession)
