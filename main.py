from gl import Renderer
import shaders

backgroundPath = "backgrounds/PARK.bmp"
outputPath = "output/scene/park.bmp"

width = 1920
height = 1080


render = Renderer(width, height)
render.glDirectionalLightDirection(1.3, 0.5, 1.2)
render.glBackgroundTexture(backgroundPath)
render.glClearBackground()
render.vertexShader = shaders.vertexShader

def loadFish(tx, ty, tz, rx, ry, rz):
    modelPath = "models/fish.obj"
    texturePath = "textures/fish.bmp"
    scale = 0.1
    
    render.fragmentShader = shaders.noShader

    render.glLoadModel(filename = modelPath,
                     textureName = texturePath,
                     translate = (tx, ty, tz),
                     rotate = (rx, ry, rz),
                     scale = (scale, scale, scale))
    
def loadDog():
    modelPath = "models/dog.obj"
    texturePath = "textures/dog.bmp"
    scale = 0.2
    
    render.fragmentShader = shaders.noShader

    render.glLoadModel(filename = modelPath,
                     textureName = texturePath,
                     translate = (-2, -2.4, -5),
                     rotate = (0, 45, 0),
                     scale = (scale, scale, scale))
    
def loadSquirrel():
    modelPath = "models/guy.obj"
    texturePath = "textures/guy.bmp"
    scale = 0.05
    
    render.fragmentShader = shaders.noShader

    render.glLoadModel(filename = modelPath,
                     textureName = texturePath,
                     translate = (2, -2.4, -5),
                     rotate = (0, -45, 0),
                     scale = (scale, scale, scale))

# loadFish(0.9, -1, -5, 35, 30, -25)
# loadFish(1.3, -1.3, -5, 35, 30, -25)
# loadFish(1.43, -0.9, -5, 35, 30, -25)
# loadDog()
loadSquirrel()

render.glRender()
render.glFinish(outputPath)