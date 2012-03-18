'''
Created on Jun 9, 2011

@author: caitlyn.ohanna@virtualxistenz.com
'''

from VXMain.model import DeclarativeBase, metadata
from VXMain.model import Collection, Resource, Page
from sqlalchemy import Column, Table, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.types import Integer, Unicode
from sqlalchemy.ext.associationproxy import association_proxy


class Project(Collection):
    __tablename__ = "projects"
#    __mapper_args__ = {'polymorphic_identity': 'project',
#                       }
    id = Column(None, ForeignKey('collections.id'), primary_key = True)

    def __init__(self, *args, **kwargs):
        super(Collection, self).__init__(*args, **kwargs)


class Guide(Collection):
    __tablename__ = "guides"
#    __mapper_args__ = {'polymorphic_identity': 'guide',
#                       }
    id = Column(None, ForeignKey('collections.id'), primary_key = True)

    def __init__(self, *args, **kwargs):
        super(Collection, self).__init__(*args, **kwargs)

