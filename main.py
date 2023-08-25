from gl import Renderer
import shaders

backgroundPath = "backgrounds/PARK.bmp"
outputPath = "output/scene/parkWithShaders.bmp"

width = 1920
height = 1080


render = Renderer(width, height)
render.glDirectionalLightDirection(1.3, 0.5, 1.2)
render.glBackgroundTexture(backgroundPath)
render.glClearBackground()
render.vertexShader = shaders.vertexShader

def loadFish(tx, ty, tz, rx, ry, rz):
    modelPath = "models/fish.obj"
    texturePathFish = "textures/fish.bmp"
    scale = 0.1
    
    render.fragmentShader = shaders.colorTinting

    render.glLoadModel(filename = modelPath,
                     textureName = texturePathFish,
                     translate = (tx, ty, tz),
                     rotate = (rx, ry, rz),
                     scale = (scale, scale, scale))
    
    render.glRender()
    
def loadDog():
    modelPath = "models/dog.obj"
    texturePathDog = "textures/dog.bmp"
    scale = 0.2
    
    render.fragmentShader = shaders.adjustedContrast

    render.glLoadModel(filename = modelPath,
                     textureName = texturePathDog,
                     translate = (-2, -2.4, -5),
                     rotate = (0, 45, 0),
                     scale = (scale, scale, scale))
    render.glRender()
    
    
def loadGuy():
    modelPath = "models/guy.obj"
    texturePathGuy = "textures/guy.bmp"
    scale = 0.045
    render.glDirectionalLightDirection(-5, 0, 0)
    render.fragmentShader = shaders.ghostShader

    render.glLoadModel(filename = modelPath,
                     textureName = texturePathGuy,
                     translate = (-2.6, -1, -5),
                     rotate = (0, -30, 0),
                     scale = (scale, scale, scale))
    
    render.glRender()
    
    
def loadHelicopter():
    modelPath = "models/helicopter.obj"
    texturePathGuy = "textures/helicopter.bmp"
    scale = 0.01
    
    render.glDirectionalLightDirection(2, -2, -2)
    render.fragmentShader = shaders.camouflageShader

    render.glLoadModel(filename = modelPath,
                     textureName = texturePathGuy,
                     translate = (-1.9, 2, -5),
                     rotate = (0, -30, 0),
                     scale = (scale, scale, scale))
    
    render.glRender()

loadFish(0.9, -1, -5, 35, 30, -25)
loadFish(1.3, -1.3, -5, 35, 30, -25)
loadFish(1.43, -0.9, -5, 35, 30, -25)
loadDog()
loadGuy()
loadHelicopter()

render.glFinish(outputPath)