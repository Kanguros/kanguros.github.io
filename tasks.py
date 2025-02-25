import os
import shlex
import shutil
import sys

from invoke import task
from invoke.main import program
from livereload import Server
from pelican import main as pelican_main
from pelican.server import ComplexHTTPRequestHandler, RootedHTTPServer
from pelican.settings import DEFAULT_CONFIG, get_settings_from_file

OPEN_BROWSER_ON_SERVE = False

SETTINGS_FILE_BASE = "pelicanconf.py"
SETTINGS = {}
SETTINGS.update(DEFAULT_CONFIG)
LOCAL_SETTINGS = get_settings_from_file(SETTINGS_FILE_BASE)
SETTINGS.update(LOCAL_SETTINGS)

CONFIG = {
    "settings_base": SETTINGS_FILE_BASE,
    "deploy_path": SETTINGS["OUTPUT_PATH"],
    "host": "localhost",
    "port": SETTINGS["PORT"],
}


def pelican_run(cmd):
    cmd += " " + program.core.remainder  # allows to pass-through args to pelican
    pelican_main(shlex.split(cmd))


@task
def clean(c):
    """Remove generated files"""
    path = CONFIG["deploy_path"]
    print(f"[{path}] Removing deploy directory")
    if os.path.isdir(path):
        shutil.rmtree(path)
        print(f"[{path}] Creating a empty folder")
        os.makedirs(path)
    else:
        print(f"[{path}] No directory")

    cache_path = "cache"
    print(f"[{cache_path}] Removing cache directory")
    if os.path.isdir(path):
        shutil.rmtree(path)
        print(f"[{cache_path}] Removed")


@task
def build(c, d=False):
    """Build local version of site"""
    debug = "--verbose --debug" if d else ""
    pelican_run("{debug} -s {settings_base} ".format(**CONFIG, debug=debug))


@task
def rebuild(c, d=False):
    """`build` with the delete switch"""
    debug = "--verbose --debug" if d else ""
    pelican_run("{debug} -d -s {settings_base}".format(**CONFIG, debug=debug))


@task
def serve(c):
    """Serve site at http://$HOST:$PORT/ (default is localhost:8000)"""

    class AddressReuseTCPServer(RootedHTTPServer):
        allow_reuse_address = True

    server = AddressReuseTCPServer(
        CONFIG["deploy_path"],
        (CONFIG["host"], int(CONFIG["port"])),
        ComplexHTTPRequestHandler,
    )

    if OPEN_BROWSER_ON_SERVE:
        # Open site in default browser
        import webbrowser

        webbrowser.open("http://{host}:{port}".format(**CONFIG))

    sys.stderr.write("Serving at {host}:{port} ...\n".format(**CONFIG))
    server.serve_forever()


@task
def reserve(c, d=False):
    """`clean`, `build`, then `serve`"""
    clean(c)
    rebuild(c, d)
    serve(c)


@task
def l(c, d=False, v=False):
    """Automatically reload browser tab upon file modification."""
    clean(c)
    cmd = "-s {settings_base} -e CACHE_CONTENT=true LOAD_CONTENT_CACHE=true".format(
        **CONFIG
    )
    print("Building site")
    if d:
        cmd = f"--debug {cmd}"
        print("With debug option")
    if v:
        cmd = f"--verbose {cmd}"
        print("With verobse option")
    build_func = lambda: pelican_run(cmd)
    build_func()

    server = Server()
    theme_path = SETTINGS["THEME"]
    watched_globs = [
        CONFIG["settings_base"],
        f"{theme_path}/templates/**/*.html",
        f"{theme_path}/templates/**/*.j2",
        f"{theme_path}/templates/static/*.*",
    ]

    content_file_extensions = [".md", ".rst"]
    for extension in content_file_extensions:
        content_glob = "{0}/**/*{1}".format(SETTINGS["PATH"], extension)
        watched_globs.append(content_glob)

    static_file_extensions = [".css", ".js"]
    for extension in static_file_extensions:
        static_file_glob = f"{theme_path}/static/**/*{extension}"
        watched_globs.append(static_file_glob)

    for glob in watched_globs:
        server.watch(glob, build_func)

    if OPEN_BROWSER_ON_SERVE:
        # Open site in default browser
        import webbrowser

        webbrowser.open("{host}:{port}".format(**CONFIG))

    root_path = CONFIG["deploy_path"]
    print(f"Serving {root_path}")
    server.serve(host=CONFIG["host"], port=CONFIG["port"], root=root_path)


@task
def showfiles(c):
    paths = [
        (r".\pyproject.toml", "Python package dependencies"),
        (r".\pelicanconf.py", "Pelican configuration file"),
        r".\README.md",
        r".\local_output\index.html",
    ]
    for path in paths:
        with open(path) as file:
            print(f"------ {path} ------")
            print(file.read())
            print("--------------------")
            print("")
