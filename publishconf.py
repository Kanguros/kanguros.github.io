import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = "https://kanguros.github.io"
RELATIVE_URLS = False
PLUGINS = PLUGINS + ['sitemap']

# Plugin - minify
CSS_MIN = True
HTML_MIN = True
INLINE_CSS_MIN = True
INLINE_JS_MIN = False

# PLUGINS = PLUGINS + ['minify', 'sitemap']
