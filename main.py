from gl import Renderer, V2, V3, color
import shaders

# Modifiable parameters for the render in the rasterizer
## Window size
height = 500
width = 1000
outputName = 'output'

starVertices = [
    V2(165, 380),
    V2(185, 360),
    V2(180, 330),
    V2(207, 345),
    V2(233, 330),
    V2(230, 360),
    V2(250, 380),
    V2(220, 385),
    V2(205, 410),
    V2(193, 383)
]

squareVertices = [
    V2(321, 335),
    V2(288, 286),
    V2(339, 251),
    V2(374, 302),
]

triangleVertices = [
    V2(377, 249),
    V2(411, 197),
    V2(436, 249)
]

teaCupVertices = [
    V2(413, 177),
    V2(448, 159),
    V2(502, 88), 
    V2(553, 53), 
    V2(535, 36),
    V2(676, 37),
    V2(660, 52),
    V2(750, 145),
    V2(761, 179), 
    V2(672, 192),
    V2(659, 214), 
    V2(615, 214),
    V2(632, 230),
    V2(580, 230),
    V2(597, 215),
    V2(552, 214), 
    V2(517, 144),
    V2(466, 180)
]

vertices = [
    V2(682, 175), 
    V2(708, 120), 
    V2(735, 148), 
    V2(739, 170)
]

polygons = [
    [starVertices, color(1, 1, 0)],
    [squareVertices, color(1, 0, 0)],
    [triangleVertices, color(0, 1, 0)],
    [teaCupVertices, color(1, 1, 1)],
    [vertices, color(0, 0, 0)]
]

render = Renderer(width, height)
render.vertexShader = shaders.vertexShader
render.fragmentShader = shaders.fragmentShader
for polygon in polygons:
    render.glFillPolygon(polygon[0], polygon[1])
render.glRender()
render.glFinish(outputName + '.bmp')