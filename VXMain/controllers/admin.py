'''
Created on Jun 28, 2012

@author: ravenoak
'''


#from VXMain import model
#from VXMain.model import DBSession
from VXMain.model.auth import User
from repoze.what.predicates import has_permission
from tgext.admin import AdminController, AdminConfig
from tgext.admin.config import CrudRestControllerConfig
from sprox.tablebase import TableBase
from sprox.fillerbase import TableFiller
#from sprox.dojo.tablebase import DojoTableBase as TableBase
#from sprox.dojo.fillerbase import DojoTableFiller as TableFiller


class VXAdminConfig(AdminConfig):
    class user(CrudRestControllerConfig):
        class table_type(TableBase):
                __entity__ = User
                __limit_fields__ = ['display_name', 'email_address']
                __url__ = '../user.json' #this just tidies up the URL a bit

        class table_filler_type(TableFiller):
                __entity__ = User
                __limit_fields__ = ['display_name', 'email_address', 'user_name']


class VXAdminController(AdminController):
    allow_only = has_permission('administrators')
