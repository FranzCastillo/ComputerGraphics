import struct
from collections import namedtuple
# import numpy as np
from obj import Obj
from matrixes import *
from math import cos, sin, pi
from mathLibrary import *

# Save the coordinates of the vertices 
V2 = namedtuple('point', ['x','y'])
V3 = namedtuple('point', ['x','y','z'])

# Save the type of primitive
POINTS = 0
LINES = 1
TRIANGLES = 2
QUADS = 3

# Write the BMP file 
def char(c):
    return struct.pack('=c', c.encode('ascii'))

# Write the BMP file
def word(w):
    return struct.pack('=h', w)

# Write the BMP file
def dword(d):
    return struct.pack('=l', d)

# Transform the color format from float to bytes
def color(r, g, b):
    return bytes([int(b*255), int(g*255), int(r*255)])

class Model(object):
    def __init__(self, filename, translate = (0,0,0), rotate = (0,0,0), scale = (1,1,1)):
        model = Obj(filename)

        self.faces = model.faces
        self.vertices = model.vertices
        self.normals = model.normals
        self.texcoords = model.texcoords

        self.translate = translate
        self.rotate = rotate
        self.scale = scale

class Renderer(object):
    # Constructor
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
        self.glClearColor(0,0,0)
        self.glClear()
        self.glColor(1,1,1)

        self.vertexShader = None
        self.fragmentShader = None
        self.primitiveType = TRIANGLES
        self.vertexBuffer = []

        self.objects = []

    def glAddVertices(self, vertices):
        for vertex in vertices:
            self.vertexBuffer.append(vertex)
       
    def glPrimitiveAssembly(self, transformedVertices):
        # Assembly the vertices into points, lines or triangles
        primitives = []

        if self.primitiveType == TRIANGLES:
            for i in range(0, len(transformedVertices), 3):
                triangle = [
                    transformedVertices[i],
                    transformedVertices[i+1],
                    transformedVertices[i+2]
                ]
                primitives.append(triangle)
    
        return primitives

    # Clear the screen
    def glClearColor(self, r, g, b):
        self.clearColor = color(r,g,b)
    
    # Clear the screen
    def glClear(self):
        self.pixels = [[self.clearColor for _ in range(self.height)] for _ in range(self.width)]
        
        self.zbuffer = [[float('inf') for _ in range(self.height)] for _ in range(self.width)]
        
    # Set the color
    def glColor(self, r, g, b):
        self.currColor = color(r,g,b)
        
    # Draw a point
    def glPoint(self, x, y, clr = None):
        if (0 <= x < self.width) and (0 <= y < self.height):
            self.pixels [x][y] = clr or self.currColor
            
    # Draw a line
    def glLine(self, v0, v1, clr = None):
        # Bressenham line algorith
        # y = mx+b
        
        #m = (v1.y-v0.y)/(v1.x-v0.x)
        #y = v0.y
        
        #for x in range(v0.x, v1.x+1):
        #   self.glPoint(x,int(y))
        #   y += m
            
        x0 = int(v0[0])
        x1 = int(v1[0])
        y0 = int(v0[1])
        y1 = int(v1[1])
        

        # Si las coordenadas son las mismas, se dibuja un solo pixel
        if x0 == x1 and y0 == y1:
            self.glPoint(x0,y0)
            return
        
        dy = abs(y1 - y0)
        dx = abs(x1 - x0)
        
        # Se verifica si la pendiente es mayor que 1 (Porque, si es así, saltaría pixeles)
        steep = dy > dx
        
        # Si la pendiente es mayor que 1 o menor que -1
        # entonces intercambiamos los valores de x y y
        # para reorientar la linea (Se dibuja vertical en vez de horizontal)
        if steep:
            x0, y0 = y0, x0
            x1, y1 = y1, x1
        
        # Si el punto inicial es mayor que el punto final, se intercambian
        if x0 > x1:
            x0, x1 = x1, x0
            y0, y1 = y1, y0
        
        # Se recalculan las diferencias
        dy = abs(y1 - y0)
        dx = abs(x1 - x0)
        
        offset = 0
        limit = 0.5
        
        m = dy/dx
        y = y0
        
        for x in range(x0, x1+1):
            # Si la pendiente es mayor que 1, se dibuja vertical
            if steep:
               self.glPoint(y, x, clr or self.currColor)
            else:
                self.glPoint(x, y, clr or self.currColor)
            
            offset += m
            
            if offset > limit:
                if y0 < y1:
                    y += 1
                else:
                    y -= 1
                
                limit += 1
        
    # Draw a triangle
    def glTriangle(self, A, B, C, clr = None):
        self.glLine(A, B, clr or self.currColor)
        self.glLine(B, C, clr or self.currColor)
        self.glLine(C, A, clr or self.currColor)

    def glBaricentricTriangle(self, A, B, C, clr = None):
        # Bounding box
        minX = round(min(A[0], B[0], C[0]))
        minY = round(min(A[1], B[1], C[1]))
        maxX = round(max(A[0], B[0], C[0]))
        maxY = round(max(A[1], B[1], C[1]))
        
        colorA = (1, 0, 0)
        colorB = (0, 1, 0)
        colorC = (0, 0, 1)
        
        for x in range(minX, maxX + 1):
            for y in range(minY, maxY + 1):
                if (0 <= x < self.width) and (0 <= y < self.height):
                    P = (x,y)
                    u, v, w = getBarycentricCoordinates(A, B, C, P)
                    if 0 <= u <= 1 and 0 <= v <= 1 and 0 <= w <= 1:
                        z = u * A[2] + v * B[2] + w * C[2]
                        if z < self.zbuffer[x][y]:
                            self.zbuffer[x][y] = z
                            pixelColor = color( u * colorA[0] + v * colorB[0] + w * colorC[0],
                                                u * colorA[1] + v * colorB[1] + w * colorC[1],
                                                u * colorA[2] + v * colorB[2] + w * colorC[2])
                            self.glPoint(x,y, pixelColor)

    def glDrawPolygon(self, vertices, clr = None):
        for i in range(len(vertices)):
            v0 = vertices[i]
            v1 = vertices[(i+1)%len(vertices)]
            self.glLine(v0, v1, clr or self.currColor)

    # https://www.cs.uic.edu/~jbell/CourseNotes/ComputerGraphics/PolygonFilling.html    
    def pointInPolygon(self, vertices, x, y):
        n = len(vertices) # Number of vertices
        inside = False # Inside or outside the polygon

        p1x, p1y = vertices[0] # First vertex
        for i in range(n+1): # For each vertex
            p2x, p2y = vertices[i % n] # Next vertex
            if y > min(p1y, p2y): # If the y coordinate is between the minimum and maximum y of the vertex
                if y <= max(p1y, p2y): 
                    if x <= max(p1x, p2x): # If the x coordinate is less than the maximum x of the vertex (then there will be no collision)
                        if p1y != p2y: 
                            m = (p2x-p1x)/(p2y-p1y)
                            xIntersection = (y-p1y)* m + p1x
                        if p1x == p2x or x <= xIntersection:
                            inside = not inside
            p1x,p1y = p2x,p2y

        return inside
    
    def glFillPolygon(self, vertices, clr = None):
        for y in range(self.height):
            for x in range(self.width):
                if self.pointInPolygon(vertices, x, y):
                    self.glPoint(x, y, clr or self.currColor)

    def glModelMatrix(self, translate = (0,0,0), scale = (1,1,1), rotate = (0,0,0)):
        rotate = [r * pi / 180 for r in rotate]
        
        translationMatrix = [
            [1,0,0,translate[0]],
            [0,1,0,translate[1]],
            [0,0,1,translate[2]],
            [0,0,0,1]
        ]

        scaleMatrix = [
            [scale[0],0,0,0],
            [0,scale[1],0,0],
            [0,0,scale[2],0],
            [0,0,0,1]
        ]

        rotationMatrix = [
            [1,0,0,0],
            [0,cos(rotate[0]),-sin(rotate[0]),0],
            [0,sin(rotate[0]),cos(rotate[0]),0],
            [0,0,0,1]
        ]

        temp = multiplyMatrices(translationMatrix, rotationMatrix)
        return multiplyMatrices(temp, scaleMatrix)

    def glLoadModel(self, filename, translate = (0,0,0), scale = (1,1,1), rotate = (0,0,0)):
        model = Model(filename, translate, rotate, scale)
        self.objects.append(model)

    def glRender(self):
        transformedVerts = []

        for model in self.objects:
            modelMatrix = self.glModelMatrix(model.translate, model.scale, model.rotate)

            for face in model.faces:
                vcount = len(face)

                v0 = model.vertices[face[0][0] - 1]
                v1 = model.vertices[face[1][0] - 1]
                v2 = model.vertices[face[2][0] - 1]
                if vcount == 4:
                    v3 = model.vertices[face[3][0] - 1]

                if self.vertexShader:
                    v0 = self.vertexShader(v0, modelMatrix = modelMatrix)
                    v1 = self.vertexShader(v1, modelMatrix = modelMatrix)
                    v2 = self.vertexShader(v2, modelMatrix = modelMatrix)
                    if vcount == 4:
                        v3 = self.vertexShader(v3, modelMatrix = modelMatrix)

                transformedVerts.append(v0)
                transformedVerts.append(v1)
                transformedVerts.append(v2)
                if vcount == 4:
                    transformedVerts.append(v0)
                    transformedVerts.append(v2)
                    transformedVerts.append(v3)

        for vert in self.vertexBuffer:
            transformedVerts.append(vert)

        primitives = self.glPrimitiveAssembly(transformedVerts)
        primitiveColor = self.currColor
        if self.fragmentShader:
            primitiveColor = self.fragmentShader()
            primitiveColor = color(
                primitiveColor[0],
                primitiveColor[1],
                primitiveColor[2]
            )
     

        for primitive in primitives:
            if self.primitiveType == TRIANGLES:
                A = primitive[0]
                B = primitive[1]
                C = primitive[2]
                self.glBaricentricTriangle(A, B, C, primitiveColor)

    # Export the BMP file
    def glFinish(self, filename):
        with open(filename, "wb") as file:
            #Header
            file.write(char("B")) #BMP
            file.write(char("M")) #BMP
            file.write(dword(14 + 40 + (self.width * self.height * 3))) #size
            file.write(dword(0)) #reserved
            file.write(dword(14 + 40)) #pixel offset

            #InfoHeader
            file.write(dword(40)) #InfoHeader size
            file.write(dword(self.width)) #width
            file.write(dword(self.height)) #height
            file.write(word(1)) #planes
            file.write(word(24)) #bits per pixel
            file.write(dword(0)) #compression
            file.write(dword(self.width * self.height * 3)) #image size
            file.write(dword(0)) #x resolution
            file.write(dword(0)) #y resolution
            file.write(dword(0)) #n colors
            file.write(dword(0)) #important colors

            #ColorTable
            for y in range(self.height):
                for x in range(self.width):
                    file.write(self.pixels[x][y])