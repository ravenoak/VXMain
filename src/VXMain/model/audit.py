'''
Created on Jul 29, 2011

@author: ravenoak
'''

from VXMain.model import DeclarativeBase, metadata, DBSession
from VXMain.model.auth import User
#from VXMain.model.resource import Resource
from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy.types import Integer, Unicode, DateTime

class AuditLog(DeclarativeBase):
    __tablename__ = 'audit_log'
    id = Column(Integer, primary_key = True)
    datetime = Column(DateTime, nullable = False)
    user = relationship(User, backref = 'audit', order_by = datetime)
    log = Column(Unicode, nullable = False)

class Versioned(DeclarativeBase):
    __tablename__ = 'versions'
