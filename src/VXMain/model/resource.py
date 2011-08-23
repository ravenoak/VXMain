'''
Created on Jul 18, 2011

@author: caitlyn.ohanna@virtualxistenz.com
'''


from VXMain.model import DeclarativeBase
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.types import Integer, Unicode, DateTime, PickleType


class Resource(DeclarativeBase):
    __tablename__ = 'resources'
    id = Column(Integer, primary_key = True)
    label = Column(Unicode(64), nullable = False)
    resource_type = relationship("ResourceType", backref = "resources")
    resource_type_id = Column(Integer, ForeignKey('resource_types.id'))
    pickle = Column(PickleType)

    def __repr__(self):
        return ('<Resource: label=%s>' % self.label).encode('utf-8')

    def __unicode__(self):
        return self.label

class ResourceType(DeclarativeBase):
    __tablename__ = 'resource_types'
    id = Column(Integer, primary_key = True)
    label = Column(Unicode(64), nullable = False)
    hint = Column(Unicode(64), nullable = False)

    def __repr__(self):
        return ('<ResourceType: label=%s>' % self.label).encode('utf-8')

    def __unicode__(self):
        return self.label

class Image(Resource):
    dataImage = Column(Unicode(), nullable = False)

class Snippet(Resource):
    dataSnippet = Column(Unicode(), nullable = False)
    lang = Column(Unicode(16), nullable = False)

class GitRepo(Resource):
    url = Column(Unicode(128), nullable = False)

class CodeRef(GitRepo):
    path = Column(Unicode(128), nullable = False)

