import pyglet

from mapgen.version import VERSION

window = pyglet.window.Window()
window.set_caption('mapgen #%s' % VERSION)

pyglet.gl.glClearColor(1.0, 0.0, 1.0, 1.0)


@window.event
def on_draw():
    window.clear()

pyglet.app.run()
