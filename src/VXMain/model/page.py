'''
Created on Jun 12, 2011

@author: caitlyn.ohanna@virtualxistenz.com
'''


from sqlalchemy import *
from sqlalchemy.orm import mapper, relation, relationship
from sqlalchemy import Table, ForeignKey, Column
from sqlalchemy.types import Integer, Unicode
#from sqlalchemy.orm import relation, backref

from VXMain.model import DeclarativeBase, metadata, DBSession


PageTags = Table('page_tags', DeclarativeBase.metadata,
    Column('page_id', Integer, ForeignKey('pages.id')),
    Column('tag_id', Integer, ForeignKey('tags.id'))
)

PageCategories = Table('page_categories', DeclarativeBase.metadata,
    Column('page_id', Integer, ForeignKey('pages.id')),
    Column('category_id', Integer, ForeignKey('categories.id'))
)

class Page(DeclarativeBase):
    __tablename__ = 'pages'

    id = Column(Integer, primary_key=True)
    title = Column(Unicode(255), nullable=False)
    body = Column(Unicode, nullable=False)
    author = Column(Integer, ForeignKey('tg_user.user_id'))
    tags = relationship("Tag",
                    secondary=PageTags,
                    backref="pages")
    categories = relationship("Category",
                    secondary=PageCategories,
                    backref="pages")

class Tag(DeclarativeBase):
    __tablename__ = 'tags'

    id = Column(Integer, primary_key=True)
    label = Column(Unicode(64), nullable=False)

class Category(DeclarativeBase):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    label = Column(Unicode(64), nullable=False)