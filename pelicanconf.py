URL = 'http://localhost'
PORT = "8080"
SITEURL = f'{URL}:{PORT}'
RELATIVE_URLS = True

SITENAME = "Kamil's Scratchpad"
TIMEZONE = 'Europe/Warsaw'
AUTHOR = 'Kamil Urbanek'
DEFAULT_LANG = 'en'
DEFAULT_CATEGORY = "Personal"
DEFAULT_DATE_FORMAT = "%d/%m/%Y"
DATE_FORMATS = {'en': "%d/%m/%Y"}
LOCALE = ('en_US',)

PLUGINS = [
    'yaml_metadata',
    'similar_posts'
]

THEME = 'theme'
THEME_STATIC_DIR = THEME
THEME_DEFAULT_HEADER = "home-bg.png"
COLOR_SCHEME_CSS = "monokai.css"
TYPOGRIFY = True
DIRECT_TEMPLATES = [
    'index',
    'archives',
    'tags',
    # 'resume'
]
STATIC_PATHS = [
    'images',
    'extra/.nojekyll',

]
EXTRA_PATH_METADATA = {
    'extra/.nojekyll': {'path': '.nojekyll'},
}

DEFAULT_PAGINATION = 3

# Paths and other files
PATH = 'content'
OUTPUT_PATH = 'local_output/'

ARTICLE_PATHS = ['posts']
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

EXCLUDED_CATEGORIES = ['resume']
MENUITEMS = (
    # Title, URL, Icon
    ('Index', f'{SITEURL}/index.html', 'house'),
    ('Tags', f'{SITEURL}/{TAGS_SAVE_AS}', 'tags'),
    ('Archive', f'{SITEURL}/{ARCHIVES_SAVE_AS}', 'archive'),
    ('About', f'{SITEURL}/about/index.html', 'file-person'),
    ('Git', "https://github.com/Kanguros/", 'github'),
)

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
