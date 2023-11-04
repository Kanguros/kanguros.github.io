import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = "https://kanguros.github.io"
RELATIVE_URLS = False
PLUGINS = PLUGINS + ['minify', 'sitemap']
