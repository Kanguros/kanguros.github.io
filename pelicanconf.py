URL = 'http://localhost'
PORT = "8080"
SITEURL = f'{URL}:{PORT}'
RELATIVE_URLS = True

SITENAME = "Kamil's Notes"
TIMEZONE = 'Europe/Warsaw'
AUTHOR = 'Kamil Urbanek'
DEFAULT_LANG = 'en'
DEFAULT_CATEGORY = "Personal"
DEFAULT_DATE_FORMAT = "%d/%m/%Y"
DATE_FORMATS = {'en': "%d/%m/%Y"}
LOCALE = ('en_US',)

PLUGINS = ['yaml_metadata']

THEME = 'theme'
THEME_STATIC_DIR = "theme"
COLOR_SCHEME_CSS = "github_jekyll.css"
COLOR_SCHEME_CSS = "github.css"
COLOR_SCHEME_CSS = "monokai.css"
TYPOGRIFY = True
DIRECT_TEMPLATES = [
    'index',
    'categories',
    'archives',
    # 'resume'
]
TEMPLATE_PAGES = {
    # 'posts/resume.md': 'resume.html',
    # 'posts/slides.slides.html': 'posts/slides.slides.html',
    # 'pyreveal': 'posts/pyreveal',
}

DEFAULT_PAGINATION = 3

# Paths and other files
PATH = 'content'
OUTPUT_PATH = 'local_output/'

ARTICLE_URL = 'posts/{slug}.html'
ARTICLE_SAVE_AS = 'posts/{slug}.html'
ARCHIVES_SAVE_AS = 'archive.html'
ARTICLE_ORDER_BY = 'reversed-date'
ARTICLE_PATHS = ['posts']

PAGE_PATHS = ['pages']
ARTICLE_URL = 'posts/{slug}.html'
ARTICLE_SAVE_AS = 'posts/{slug}.html'
ARCHIVES_SAVE_AS = 'archive.html'

STATIC_PATHS = [
    'images',
    'extra/.nojekyll',

]
EXTRA_PATH_METADATA = {
    'extra/.nojekyll': {'path': '.nojekyll'},
}

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
TAG_URL = 'tags/{slug}/'
TAG_SAVE_AS = 'tags/{slug}/index.html'
TAGS_SAVE_AS = 'tags.html'
CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
CATEGORIES_SAVE_AS = 'categories.html'

EXCLUDED_CATEGORIES = ['resume']

MENUITEMS = (
    # ('Tags', f'{TAGS_SAVE_AS}'),
    # ('Categories', f'{CATEGORIES_SAVE_AS}'),
    ('Archive', f'{ARCHIVES_SAVE_AS}'),
    ('About', f'about/index.html')
)

FOOTER_LINKS = (
    # ('github', "https://github.com/Kanguros/"),
)

GITHUB_URL = "https://github.com/Kanguros/"

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
