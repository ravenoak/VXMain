'''
Created on Jul 29, 2011

@author: ravenoak
'''

from VXMain.model import DeclarativeBase, metadata, DBSession
from VXMain.model.auth import User
from VXMain.model.resource import Resource
from sqlalchemy import *
from sqlalchemy.orm import mapper, relation, relationship, backref
from sqlalchemy.types import Integer, Unicode, DateTime

class Audit(DeclarativeBase):
    __tablename__ = 'audit'
    id = Column(Integer, primary_key = True)
    datetime = Column(DateTime, nullable = False)
    user = Column(User, nullable = False)
    object = Column(Unicode, nullable = False)
    change = Column(Unicode, nullable = False)
