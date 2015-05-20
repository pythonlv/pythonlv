#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = 'Python Latvia'
SITENAME = 'Python Latvia'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Riga'

DEFAULT_LANG = 'en'
DEFAULT_DATE_FORMAT = '%Y-%m-%d'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
)

# Social widget
SOCIAL = (
    ('Meetup', 'http://bit.ly/pythonlv-meetup'),
    ('Twitter', 'http://bit.ly/pythonlv-tw'),
    ('Facebook', 'http://bit.ly/pythonlv-fb'),
    ('Google Plus', 'http://bit.ly/pythonlv-plus'),
    ('GitHub', 'http://bit.ly/pythonlv-gh'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
THEME = "themes/built-texts/"
TWITTER_USERNAME = 'pythonlatvia'
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = [
    'google_embed',
    'extended_sitemap',
]
GMAPS_KEY = 'AIzaSyBGSFTSfCZvGCg6IPTrkVZyXj6EUPQPLtY'
