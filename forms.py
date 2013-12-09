"""
Alliance Digital Repository - Colorado College Utilities - Forms
----------------------------------------------------------------

A collection of Flask_WTF forms
"""
__version_info__ = ('0', '0', '1')
__version__ = '.'.join(__version_info__)
__author__ = "Jeremy Nelson"
__license__ = 'Apache License, Version 2.0'
__copyright__ = '(c) 2013 by Jeremy Nelson'

from flask_wtf import Form
from wtforms import DateField, SelectField, TextField, TextAreaField
from wtforms.validators import DataRequired, Length

MARC_FREQUENCY = [('choose', 'Choose...'),
                  ('Semiweekly', 'Semiweekly - 2 times a week'),
                  ('Three times a week', 'Three times a week'),
                  ('Weekly', 'Weekly'),
                  ('Biweekly', 'Biweekly - every 2 weeks'),
                  ('Three times a month', 'Three times a month'),
                  ('Semimonthly', 'Semimonthly - 2 times a month'),
                  ('Monthly', 'Monthly'),
                  ('Bimonthly', 'Bimonthly - every 2 months'),
                  ('Quarterly', 'Quarterly'),
                  ('Three times a year', 'Three times a year'),
                  ('Semiannual', 'Semiannual - 2 times a year'),
                  ('Annual', 'Annual'),
                  ('Biennial', 'Biennial - every 2 years'),
                  ('Triennial', 'Triennial - every 3 years'),
                  ('Completely irregular', 'Completely irregular')]

MARC_LEADER_06 = [('text', 'text'),
                  ('cartographic', 'cartographic'),
                  ('notated music', 'notated music'),
                  ('sound recording-musical', 'sound recording-musical'),
                  ('sound recording-nonmusical', 'sound recording-nonmusical'),
                  ('still image', 'still image'),
                  ('moving image', 'moving image'),
                  ('three dimensional object', 'three dimensional object'),
                  ('software, multimedia', 'software, multimedia'),
                  ('mixed material', 'mixed material')]

DIGITAL_ORIGIN = [(1, 'born digital'),
                  (2, 'reformatted digital'),
                  (3, 'digitized microfilm'),
                  (4, 'digitized other analog')]

OBJECT_TEMPLATES = [(0, 'Choose model'),
                    (1, 'Meeting Minutes'),
                    (2, 'Newsletter'),
                    (3, 'Podcast'),
                    (4, 'Video'),
                    (5, 'Master (All fields)')]

class MODSCommonVariablesForm(Form):
    """CRUD operations on variables that are common to all MODS loads"""
    institution = TextField()
    location = TextField()
    rights_statement = TextField()
    

class MODSFedoraObjectForm(Form):
    admin_note = TextAreaField('Administrative Notes',
                            [Length(max=1500)])
    alt_title = TextField('Alternative Title',
                                )
    collection_pid = TextField("PID of Parent Collection",
                                [DataRequired, Length(max=20)])
    content_model = SelectField("Fedora Content Model",
                                choices=[])

    contributors = TextField("Contributors")
    corporate_contributors = TextField()
    corporate_contributors = TextField()
    corporate_creators = TextField()
    creators = TextField()
    date_created = DateField()
    digital_origin = SelectField(choices=DIGITAL_ORIGIN)
    
    description = TextAreaField('Description',
                                [Length(max=1500)])
    extent = TextAreaField('Extent',
                           [Length(max=1500)])
    form_of = TextField('Form')
    frequency_free_form = TextField('Other')
    frequency = SelectField(choices=MARC_FREQUENCY)
    genre = SelectField()
##    genre = forms.ChoiceField(
##        label='Genre',
##        required=False,
##        widget=forms.Select(
##            attrs={'data-bind': "options: genreOptions, optionsText: 'name', optionsValue: 'value'",
##                   'class': 'form-control'}))
##    genre_free_form = forms.CharField(label='Other',
##                                      required=False,
##                                      widget=forms.TextInput(
##                                              attrs={'class': 'form-control'}))
    number_objects = TextField('Number of stub records',
                               default=1)
    object_template = SelectField('Content Model Template',
                                  choices=OBJECT_TEMPLATES)
    organizations = TextField('Organizations',
                              [Length(max=255)])
    rights_holder = TextField('Rights Statement',
                              [Length(max=255)])
    subject_dates = TextField('Subject -- Dates')
    subject_people = TextField('Subject -- People')
    subject_places = TextField('Subject -- Places')
    subject_topics = TextField('Subject -- Topic')

    title = TextField('Title',
                      [Length(max=120)])
    type_of_resource = SelectField("Type of Resource",
                                   choices=MARC_LEADER_06)
