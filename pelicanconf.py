#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'gauravssnl'
SITENAME = 'Gauravssnl Tech Blog'
SITEURL = 'https://gauravssnl.github.io'
# Legal
SITE_LICENSE = """
&copy; Copyright 2020 by Gaurav (@gauravssnl) and licensed under a <a rel="license"
  href="http://creativecommons.org/licenses/by/4.0/">
  <img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/80x15.png" />
  Creative Commons Attribution 4.0 International License</a>.
"""
PATH = 'content'

TIMEZONE = 'Asia/Kolkata'

DEFAULT_LANG = 'English'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'https://getpelican.com/'),
#          ('Python.org', 'https://www.python.org/'),
#          ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
#          ('You can modify those links in your config file', '#'),)

# # Social widget
SOCIAL = (
    ("Github", "https://github.com/gauravssnl", "Github"),
    ("LinkedIn", "https://www.linkedin.com/in/gauravssnl/", "LinkedIn"),
    ("Twitter", "https://twitter.com/gauravssnl", "Twitter"),
    ('Email', 'gauravssnl@gmail.com', 'My Email Address', "Email"),
    ("RSS", SITEURL + "/feeds/all.atom.xml", "RSS"),
    
)
SOCIAL_PROFILE_LABEL = u'Stay in Touch'

# Pagination
DEFAULT_PAGINATION = 20

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
# import alchemy
# THEME = alchemy.path()
# THEME = "notmyidea"
# THEME = "simple"
# CSS_FILE = "wide.css"
THEME = "themes/elegant-master"

ARTICLE_PATHS = ['blog']
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}'

TWITTER_USERNAME = "gauravssnl"

FOOTER_LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

DIRECT_TEMPLATES = ['404', 'search', 'index', 'tags', 'categories','archives']

# Plugins and extensions
MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.admonition": {},
        "markdown.extensions.codehilite": {"css_class": "highlight"},
        "markdown.extensions.extra": {},
        "markdown.extensions.meta": {},
        "markdown.extensions.toc": {"permalink": " "},
    }
}

PLUGIN_PATHS = ["plugins/"]
PLUGINS = [
    "extract_toc",
    "liquid_tags.img",
    "liquid_tags.include_code",
    "neighbors",
    "related_posts",
    "render_math",
    "series",
    "share_post",
    "tipue_search",
    "post_stats",
    "sitemap",
    "assets",
]

SITEMAP = {
    "format": "xml",
    "priorities": {"articles": 0.5, "indexes": 0.5, "pages": 0.5},
    "changefreqs": {"articles": "monthly", "indexes": "daily", "pages": "monthly"},
}

# Hide About
# DISPLAY_PAGES_ON_MENU = True
# DISPLAY_CATEGORIES_ON_MENU = True
# USE_FOLDER_AS_CATEGORY = False
# PAGE_PATHS = ['pages']
# # Add page titles here if you don't want them linked to automatically
# EXCLUDED_PAGES = ['Web Chat']

# Additional main menue items
# MENUITEMS = [
#     ('<i class="fas fa-info-circle"></i> About', '/pages/about.html'),
#     ('<i class="fas fa-file-powerpoint"></i> Presentations', '/pages/presentations.html'),
#     ('<i class="fab fa-discord"></i> Discord Chat <i class="fas fa-external-link-alt"></i>', 'https://discord.gg/ch7TPCx'),
#     ('<i class="fab fa-meetup"></i> Meetup Group <i class="fas fa-external-link-alt"></i>', 'https://www.meetup.com/Phoenix-Python-Meetup-Group/'),
# ]

STATIC_PATHS = ['images', 'extra/robots.txt', 'extra/favicon.ico', 'extra/googlec4c83e4356cde945.html']
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/googlec4c83e4356cde945.html': {'path' : 'googlec4c83e4356cde945.html'},
}
