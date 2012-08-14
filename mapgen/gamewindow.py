import pyglet
import random

from mapgen.map import Map


class GameWindow(pyglet.window.Window):

    FRAMERATE = 1.0 / 60
    WINDOW_SIZE = (640, 480)

    def __init__(self):
        super(GameWindow, self).__init__(*GameWindow.WINDOW_SIZE)

        pyglet.gl.glClearColor(1.0, 0.0, 1.0, 1.0)
        pyglet.gl.glDisable(pyglet.gl.GL_DEPTH_TEST)

        self.fps_label = pyglet.clock.ClockDisplay(color=(1.0, 0.0, 0.0, 0.5))
        
        self.map = Map()

    def on_draw(self):
        self.clear()

        self.map.draw()

        self.fps_label.draw()

    def on_resize(self, width, height):
        pyglet.gl.glViewport(0, 0, width, height)
        pyglet.gl.glMatrixMode(pyglet.gl.GL_PROJECTION)
        pyglet.gl.glLoadIdentity()
        pyglet.gl.glOrtho(0.0, 320.0, 0.0, 240.0, -1.0, 1.0)
        pyglet.gl.glMatrixMode(pyglet.gl.GL_MODELVIEW)

    def on_key_press(self, symbol, modifiers):
        super(GameWindow, self).on_key_press(symbol, modifiers)
        if symbol == pyglet.window.key.A:
            self.progress()

    def progress(self):
        self.map = Map()
