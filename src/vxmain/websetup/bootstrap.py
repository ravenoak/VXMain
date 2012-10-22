# -*- coding: utf-8 -*-
"""Setup the vxmain application"""

import logging
from tg import config
from PIL import Image
from vxmain import model
import transaction

def bootstrap(command, conf, vars):
    """Place any commands to setup vxmain here"""

    # <websetup.bootstrap.before.auth
    from sqlalchemy.exc import IntegrityError
    try:
#        u = model.User()
#        u.user_name = u'manager'
#        u.display_name = u'Example manager'
#        u.email_address = u'manager@somedomain.com'
#        u.password = u'managepass'
#    
#        model.DBSession.add(u)
#    
#        g = model.Group()
#        g.group_name = u'managers'
#        g.display_name = u'Managers Group'
#    
#        g.users.append(u)
#    
#        model.DBSession.add(g)
#    
#        p = model.Permission()
#        p.permission_name = u'manage'
#        p.description = u'This permission give an administrative right to the bearer'
#        p.groups.append(g)
#    
#        model.DBSession.add(p)
    
        u1 = model.User()
        u1.user_name = u'editor'
        u1.display_name = u'Example editor'
        u1.email_address = u'editor@somedomain.com'
        u1.password = u'editpass'
        
        
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
        
        
        model.DBSession.add(u1)
        model.DBSession.flush()
        transaction.commit()
    except IntegrityError:
        print 'Warning, there was a problem adding your auth data, it may have already been added:'
        import traceback
        print traceback.format_exc()
        transaction.abort()
        print 'Continuing with bootstrapping...'

    # <websetup.bootstrap.after.auth>
