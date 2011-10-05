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

    adminU = model.User()
    adminU.user_name = u'ravenoak'
    adminU.display_name = u'Caitlyn O\'Hanna'
    adminU.email_address = u'caitlyn.ohanna@virtualxistenz.com'
    adminU.password = u'Passw0rd'

    manageG = model.Group()
    manageG.group_name = u'managers'
    manageG.display_name = u'Managers Group'
    manageG.users.append(adminU)

    manageP = model.Permission()
    manageP.permission_name = u'managers'
    manageP.description = u'This permission give an administrative right to the bearer'
    manageP.groups.append(manageG)

    welcomePage = model.Page()
    welcomePage.name = u'Welcome'
    welcomePage.title = u'Welcome to VirtualXistenz: where digital dreams come alive'
    welcomePage.author = adminU
    welcomePage.body = u'**Welcome and HelloWorld!**'
    welcomePage.created = datetime.now()
    welcomePage.updated = datetime.now()

    aboutPage = model.Page()
    aboutPage.name = u'About'
    aboutPage.title = u'VirtualXistenz: What this site is all about'
    aboutPage.author = adminU
    aboutPage.body = u'**To Be...**\n\n*...Continued!*'
    aboutPage.created = datetime.now()
    aboutPage.updated = datetime.now()

    contactPage = model.Page()
    contactPage.name = u'Contact'
    contactPage.title = u'How to get a hold of us (me)'
    contactPage.author = adminU
    contactPage.body = u'...' + unicode(adminU.email_address)
    contactPage.created = datetime.now()
    contactPage.updated = datetime.now()

    somePage = model.Page()
    somePage.name = u'SomePage'
    somePage.title = u'VirtualXistenz: Where digital dreams come alive'
    somePage.author = adminU
    somePage.body = u'*Welcome and HelloWorld!*\n\nBlah Blah'
    somePage.created = datetime.now()
    somePage.updated = datetime.now()

    try:
        model.DBSession.add(manageG)
        model.DBSession.add(manageP)
        model.DBSession.add(adminU)
        model.DBSession.add(welcomePage)
        model.Tagging.set_tags(welcomePage, 'default')
        model.DBSession.add(aboutPage)
        model.Tagging.set_tags(aboutPage, 'default')
        model.DBSession.add(contactPage)
        model.Tagging.set_tags(contactPage, 'default')
        model.DBSession.add(somePage)
        model.Tagging.set_tags(somePage, 'default')
        model.DBSession.flush()
        transaction.commit()
    except IntegrityError:
        print 'Warning, there was a problem adding your auth data, it may have already been added:'
        import traceback
        print traceback.format_exc()
        transaction.abort()
        print 'Continuing with bootstrapping...'
