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
#! Hack to load Fedora commons Flask Extension for test and usage
import sys
sys.path.append("C:\\Users\\jernelson\\Development\\flask-fedora")
from flask_fedora_commons import FedoraCommons

app = Flask(__name__)
app.config.from_pyfile('fedora.cfg')
fedora = FedoraCommons(app)

@app.route('/')
def default():
    return "ADR-CC Utilities, fedora={0}".format(fedora.__doc__)

if __name__ == '__main__':
    host = '0.0.0.0'
    port = 8003
    mode = 'dev'
    if mode == 'dev':
        app.run(host=host,
                port=port,
                debug=True)
    else:
        app.run(host=host,
                port=port)
