.. ADR Colorado College Utilities documentation master file, created by
   sphinx-quickstart on Tue Nov 12 17:01:17 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

ADR and Colorado College Utilities Web App Documentation
========================================================
All technical documentation is located at 
https://readthedocs.org/projects/adr-cc-utilities-web-app

.. toctree::
   :maxdepth: 3

Installing
----------
To install this web app, you can either fork/clone the project's source code 
from https://github.com/jermnelson/adr-cc-utilities/:: 

    $ git clone https://github.com/jermnelson/adr-cc-utilities

or download a `zip file <https://github.com/jermnelson/adr-cc-utilities/archive/master.zip>`_
and unzip the  file to create the app's working directory.::

    $ unzip adr-cc-utilities-master.zip adr-cc-utilities

Change directories to the new ``adr-cc-utilities`` directory and run this 
command to install the Python modules required by this web app ::

    $ cd adr-cc-utilities
    $ python setup.py install

Configuration
-------------
To use this web app, you'll need two Flask configuration files, **fedora.cfg** 
and **form-variables.cfg** both located in ``adr-cc-utilities`` directory.
Variables for **fedora.cfg** are listed in the configuration section in the
`Flask Fedora Commons Documentation`_.

Variables in **form-variables.cfg** provide common information, such as 
INSTITUTION_NAME, for the forms used in this web app These variables (and
examples values) are :

=================== ====================================================
`CONTENT_MODELS`    '["adr:adrBasicObject", "adr:adrETD"]'
`INSTITUTION_NAME`  'Colorado College'
`LOCATION`          'Colorado Springs, Colorado'
`RIGHTS_STATEMENTS` 'Copyright by Colorado College, all rights reserved'
=================== ====================================================

Running as a local web app
--------------------------
To run this web app from the command line in either **development** or 
**production** mode, use the following command with these options. 

Run in development mode with default **host** of `0.0.0.0` and default 
**port** of 8003 ::

    $ python server.py dev

Run in production mode with optional `--host` and `--port` options ::

    $ python server.py prod --host=localhost --port=8080

You should now be able to use your web browser of choice to access the web app. In the
default **development** or **production** modes, load http://localhost:8003/ into the
browser's address bar.

Classes and Methods
-------------------

.. automodule:: server
   :members:

.. automodule:: forms
   :members:

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

.. _Flask Fedora Commons Documentation: http://pythonhosted.org/Flask-FedoraCommons/#configuration
.. _Fedora Commons: http://fedora-commons.org/
