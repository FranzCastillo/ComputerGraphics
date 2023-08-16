from gl import Renderer
import shaders

# Modifiable parameters for the render
modelPath = "models/pumpkin.obj"
texturePath = "textures/pumpkin.bmp"

width = 512
height = 512

scale = 4

render = Renderer(width, height)
render.glDirectionalLightDirection(1.3, 0.5, 1.2)
render.glClearColor(0.65, 0.65, 0.65)
render.glClear()
render.vertexShader = shaders.vertexShader


def gouradShader(outputPath):
    render.fragmentShader = shaders.gouradShader

    render.glLoadModel(filename = modelPath,
                     textureName = texturePath,
                     translate = (0, -1, -5),
                     rotate = (0, 0, 0),
                     scale = (scale, scale, scale))

    render.glRender()
    render.glFinish(outputPath)
    
def thermalToonShader(outputPath):
    render.fragmentShader = shaders.thermalToonShader

    render.glLoadModel(filename = modelPath,
                     textureName = texturePath,
                     translate = (0, -1, -5),
                     rotate = (0, 45, 0),
                     scale = (scale, scale, scale))

    render.glRender()
    render.glFinish(outputPath)
    
def negativeThermalShader(outputPath):
    render.fragmentShader = shaders.negativeToonShader

    render.glLoadModel(filename = modelPath,
                     textureName = texturePath,
                     translate = (0, -1, -5),
                     rotate = (0, 45, 0),
                     scale = (scale, scale, scale))

    render.glRender()
    render.glFinish(outputPath)
    
def xRay(outputPath):
    render.fragmentShader = shaders.xRayShader

    render.glLoadModel(filename = modelPath,
                     textureName = texturePath,
                     translate = (0, -1, -5),
                     rotate = (0, 45, 0),
                     scale = (scale, scale, scale))

    render.glRender()
    render.glFinish(outputPath)
    
def textureLoader(outputPath):
    render.fragmentShader = shaders.textureLoaderShader

    render.glLoadModel(filename = modelPath,
                     textureName = texturePath,
                     translate = (0, -1, -5),
                     rotate = (0, 45, 0),
                     scale = (scale, scale, scale))

    render.glRender()
    render.glFinish(outputPath)
    
def textureRemover(outputPath):
    render.fragmentShader = shaders.removeTextureShader

    render.glLoadModel(filename = modelPath,
                     textureName = texturePath,
                     translate = (0, -1, -5),
                     rotate = (0, 45, 0),
                     scale = (scale, scale, scale))

    render.glRender()
    render.glFinish(outputPath)
    
def transparent(outputPath):
    render.fragmentShader = shaders.transparentShader

    render.glLoadModel(filename = modelPath,
                     textureName = texturePath,
                     translate = (0, -1, -5),
                     rotate = (0, 45, 0),
                     scale = (scale, scale, scale))

    render.glRender()
    render.glFinish(outputPath)
    
def blackAndWhite(outputPath):
    render.fragmentShader = shaders.blackAndWhite

    render.glLoadModel(filename = modelPath,
                     textureName = texturePath,
                     translate = (0, -1, -5),
                     rotate = (0, 45, 0),
                     scale = (scale, scale, scale))

    render.glRender()
    render.glFinish(outputPath)
    
def contrast(outputPath):
    render.fragmentShader = shaders.contrastShader

    render.glLoadModel(filename = modelPath,
                     textureName = texturePath,
                     translate = (0, -1, -5),
                     rotate = (0, 45, 0),
                     scale = (scale, scale, scale))

    render.glRender()
    render.glFinish(outputPath)
    
def adjustedContrast(outputPath):
    render.fragmentShader = shaders.adjustedContrast

    render.glLoadModel(filename = modelPath,
                     textureName = texturePath,
                     translate = (0, -1, -5),
                     rotate = (0, 45, 0),
                     scale = (scale, scale, scale))

    render.glRender()
    render.glFinish(outputPath)
    
def colorTinting(outputPath):
    render.fragmentShader = shaders.colorTinting

    render.glLoadModel(filename = modelPath,
                     textureName = texturePath,
                     translate = (0, -1, -5),
                     rotate = (0, 45, 0),
                     scale = (scale, scale, scale))

    render.glRender()
    render.glFinish(outputPath)
    
def posterization(outputPath):
    render.fragmentShader = shaders.posterizationShader

    render.glLoadModel(filename = modelPath,
                     textureName = texturePath,
                     translate = (0, -1, -5),
                     rotate = (0, 45, 0),
                     scale = (scale, scale, scale))

    render.glRender()
    render.glFinish(outputPath)
    
def gradient(outputPath):
    render.fragmentShader = shaders.gradient

    render.glLoadModel(filename = modelPath,
                     textureName = texturePath,
                     translate = (0, -1, -5),
                     rotate = (0, 45, 0),
                     scale = (scale, scale, scale))

    render.glRender()
    render.glFinish(outputPath)
    
def nightVision(outputPath):
    render.fragmentShader = shaders.nightVision

    render.glLoadModel(filename = modelPath,
                     textureName = texturePath,
                     translate = (0, -1, -5),
                     rotate = (0, 45, 0),
                     scale = (scale, scale, scale))

    render.glRender()
    render.glFinish(outputPath)
    
# gouradShader("output/shaders/gourad.bmp")
# thermalToonShader("output/shaders/thermalToon.bmp")
# negativeThermalShader("output/shaders/negativeThermal.bmp")
# xRay("output/shaders/xRay.bmp")
# textureLoader("output/shaders/textureLoader.bmp")
# textureRemover("output/shaders/textureRemover.bmp")
# transparent("output/shaders/transparent.bmp")
# blackAndWhite("output/shaders/blackAndWhite.bmp")
# contrast("output/shaders/contrast.bmp")
# adjustedContrast("output/shaders/adjustedContrast.bmp")
# colorTinting("output/shaders/colorTinting.bmp")
# posterization("output/shaders/posterization.bmp")
# gradient("output/shaders/gradient.bmp")
# nightVision("output/shaders/nightVision.bmp")