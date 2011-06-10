# -*- coding: utf-8 -*-
'''
Created on Jun 9, 2011

@author: cohanna
'''

from sqlalchemy import *
from sqlalchemy.orm import mapper, relation
from sqlalchemy import Table, ForeignKey, Column
from sqlalchemy.types import Integer, Unicode
#from sqlalchemy.orm import relation, backref

from VXMain.model import DeclarativeBase, metadata, DBSession


class Page(DeclarativeBase):
    __tablename__ = 'pages'

    id = Column(Integer, primary_key=True)
    title = Column(Unicode(255), nullable=False)
    body = Column(Unicode, nullable=False)


class Project(DeclarativeBase):
    __tablename__ = 'projects'

    id = Column(Integer, primary_key=True)
    name = Column(Unicode(128), nullable=False)
    descr = Column(Unicode, nullable=False)
