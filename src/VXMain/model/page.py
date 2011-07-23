'''
Created on Jun 12, 2011

@author: caitlyn.ohanna@virtualxistenz.com
'''


from VXMain.model import DeclarativeBase, metadata, DBSession
from VXMain.model.auth import User
from VXMain.model.resource import Resource


PageTags = Table('page_tags', DeclarativeBase.metadata,
    Column('page_id', Integer, ForeignKey('pages.id')),
    Column('tag_id', Integer, ForeignKey('tags.id'))
)

PageCategories = Table('page_categories', DeclarativeBase.metadata,
    Column('page_id', Integer, ForeignKey('pages.id')),
    Column('category_id', Integer, ForeignKey('categories.id'))

CollectionCategories = Table('collection_categories', metadata,
    Column('collection_id', Integer, ForeignKey('page_collection.id')),
    Column('category_id', Integer, ForeignKey('category.id'))
)

CollectionResources = Table('collection_resources', metadata,
    Column('collection_id', Integer, ForeignKey('collections.id')),
    Column('resource_id', Integer, ForeignKey('resources.id'))
)

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
    collection = Column(Integer, ForeignKey('page_collection.id'), nullable = True)

class Tag(DeclarativeBase):
    __tablename__ = 'tags'
    id = Column(Integer, primary_key = True)
    label = Column(Unicode(64), nullable = False)

class Category(DeclarativeBase):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key = True)
    label = Column(Unicode(64), nullable = False)

class Collection(DeclarativeBase):
    __tablename__ = 'collections'
    id = Column(Integer, primary_key = True)
    label = Column(Unicode(64), nullable = False)
    pages = relationship("Page", backref = "collection")
    categories = relationship("Category",
                    secondary = CollectionCategories,
                    backref = "collections")
    resources = relationship("Resource",
                    secondary = CollectionResources,
                    backref = "collections")
