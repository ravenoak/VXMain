'''
Created on Jul 25, 2011

@author: ravenoak
'''

from VXMain import model
from VXMain.model import DBSession
from tgext.admin.controller import AdminController
from tgext.admin.tgadminconfig import TGAdminConfig

adminController = AdminController(model, DBSession, config_type = TGAdminConfig)
