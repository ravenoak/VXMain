'''
Created on Jul 10, 2011

@author: ravenoak
'''

from sprox.formbase import EditableForm, AddRecordForm
from tw.forms import TextField
from VXMain.model import DBSession
from VXMain.model.page import Page

class UpdatePage(EditableForm):
    __model__ = Page
    __omit_fields__ = [
        'id', 'author_id', 'updated', 'created'
    ]
    title = TextField

class CreatePage(AddRecordForm):
    __model__ = Page
    __omit_fields__ = [
        'id', 'author_id', 'updated', 'created'
    ]
    title = TextField

createPageForm = CreatePage(DBSession)
updatePageForm = UpdatePage(DBSession)
