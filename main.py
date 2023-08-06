from gl import Renderer
import shaders

# Modifiable parameters for the render
modelPath = "models/model.obj"
texturePath = "textures/model.bmp"
outputPath = "output/output.bmp"

width = 960
height = 540

scale = 2

cameraPositionX = -3
cameraPositionY = -1
cameraPositionZ = -2

eyePositionX = 0
eyePositionY = 0
eyePositionZ = -5


render = Renderer(width, height)
render.vertexShader = shaders.vertexShader
render.fragmentShader = shaders.fragmentShader

render.glLookAt(
    camPos = (cameraPositionX, cameraPositionY, cameraPositionZ), 
    eyePos= (eyePositionX, eyePositionY, eyePositionZ))

render.glLoadModel(filename = "models/model.obj",
                 textureName = "textures/model.bmp",
                 translate = (0, 0, -5),
                 rotate = (0, 0, 0),
                 scale = (scale, scale, scale))

render.glRender()
render.glFinish(outputPath)