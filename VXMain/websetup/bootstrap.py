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
from PIL import Image

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
    adminP.description = u'This permission gives an administrative right to the bearer'
    adminP.groups.append(adminG)

    welcomePage = model.Page(label = u'Welcome')
    welcomePage.title = u'Welcome to VirtualXistenz: where digital dreams come alive'
    welcomePage.body = u'**Welcome and HelloWorld!**'

    testProj = model.Project(label = u'Test Project')
    testGuide = model.Guide(label = u'Test Guide')

    aboutPage = model.Page(label = u'About')
    aboutPage.title = u'VirtualXistenz: What this site is all about'
    aboutPage.body = u'**To Be...**\n\n*...Continued!*'
    #aboutPage.author = adminU

    contactPage = model.Page(label = u'Contact')
    contactPage.title = u'How to get a hold of us (me)'
    contactPage.body = u'...' + unicode(adminU.email_address)
    #contactPage.author = adminU

    img = Image.open('078ee2af3097a206.jpg')
    imgraw = file('078ee2af3097a206.jpg', 'rb')
    testImage = model.Image(label = u'Lotus')
    testImage.data = imgraw.read()
    testImage.mode = img.mode
    testImage.sizex, testImage.sizey = img.size
    testImage.encoding = img.format

    somePage = model.Page(label = u'SomePage')
    somePage.title = u'VirtualXistenz: Where digital dreams come alive'
    somePage.body = u'*Welcome and HelloWorld!*\n\nBlah Blah'
    #somePage.author = adminU
    somePage.resources.append(testImage)




    try:
        model.DBSession.add(adminG)
        model.DBSession.add(adminP)
        model.DBSession.add(adminU)
        model.DBSession.add(welcomePage)
        model.DBSession.add(testProj)
        model.DBSession.add(testGuide)
        model.DBSession.add(aboutPage)
        model.DBSession.add(contactPage)
        model.DBSession.add(testImage)
        model.DBSession.add(somePage)
        model.DBSession.flush()
        transaction.commit()
    except IntegrityError:
        print 'Warning, there was a problem adding your data'
        import traceback
        print traceback.format_exc()
        transaction.abort()
