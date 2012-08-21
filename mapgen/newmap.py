from pyglet import gl, graphics
from random import randint
from voronoi import diagram

class NewMap(object):
    NUM_POINTS = 50

    def __init__(self):
        points = []
        while len(points) < NewMap.NUM_POINTS:
            point = (randint(81, 239), randint(61, 179))
            if not point in points:
                points.append(point)
                if point[0] < 160:
                    points.append((point[0] + 160, point[1]))
                else:
                    points.append((point[0] - 160, point[1]))

        vor_diagram = diagram(tuple(p[0] for p in points), tuple(p[1] for p in points), 0)

        self.gl_points = reduce(lambda s, c: s + c, points, tuple())

        self.gl_lines = reduce(lambda s, c: s + c[0] + c[1], vor_diagram, tuple())
        self.gl_lines = [int(i) for i in self.gl_lines]

    def draw(self):
        gl.glColor3f(1.0, 0.0, 0.0)
        gl.glLineWidth(2)
        graphics.draw(4, gl.GL_LINE_LOOP, ('v2i', (80, 60, 240, 60, 240, 180, 80, 180)))

        gl.glColor3f(0.0, 1.0, 1.0)
        gl.glPointSize(2)
        graphics.draw(len(self.gl_points) // 2, gl.GL_POINTS, ('v2i', self.gl_points))

        gl.glColor3f(0.0, 1.0, 0.0)
        gl.glLineWidth(2)
        graphics.draw(len(self.gl_lines) // 2, gl.GL_LINES, ('v2i', self.gl_lines))
