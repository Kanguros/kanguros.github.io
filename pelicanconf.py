URL = "http://localhost"
PORT = "8080"
SITEURL = f"{URL}:{PORT}"
RELATIVE_URLS = True

TIMEZONE = "Europe/Warsaw"
AUTHOR = "Kamil Urbanek"
DEFAULT_LANG = "en"
DEFAULT_DATE_FORMAT = "%Y-%m-%d"

# Paths and other files
PATH = "content"
OUTPUT_PATH = "_output/"

# Plugins
PLUGINS = [
    "yaml_metadata",
    "similar_posts",
    "readtime",
    "neighbors",
    "pelican.plugins.jinja_filters",
    # "sitemap",  In publishconf.py
    # "minify",  In publishconf.py
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

"""

THEME_STATIC_DIR = THEME = "theme"
COLOR_SCHEME_CSS = "darkly.css"
SUMMARY_END_SUFFIX = ""
# TYPOGRIFY = False
TYPOGRIFY = True
TYPOGRIFY_IGNORE_TAGS = ["pre", "code", "svg", "img", "style"]

DIRECT_TEMPLATES = [
    "index",
    "archives",
    "tags",
    "under_construction",
    "private",
    # "posts"
]

DEFAULT_PAGINATION = 5
PAGINATED_TEMPLATES = {
    "index": None,
    "tag": None,
}
PAGINATION_PATTERNS = (
    (1, "{url}", "{save_as}"),
    (2, "{base_name}/{number}/", "{base_name}/{number}/index.html"),
)

STATIC_PATHS = [
    "images",
    "code",
    "extra/.nojekyll",
    # "slides",

]
EXTRA_PATH_METADATA = {
    "extra/.nojekyll": {"path": ".nojekyll"},
}

INDEX_SAVE_AS = POSTS_SAVE_AS = "posts/index.html"
POSTS_URL = "posts/"
ARCHIVES_URL = "archive/"
ARCHIVES_SAVE_AS = "archive/index.html"

ABOUT_URL = "about/"
ABOUT_SAVE_AS = "about/index.html"

AUTHOR_SAVE_AS = ""
CATEGORY_SAVE_AS = ""
CATEGORIES_SAVE_AS = ""

ARTICLE_PATHS = ["private", "posts"]
ARTICLE_URL = "post/{slug}/"
ARTICLE_SAVE_AS = "post/{slug}/index.html"
ARTICLE_ORDER_BY = "reversed-date"

TEMPLATE_PAGES = {
    "private.html": "private/index.html"
}
DRAFTS_URL = "private/"
DRAFTS_SAVE_AS = "private/index.html"
DRAFT_URL = "private/{slug}/"
DRAFT_SAVE_AS = "private/{slug}/index.html"

PAGE_PATHS = ["pages"]
PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"

TAG_URL = "tag/{slug}/"
TAG_SAVE_AS = "tag/{slug}/index.html"

TAGS_URL = "tags/"
TAGS_SAVE_AS = "tags/index.html"

TAGS_DESCRIPTION = {
    "python": "Knowledge of Python",
    "cheatsheet": "Shortcut of tips and tricks."
}

DEFAULT_CATEGORY = "post"

GIT_LINK = "https://github.com/Kanguros/"
NAV_LINKS = [
    ("Posts", POSTS_URL, "post"),
    ("Tags", TAGS_URL, "tags"),
    ("About", ABOUT_URL, "file-person"),
    # ("Git", GIT_LINK, "github"),
]

FOOTER_LINKS = [
    ("Index", "", "home"),
    *NAV_LINKS,
]

MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.extra": {},
        # "markdown.extensions.attr_list": {},
        "markdown.extensions.admonition": {},
        "markdown.extensions.codehilite": {
            "css_class": "highlight"
        },
        "markdown.extensions.toc": {
            "permalink": "false",
            "anchorlink": "true",
            "toc_depth": 3,
            "title": "Content"
        },
        "pymdownx.progressbar": {},
        "pymdownx.blocks.tab": {},
        "pymdownx.snippets": {
            "check_paths": "true",
            "base_path": "content"
        },
        "pymdownx.magiclink": {},
        # "pymdownx.saneheaders": {},
        "markdown_extension_mermaid": {},
    },
    "output_format": "html5"
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
GZIP_CACHE = False
DELETE_OUTPUT_DIRECTORY = False
