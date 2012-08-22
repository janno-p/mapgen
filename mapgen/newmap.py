from pyglet import gl, graphics
from random import randint, random
from voronoi import diagram_ext

import math

class NewMap(object):
    DIM = (16, 13)

    def __init__(self):
        h_space = 160 // NewMap.DIM[0]
        v_space = 120 // NewMap.DIM[1]

        h_offset = 81 + h_space // 4

        h_extra = h_space // 2

        shuffle_rate = 0.50 * min(h_space, v_space)

        v_offset = 61 + v_space // 4 + int(shuffle_rate) // 2

        points = []
        for x in xrange(0, NewMap.DIM[0]):
            for y in xrange(0, NewMap.DIM[1]):
                a = random() * 2 * math.pi
                r = random() * shuffle_rate
                dx = int(math.cos(a) * r)
                dy = int(math.sin(a) * r)


                extra = 0 if y % 2 == 0 else h_extra
                point = (h_offset + extra + x * h_space + dx, v_offset + y * v_space + dy)
                points.append(point)
                if point[0] < 160:
                    points.append((point[0] + 160, point[1]))
                else:
                    points.append((point[0] - 160, point[1]))

        self.initialize_gl_objects(points)

    def initialize_gl_objects(self, points):
        vor_diagram = diagram_ext(points, bounds=(0, 60, 160, 180))

        self.gl_points = reduce(lambda s, c: s + c, points, tuple())

        self.gl_lines = reduce(lambda s, c: s + c[0] + c[1], vor_diagram, tuple())
        self.gl_lines = [int(i) for i in self.gl_lines]

        self.process_diagram(vor_diagram)

    def draw_frame(self):
        gl.glColor3f(1.0, 0.0, 0.0)
        gl.glLineWidth(1)
        graphics.draw(4, gl.GL_LINE_LOOP, ('v2i', (80, 60, 240, 60, 240, 180, 80, 180)))

    def draw(self):
        gl.glColor3f(0.0, 1.0, 1.0)
        gl.glPointSize(1)
        graphics.draw(len(self.gl_points) // 2, gl.GL_POINTS, ('v2i', self.gl_points))

        gl.glColor3f(0.0, 1.0, 0.0)
        gl.glLineWidth(1)
        graphics.draw(len(self.gl_lines) // 2, gl.GL_LINES, ('v2i', self.gl_lines))

        gl.glColor3f(0.0, 0.0, 0.0)
        gl.glPointSize(2)
        graphics.draw(len(self.gl_vertices) // 2, gl.GL_POINTS, ('v2i', self.gl_vertices))

        self.draw_frame()

    def process_diagram(self, vor_diagram):
        vertices = []
        edges = []
        for e in vor_diagram:
            e = tuple(tuple(int(x) for x in y) for y in e)
            if e[0] == e[1]:
                continue
            edge = []
            for p in e:
                if p in vertices:
                    edge.append(vertices.index(p))
                else:
                    edge.append(len(vertices))
                    vertices.append(p)
            edges.append(edge)
        self.gl_vertices = reduce(lambda x, y: x + y, vertices, tuple())

        self.build_polygons(vertices, edges)

    def build_polygons(self, vertices, edges):
        pass
