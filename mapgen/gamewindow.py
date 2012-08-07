import pyglet
import random


class GameWindow(pyglet.window.Window):

    FRAMERATE = 1.0 / 60
    WINDOW_SIZE = (640, 480)

    def __init__(self):
        super(GameWindow, self).__init__(*GameWindow.WINDOW_SIZE)

        pyglet.gl.glClearColor(1.0, 0.0, 1.0, 1.0)
        pyglet.gl.glDisable(pyglet.gl.GL_DEPTH_TEST)

        self.fps_label = pyglet.clock.ClockDisplay(color=(1.0, 0.0, 0.0, 0.5))

        self.points = []
        self.point_count = int(0.25 * 320 * 240)
        for i in xrange(0, self.point_count):
            self.points.append(random.randint(0, 320))
            self.points.append(random.randint(0, 240))

    def on_draw(self):
        self.clear()

        pyglet.gl.glColor4ub(0, 255, 0, 255)
        pyglet.gl.glPointSize(2)
        pyglet.graphics.draw(self.point_count, pyglet.gl.GL_POINTS,
            ('v2i', self.points)
        )

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
        print('progressing')
