# Do not remove these lines
from setup_ursina_android import setup_ursina_android
setup_ursina_android()

from ursina import *


# Initialize ursina app
app = Ursina()

# Window setttings
window.exit_button.enabled = False

# Mesh from cube.ursinamesh
""" cubeMesh = Mesh(
    vertices=((0.5, -0.5, -0.5), (-0.5, -0.5, 0.5), (0.5, -0.5, 0.5), (-0.5, 0.5, 0.5), (0.5, 0.5, -0.5), (0.5, 0.5, 0.5), (0.5, 0.5, 0.5), (0.5, -0.5, -0.5), (0.5, -0.5, 0.5), (0.5, 0.5, -0.5), (-0.5, -0.5, -0.5), (0.5, -0.5, -0.5), (-0.5, -0.5, -0.5), (-0.5, 0.5, 0.5), (-0.5, -0.5, 0.5), (0.5, -0.5, 0.5), (-0.5, 0.5, 0.5), (0.5, 0.5, 0.5), (0.5, -0.5, -0.5), (-0.5, -0.5, -0.5), (-0.5, -0.5, 0.5), (-0.5, 0.5, 0.5), (-0.5, 0.5, -0.5), (0.5, 0.5, -0.5), (0.5, 0.5, 0.5), (0.5, 0.5, -0.5), (0.5, -0.5, -0.5), (0.5, 0.5, -0.5), (-0.5, 0.5, -0.5), (-0.5, -0.5, -0.5), (-0.5, -0.5, -0.5), (-0.5, 0.5, -0.5), (-0.5, 0.5, 0.5), (0.5, -0.5, 0.5), (-0.5, -0.5, 0.5), (-0.5, 0.5, 0.5)), 
    uvs=((1.0, 0.0), (0.0, 1.0), (1.0, 1.0), (0.0, 1.0), (1.0, -0.0), (1.0, 1.0), (1.0, 1.0), (0.0, 0.0), (1.0, 0.0), (1.0, 1.0), (-0.0, 0.0), (1.0, 0.0), (-0.0, 0.0), (1.0, 1.0), (1.0, 0.0), (1.0, 0.0), (0.0, 1.0), (1.0, 1.0), (1.0, 0.0), (-0.0, 0.0), (0.0, 1.0), (0.0, 1.0), (-0.0, 0.0), (1.0, -0.0), (1.0, 1.0), (-0.0, 1.0), (0.0, 0.0), (1.0, 1.0), (-0.0, 1.0), (-0.0, 0.0), (-0.0, 0.0), (-0.0, 1.0), (1.0, 1.0), (1.0, 0.0), (0.0, 0.0), (0.0, 1.0)), 
    normals=[(-0.0, -1.0, 0.0), (-0.0, -1.0, 0.0), (-0.0, -1.0, 0.0), (-0.0, 1.0, -0.0), (-0.0, 1.0, -0.0), (-0.0, 1.0, -0.0), (1.0, -0.0, 0.0), (1.0, -0.0, 0.0), (1.0, -0.0, 0.0), (-0.0, -0.0, -1.0), (-0.0, -0.0, -1.0), (-0.0, -0.0, -1.0), (-1.0, -0.0, 0.0), (-1.0, -0.0, 0.0), (-1.0, -0.0, 0.0), (0.0, 0.0, 1.0), (0.0, 0.0, 1.0), (0.0, 0.0, 1.0), (-0.0, -1.0, 0.0), (-0.0, -1.0, 0.0), (-0.0, -1.0, 0.0), (-0.0, 1.0, -0.0), (-0.0, 1.0, -0.0), (-0.0, 1.0, -0.0), (1.0, -0.0, 0.0), (1.0, -0.0, 0.0), (1.0, -0.0, 0.0), (-0.0, -0.0, -1.0), (-0.0, -0.0, -1.0), (-0.0, -0.0, -1.0), (-1.0, -0.0, 0.0), (-1.0, -0.0, 0.0), (-1.0, -0.0, 0.0), (0.0, 0.0, 1.0), (0.0, 0.0, 1.0), (0.0, 0.0, 1.0)], 
    mode='triangle'
) """
# Widget
Text("Ursina on Android", scale=2, position=(.0, .3), origin=(0, 0))
Text("It finally works", position=(.0, .1), origin=(0, 0))

welcomeText = Text("Hello, World!", position=(0, 0), scale=1.5, origin=(0, 0))
cube = Entity(model="cube.ursinamesh", scale=.1, position=(0, -.1), origin=(0, 0), color=color.red, parent=camera.ui)
Entity(model="quad.ursinamesh", scale=.1, position=(.0, .3), origin=(0, 0), texture="ursina", parent=camera.ui)
button = Button("Change background color", color=color.lime, pressed_color=color.yellow, origin=(0, 0), position=(0, -.3), scale=(.4, .07), text_color=color.gray)

# Change window color to random color on button click
def changeBack():
    window.color = color.random_color()

# Make cube rotating
def update():
    cube.rotation += Vec3(1, 1, 0)

# Add the onclick event
button.on_click = changeBack

# Run your app
app.run()