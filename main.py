from gl import Renderer, V2, V3, color
import shaders

# Modifiable parameters for the render in the rasterizer
width = 1000
height = 1000

## Original obj scale is 1, we recommend to scale it up a couple hundred times
scaleX = 425
scaleY = 425
scaleZ = 425


## Path to the model that can be either the absolute or relative path
objPath = 'obj\pumpkin.obj'
texturePath = 'textures\pumpkin.bmp'
outputName = 'pumpkin' # No need to add the extension, it'll output a bmp file

render = Renderer(width, height)
render.vertexShader = shaders.vertexShader
render.fragmentShader = shaders.fragmentShader
render.glLoadModel(
    objPath,
    texturePath,
    translate=(175, 0, 0), 
    scale=(scaleX, scaleY, scaleZ),
    rotate=(0, 180, 0)
)

render.glLoadModel(
    objPath,
    texturePath,
    translate=(800, 0, 0),
    scale=(scaleX, scaleY, scaleZ),
    rotate=(0, 90, 0)
)

render.glLoadModel(
    objPath,
    texturePath,
    translate=(175, 800, 0),
    scale=(scaleX, scaleY, scaleZ),
    rotate=(90, 0, 0)
)

render.glLoadModel(
    objPath,
    texturePath,
    translate=(800, 800, 0),
    scale=(scaleX, scaleY, scaleZ),
    rotate=(-90, 0, 0)
)

render.glRender()
render.glFinish("output/" + outputName + '.bmp')