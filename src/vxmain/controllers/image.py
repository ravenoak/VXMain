'''
Created on Mar 23, 2012

@author: ravenoak
'''


from vxmain.lib.base import BaseController
from vxmain.model import DBSession
from vxmain.model.auth import User
from vxmain.model.primitives import Image
from datetime import datetime
from pylons.i18n import ugettext as _, lazy_ugettext as l_
from sprox.tablebase import TableBase
from sqlalchemy.orm.exc import NoResultFound
from tg import expose, flash, require, url, request, redirect, response, tmpl_context, validate
from tg.controllers import CUSTOM_CONTENT_TYPE


class ImageController(BaseController):

    @expose(content_type = 'text/csv')
    def _default(self, label):
        return self.get(label)

    @expose(content_type = CUSTOM_CONTENT_TYPE)
    def get(self, label):
        img = DBSession.query(Image).filter_by(label = unicode(label)).one()
        response.content_type = 'image/' + img.encoding
        #response.headerlist.append(('Content-Disposition', 'attachment;filename=' + image.image.filename))
        return img.data
