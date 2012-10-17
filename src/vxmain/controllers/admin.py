'''
Created on Jun 28, 2012

@author: ravenoak
'''


#from VXMain import model
from vxmain.model import DBSession
from vxmain.model.auth import User, Group, Permission
from vxmain.model.primitives import Page, Resource, Collection
from repoze.what.predicates import has_permission
from tgext.admin import AdminController, AdminConfig
from tgext.admin.config import CrudRestControllerConfig
from sprox.tablebase import TableBase
from sprox.fillerbase import TableFiller
#from sprox.dojo.tablebase import DojoTableBase
#from sprox.dojo.fillerbase import DojoTableFiller
from sprox.formbase import AddRecordForm, EditableForm
from sprox.widgets import PropertyMultipleSelectField
from formencode import Schema
from formencode.validators import FieldsMatch
from tw2.forms import PasswordField, TextField, MultipleSelectField


class ResourceField(PropertyMultipleSelectField):
    def _my_update_params(self, d, nullable=False):
        resources = DBSession.query(Resource).all()
        options = [(resource.id, '%s (%s)'%(resource.label, resource.rtype))
                            for resource in resources]
        d['options']= options
        return d


class CollectionField(PropertyMultipleSelectField):
    def _my_update_params(self, d, nullable=False):
        collections = DBSession.query(Collection).all()
        options = [(collection.id, '%s (%s)'%(collection.label, collection.rtype))
                            for collection in collections]
        d['options']= options
        return d


addUserForm_validator =  Schema(chained_validators=(FieldsMatch('password',
                                                         'verify_password',
                                                         messages={'invalidNoMatch':
                                                         'Passwords do not match'}),))

class AddUserForm(AddRecordForm):
    __model__ = User
    __require_fields__     = ['password', 'user_name', 'email_address', ]
    __omit_fields__        = ['_password', 'groups', 'created', 'user_id', ]
    __field_order__        = ['user_name', 'email_address', 'display_name', 'password', 'verify_password', ]
    __base_validator__     = addUserForm_validator
    email_address          = TextField
    display_name           = TextField
    verify_password        = PasswordField('verify_password')


class EditUserForm(EditableForm):
    __model__ = User
    __require_fields__     = ['password', 'user_name', 'email_address', ]
    __omit_fields__        = ['created', '_password', 'user_id', ]
    __field_order__        = ['user_name', 'email_address', 'display_name', 'groups', 'password', 'verify_password']
    __base_validator__     = addUserForm_validator
    email_address          = TextField
    display_name           = TextField
    verify_password        = PasswordField('verify_password')


class UserCrudConfig(CrudRestControllerConfig):
    new_form_type = AddUserForm
    edit_form_type = EditUserForm


class AddPageForm(AddRecordForm):
    __model__ = Page
    __require_fields__     = ['label', 'title', ]
    __omit_fields__        = [ 'id', 'rtype', '', ]
    __field_order__        = ['label', 'title', 'body', 'resources', 'collections', ]
    #__base_validator__     = addPageForm_validator
    collections = CollectionField
    resources = ResourceField
    title = TextField


class EditPageForm(EditableForm):
    __model__ = Page
    __require_fields__     = ['label', 'title', ]
    __omit_fields__        = ['id', 'rtype', ]
    __field_order__        = ['label', 'title', 'body', 'resources', 'collections', ]
    #__dropdown_field_names__ = {'resources':'label', 'collections':'label'}
    #__base_validator__     = addPageForm_validator
    collections = CollectionField
    resources = ResourceField
    title = TextField


class PageCrudConfig(CrudRestControllerConfig):
    new_form_type = AddPageForm
    edit_form_type = EditPageForm





class VXAdminConfig(AdminConfig):
    class user(UserCrudConfig):
        class table_type(TableBase):
                __entity__ = User
                __omit_fields__ = [ 'user_id', '_password', 'password', ]
                __url__ = '../user.json' #this just tidies up the URL a bit

        class table_filler_type(TableFiller):
                __entity__ = User
                __omit_fields__ = ['user_id', '_password', 'password', ]

    class page(PageCrudConfig):
        class table_type(TableBase):
                __entity__ = Page
                __limit_fields__ = ['label', 'title', ]
                __url__ = '../page.json' #this just tidies up the URL a bit

        class table_filler_type(TableFiller):
                __entity__ = Page
                __limit_fields__ = ['label', 'title', ]


class VXAdminController(AdminController):
    allow_only = has_permission('administrators')
