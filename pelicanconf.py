#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Yang Sun'
SITENAME = u'Yang Sun'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Dublin'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (#('Pelican', 'http://getpelican.com/'),
         #('Python.org', 'http://python.org/'),
         #('Jinja2', 'http://jinja.pocoo.org/'),
         #('You can modify those links in your config file', '#'),
         )

# Social widget
SOCIAL = (('LinkedIn', 'https://ie.linkedin.com/in/yangsuntcd'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME="pelican-themes/simple"

# The name of the subfolder is not  category name
USE_FOLDER_AS_CATEGORY = False

DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False

# The number of words from the beginning of an article are used as the summary
SUMMARY_MAX_LENGTH = 100

# Static path to be copied as is under 'output/'
STATIC_PATHS = [
    'images',
    'pages',
    'posts',
    'extra',
    #'extra/favicon.ico'
]

EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/CNAME': {'path': 'CNAME'},
    'extra/README.md': {'path': 'README.md'},
    'extra/karmatic_arcade.ttf': {'path': 'theme/css/karmatic_arcade.ttf'},
    #'extra/favicon.ico': {'path': 'favicon.ico'}
}

ARTICLE_SAVE_AS = 'posts/{date:%Y-%m}/{slug}.html'
ARTICLE_URL = 'posts/{date:%Y-%m}/{slug}.html'
PAGE_URL = 'pages/{slug}.html'
PAGE_SAVE_AS = 'pages/{slug}.html'

LANDING_PAGE_ABOUT = True
