import math

from pyglet import gl, graphics
from random import random
from voronoi import diagram

class SphereMap(object):

    def __init__(self, radius):
        self.radius = radius

        self.half_diam = self.radius * math.pi

        self.points = []
        self.radial_map = []
        while len(self.points) < 5:
            ran1 = random()
            ran2 = random()

            width = ran1 * 2 * math.pi
            height = (ran2 - 0.5) * math.pi
            point = (int(self.radius * math.cos(height) * math.cos(width)) + 160, int(self.radius * math.sin(height)) + 120, int(self.radius * math.cos(height) * math.sin(width)))
            if not point in self.points:
                self.points.append(point)
                self.radial_map.append((width, self.half_diam * ran2))

        self.gl_points2 = []
        self.points2 = []
        for p in self.radial_map:
            self.points2.append((160 + int(math.cos(p[0]) * p[1]), 120 + int(math.sin(p[0]) * p[1])))

        dg = diagram([p[0] for p in self.points2], [p[1] for p in self.points2], 0)

        self.gl_points1 = reduce(lambda s, c: s + c, self.points, tuple())
        self.gl_points2 = reduce(lambda s, c: s + c, self.points2, tuple())

        self.gl_lines2 = []
        for e in dg:
            for c in self.get_polar(e[0][0], e[0][1]):
                self.gl_lines2.append(c)
            for c in self.get_polar(e[1][0], e[1][1]):
                self.gl_lines2.append(c)

        self.gl_lines = reduce(lambda s, c: s + c[0] + c[1], dg, tuple())
        self.gl_lines = [int(i) for i in self.gl_lines]

        self.draw = self.draw_sphere

    def draw_sphere(self):
        gl.glColor3f(0.0, 0.0, 0.0)
        gl.glPointSize(2)
        graphics.draw(len(self.gl_points1) // 3, gl.GL_POINTS, ('v3i', self.gl_points1))

        gl.glColor3f(0.0, 1.0, 0.0)
        gl.glLineWidth(1)
        graphics.draw(len(self.gl_lines2) // 3, gl.GL_LINES, ('v3i', self.gl_lines2))

    def draw_plane(self):
        gl.glColor3f(0.0, 0.0, 0.0)
        gl.glPointSize(2)
        graphics.draw(len(self.gl_points2) // 2, gl.GL_POINTS, ('v2i', self.gl_points2))

        gl.glColor3f(0.0, 1.0, 0.0)
        gl.glLineWidth(1)
        graphics.draw(len(self.gl_lines) // 2, gl.GL_LINES, ('v2i', self.gl_lines))

    def toggle_view(self):
        if self.draw == self.draw_sphere:
            self.draw = self.draw_plane
        else:
            self.draw = self.draw_sphere

    def get_polar(self, x, y):
        d = math.sqrt(x ** 2 + y ** 2)
        ran2 = d / self.half_diam

        width = x
        height = (ran2 - 0.5) * math.pi

        return (
            int(self.radius * math.cos(height) * math.cos(width)) + 160,
            int(self.radius * math.sin(height)) + 120,
            int(self.radius * math.cos(height) * math.sin(width))
        )
