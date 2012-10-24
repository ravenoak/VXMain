'''
Created on Jul 18, 2011

@author: caitlyn.ohanna@virtualxistenz.com
'''


from vxmain.model import DeclarativeBase, metadata
from vxmain.lib.wiki.macros import Markup
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.ext.orderinglist import ordering_list
from sqlalchemy import Column, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.types import Integer, Unicode, String, LargeBinary
from sqlalchemy.types import TypeDecorator, CHAR
#from sqlalchemy.types import PickleType, DateTime
from sqlalchemy.dialects.postgresql import UUID
import uuid


# From http://docs.sqlalchemy.org/en/latest/core/types.html
class GUID(TypeDecorator):
    """Platform-independent GUID type.

    Uses Postgresql's UUID type, otherwise uses
    CHAR(32), storing as stringified hex values.

    """
    impl = CHAR

    def load_dialect_impl(self, dialect):
        if dialect.name == 'postgresql':
            return dialect.type_descriptor(UUID())
        else:
            return dialect.type_descriptor(CHAR(32))

    def process_bind_param(self, value, dialect):
        if value is None:
            return value
        elif dialect.name == 'postgresql':
            return str(value)
        else:
            if not isinstance(value, uuid.UUID):
                return "%.32x" % uuid.UUID(value)
            else:
                # hexstring
                return "%.32x" % value

    def process_result_value(self, value, dialect):
        if value is None:
            return value
        else:
            return uuid.UUID(value)


resource_collections = Table("resource_collections", metadata,
    Column('collection_id', Integer, ForeignKey('collections.id')),
    Column('resource_id', Integer, ForeignKey('resources.id')),
    Column('position', Integer)
)


# This is a MixIn
class Versioned(object):
    atomic_number = Column(GUID, nullable = False)
    revision = Column(Integer, nullable = False)

    def __init__(self, revision = 0):
        self.atomic_number = uuid.uuid4()
        self.revision = revision


class Resource(DeclarativeBase):
    __tablename__ = "resources"
    id = Column(Integer, primary_key = True)
    rtype = Column(String(50), nullable = False)
    label = Column(Unicode(64), nullable = False)
    renderer = Markup()

#    def __init__(self, *args, **kwargs):
#        #self.label = label
#        super(DeclarativeBase, self).__init__(*args, **kwargs)

    def __repr__(self):
        return ("<%s: '%s'>" % (self.__class__.__name__, self.label)).encode('utf-8')

    def __unicode__(self):
        return self.label

    @declared_attr
    def __mapper_args__(self):
        # in this case self really is cls
        if self.__name__ == 'Resource':
            return {
                    "polymorphic_on": self.rtype,
                    "polymorphic_identity": "Resource"
            }
        else:
            return {"polymorphic_identity": self.__name__}
    
    
    def render(self, output_type='xhtml5'):
        return self.renderer.render(self.body, output_type)



class Collection(Resource):
    __tablename__ = "collections"
    id = Column(None, ForeignKey('resources.id'), primary_key = True)
    resources = relationship("Resource",
                    secondary = resource_collections,
                    backref = "collections")

    def __init__(self, *args, **kwargs):
        super(Resource, self).__init__(*args, **kwargs)


class OrderedCollection(Collection):
    __tablename__ = None
    oresources = relationship("Resource",
                         secondary = resource_collections,
                         backref = "ocollections",
                         collection_class = ordering_list('position'),
                         order_by = 'resource_collections.c.position')


class Page(Collection):
    __tablename__ = "pages"
    id = Column(None, ForeignKey('collections.id'), primary_key = True)
    title = Column(Unicode(255), nullable = False)
    body = Column(Unicode, nullable = False)

    def __init__(self, *args, **kwargs):
        super(Collection, self).__init__(*args, **kwargs)
        


class Image(Resource):
    __tablename__ = "images"
    id = Column(None, ForeignKey('resources.id'), primary_key = True)
    data = Column(LargeBinary, nullable = False)
    sizex = Column(Integer, nullable = False)
    sizey = Column(Integer, nullable = False)
    mode = Column(Unicode(10), nullable = False)
    encoding = Column(Unicode(10), nullable = False)

    def __init__(self, *args, **kwargs):
        # Lastly
        super(Resource, self).__init__(*args, **kwargs)
