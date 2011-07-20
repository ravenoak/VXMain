# -*- coding: utf-8 -*-
"""Setup the VXMain application"""

# investigate
import logging
# investigate
from tg import config
from datetime import datetime
from VXMain import model
import transaction

# why is it wanting command, conf...vars?!?!
def bootstrap(command, conf, vars):
    """Place any commands to setup VXMain here"""

    from sqlalchemy.exc import IntegrityError

    editorU = model.User()
    editorU.user_name = u'editor'
    editorU.display_name = u'Example editor'
    editorU.email_address = u'editor@somedomain.com'
    editorU.password = u'editpass'

    editorG = model.Group()
    editorG.group_name = u'editors'
    editorG.display_name = u'Editors Group'
    editorG.users.append(editorU)

    editorP = model.Permission()
    editorP.permission_name = u'editor'
    editorP.description = u'This permission give an administrative right to the bearer'
    editorP.groups.append(editorG)

    specPageCat = model.Category()
    specPageCat.label = u'Special Pages'

    frontPageTag = model.Tag()
    frontPageTag.label = u'FrontPage'

    frontPage = model.Page()
    frontPage.name = u'FrontMain'
    frontPage.title = u'VirtualXistenz: where digital dreams come alive'
    frontPage.author = editorU
    frontPage.body = u'Welcome and HelloWorld!'
    frontPage.created = datetime.now()
    frontPage.updated = datetime.now()
    #frontPage.categories.append(specPageCat)
    frontPage.tags.append(frontPageTag)

    try:
        model.DBSession.add(editorG)
        model.DBSession.add(editorP)
        model.DBSession.add(editorU)
        model.DBSession.add(specPageCat)
        model.DBSession.add(frontPage)
        model.DBSession.flush()
        transaction.commit()
    except IntegrityError:
        print 'Warning, there was a problem adding your auth data, it may have already been added:'
        import traceback
        print traceback.format_exc()
        transaction.abort()
        print 'Continuing with bootstrapping...'
