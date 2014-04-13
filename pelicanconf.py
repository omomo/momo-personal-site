#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Momo Ong'
SITENAME = u"Momo Ong"
SITEURL = ''

TIMEZONE = 'US/Eastern'

#Navigation sections and relative URL:
SECTIONS = [
        ('Blog', 'index.html'),
        ('Archive', 'archives.html'),
        ('Tags', 'tags.html'),
        ('About', 'pages/about.html')
        ]

DEFAULT_LANG = u'en'

DEFAULT_CATEGORY = 'Uncategorized'
DATE_FORMAT = {
'en': '%d %m %Y'
}
DEFAULT_DATE_FORMAT = '%d %m %Y'

# DISQUS_SITENAME = "your_disqus_user"
# TWITTER_USERNAME = 'your_twitter_user_without @'
LINKEDIN_URL = 'http://linkedin.com/in/momoong'
GITHUB_URL = 'http://github.com/omomo'
# FACEBOOK_URL = 'http://www.facebook.com/you'
# GOOGLEPLUS_URL = 'https://plus.google.com/your_profile_id/posts'
# PINTEREST_URL = 'http://pinterest.com/you'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

THEME = "themes/flasky"

# Blogroll
# LINKS =  (('Pelican', 'http://getpelican.com/'),
#           ('Python.org', 'http://python.org/'),
#           ('Jinja2', 'http://jinja.pocoo.org/'),
#           ('You can modify those links in your config file', '#'),)

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

PDF_GENERATOR = False
REVERSE_CATEGORY_ORDER = True
LOCALE = ""
DEFAULT_PAGINATION = 10

FEED_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

OUTPUT_PATH = '/your/output/directory'

# GOOGLE_ANALYTICS_ACCOUNT = 'UA-00000000-1'

# PIWIK_URL = 'myurl.com/piwik'
# PIWIK_SSL_URL = 'myurl.com/piwik'
# PIWIK_SITE_ID = '1'

# MAIL_USERNAME = 'your_user'
# MAIL_HOST = 'gmail.com'

# static paths will be copied under the same name
STATIC_PATHS = ["images"]

# A list of files to copy from the source to the destination
#FILES_TO_COPY = (('extra/robots.txt', 'robots.txt'),)
