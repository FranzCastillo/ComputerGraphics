from gl import Renderer
import shaders

# Modifiable parameters for the render
modelPath = "models/pumpkin.obj"
texturePath = "textures/pumpkin.bmp"
outputPath = "output/output.bmp"

width = 512
height = 512

scale = 2

render = Renderer(width, height)
render.glDirectionalLightDirection(0, -1, -0.5)
render.glClearColor(0.65, 0.65, 0.65)
render.glClear()
render.vertexShader = shaders.vertexShader
render.fragmentShader = shaders.newShader

render.glLoadModel(filename = modelPath,
                 textureName = texturePath,
                 translate = (0, 0, -5),
                 rotate = (0, 25, 0),
                 scale = (scale, scale, scale))

render.glRender()
render.glFinish(outputPath)