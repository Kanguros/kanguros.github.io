URL = 'http://localhost'
PORT = "8080"
SITEURL = f'{URL}:{PORT}'
RELATIVE_URLS = True

TIMEZONE = 'Europe/Warsaw'
AUTHOR = 'Kamil Urbanek'
DEFAULT_LANG = 'en'
DEFAULT_DATE_FORMAT = "%Y-%m-%d"

PLUGINS = [
    'yaml_metadata',
    'similar_posts',
    'readtime',
    'sitemap',
    'neighbors',
    # 'minify',  In publishconf.py
]

# readtime
LANG_SETTINGS = 150

# similarposts
SIMILAR_POSTS_ENABLED = True
SIMILAR_POSTS_MAX_COUNT = 3
SIMILAR_POSTS_MIN_SCORE = 0.0001

# minify
CSS_MIN = True
HTML_MIN = True
INLINE_CSS_MIN = True
INLINE_JS_MIN = True

SITENAME = "Code Scratchpad"
SITEINFO = "Welcome to my digital notepad, a space where I share my notes and thoughts on programming, pipelines, automation, and an array of other, yet to be discovered, buzzwords."

THEME = 'theme'
THEME_STATIC_DIR = THEME
COLOR_SCHEME_CSS = "darkly.css"
SUMMARY_END_SUFFIX = ''
TYPOGRIFY = True
DIRECT_TEMPLATES = [
    'posts',
    'index',
    'archives',
    'tags',
    'under_construction',
    'notes',
]

TEMPLATE_PAGES = {'notes.html': 'notes/index.html'}
DEFAULT_PAGINATION = 3
PAGINATED_TEMPLATES = {
    'index': None,
    'posts': None,
    'notes': None,
    'tag': None,
    'category': None,
}

STATIC_PATHS = [
    'images',
    'code',
    'slides',
    'extra/.nojekyll',

]
EXTRA_PATH_METADATA = {
    'extra/.nojekyll': {'path': '.nojekyll'},
}

# Paths and other files
PATH = 'content'
OUTPUT_PATH = '_output/'

ARTICLE_PATHS = ['posts', 'notes']
ARTICLE_URL = 'posts/{slug}.html'
ARTICLE_SAVE_AS = 'posts/{slug}.html'
ARTICLE_ORDER_BY = 'reversed-date'

DRAFT_URL = 'notes/{slug}.html'
DRAFT_SAVE_AS = 'notes/{slug}.html'
NOTES_URL = 'notes/index.html'
POSTS_URL = 'posts.html'

PAGE_PATHS = ['pages']
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

TAG_URL = 'tags/{slug}/'
TAG_SAVE_AS = 'tags/{slug}/index.html'
TAGS_SAVE_AS = 'tags/index.html'

CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
CATEGORIES_SAVE_AS = 'categories.html'

ARCHIVES_SAVE_AS = 'archive.html'

AUTHOR_SAVE_AS = ""

GIT_LINK = ('Git', "https://github.com/Kanguros/", 'github'),

OTHER_LINKS = [
    ('Tags', TAGS_SAVE_AS, 'tags'),
    ('Archive', ARCHIVES_SAVE_AS, 'archive'),

]

NAV_LINKS = [
    # Title, URL, Icon
    ('Home', 'index.html', 'house'),
    ('Posts', POSTS_URL, 'journal-code'),
    ('Notes', NOTES_URL, 'file-code'),
    ('About', 'resume.html', 'file-person'),
]

ALL_LINKS = [
    *NAV_LINKS,
    *OTHER_LINKS
]

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.extra': {},
        'markdown.extensions.attr_list': {},
        'markdown.extensions.admonition': {},
        'markdown.extensions.codehilite': {
            'css_class': 'highlight'
        },
        'markdown.extensions.toc': {
            'permalink': 'false',
            'anchorlink': 'true'
        },
        'pymdownx.progressbar': {},
        'pymdownx.blocks.tab': {},
        'pymdownx.snippets': {
            'check_paths': 'true',
            'base_path': "content"
        },
        'pymdownx.magiclink': {},
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
CACHE_CONTENT = False
LOAD_CONTENT_CACHE = False
DELETE_OUTPUT_DIRECTORY = True
