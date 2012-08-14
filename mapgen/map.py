from random import randint
from voronoi import diagram
import pyglet

class Map(object):
    NUM_TILES = 4 * 3 * 4
    SIZE = (320, 240)
    
    def __init__(self):
        points = []
        while len(points) < Map.NUM_TILES:
            new_point = (randint(1, Map.SIZE[0]) - 1, randint(1, Map.SIZE[1]) - 1)
            if not new_point in points:
                points.append(new_point)
        
        self.diagram = diagram([i[0] for i in points], [i[1] for i in points], 0)
        
        self.gl_points = reduce(lambda s, c: s + c, points, tuple())
        
        self.gl_lines = reduce(lambda s, c: s + c[0] + c[1], self.diagram, tuple())
        self.gl_lines = [int(i) for i in self.gl_lines]
    
    def draw(self):
        pyglet.gl.glColor3f(0.0, 1.0, 0.0)
        pyglet.gl.glPointSize(2)
        pyglet.graphics.draw(len(self.gl_points) // 2, pyglet.gl.GL_POINTS, ('v2i', self.gl_points))
        
        pyglet.gl.glColor3f(0.0, 0.0, 1.0)
        pyglet.gl.glLineWidth(2)
        pyglet.graphics.draw(len(self.gl_lines) // 2, pyglet.gl.GL_LINES, ('v2i', self.gl_lines))
