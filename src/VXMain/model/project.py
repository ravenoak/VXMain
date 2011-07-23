'''
Created on Jun 9, 2011

@author: caitlyn.ohanna@virtualxistenz.com
'''


from sqlalchemy import *
from sqlalchemy.orm import mapper, relation, relationship, backref
from sqlalchemy import Table, ForeignKey, Column
from sqlalchemy.types import Integer, Unicode, LargeBinary
from VXMain.model import DeclarativeBase, metadata, DBSession
from VXMain.model.page import Collection as PageCollection


ProjectPages = Table('project_pages', DeclarativeBase.metadata,
    Column('project_id', Integer, ForeignKey('projects.id')),
    Column('page_id', Integer, ForeignKey('pages.id'))
)

class Project(DeclarativeBase):
    __tablename__ = 'projects'
    id = Column(Integer, primary_key = True)
    label = Column(Unicode(128), nullable = False)
    descr = Column(Unicode, nullable = False)
    pages = relationship("Page",
                    secondary = ProjectPages,
                    backref = "project")

class ResourceType(DeclarativeBase):
    __tablename__ = 'resource_types'
    id = Column(Integer, primary_key = True)
    label = Column(Unicode(128), nullable = False)
    # Not sure how this is really going to be yet.
    class_string = Column(Unicode, nullable = False)
    pickle = Column(LargeBinary, nullable = False)

class Resource(DeclarativeBase):
    __tablename__ = 'resources'
    id = Column(Integer, primary_key = True)
    label = Column(Unicode(128), nullable = False)
    descr = Column(Unicode, nullable = True)
    type = relation(ResourceType, backref = (backref('resources', order_by = label)))

class Guide(PageCollection):
    pass

class PoC(PageCollection):
    pass
