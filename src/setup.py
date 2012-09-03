# -*- coding: utf-8 -*-
#quckstarted Options:
#
# sqlalchemy: True
# auth:       sqlalchemy
# mako:       False
#
#

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

setup(
    name='VXMain',
    version='0.1',
    description='',
    author='',
    author_email='',
    #url='',
 testpkgs=['WebTest >= 1.2.3',
                'nose',
                'coverage',
                'wsgiref',
                ],
 install_requires=[
     "TurboGears2 >= 2.2.0",
     "Genshi",
     "zope.sqlalchemy >= 0.4",
     "repoze.tm2 >= 1.0a5",
     "sqlalchemy",
     "sqlalchemy-migrate",
     "repoze.who",
     "repoze.who-friendlyform >= 1.0.4",
     "tgext.admin >= 0.5.1",
     "repoze.who.plugins.sa",
     "tw2.forms",
     ],
    setup_requires=["PasteScript >= 1.7"],
    paster_plugins=['PasteScript', 'Pylons', 'TurboGears2'],
    packages=find_packages(exclude=['ez_setup']),
    include_package_data=True,
    test_suite='nose.collector',
    tests_require=['WebTest',
                   'nosetests',
                   'coverage',
                   'wsgiref'
                   'repoze.who-testutil >= 1.0',
                   ],
    package_data={'VXMain': ['i18n/*/LC_MESSAGES/*.mo',
                                 'templates/*/*',
                                 'public/*/*']},
    message_extractors={'VXMain': [
            ('**.py', 'python', None),
            ('templates/**.mako', 'mako', None),
            ('templates/**.html', 'genshi', None),
            ('public/**', 'ignore', None)]},

    entry_points="""
    [paste.app_factory]
    main = VXMain.config.middleware:make_app

    [paste.app_install]
    main = pylons.util:PylonsInstaller
    """,
)
