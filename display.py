import pyglet

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
CAPTION = "Pyglet"

window = pyglet.window.Window(WINDOW_WIDTH, WINDOW_HEIGHT, caption=CAPTION)

@window.event
def on_draw():
    window.clear()

pyglet.app.run()