#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Python Latvia'
SITENAME = 'Python Latvia'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Riga'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (
    ('Meetup', 'http://bit.ly/pythonlv-meetup'),
    ('@pythonlv', 'http://bit.ly/pythonlv-tw'),
    ('Facebook', 'http://bit.ly/pythonlv-fb'),
    ('Google Plus', 'http://bit.ly/pythonlv-plus'),
    ('GitHub', 'http://bit.ly/pythonlv-gh'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
THEME = "themes/pelican-bootstrap3"
