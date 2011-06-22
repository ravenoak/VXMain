'''
Created on Jun 9, 2011

@author: caitlyn.ohanna@virtualxistenz.com
'''


from sqlalchemy import *
from sqlalchemy.orm import mapper, relation, relationship
from sqlalchemy import Table, ForeignKey, Column
from sqlalchemy.types import Integer, Unicode
#from sqlalchemy.orm import relation, backref

from VXMain.model import DeclarativeBase, metadata, DBSession
from VXMain.model.page import Page


ProjectPages = Table('project_pages', DeclarativeBase.metadata,
    Column('project_id', Integer, ForeignKey('projects.id')),
    Column('page_id', Integer, ForeignKey('pages.id'))
)

class Project(DeclarativeBase):
    __tablename__ = 'projects'

    id = Column(Integer, primary_key=True)
    name = Column(Unicode(128), nullable=False)
    descr = Column(Unicode, nullable=False)
    pages = relationship("Page",
                    secondary=ProjectPages,
                    backref="projects")