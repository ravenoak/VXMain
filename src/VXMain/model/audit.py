'''
Created on Jul 29, 2011

@author: ravenoak
'''

from VXMain.model import DeclarativeBase, metadata, DBSession
from VXMain.model.auth import User
from VXMain.model.resource import Resource
from sqlalchemy import Column
from sqlalchemy.orm import mapper, relation, relationship, backref
from sqlalchemy.types import Integer, Unicode, DateTime

class AuditLog(DeclarativeBase):
    __tablename__ = 'audit_log'
    id = Column(Integer, primary_key = True)
    datetime = Column(DateTime, nullable = False)
    user = relation(User, backref = (backref('audit', order_by = datetime)))
    change = Column(Unicode, nullable = False)

class Versioned(DeclarativeBase):
    __tablename__ = 'versions'
