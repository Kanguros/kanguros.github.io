URL = 'http://localhost'
PORT = "8080"
SITEURL = f'{URL}:{PORT}'
RELATIVE_URLS = True

SITENAME = "Kamil's Scratchpad"
GITHUB_URL = "https://github.com/Kanguros/"
TIMEZONE = 'Europe/Warsaw'
AUTHOR = 'Kamil Urbanek'
DEFAULT_LANG = 'en'
DEFAULT_CATEGORY = "Personal"
DEFAULT_DATE_FORMAT = "%d/%m/%Y"
DATE_FORMATS = {'en': "%d/%m/%Y"}
LOCALE = ('en_US',)

PLUGINS = ['yaml_metadata']

THEME = 'theme'
THEME_STATIC_DIR = THEME
THEME_JS = f"{SITEURL}/{THEME_STATIC_DIR}/js"
THEME_CSS = f"{SITEURL}/{THEME_STATIC_DIR}/css"
COLOR_SCHEME_CSS = "github_jekyll.css"
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
    ('Index', 'index.html', 'house'),
    ('Archive', ARCHIVES_SAVE_AS, 'archive'),
    ('About', 'about/index.html', 'file-person'),
    ('Tags', TAGS_SAVE_AS, 'tags'),
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
