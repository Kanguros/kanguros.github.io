2  # -*- coding: utf-8 -*-

import os
import shlex
import shutil
import sys

from invoke import task
from invoke.main import program
from pelican import main as pelican_main
from pelican.server import ComplexHTTPRequestHandler, RootedHTTPServer
from pelican.settings import DEFAULT_CONFIG, get_settings_from_file

OPEN_BROWSER_ON_SERVE = True

SETTINGS_FILE_BASE = 'pelicanconf.py'
SETTINGS = {}
SETTINGS.update(DEFAULT_CONFIG)
LOCAL_SETTINGS = get_settings_from_file(SETTINGS_FILE_BASE)
SETTINGS.update(LOCAL_SETTINGS)

CONFIG = {
    'settings_base': SETTINGS_FILE_BASE,
    'deploy_path': SETTINGS['OUTPUT_PATH'],
    'host': "localhost",
    'port': SETTINGS['PORT']
}


def pelican_run(cmd):
    cmd += ' ' + program.core.remainder  # allows to pass-through args to pelican
    pelican_main(shlex.split(cmd))


@task
def clean(c):
    """Remove generated files"""
    path = CONFIG['deploy_path']
    if os.path.isdir(path):
        print(f"Removing directory: {path}")
        shutil.rmtree(path)
        print(f"Creating a empty folder: {path}")
        os.makedirs(path)
    print(f"No directory as: {path}")


@task
def build(c, d=False):
    """Build local version of site"""
    debug = "--verbose --debug" if d else ""
    pelican_run('{debug} -s {settings_base} '.format(**CONFIG, debug=debug))


@task
def rebuild(c, d=False):
    """`build` with the delete switch"""
    debug = "--verbose --debug" if d else ""
    pelican_run('{debug} -d -s {settings_base}'.format(**CONFIG, debug=debug))


@task
def serve(c):
    """Serve site at http://$HOST:$PORT/ (default is localhost:8000)"""

    class AddressReuseTCPServer(RootedHTTPServer):
        allow_reuse_address = True

    server = AddressReuseTCPServer(
        CONFIG['deploy_path'],
        (CONFIG['host'], int(CONFIG['port'])),
        ComplexHTTPRequestHandler)

    if OPEN_BROWSER_ON_SERVE:
        # Open site in default browser
        import webbrowser
        webbrowser.open("http://{host}:{port}".format(**CONFIG))

    sys.stderr.write('Serving at {host}:{port} ...\n'.format(**CONFIG))
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
    from livereload import Server
    debug = " --debug " if d else d
    verbose = " --verbose" if v else v

    def cached_build(inner_debug="", inner_verbose=""):
        cmd = '-s {settings_base} -e CACHE_CONTENT=true LOAD_CONTENT_CACHE=true'
        # if inner_debug:
        #     cmd = inner_debug + cmd
        # if inner_verbose:
        #     cmd = inner_verbose + cmd
        # print(cmd)
        pelican_run(cmd.format(**CONFIG))

    cached_build(debug, verbose)
    server = Server()
    theme_path = SETTINGS['THEME']
    watched_globs = [
        CONFIG['settings_base'],
        '{}/templates/**/*.html'.format(theme_path),
        '{}/templates/**/*.j2'.format(theme_path),
        '{}/templates/static/*.*'.format(theme_path),
    ]

    content_file_extensions = ['.md', '.rst']
    for extension in content_file_extensions:
        content_glob = '{0}/**/*{1}'.format(SETTINGS['PATH'], extension)
        watched_globs.append(content_glob)

    static_file_extensions = ['.css', '.js']
    for extension in static_file_extensions:
        static_file_glob = '{0}/static/**/*{1}'.format(theme_path, extension)
        watched_globs.append(static_file_glob)

    for glob in watched_globs:
        server.watch(glob, cached_build)

    if OPEN_BROWSER_ON_SERVE:
        # Open site in default browser
        import webbrowser
        webbrowser.open("http://{host}:{port}".format(**CONFIG))

    server.serve(host=CONFIG['host'], port=CONFIG['port'], root=CONFIG['deploy_path'])


@task
def showfiles(c):
    paths = [
        ('.\pyproject.toml', "Python package dependencies"),
        ('.\pelicanconf.py', "Pelican configuration file"),

        '.\README.md',
        '.\local_output\index.html'
    ]
    for path in paths:
        with open(path, "r") as file:
            print(f"------ {path} ------")
            print(file.read())
            print(f"--------------------")
            print("")
