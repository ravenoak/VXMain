'''
Created on Jul 18, 2011

@author: caitlyn.ohanna@virtualxistenz.com
'''


from VXMain.model import DeclarativeBase
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.types import Integer, Unicode, DateTime, PickleType, String


class Resource(DeclarativeBase):
    __tablename__ = 'resources'
    id = Column(Integer(), primary_key = True)
    discriminator = Column('type', String(50))
    label = Column(Unicode(64), nullable = False)
    pickle = Column(PickleType())
    __mapper_args__ = {'polymorphic_on': discriminator}

    def __repr__(self):
        return ('<Resource: label=%s>' % self.label).encode('utf-8')

    def __unicode__(self):
        return self.label

class Image(Resource):
    __mapper_args__ = {'polymorphic_identity': 'image'}
    dataImage = Column(PickleType(), nullable = False)

class Snippet(Resource):
    __mapper_args__ = {'polymorphic_identity': 'snippet'}
    dataSnippet = Column(PickleType(), nullable = False)
    lang = Column(Unicode(16), nullable = False)

class GitRepo(Resource):
    __mapper_args__ = {'polymorphic_identity': 'gitrepo'}
    url = Column(Unicode(128), nullable = False)

#class CodeRef(GitRepo):
#    __mapper_args__ = {'polymorphic_identity': 'coderef'}
#    dataCodeRef = Column(PickleType(), nullable = False)

