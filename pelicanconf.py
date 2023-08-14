URL = 'http://localhost'
PORT = "8080"
SITEURL = f'{URL}:{PORT}'
RELATIVE_URLS = True

TIMEZONE = 'Europe/Warsaw'
AUTHOR = 'Kamil Urbanek'
DEFAULT_LANG = 'en'
DEFAULT_CATEGORY = "Personal"
DEFAULT_DATE_FORMAT = "%d/%m/%Y"
DATE_FORMATS = {'en': "%d/%m/%Y"}
LOCALE = ('en_US',)

PLUGINS = [
    'yaml_metadata',
    'similar_posts',
    'readtime',
    'sitemap',
    'neighbors',
]

SITENAME = "Kamil's Scratchpad"
SITEINFO = "Welcome to my digital notepad, a space where I share my notes and thoughts on programming, pipelines, automation, and an array of other, yet to be discovered, buzzwords."
SITELINKS = (
    # ('About', 'about/index.html', 'file-person'),
    ('About', 'resume.html', 'file-person'),
    # ('About', 'under_construction.html', 'file-person'),
    ('Git', "https://github.com/Kanguros/", 'github'),
)

THEME = 'theme'
THEME_STATIC_DIR = THEME
# THEME_DEFAULT_HEADER = "home-bg.png"
THEME_DEFAULT_HEADER = "home-bg.jpg"
COLOR_SCHEME_CSS = "monokai.css"
SUMMARY_END_SUFFIX = ''
TYPOGRIFY = True
DIRECT_TEMPLATES = [
    'index',
    'archives',
    'tags',
    'under_construction',
    'notes',
    # 'resume'
]
PAGINATED_DIRECT_TEMPLATES = [
    'index',
    'notes'
]

STATIC_PATHS = [
    'images',
    'slides',
    'extra/.nojekyll',

]
EXTRA_PATH_METADATA = {
    'extra/.nojekyll': {'path': '.nojekyll'},
}

DEFAULT_PAGINATION = 3

# Paths and other files
PATH = 'content'
OUTPUT_PATH = 'local_output/'

ARTICLE_PATHS = ['posts', 'raw_notes']
ARTICLE_URL = 'posts/{slug}.html'
ARTICLE_SAVE_AS = 'posts/{slug}.html'
ARTICLE_ORDER_BY = 'reversed-date'

PAGE_PATHS = ['pages']
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

TAG_URL = 'tags/{slug}/'
TAG_SAVE_AS = 'tags/{slug}/index.html'
TAGS_SAVE_AS = 'tags.html'

CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
CATEGORIES_SAVE_AS = 'categories.html'

ARCHIVES_SAVE_AS = 'archive.html'

NOTES_URL = 'notes.html'
EXCLUDED_CATEGORIES = ['notes']

PAGESMENUITEMS = [
    ('Tags', TAGS_SAVE_AS, 'tags'),
    ('Notes', NOTES_URL, 'journal-code'),
    ('Archive', ARCHIVES_SAVE_AS, 'archive'),
]

MENUITEMS = [
    # Title, URL, Icon
    ('Index', 'index.html', 'house'),
    *PAGESMENUITEMS
]

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.extra': {},
        'markdown.extensions.attr_list': {},
        'markdown.extensions.admonition': {},
        'markdown.extensions.codehilite': {
            'css_class': 'highlight'},
        'markdown.extensions.toc': {
            'permalink': 'false'},
        'pymdownx.progressbar': {},
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

SIMILAR_POSTS_ENABLED = True
SIMILAR_POSTS_MAX_COUNT = 3
SIMILAR_POSTS_MIN_SCORE = 0.0001
