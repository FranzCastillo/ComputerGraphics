from gl import Renderer
import shaders

# Modifiable parameters for the render
modelPath = "models/fish.obj"
texturePath = "textures/fish.bmp"
backgroundPath = "backgrounds/PARK.bmp"

width = 1920
height = 1080

scale = 1

render = Renderer(width, height)
render.glDirectionalLightDirection(1.3, 0.5, 1.2)
render.glBackgroundTexture(backgroundPath)
render.glClearBackground()
render.vertexShader = shaders.vertexShader

    
def noShader(outputPath):
    render.fragmentShader = shaders.noShader

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
noShader("output/shaders/noShader.bmp")