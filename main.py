from gl import Renderer
import shaders

# Modifiable parameters for the render
modelPath = "models/pumpkin.obj"
texturePath = "textures/pumpkin.bmp"

width = 520
height = 520
scale = 1

eyePositionX = 0
eyePositionY = 0
eyePositionZ = 0
render = Renderer(width, height)
render.vertexShader = shaders.vertexShader
render.fragmentShader = shaders.fragmentShader

def mediumShot():
    outputPath = "output/pumpkinMediumShot.bmp"

    cameraPositionX = 1
    cameraPositionY = 0.5
    cameraPositionZ = 1

    render.glLookAt(
        camPos = (cameraPositionX, cameraPositionY, cameraPositionZ), 
        eyePos= (eyePositionX, eyePositionY, eyePositionZ))

    render.glLoadModel(filename = modelPath,
                     textureName = texturePath,
                     translate = (0, -0.2, 0),
                     rotate = (0, 45, 0),
                     scale = (scale, scale, scale))

    render.glRender()
    render.glFinish(outputPath)

def lowAngle():
    outputPath = "output/pumpkinLowAngle.bmp"

    cameraPositionX = 1
    cameraPositionY = -0.3
    cameraPositionZ = 1

    render.glLookAt(
        camPos = (cameraPositionX, cameraPositionY, cameraPositionZ), 
        eyePos= (eyePositionX, eyePositionY, eyePositionZ))

    render.glLoadModel(filename = modelPath,
                     textureName = texturePath,
                     translate = (0, -0.2, 0),
                     rotate = (0, 45, 0),
                     scale = (scale, scale, scale))

    render.glRender()
    render.glFinish(outputPath)
    
def highAngle():
    outputPath = "output/pumpkinHighAngle.bmp"

    cameraPositionX = 1
    cameraPositionY = 0.9
    cameraPositionZ = 1

    render.glLookAt(
        camPos = (cameraPositionX, cameraPositionY, cameraPositionZ), 
        eyePos= (eyePositionX, eyePositionY, eyePositionZ))

    render.glLoadModel(filename = modelPath,
                     textureName = texturePath,
                     translate = (0, -0.2, 0),
                     rotate = (0, 45, 0),
                     scale = (scale, scale, scale))

    render.glRender()
    render.glFinish(outputPath)    
    
def dutchAngle():
    outputPath = "output/pumpkinDutchAngle.bmp"

    cameraPositionX = 0.5
    cameraPositionY = -0.2
    cameraPositionZ = 1

    render.glLookAt(
        camPos = (cameraPositionX, cameraPositionY, cameraPositionZ), 
        eyePos= (eyePositionX, eyePositionY, eyePositionZ))

    render.glLoadModel(filename = modelPath,
                     textureName = texturePath,
                     translate = (0, -0.2, 0),
                     rotate = (0, 45, -15),
                     scale = (scale, scale, scale))

    render.glRender()
    render.glFinish(outputPath)

# mediumShot()
# lowAngle()
# highAngle()
dutchAngle()