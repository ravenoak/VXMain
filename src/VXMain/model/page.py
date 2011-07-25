'''
Created on Jun 12, 2011

@author: caitlyn.ohanna@virtualxistenz.com
'''

from VXMain.model import DeclarativeBase, metadata, DBSession
from VXMain.model.auth import User
from VXMain.model.resource import Resource
from sqlalchemy import *
from sqlalchemy.orm import mapper, relation, relationship, backref
from sqlalchemy.types import Integer, Unicode, DateTime


# DeclarativeBase.metadata ?
CollectionCategories = Table('collection_categories', metadata,
    Column('collection_id', Integer, ForeignKey('page_collections.id')),
    Column('category_id', Integer, ForeignKey('categories.id'))
)

CollectionResources = Table('collection_resources', metadata,
    Column('collection_id', Integer, ForeignKey('page_collections.id')),
    Column('resource_id', Integer, ForeignKey('resources.id'))
)

PageResources = Table('page_resources', DeclarativeBase.metadata,
    Column('page_id', Integer, ForeignKey('pages.id')),
    Column('resource_id', Integer, ForeignKey('resources.id'))
)

PageTags = Table('page_tags', DeclarativeBase.metadata,
    Column('page_id', Integer, ForeignKey('pages.id')),
    Column('tag_id', Integer, ForeignKey('tags.id'))
)


class Category(DeclarativeBase):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key = True)
    label = Column(Unicode(64), nullable = False)

    def __repr__(self):
        return ('<Category: label=%s>' % self.label).encode('utf-8')

    def __unicode__(self):
        return self.label

class Collection(DeclarativeBase):
    __tablename__ = 'page_collections'
    id = Column(Integer, primary_key = True)
    label = Column(Unicode(64), nullable = False)
    pages = relationship("Page", backref = "collection")
    categories = relationship("Category",
                    secondary = CollectionCategories,
                    backref = "collections")
    resources = relationship("Resource",
                    secondary = CollectionResources,
                    backref = "collections")

    def __repr__(self):
        return ('<page.Collection: label=%s>' % self.label).encode('utf-8')

    def __unicode__(self):
        return self.label

class Page(DeclarativeBase):
    __tablename__ = 'pages'
    id = Column(Integer, primary_key = True)
    name = Column(Unicode(32), nullable = False)
    title = Column(Unicode(128), nullable = False)
    body = Column(Unicode, nullable = False)
    updated = Column(DateTime, nullable = False)
    created = Column(DateTime, nullable = False)
    author_id = Column(Integer, ForeignKey('tg_user.user_id'), nullable = False)
    author = relation(User, backref = (backref('pages', order_by = updated)))
    tags = relationship("Tag", secondary = PageTags, backref = "pages")
    collection_id = Column(Integer, ForeignKey('page_collections.id'), nullable = True)
    resources = relationship("Resource", secondary = PageResources, backref = "pages")

    def __repr__(self):
        return ('<Page: name=%s>' % self.name).encode('utf-8')

    def __unicode__(self):
        return self.name

#    def __init__(self, name, title, body, author, created, updated, tags):
#        self.name = unicode(name)
#        self.title = unicode(title)
#        self.body = body
#        if (author == type(User)):
#            self.author = author
#        else:
#            self.set_author_by_username(author)
#        self.created = created
#        self.updated = updated
#        self.tags = tags

    def set_author_by_username(self, username):
        self.author = DBSession.query(User).filter_by(user_name = unicode(username)).one()

class Tag(DeclarativeBase):
    __tablename__ = 'tags'
    id = Column(Integer, primary_key = True)
    label = Column(Unicode(64), nullable = False)

    def __repr__(self):
        return ('<Tag: label=%s>' % self.label).encode('utf-8')

    def __unicode__(self):
        return self.label

