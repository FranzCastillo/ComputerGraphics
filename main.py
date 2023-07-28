from gl import Renderer, V2, V3, color
import shaders

# Modifiable parameters for the render in the rasterizer
## Window size (4K size  by default)
height = 500
width = 500

## Translated to the center of the screen with width/2 and height/2
translateX = width/2
translateY = height/2
translateZ = 0

## Original obj scale is 1, we recommend to scale it up a couple hundred times
scaleX = 750
scaleY = 750
scaleZ = 750

## Rotation in degrees
rotateX = 0
rotateY = 0
rotateZ = 0

## Path to the model that can be either the absolute or relative path
outputName = 'brg' # No need to add the extension, it'll output a bmp file

render = Renderer(width, height)
render.vertexShader = shaders.vertexShader
render.fragmentShader = shaders.fragmentShader

vertices =[
    V2(50, 50),
    V2(250, 450),
    V2(450, 50)
]

render.glBaricentricTriangle(vertices[0], vertices[1], vertices[2], color(1, 0, 0))

render.glRender()
render.glFinish(outputName + '.bmp')