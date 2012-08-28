import pyglet

from mapgen.spheremap import SphereMap
from mapgen.globe import Globe


class GameWindow(pyglet.window.Window):

    FRAMERATE = 1.0 / 60
    WINDOW_SIZE = (640, 480)

    def __init__(self):
        super(GameWindow, self).__init__(*GameWindow.WINDOW_SIZE)

        pyglet.gl.glClearColor(1.0, 0.0, 1.0, 1.0)
        pyglet.gl.glDisable(pyglet.gl.GL_DEPTH_TEST)

        self.fps_label = pyglet.clock.ClockDisplay(color=(1.0, 0.0, 0.0, 0.5))

        self.initialize_map()
        self.globe = Globe(100, (10, 10))

    def on_draw(self):
        self.clear()
        self.map.draw()
        self.globe.draw()
        self.fps_label.draw()

    def on_resize(self, width, height):
        pyglet.gl.glViewport(0, 0, width, height)
        pyglet.gl.glMatrixMode(pyglet.gl.GL_PROJECTION)
        pyglet.gl.glLoadIdentity()
        pyglet.gl.glOrtho(0.0, 320.0, 0.0, 240.0, -120.0, 120.0)
        pyglet.gl.glMatrixMode(pyglet.gl.GL_MODELVIEW)

    def on_key_press(self, symbol, modifiers):
        super(GameWindow, self).on_key_press(symbol, modifiers)
        if symbol == pyglet.window.key.A:
            self.progress()
        if symbol == pyglet.window.key.R:
            self.map.toggle_view()

    def progress(self):
        self.initialize_map()

    def initialize_map(self):
        self.map = SphereMap(38)
