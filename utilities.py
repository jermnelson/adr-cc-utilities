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
from flask import abort, jsonify, render_template, flash
#! Hack to load Fedora commons Flask Extension for test and usage
import sys
sys.path.append("C:\\Users\\jernelson\\Development\\flask-fedora")
from flask_fedora_commons import FedoraCommons

app = Flask(__name__)
app.config.from_pyfile('fedora.cfg')
fedora = FedoraCommons(app)

@app.route('/')
def default():
    "Default view of utilities"
    return render_template('index.html')
                           

@app.route("/pid-mover", methods=['POST', 'GET'])
def pid_mover():
    "PID Mover view"
    # Should be an AJAX call
    if request.method == 'POST':
        collection_pid = request.form['collection_pid']
        source_pid = request.form['source_pid']
        if not fedora.move(source_pid, collection_pid):
            result = "error"
            msg = "Could not move {0} to {1} collection".format(
                source_pid,
                collection_pid)
        else:
            result = "ok",
            msg = "{0} moved to {1} collection".format(
                source_pid,
                collection_pid)
        return jsonify(**{"result": result,
                          "message": msg})
    return render_template("pid-mover.html",
                           section='mover')

@app.route("/batch-template-add",)
def batch_template_add():
    """View for adding one or more Fedora objects to the repository by using a
    template."""
    return render_template('batch-template-add.html',
                           section='batch-add')

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
