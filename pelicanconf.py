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
    # "similar_posts",
    # "readtime",
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
INDEX_POSTS_COUNT = 3
INDEX_TAGS_COUNT = 5
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

SVG_HOME_K = """
<svg width="40" height="40" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg" style="vertical-align: middle; margin-right: 8px;">
    <!-- Outer border -->
    <rect x="5" y="5" width="90" height="90" rx="15" fill="var(--main-font-color)" stroke="#404040" stroke-width="4"></rect>
    <text x="50%" y="50%" font-family="Arial, sans-serif" font-size="70" fill="#fff" text-anchor="middle" alignment-baseline="central">K</text>
  </svg>
"""
SVG_POST = """<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-file-post" viewBox="0 0 16 16">
  <path d="M4 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 0 1h-5a.5.5 0 0 1-.5-.5m0 2a.5.5 0 0 1 .5-.5h7a.5.5 0 0 1 .5.5v8a.5.5 0 0 1-.5.5h-7a.5.5 0 0 1-.5-.5z"/>
  <path d="M2 2a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2zm10-1H4a1 1 0 0 0-1 1v12a1 1 0 0 0 1 1h8a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1"/>
</svg>"""
SVG_GITHUB = """<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-github" viewBox="0 0 16 16">
  <path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27s1.36.09 2 .27c1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.01 8.01 0 0 0 16 8c0-4.42-3.58-8-8-8"/>
</svg>"""
SVG_PERSON = """<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-file-person" viewBox="0 0 16 16">
  <path d="M12 1a1 1 0 0 1 1 1v10.755S12 11 8 11s-5 1.755-5 1.755V2a1 1 0 0 1 1-1zM4 0a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h8a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2z"/>
  <path d="M8 10a3 3 0 1 0 0-6 3 3 0 0 0 0 6"/>
</svg>"""
SVG_CALENDAR = """<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-calendar" viewBox="0 0 16 16">
  <path d="M3.5 0a.5.5 0 0 1 .5.5V1h8V.5a.5.5 0 0 1 1 0V1h1a2 2 0 0 1 2 2v11a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V3a2 2 0 0 1 2-2h1V.5a.5.5 0 0 1 .5-.5M1 4v10a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1V4z"/>
</svg>"""
SVG_ARROW_LEFT = """<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-arrow-left" viewBox="0 0 16 16">
  <path fill-rule="evenodd" d="M15 8a.5.5 0 0 0-.5-.5H2.707l3.147-3.146a.5.5 0 1 0-.708-.708l-4 4a.5.5 0 0 0 0 .708l4 4a.5.5 0 0 0 .708-.708L2.707 8.5H14.5A.5.5 0 0 0 15 8"/>
</svg>"""
SVG_ARROW_RIGHT = """<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-arrow-right" viewBox="0 0 16 16">
  <path fill-rule="evenodd" d="M1 8a.5.5 0 0 1 .5-.5h11.793l-3.147-3.146a.5.5 0 0 1 .708-.708l4 4a.5.5 0 0 1 0 .708l-4 4a.5.5 0 0 1-.708-.708L13.293 8.5H1.5A.5.5 0 0 1 1 8"/>
</svg>"""

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
