import math

from pyglet import gl, graphics
from random import random

class SphereMap(object):

    def __init__(self, radius):
        self.radius = radius

        self.points = []
        while len(self.points) < 1000:
            width = random() * 2 * math.pi
            height = (random() - 0.5) * math.pi
            point = (int(self.radius * math.cos(height) * math.cos(width)) + 160, int(self.radius * math.sin(height)) + 120, int(self.radius * math.cos(height) * math.sin(width)))
            if not point in self.points:
                self.points.append(point)

        self.gl_points = reduce(lambda s, c: s + c, self.points, tuple())

    def draw(self):
        gl.glColor3f(0.0, 0.0, 0.0)
        gl.glPointSize(2)
        graphics.draw(len(self.gl_points) // 3, gl.GL_POINTS, ('v3i', self.gl_points))

