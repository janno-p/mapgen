import math

from pyglet import gl, graphics

class Globe(object):
    def __init__(self, radius, dim):
        self.angle = 0.0
        self.radius = radius
        self.vertices = []
        for y in xrange(0, dim[1]):
            current_list = []
            self.vertices.append(current_list)
            a1 = float(y) / dim[1] * math.pi
            a2 = float(y + 1) / dim[1] * math.pi
            y1 = round(self.radius * (0.5 - math.cos(a1)), 2)
            y2 = round(self.radius * (0.5 - math.cos(a2)), 2)
            r1 = self.radius * math.sin(a1)
            r2 = self.radius * math.sin(a2)
            for x in xrange(0, dim[0] + 1):
                a = float(x) / dim[0] * math.pi * 2
                x1 = round(math.cos(a) * r1, 2)
                z1 = round(math.sin(a) * r1, 2)
                x2 = round(math.cos(a) * r2, 2)
                z2 = round(math.sin(a) * r2, 2)
                current_list.append(x1)
                current_list.append(y1)
                current_list.append(z1)
                current_list.append(x2)
                current_list.append(y2)
                current_list.append(z2)

    def draw(self):
        self.angle += 0.1
        gl.glColor3f(0.0, 1.0, 0.0)
        gl.glLoadIdentity()
        gl.glRotatef(self.angle, 1.0, 1.0, 0.0)
        #gl.glTranslatef(0.0, 0.0, 0.0)
        gl.glPolygonMode(gl.GL_FRONT_AND_BACK, gl.GL_LINE)
        for section in self.vertices:
            graphics.draw(len(section) // 3, gl.GL_TRIANGLE_STRIP, ('v3f', section))
        gl.glPolygonMode(gl.GL_FRONT_AND_BACK, gl.GL_FILL)
        gl.glLoadIdentity()
