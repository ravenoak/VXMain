'''
Created on Jul 18, 2011

@author: caitlyn.ohanna@virtualxistenz.com
'''


from sqlalchemy import *
from sqlalchemy.orm import mapper, relation, relationship, backref
from sqlalchemy import Table, ForeignKey, Column
from sqlalchemy.types import Integer, Unicode, DateTime
from VXMain.model import DeclarativeBase, metadata


class Resource(DeclarativeBase):
    __tablename__ = 'resources'
    pass
