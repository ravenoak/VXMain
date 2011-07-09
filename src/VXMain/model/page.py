'''
Created on Jun 12, 2011

@author: caitlyn.ohanna@virtualxistenz.com
'''


from sqlalchemy import *
from sqlalchemy.orm import mapper, relation, relationship, backref
from sqlalchemy import Table, ForeignKey, Column
from sqlalchemy.types import Integer, Unicode, DateTime
#from sqlalchemy.orm import relation, backref

from VXMain.model import DeclarativeBase, metadata, DBSession
from VXMain.model.auth import User


PageTags = Table('page_tags', DeclarativeBase.metadata,
    Column('page_id', Integer, ForeignKey('page.id')),
    Column('tag_id', Integer, ForeignKey('tag.id'))
)

PageCategories = Table('page_categories', DeclarativeBase.metadata,
    Column('page_id', Integer, ForeignKey('page.id')),
    Column('category_id', Integer, ForeignKey('category.id'))
)

class Page(DeclarativeBase):
    __tablename__ = 'page'

    id = Column(Integer, primary_key = True)
    name = Column(Unicode(32), nullable = False)
    title = Column(Unicode(128), nullable = False)
    body = Column(Unicode, nullable = False)
    author_id = Column(Integer, ForeignKey('tg_user.user_id'), nullable = False)
    updated = Column(DateTime, nullable = False)
    created = Column(DateTime, nullable = False)
    author = relation(User, backref = (backref('pages', order_by = updated)))
    tags = relationship("Tag",
                    secondary = PageTags,
                    backref = "pages")
    categories = relationship("Category",
                    secondary = PageCategories,
                    backref = "pages")

class Tag(DeclarativeBase):
    __tablename__ = 'tag'

    id = Column(Integer, primary_key = True)
    label = Column(Unicode(64), nullable = False)

class Category(DeclarativeBase):
    __tablename__ = 'category'

    id = Column(Integer, primary_key = True)
    label = Column(Unicode(64), nullable = False)
