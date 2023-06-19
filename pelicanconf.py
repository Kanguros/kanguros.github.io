URL = 'http://localhost'
PORT = "8080"
SITEURL = f'{URL}:{PORT}'
RELATIVE_URLS = True

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

SITENAME = 'DevNet Notes'
TIMEZONE = 'Europe/Warsaw'
AUTHOR = 'Kamil Urbanek'
DEFAULT_LANG = 'en'
DEFAULT_CATEGORY = "General"

THEME = 'theme'
TYPOGRIFY = True
DIRECT_TEMPLATES = ['index',
                    'tags',
                    'archives']

DEFAULT_PAGINATION = 7

# Paths and other files
PATH = 'content'
OUTPUT_PATH = 'local_output/'
ARTICLE_PATHS = ['posts']
PAGE_PATHS = ['pages']

STATIC_PATHS = ['images',
                'extra/.nojekyll']

EXTRA_PATH_METADATA = {
    'extra/.nojekyll': {'path': '.nojekyll'}
}

ARTICLE_URL = 'posts/{slug}.html'
ARTICLE_SAVE_AS = 'posts/{slug}.html'

ARCHIVES_SAVE_AS = 'archive.html'

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

TAG_URL = 'tags/{slug}/'
TAG_SAVE_AS = 'tags/{slug}/index.html'
TAGS_SAVE_AS = 'tags/index.html'

MENUITEMS = (
    ('Tags', f'{TAGS_SAVE_AS}'),
    ('Archive', f'{ARCHIVES_SAVE_AS}'),
    ('About', f'about/index.html')
)

AUTHORS_BIO = "Short bio about the site and the author."

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
    'output_format': 'html5'}

COLOR_SCHEME_CSS = "darkly.css"

DISPLAY_PAGES_ON_MENU = False
THEME_STATIC_DIR = "theme"
# HEADER_COVER = "theme/static/images/home-bg.png"
