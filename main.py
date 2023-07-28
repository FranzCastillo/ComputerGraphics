from gl import Renderer, V2, V3, color
import shaders

# Modifiable parameters for the render in the rasterizer
## Window size (4K size  by default)
width = 512
height = 512

## Translated to the center of the screen with width/2 and height/2
translateX = width/2
translateY = height/2
translateZ = 0

## Original obj scale is 1, we recommend to scale it up a couple hundred times
scaleX = 200
scaleY = 200
scaleZ = 200

## Rotation in degrees
rotateX = 0
rotateY = 90
rotateZ = 0

## Path to the model that can be either the absolute or relative path
path = 'model.obj'
outputName = 'person' # No need to add the extension, it'll output a bmp file

render = Renderer(width, height)
render.vertexShader = shaders.vertexShader
render.fragmentShader = shaders.fragmentShader
render.glLoadModel(
    path, 
    translate=(translateX, translateY, translateZ), 
    scale=(scaleX, scaleY, scaleZ),
    rotate=(rotateX, rotateY, rotateZ)
)

render.glRender()
render.glFinish(outputName + '.bmp')