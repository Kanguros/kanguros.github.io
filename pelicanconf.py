SITENAME = "Kamil's Scratchpad"
SITENAME_BRAND = "KS"
URL = "http://localhost"
PORT = "8080"
SITEURL = f"{URL}:{PORT}"
RELATIVE_URLS = True
GOOGLE_ANALYTICS = False
TIMEZONE = "Europe/Warsaw"
AUTHOR = "Kamil Urbanek"
DEFAULT_LANG = "en"
DEFAULT_DATE_FORMAT = "%Y-%m-%d"
THEME_STATIC_DIR = THEME = "theme"
PATH = "content"
OUTPUT_PATH = "_output/"
# Plugins
PLUGINS = [
    "yaml_metadata",
    "neighbors",
    "pelican.plugins.jinja_filters",
    # "sitemap",  In publishconf.py
    # "minify",  In publishconf.py
]
# Plugin - sitemap
SITEMAP = {
    "format": "xml",
    "priorities": {"articles": 0.6, "indexes": 0.5, "pages": 0.4},
    "changefreqs": {"articles": "weekly", "indexes": "weekly", "pages": "monthly"},
}
# Plugin - readtime
LANG_SETTINGS = 120
# Plugin - similarposts
SIMILAR_POSTS_ENABLED = False
SIMILAR_POSTS_MAX_COUNT = 3
SIMILAR_POSTS_MIN_SCORE = 0.0001

SUMMARY_END_SUFFIX = ""
TYPOGRIFY = True
TYPOGRIFY_IGNORE_TAGS = ["pre", "code", "svg", "img", "style"]

DIRECT_TEMPLATES = [
    "index",
    "tags",
    "private",
    "error",
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
    "extra/favicon.ico",
    "extra/robots.txt",
]
FAVICON = "favicon.ico"
EXTRA_PATH_METADATA = {
    "extra/.nojekyll": {"path": ".nojekyll"},
    "extra/favicon.ico": {"path": "favicon.ico"},
    "extra/robots.txt": {"path": "robots.txt"},
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
    "private.html": "private/index.html",
    "error.html": "404.html",
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
    "cheatsheet": "Shortcut of tips and tricks.",
}

DEFAULT_CATEGORY = "post"

GIT_LINK = "https://github.com/Kanguros/"
NAV_LINKS = [
    ("Posts", POSTS_URL, "post"),
    ("Tags", TAGS_URL, "tags"),
    ("About", ABOUT_URL, "file-person"),
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
        "markdown.extensions.codehilite": {"css_class": "highlight"},
        "markdown.extensions.toc": {
            "permalink": "false",
            "anchorlink": "true",
            "toc_depth": 2,
            "title": "Contents"
        },
        "pymdownx.progressbar": {},
        "pymdownx.blocks.html": {},
        "pymdownx.snippets": {"check_paths": "true", "base_path": "."},
        "pymdownx.magiclink": {},
        "markdown_extension.inline_mermaid": {},
    },
    "output_format": "html5",
}

