"""
Alliance Digital Repository - Colorado College Utilities
--------------------------------------------------------

A simple web-based application for a number of management and ingestion
tasks for a Fedora Commons digital repository.
"""
__version_info__ = ('0', '0', '1')
__version__ = '.'.join(__version_info__)
__author__ = "Jeremy Nelson"
__license__ = 'Apache License, Version 2.0'
__copyright__ = '(c) 2013 by Jeremy Nelson'

from flask import Flask, request, session, redirect, url_for
from flask import abort, render_template, flash
from flask_fedora_commons import FedoraCommons

app = Flask(__app__)
app.config.from_pyfile('fedora.cfg')
fedora = FedoraCommons(app)
