"""
Main entry point of the application.
"""

import pyglet
import sys

from mapgen.version import VERSION


def print_version():
    """Displays the version number of the application."""
    print(VERSION)


def run_app():
    """Start the main application."""
    window = pyglet.window.Window()
    window.set_caption('mapgen #%s' % VERSION)

    pyglet.gl.glClearColor(1.0, 0.0, 1.0, 1.0)

    @window.event
    def on_draw():
        window.clear()

    pyglet.app.run()

if __name__ == '__main__':
    COMMANDS = {
        '-v': print_version,
        '--version': print_version,
    }

    options = sys.argv[1:]

    for command in options:
        if command in COMMANDS:
            COMMANDS[command]()
        else:
            print('Unknown option: %s' % command)
        sys.exit()

    run_app()
