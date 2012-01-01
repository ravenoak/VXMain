'''
Created on Jun 9, 2011

@author: caitlyn.ohanna@virtualxistenz.com
'''

from VXMain.model import DeclarativeBase, metadata
from VXMain.model.page import Collection as PageCollection
from VXMain.model.resource import Resource
#from VXMain.model import Tag
from sqlalchemy import Column, Table, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.types import Integer, Unicode


#ProjectPageCollections = Table('project_page_collections', metadata,
#    Column('project_id', Integer, ForeignKey('projects.id')),
#    Column('tag_id', Integer, ForeignKey('tags.id'))
#)
#
#ProjectResources = Table('project_tags', metadata,
#    Column('project_id', Integer, ForeignKey('projects.id')),
#    Column('tag_id', Integer, ForeignKey('tags.id'))
#)

class Project(DeclarativeBase):
    __tablename__ = "projects"

    id = Column(Integer, primary_key = True)
    label = Column(Unicode(64), nullable = False)
#    page_collections = relationship(PageCollection,
#                                    secondary = ProjectPageCollections,
#                                    backref = "projects")
#    tags = None
#    resources = relationship(Resource,
#                    secondary = ProjectResources,
#                    backref = "projects")

    def __repr__(self):
        return ('<Project: label=%s>' % self.label).encode('utf-8')

    def __unicode__(self):
        return self.label
