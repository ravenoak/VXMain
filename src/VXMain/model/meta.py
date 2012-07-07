'''
Created on Aug 18, 2011

@author: ravenoak
'''

from VXMain.model import DeclarativeBase
from sqlalchemy import Column, Integer, Unicode

class Tag(DeclarativeBase):
    __tablename__ = 'tags'
    id = Column(Integer, primary_key = True)
    label = Column(Unicode(64), nullable = False)

    def __repr__(self):
        return ('<Tag: label=%s>' % self.label).encode('utf-8')

    def __unicode__(self):
        return self.label