SVG_HOME_K = """
<svg viewBox="0 0 100 100" width="100" height="auto" xmlns="http://www.w3.org/2000/svg"
     style="vertical-align: middle;">
  <rect x="3" y="3" width="94" height="94" rx="20" fill="rgb(64, 64, 64)" stroke="#404040" stroke-width="5"></rect>
  <text x="50" y="50" font-family="Arial, sans-serif" font-size="80" fill="#fff" text-anchor="middle" alignment-baseline="central">K
    </text>
</svg>
"""
SVG_POST = """<svg xmlns="http://www.w3.org/2000/svg" width="20" height="auto" fill="currentColor" viewBox="0 0 16 16">
  <path d="M4 3.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 0 1h-5a.5.5 0 0 1-.5-.5m0 2a.5.5 0 0 1 .5-.5h7a.5.5 0 0 1 .5.5v8a.5.5 0 0 1-.5.5h-7a.5.5 0 0 1-.5-.5z"/>
  <path d="M2 2a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2zm10-1H4a1 1 0 0 0-1 1v12a1 1 0 0 0 1 1h8a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1"/>
</svg>"""
SVG_GITHUB = """<svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" fill="currentColor" viewBox="0 0 16 16">
  <path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27s1.36.09 2 .27c1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.01 8.01 0 0 0 16 8c0-4.42-3.58-8-8-8"/>
</svg>"""
SVG_GITHUB_BIGGER = """
<svg xmlns="http://www.w3.org/2000/svg" width="25" height="auto" fill="currentColor" viewBox="0 0 16 16">
  <path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27s1.36.09 2 .27c1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.01 8.01 0 0 0 16 8c0-4.42-3.58-8-8-8"/>
</svg>"""
SVG_PERSON = """<svg xmlns="http://www.w3.org/2000/svg" width="16" height="auto" fill="currentColor" viewBox="0 0 16 16">
  <path d="M12 1a1 1 0 0 1 1 1v10.755S12 11 8 11s-5 1.755-5 1.755V2a1 1 0 0 1 1-1zM4 0a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h8a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2z"/>
  <path d="M8 10a3 3 0 1 0 0-6 3 3 0 0 0 0 6"/>
</svg>"""
SVG_EMAIL = """<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewBox="0 0 16 16">
  <path d="M2 2A2 2 0 0 0 .05 3.555L8 8.414l7.95-4.859A2 2 0 0 0 14 2zm-2 9.8V4.698l5.803 3.546zm6.761-2.97-6.57 4.026A2 2 0 0 0 2 14h6.256A4.5 4.5 0 0 1 8 12.5a4.49 4.49 0 0 1 1.606-3.446l-.367-.225L8 9.586zM16 9.671V4.697l-5.803 3.546.338.208A4.5 4.5 0 0 1 12.5 8c1.414 0 2.675.652 3.5 1.671"/>
  <path d="M15.834 12.244c0 1.168-.577 2.025-1.587 2.025-.503 0-1.002-.228-1.12-.648h-.043c-.118.416-.543.643-1.015.643-.77 0-1.259-.542-1.259-1.434v-.529c0-.844.481-1.4 1.26-1.4.585 0 .87.333.953.63h.03v-.568h.905v2.19c0 .272.18.42.411.42.315 0 .639-.415.639-1.39v-.118c0-1.277-.95-2.326-2.484-2.326h-.04c-1.582 0-2.64 1.067-2.64 2.724v.157c0 1.867 1.237 2.654 2.57 2.654h.045c.507 0 .935-.07 1.18-.18v.731c-.219.1-.643.175-1.237.175h-.044C10.438 16 9 14.82 9 12.646v-.214C9 10.36 10.421 9 12.485 9h.035c2.12 0 3.314 1.43 3.314 3.034zm-4.04.21v.227c0 .586.227.8.581.8.31 0 .564-.17.564-.743v-.367c0-.516-.275-.708-.572-.708-.346 0-.573.245-.573.791"/>
</svg>
"""
SVG_CALENDAR = """<svg xmlns="http://www.w3.org/2000/svg" width="16" height="auto" fill="currentColor" viewBox="0 0 16 16">
  <path d="M3.5 0a.5.5 0 0 1 .5.5V1h8V.5a.5.5 0 0 1 1 0V1h1a2 2 0 0 1 2 2v11a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V3a2 2 0 0 1 2-2h1V.5a.5.5 0 0 1 .5-.5M1 4v10a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1V4z"/>
</svg>"""
SVG_ARROW_LEFT = """<svg xmlns="http://www.w3.org/2000/svg" width="16" height="auto" fill="currentColor" viewBox="0 0 16 16">
  <path fill-rule="evenodd" d="M15 8a.5.5 0 0 0-.5-.5H2.707l3.147-3.146a.5.5 0 1 0-.708-.708l-4 4a.5.5 0 0 0 0 .708l4 4a.5.5 0 0 0 .708-.708L2.707 8.5H14.5A.5.5 0 0 0 15 8"/>
</svg>"""
SVG_ARROW_RIGHT = """<svg xmlns="http://www.w3.org/2000/svg" width="16" height="auto" fill="currentColor" viewBox="0 0 16 16">
  <path fill-rule="evenodd" d="M1 8a.5.5 0 0 1 .5-.5h11.793l-3.147-3.146a.5.5 0 0 1 .708-.708l4 4a.5.5 0 0 1 0 .708l-4 4a.5.5 0 0 1-.708-.708L13.293 8.5H1.5A.5.5 0 0 1 1 8"/>
</svg>"""
SVG_ARROW_SHORT_LEFT = """<svg xmlns="http://www.w3.org/2000/svg" width="16" height="auto" fill="currentColor" viewBox="0 0 16 16">
  <path fill-rule="evenodd" d="M12 8a.5.5 0 0 1-.5.5H5.707l2.147 2.146a.5.5 0 0 1-.708.708l-3-3a.5.5 0 0 1 0-.708l3-3a.5.5 0 1 1 .708.708L5.707 7.5H11.5a.5.5 0 0 1 .5.5"/>
</svg>"""
SVG_ARROW_SHORT_RIGHT = """<svg xmlns="http://www.w3.org/2000/svg" width="16" height="auto" fill="currentColor" viewBox="0 0 16 16">
  <path fill-rule="evenodd" d="M4 8a.5.5 0 0 1 .5-.5h5.793L8.146 5.354a.5.5 0 1 1 .708-.708l3 3a.5.5 0 0 1 0 .708l-3 3a.5.5 0 0 1-.708-.708L10.293 8.5H4.5A.5.5 0 0 1 4 8"/>
</svg>"""
SVG_X_ERROR = """<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="error-icon" viewBox="0 0 16 16">
  <path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14m0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16"/>
  <path d="M4.646 4.646a.5.5 0 0 1 .708 0L8 7.293l2.646-2.647a.5.5 0 0 1 .708.708L8.707 8l2.647 2.646a.5.5 0 0 1-.708.708L8 8.707l-2.646 2.647a.5.5 0 0 1-.708-.708L7.293 8 4.646 5.354a.5.5 0 0 1 0-.708"/>
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
