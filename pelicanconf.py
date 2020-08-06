#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Damani'
SITENAME = 'Damani blog'
SITEURL = 'https://damani42.github.io'
GITHUB_URL = 'https://github.com/damani42'
TWITTER_USERNAME = 'ewe'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Jinja2', 'http://jinja.pocoo.org/'),
         ('Victor Stinner', 'https://vstinner.github.io/'),
         ('Hervé Beraud', 'https://herve.beraud.io'))

# Social widget
SOCIAL = (('github', 'https://github.com/damani42'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True