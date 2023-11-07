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
    'neighbors',
    # 'sitemap',  In publishconf.py
    # 'minify',  In publishconf.py
]

# readtime
LANG_SETTINGS = 120

# similarposts
SIMILAR_POSTS_ENABLED = True
SIMILAR_POSTS_MAX_COUNT = 3
SIMILAR_POSTS_MIN_SCORE = 0.0001

# minify
CSS_MIN = True
HTML_MIN = True
INLINE_CSS_MIN = True
INLINE_JS_MIN = False

SITENAME = "Kamil's Scratchpad"
SITENAME_BRAND = "KS"
SITEINFO = "Welcome to my digital notepad. Space where <strong>I share</strong> my <strong>notes and thoughts</strong> on <strong>programming, pipelines, automation,</strong> and an array of other, yet to be discovered, fancy stuff."

THEME = 'theme'
THEME_STATIC_DIR = THEME
COLOR_SCHEME_CSS = "darkly.css"
SUMMARY_END_SUFFIX = ''
TYPOGRIFY = True
DIRECT_TEMPLATES = [
    'index',
    'archives',
    'categories',
    'tags',
    'under_construction',
    'homepage',
]

TEMPLATE_PAGES = {'homepage.html': 'index.html'}
DEFAULT_PAGINATION = 5
PAGINATED_TEMPLATES = {
    'index': None,
    'tag': None,
    'category': None,
}

STATIC_PATHS = [
    'images',
    'code',
    # 'slides',
    'extra/.nojekyll',

]
EXTRA_PATH_METADATA = {
    'extra/.nojekyll': {'path': '.nojekyll'},
}

# Paths and other files
PATH = 'content'
OUTPUT_PATH = '_output/'

INDEX_SAVE_AS = "all_posts.html"

ARCHIVES_SAVE_AS = 'archive.html'

AUTHOR_SAVE_AS = ""

ARTICLE_PATHS = ['posts', 'notes']
ARTICLE_URL = '{category}/{slug}.html'
ARTICLE_SAVE_AS = '{category}/{slug}.html'
ARTICLE_ORDER_BY = 'reversed-date'

DRAFT_URL = 'drafts/{slug}.html'
DRAFT_SAVE_AS = 'drafts/{slug}.html'

PAGE_PATHS = ['pages']
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}.html'

TAG_URL = 'tags/{slug}.html'
TAG_SAVE_AS = 'tags/{slug}.html'
TAGS_SAVE_AS = 'tags.html'

CATEGORY_URL = '{slug}s.html'
CATEGORY_SAVE_AS = '{slug}s.html'
CATEGORIES_SAVE_AS = 'categories.html'
CATEGORY_ARTICLES_URL = "articles.html"
CATEGORY_NOTES_URL = "notes.html"
DEFAULT_CATEGORY = "Note"

GIT_LINK = "https://github.com/Kanguros/"

OTHER_LINKS = [
    ('Archive', ARCHIVES_SAVE_AS, 'archive'),

]

NAV_LINKS = [
    # Title, URL, Icon
    # ('Home', 'index.html', 'house'),
    ('Articles', CATEGORY_ARTICLES_URL, 'journal-code'),
    ('Notes', CATEGORY_NOTES_URL, 'file-code'),
    ('Tags', TAGS_SAVE_AS, 'tags'),
    ('About', 'about.html', 'file-person'),
]

ALL_LINKS = [
    *NAV_LINKS
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
