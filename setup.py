"""
Setup for Alliance Digital Repository - Colorado College Utilities
------------------------------------------------------------------

This Flask application provides a lightweight app for a number of utilities
to help manage a Fedora Commons digital repository
"""
__version_info__ = ('0', '0', '1')
__version__ = '.'.join(__version_info__)
__author__ = "Jeremy Nelson"
__license__ = 'Apache License, Version 2.0'
__copyright__ = '(c) 2013 by Jeremy Nelson'

from setuptools import setup

setup(
    name='ADR Colorado College Utilities',
    version='0.0.1',
    url='http://github.com/jermnelson/adr-cc-utilities',
    license='Apache License, Version 2.0',
    author=__author__,
    author_email='jermnelson@gmail.com',
    description='App for simple management tasks for Fedora digital repository.',
    long_description=__doc__,
    py_modules=['utilities'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',
        'Flask-FedoraCommons'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache 2 License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Framework :: Flask',
        'Topic :: Software Development :: Libraries :: Python Modules'

    ]
)
