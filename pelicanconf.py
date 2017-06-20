#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Brian Jimenez-Garcia'
SITENAME = u'Bioinformatics Sandbox'
SITEURL = ''
SITESUBTITLE = '/bio'
SITETAGLINE = 'Sandbox'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'English'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

LOCALE = ('en_US', 'es_ES')

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),)

# Social widget
SOCIAL = (('Github', 'https://github.com/brianjimenez'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = "themes/bjg"
