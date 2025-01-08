URL = 'http://localhost'
PORT = "8080"
SITEURL = f'{URL}:{PORT}'
RELATIVE_URLS = True

TIMEZONE = 'Europe/Warsaw'
AUTHOR = 'Kamil Urbanek'
DEFAULT_LANG = 'en'
DEFAULT_DATE_FORMAT = "%Y-%m-%d"

# Paths and other files
PATH = 'content'
OUTPUT_PATH = '_output/'

# Plugins
PLUGINS = [
    'yaml_metadata',
    'similar_posts',
    'readtime',
    'neighbors',
    "pelican.plugins.jinja_filters",
    # 'sitemap',  In publishconf.py
    # 'minify',  In publishconf.py
]

# Plugin - readtime
LANG_SETTINGS = 120

# Plugin - similarposts
SIMILAR_POSTS_ENABLED = False
SIMILAR_POSTS_MAX_COUNT = 3
SIMILAR_POSTS_MIN_SCORE = 0.0001

# # Plugin - minify
# CSS_MIN = True
# HTML_MIN = True
# INLINE_CSS_MIN = True
# INLINE_JS_MIN = False

SITENAME = "Kamil's Scratchpad"
SITENAME_BRAND = "KS"
SITEINFO = """
<p>Welcome to my digital notepad.</p>
<p>Space where <strong>I share</strong> my <strong>notes and thoughts</strong> on 
<strong>programming, pipelines, automation,</strong> 
and an array of other, yet to be discovered, fancy stuff.</p>
"""

THEME_STATIC_DIR = THEME = "theme"
COLOR_SCHEME_CSS = "darkly.css"
SUMMARY_END_SUFFIX = ''
TYPOGRIFY = True

DIRECT_TEMPLATES = [
    'index',
    'archives',
    'tags',
    'under_construction',
    'privates',
]

DEFAULT_PAGINATION = 5
PAGINATED_TEMPLATES = {
    'index': None,
    'tag': None,
}

TEMPLATE_PAGES = {'privates.html': 'private/index.html'}

STATIC_PATHS = [
    'images',
    'code',
    'extra/.nojekyll',
    # 'slides',

]
EXTRA_PATH_METADATA = {
    'extra/.nojekyll': {'path': '.nojekyll'},
}

INDEX_SAVE_AS = 'index.html'
ARCHIVES_SAVE_AS = 'archive.html'
ABOUT_URL = "about.html"

AUTHOR_SAVE_AS = ""
CATEGORY_SAVE_AS = ""
CATEGORIES_SAVE_AS = ""

ARTICLE_PATHS = ['private', 'posts']
ARTICLE_URL = 'post/{slug}.html'
ARTICLE_SAVE_AS = 'post/{slug}.html'
ARTICLE_ORDER_BY = 'reversed-date'

DRAFTS_URL = "private/index.html"
DRAFT_URL = 'private/{slug}.html'
DRAFT_SAVE_AS = 'private/{slug}.html'

PAGE_PATHS = ['pages']
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'

TAG_URL = 'tag/{slug}.html'
TAG_SAVE_AS = 'tag/{slug}.html'
TAGS_SAVE_AS = 'tag/index.html'
TAGS_DESCRIPTION = {
    "python": "Knowledge of Python",
    "cheatsheet": "Shortcut of tips and tricks."
}

DEFAULT_CATEGORY = "post"

GIT_LINK = "https://github.com/Kanguros/"
NAV_LINKS = [
    ('Tags', TAGS_SAVE_AS, 'tags'),
    ('About', ABOUT_URL, 'file-person'),
    ('Git', GIT_LINK, 'github'),
]

FOOTER_LINKS = [
    ('Index', "", 'home'),
    *NAV_LINKS,

]

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.extra': {},
        # 'markdown.extensions.attr_list': {},
        'markdown.extensions.admonition': {},
        'markdown.extensions.codehilite': {
            'css_class': 'highlight'
        },
        'markdown.extensions.toc': {
            'permalink': 'false',
            'anchorlink': 'true',
            'toc_depth': 3,
            'title': 'Content'
        },
        'pymdownx.progressbar': {},
        'pymdownx.blocks.tab': {},
        'pymdownx.snippets': {
            'check_paths': 'true',
            'base_path': "content"
        },
        'pymdownx.magiclink': {},
        'markdown_extension_mermaid': {},
    },
    'output_format': 'html5'
}

# RSS and ATOM feeds
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
# CACHING

CACHE_CONTENT = True
LOAD_CONTENT_CACHE = True
GZIP_CACHE = False
DELETE_OUTPUT_DIRECTORY = False
