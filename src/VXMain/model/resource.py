'''
Created on Jul 18, 2011

@author: caitlyn.ohanna@virtualxistenz.com
'''


from sqlalchemy import *
from sqlalchemy import Table, ForeignKey, Column
from sqlalchemy.orm import mapper, relation, relationship, backref
from sqlalchemy.types import Integer, Unicode, DateTime
from VXMain.model import DeclarativeBase, metadata


class Resource(DeclarativeBase):
    __tablename__ = 'resources'
    id = Column(Integer, primary_key = True)
    label = Column(Unicode(64), nullable = False)
    resource_type = relationship("ResourceType", backref = "resources")
    resource_type_id = Column(Integer, ForeignKey('resource_types.id'))

class ResourceType(DeclarativeBase):
    __tablename__ = 'resource_types'
    id = Column(Integer, primary_key = True)
    label = Column(Unicode(64), nullable = False)
    class_type = Column(Unicode(64), nullable = False)

class Image(Resource):
    data = Column(Unicode(), nullable = False)

class Snippet(Resource):
    data = Column(Unicode(), nullable = False)
    lang = Column(Unicode(16), nullable = False)

class GitRepo(Resource):
    url = Column(Unicode(128), nullable = False)

class CodeRef(GitRepo):
    pass
