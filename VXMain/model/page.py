'''
Created on Jun 12, 2011

@author: caitlyn.ohanna@virtualxistenz.com
'''

from VXMain.model import DeclarativeBase, metadata, DBSession
from VXMain.model.auth import User
#from VXMain.model import Tag
from VXMain.model.resource import Resource
from sqlalchemy import Column, Table, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.types import Integer, Unicode, DateTime


# DeclarativeBase.metadata ?

#CollectionResources = Table('collection_resources', metadata,
#    Column('collection_id', Integer, ForeignKey('page_collections.id')),
#    Column('resource_id', Integer, ForeignKey('resources.id'))
#)
#
#PageResources = Table('page_resources', metadata,
#    Column('page_id', Integer, ForeignKey('pages.id')),
#    Column('resource_id', Integer, ForeignKey('resources.id'))
#)


class Page(DeclarativeBase):
    __tablename__ = 'pages'
    id = Column(Integer, primary_key = True)
    name = Column(Unicode(32), nullable = False)
    title = Column(Unicode(128), nullable = False)
    body = Column(Unicode, nullable = False)
#    collection_id = Column(Integer, ForeignKey('page_collections.id'), nullable = True)
#    resources = relationship(Resource, secondary = PageResources, backref = "pages")
    tags = None

    def __repr__(self):
        return ('<Page: name=%s>' % self.name).encode('utf-8')

    def __unicode__(self):
        return self.name

class Collection(DeclarativeBase):
    __tablename__ = 'page_collections'
    id = Column(Integer, primary_key = True)
    label = Column(Unicode(64), nullable = False)
#    pages = relationship(Page, backref = "collection")
    tags = None
#    resources = relationship(Resource,
#                    secondary = CollectionResources,
#                    backref = "collections")

    def __repr__(self):
        return ('<page.Collection: label=%s>' % self.label).encode('utf-8')

    def __unicode__(self):
        return self.label

