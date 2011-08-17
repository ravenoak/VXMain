'''
Created on Jun 9, 2011

@author: caitlyn.ohanna@virtualxistenz.com
'''


from VXMain.model import DeclarativeBase, metadata, DBSession
from VXMain.model.page import Collection as PageCollection
from VXMain.model.resource import Resource
from sqlalchemy import *
from sqlalchemy.orm import mapper, relation, relationship, backref
from sqlalchemy.types import Integer, Unicode, LargeBinary


class Project(DeclarativeBase):
    __tablename__ = "projects"

    id = Column(Integer, primary_key = True)
    label = Column(Unicode(64), nullable = False)
    page_collections = relationship("PageCollection", backref = "parent")
    child_id = Column(Integer, ForeignKey('child.id'))
    child = relationship("Child", backref = "parents")
    categories = relationship("Category",
                    secondary = CollectionCategories,
                    backref = "collections")
    resources = relationship("Resource",
                    secondary = CollectionResources,
                    backref = "collections")

    def __repr__(self):
        return ('<Project: label=%s>' % self.label).encode('utf-8')

    def __unicode__(self):
        return self.label

class Guide(DeclarativeBase):

    def __repr__(self):
        return ('<Guide: label=%s>' % self.label).encode('utf-8')

    def __unicode__(self):
        return self.label

class PoC(DeclarativeBase):

    def __repr__(self):
        return ('<PoC: label=%s>' % self.label).encode('utf-8')

    def __unicode__(self):
        return self.label
