'''
Created on Mar 23, 2012

@author: ravenoak
'''


from vxweb.lib.base import BaseController
from vxweb.model import DBSession
from vxweb.model.auth import User
from vxweb.model.primitives import Image
from datetime import datetime
from tg.i18n import ugettext as _, lazy_ugettext as l_
from sprox.tablebase import TableBase
from sqlalchemy.orm.exc import NoResultFound
from tg import expose, flash, require, url, request, redirect, response, tmpl_context, validate


class ImageController(BaseController):

    @expose(content_type = 'text/csv')
    def _default(self, label):
        return self.get(label)

    @expose()
    def get(self, label):
        img = DBSession.query(Image).filter_by(label = unicode(label)).one()
        response.headers['Content-type'] = 'image/' + img.encoding
        #response.headerlist.append(('Content-Disposition', 'attachment;filename=' + image.image.filename))
        return img.data
