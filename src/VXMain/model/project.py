'''
Created on Jun 9, 2011

@author: caitlyn.ohanna@virtualxistenz.com
'''


from sqlalchemy import *
from sqlalchemy.orm import mapper, relation, relationship
from sqlalchemy import Table, ForeignKey, Column
from sqlalchemy.types import Integer, Unicode
from VXMain.model import DeclarativeBase, metadata, DBSession
from VXMain.model.page import PageCollection


class Project(PageCollection):
    pass
