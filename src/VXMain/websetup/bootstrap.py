# -*- coding: utf-8 -*-
"""Setup the VXMain application"""

# investigate
#import logging
# investigate
#from tg import config
from datetime import datetime
from VXMain import model
import transaction

# why is it wanting command, conf...vars?!?!
def bootstrap(command, conf, vars):
    """Place any commands to setup VXMain here"""

    from sqlalchemy.exc import IntegrityError

    editorU = model.User()
    editorU.user_name = u'ravenoak'
    editorU.display_name = u'Caitlyn O\'Hanna'
    editorU.email_address = u'caitlyn.ohanna@virtualxistenz.com'
    editorU.password = u'editpass'

    editorG = model.Group()
    editorG.group_name = u'editors'
    editorG.display_name = u'Editors Group'
    editorG.users.append(editorU)

    editorP = model.Permission()
    editorP.permission_name = u'editor'
    editorP.description = u'This permission give an administrative right to the bearer'
    editorP.groups.append(editorG)

    defaultPagesTag = model.Tag()
    defaultPagesTag.label = u'Special:DefaultPage'
    otherTag = model.Tag()
    otherTag.label = u'Other'
    anotherTag = model.Tag()
    anotherTag.label = u'Another Tag'

    welcomePage = model.Page()
    welcomePage.name = u'Welcome'
    welcomePage.title = u'Welcome to VirtualXistenz: where digital dreams come alive'
    welcomePage.author = editorU
    welcomePage.body = u'**Welcome and HelloWorld!**'
    welcomePage.created = datetime.now()
    welcomePage.updated = datetime.now()
    welcomePage.tags.append(defaultPagesTag)
    aboutPage = model.Page()
    aboutPage.name = u'About'
    aboutPage.title = u'VirtualXistenz: What this site is all about'
    aboutPage.author = editorU
    aboutPage.body = u'**To Be...**\n\n*...Continued!*'
    aboutPage.created = datetime.now()
    aboutPage.updated = datetime.now()
    aboutPage.tags.append(defaultPagesTag)
    contactPage = model.Page()
    contactPage.name = u'Contact'
    contactPage.title = u'How to get a hold of us (me)'
    contactPage.author = editorU
    contactPage.body = u'Yes, well, about that...' + unicode(editorU.email_address)
    contactPage.created = datetime.now()
    contactPage.updated = datetime.now()
    contactPage.tags.append(defaultPagesTag)
    somePage = model.Page()
    somePage.name = u'SomePage'
    somePage.title = u'VirtualXistenz: Where digital dreams come alive'
    somePage.author = editorU
    somePage.body = u'*Welcome and HelloWorld!*\n\nBlah Blah'
    somePage.created = datetime.now()
    somePage.updated = datetime.now()
    somePage.tags.append(defaultPagesTag)

    specialPagesCollection = model.Collection()
    specialPagesCollection.label = u'Special Pages'
    specialPagesCollection.pages.append(welcomePage)
    specialPagesCollection.pages.append(aboutPage)
    specialPagesCollection.pages.append(contactPage)

    testCategory = model.Category()
    testCategory.label = u'Testing'

    try:
        model.DBSession.add(testCategory)
        model.DBSession.add(anotherTag)
        model.DBSession.add(defaultPagesTag)
        model.DBSession.add(otherTag)
        model.DBSession.add(editorG)
        model.DBSession.add(editorP)
        model.DBSession.add(editorU)
        model.DBSession.add(welcomePage)
        model.DBSession.add(aboutPage)
        model.DBSession.add(contactPage)
        model.DBSession.add(somePage)
        model.DBSession.flush()
        transaction.commit()
    except IntegrityError:
        print 'Warning, there was a problem adding your auth data, it may have already been added:'
        import traceback
        print traceback.format_exc()
        transaction.abort()
        print 'Continuing with bootstrapping...'
