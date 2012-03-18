# -*- coding: utf-8 -*-
"""Setup the VXMain application"""

# investigate
import logging
# investigate
from tg import config
from datetime import datetime
from VXMain import model
import transaction
import uuid

# why is it wanting command, conf...vars?!?!
def bootstrap(command, conf, vars):
    """Place any commands to setup VXMain here"""

    from sqlalchemy.exc import IntegrityError

    adminU = model.User(user_name = u'ravenoak',
                        display_name = u'Caitlyn O\'Hanna',
                        email_address = u'caitlyn.ohanna@virtualxistenz.com',
                        password = u'Passw0rd')

    adminG = model.Group()
    adminG.group_name = u'administrators'
    adminG.display_name = u'Administrators Group'
    adminG.users.append(adminU)

    adminP = model.Permission()
    adminP.permission_name = u'administrators'
    adminP.description = u'This permission give an administrative right to the bearer'
    adminP.groups.append(adminG)

    welcomePage = model.Page(u'Welcome')
    welcomePage.title = u'Welcome to VirtualXistenz: where digital dreams come alive'
    welcomePage.body = u'**Welcome and HelloWorld!**'

    testProj = model.Project(u'Test Project')
    testGuide = model.Guide(u'Test Guide')

    aboutPage = model.Page(u'About')
    aboutPage.title = u'VirtualXistenz: What this site is all about'
    aboutPage.body = u'**To Be...**\n\n*...Continued!*'
    #aboutPage.author = adminU

    contactPage = model.Page(u'Contact')
    contactPage.title = u'How to get a hold of us (me)'
    contactPage.body = u'...' + unicode(adminU.email_address)
    #contactPage.author = adminU

    somePage = model.Page(u'SomePage')
    somePage.title = u'VirtualXistenz: Where digital dreams come alive'
    somePage.body = u'*Welcome and HelloWorld!*\n\nBlah Blah'
    #somePage.author = adminU

    try:
        model.DBSession.add(adminG)
        model.DBSession.add(adminP)
        model.DBSession.add(adminU)
        model.DBSession.add(welcomePage)
        model.DBSession.add(testProj)
        model.DBSession.add(testGuide)
        model.DBSession.add(aboutPage)
        model.DBSession.add(contactPage)
        model.DBSession.add(somePage)
        model.DBSession.flush()
        transaction.commit()
    except IntegrityError:
        print 'Warning, there was a problem adding your data'
        import traceback
        print traceback.format_exc()
        transaction.abort()
