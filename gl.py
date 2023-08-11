import struct
import numpy as np
from math import pi, sin, cos, tan
from mathLibrary import *
from model import Model

def char(c):
    # 1 byte
    return struct.pack('=c', c.encode('ascii'))

def word(w):
    # 2 bytes
    return struct.pack('=h', w)

def dword(d):
    # 4 bytes
    return struct.pack('=l', d)

def color(r, g, b):
    return bytes([int(b * 255),
                  int(g * 255),
                  int(r * 255)])


POINTS = 0
LINES = 1
TRIANGLES = 2
QUADS = 3

class Renderer(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.objects = []
        self.vertexShader = None
        self.fragmentShader = None
        self.primitiveType = TRIANGLES
        self.activeTexture = None
        
        self.direcitonalLigth = (1, 0, 0)
        
        self.glClearColor(0,0,0)
        self.glClear()
        self.glColor(1,1,1)
        self.glViewPort(0,0,self.width,self.height)
        self.glCamMatrix()
        self.glProjectionMatrix()

    def glClear(self):
        self.pixels = [[self.clearColor for _ in range(self.height)]
                       for _ in range(self.width)]

        self.zbuffer = [[float('inf') for _ in range(self.height)]
                       for _ in range(self.width)]
        
    def glColor(self, r, g, b):
        self.currColor = color(r,g,b)
    
    def glClearColor(self, r, g, b):
        self.clearColor = color(r,g,b)

    def glPoint(self, x, y, clr = None):
        if (0 <= x < self.width) and (0 <= y < self.height):
            self.pixels[x][y] = clr or self.currColor


    def glTriangle(self, A, B, C, vtA, vtB, vtC, triangleNormal):
        minX = round(min(A[0], B[0], C[0]))
        maxX = round(max(A[0], B[0], C[0]))
        minY = round(min(A[1], B[1], C[1]))
        maxY = round(max(A[1], B[1], C[1]))

        # Para cada pixel dentro del bounding box
        for x in range(minX, maxX + 1):
            for y in range(minY, maxY + 1):
                # Si el pixel est� dentro del FrameBuffer
                if (0 <= x < self.width) and (0 <= y < self.height):
                    P = (x,y)
                    bCoords = getBarycentricCoords(A, B, C, P)
                    
                    if bCoords != None:
                        u, v, w = bCoords
                        
                        z = u * A[2] + v * B[2] + w * C[2]
                        if z < self.zbuffer[x][y]:
                            self.zbuffer[x][y] = z
                            
                            uvs = (u * vtA[0] + v * vtB[0] + w * vtC[0],
                                   u * vtA[1] + v * vtB[1] + w * vtC[1])
                            
                            if self.fragmentShader != None:
                                colorP = self.fragmentShader(texCoords = uvs,
                                                             texture = self.activeTexture,
                                                             triangleNormal = triangleNormal,
                                                             dLight = self.direcitonalLigth)

                                self.glPoint(x, y, color(colorP[0], colorP[1], colorP[2]))
                            else:
                                self.glPoint(x, y)


    def glPrimitiveAssembly(self, tVerts, tTexCoords, normals):
        primitives = [ ]
        if self.primitiveType == TRIANGLES:
            for i in range(0, len(tVerts), 3):
                triangle = [
                    tVerts[i],
                    tVerts[i + 1],
                    tVerts[i + 2],
                    tTexCoords[i],
                    tTexCoords[i + 1],
                    tTexCoords[i + 2],
                    normals[int(i / 3)]
                ]
                primitives.append(triangle)
        return primitives

    def glViewPort(self,x,y,width,height):
        self.vpX = x
        self.vpY = y
        self.vpWidth = width
        self.vpHeight = height
        self.vpMatrix = np.matrix([[self.vpWidth/2,0,0,self.vpX+self.vpWidth/2],
                                   [0,self.vpHeight/2,0,self.vpY+self.vpHeight/2],
                                   [0,0,0.5,0.5],
                                   [0,0,0,1]])

    def glCamMatrix(self, translate = (0,0,0), rotate = (0,0,0)):
        self.camMatrix = self.glModelMatrix(translate, rotate)
        self.viewMatrix = np.linalg.inv(self.camMatrix)
          
    def glLookAt(self, camPos = (0,0,0), eyePos = (0,0,0)):
        worldUp = (0,1,0)
        
        forward = np.subtract(camPos, eyePos)
        forward = forward / np.linalg.norm(forward)
        
        right = np.cross(worldUp, forward)
        right = right / np.linalg.norm(right)
        
        up = np.cross(forward, right)
        up = up / np.linalg.norm(up)
        
        self.camMatrix = np.matrix([[right[0],up[0],forward[0],camPos[0]],
                                    [right[1],up[1],forward[1],camPos[1]],
                                    [right[2],up[2],forward[2],camPos[2]],
                                    [0,0,0,1]])
        
        self.viewMatrix = np.linalg.inv(self.camMatrix)
        
    def glProjectionMatrix(self, fov = 60, n = 0.1, f = 1000):
        aspectRatio = self.vpWidth/self.vpHeight
        
        t = tan((fov*pi/180)/2)*n
        
        r = t * aspectRatio
        
        self.projectionMatrix = np.matrix([[n/r,0,0,0],
                                           [0,n/t,0,0],
                                           [0,0,-(f+n)/(f-n),(-2*f*n)/(f-n)],
                                           [0,0,-1,0]])
    
    def glModelMatrix(self, translate = (0,0,0), rotate = (0,0,0), scale = (1,1,1)):
        translation = np.matrix([[1,0,0,translate[0]],
                                 [0,1,0,translate[1]],
                                 [0,0,1,translate[2]],
                                 [0,0,0,1]])

        rotMat = self.glRotationMatrix(rotate[0], rotate[1], rotate[2])

        scaleMat = np.matrix([[scale[0],0,0,0],
                              [0,scale[1],0,0],
                              [0,0,scale[2],0],
                              [0,0,0,1]])
        
        return translation * rotMat * scaleMat


    def glRotationMatrix(self, pitch = 0, yaw = 0, roll = 0):
        pitch *= pi / 180
        yaw *= pi / 180
        roll *= pi / 180

        pitchMat = np.matrix([[1,0,0,0],
                              [0,cos(pitch),-sin(pitch),0],
                              [0,sin(pitch),cos(pitch),0],
                              [0,0,0,1]])

        yawMat = np.matrix([[cos(yaw),0,sin(yaw),0],
                            [0,1,0,0],
                            [-sin(yaw),0,cos(yaw),0],
                            [0,0,0,1]])

        rollMat = np.matrix([[cos(roll),-sin(roll),0,0],
                             [sin(roll),cos(roll),0,0],
                             [0,0,1,0],
                             [0,0,0,1]])

        return pitchMat * yawMat * rollMat



    def glLine(self, v0, v1, clr = None):
        x0 = int(v0[0])
        x1 = int(v1[0])
        y0 = int(v0[1])
        y1 = int(v1[1])

        if x0 == x1 and y0 == y1:
            self.glPoint(x0,y0)
            return

        dy = abs(y1 - y0)
        dx = abs(x1 - x0)

        steep = dy > dx
        if steep:
            x0, y0 = y0,x0
            x1, y1 = y1,x1

        if x0 > x1:
            x0, x1 = x1, x0
            y0, y1 = y1, y0

        dy = abs(y1 - y0)
        dx = abs(x1 - x0)
        offset = 0
        limit = 0.5
        m = dy/dx
        y = y0

        for x in range(x0, x1 + 1):
            if steep:
                self.glPoint(y, x, clr or self.currColor)
            else:
                self.glPoint(x, y, clr or self.currColor)

            offset += m
            if offset >= limit:
                if y0 < y1:
                    y += 1
                else:
                    y -= 1

                limit += 1


    def glLoadModel(self, filename, textureName, translate = (0,0,0), rotate = (0,0,0), scale = (1,1,1)):
        model = Model(filename, translate, rotate, scale)
        model.LoadTexture(textureName)
        self.objects.append(model)


    def glRender(self):
        transformedVerts = []
        texCoords = []
        normals = []
        
        for model in self.objects:
            self.activeTexture = model.texture
            mMat = self.glModelMatrix(model.translate, model.rotate, model.scale)
            for face in model.faces:
                vertCount = len(face)

                v0 = model.vertices[ face[0][0] - 1]
                v1 = model.vertices[ face[1][0] - 1]
                v2 = model.vertices[ face[2][0] - 1]
                if vertCount == 4:
                    v3 = model.vertices[ face[3][0] - 1]
                    
                triangleNormal0 = np.cross(np.subtract(v1, v0), np.subtract(v2, v0))
                triangleNormal0 = triangleNormal0 / np.linalg.norm(triangleNormal0)
                normals.append(triangleNormal0)
                if vertCount == 4:
                    triangleNormal1 = np.cross(np.subtract(v2, v0), np.subtract(v3, v0))
                    triangleNormal1 = triangleNormal1 / np.linalg.norm(triangleNormal1)
                    normals.append(triangleNormal1)
                    

                if self.vertexShader:
                    v0 = self.vertexShader(v0,
                                           modelMatrix = mMat,
                                           viewMatrix = self.viewMatrix,
                                           projectionMatrix = self.projectionMatrix,
                                           vpMatrix = self.vpMatrix)
                    v1 = self.vertexShader(v1, 
                                           modelMatrix = mMat,
                                           viewMatrix = self.viewMatrix,
                                           projectionMatrix = self.projectionMatrix,
                                           vpMatrix = self.vpMatrix)
                    v2 = self.vertexShader(v2, 
                                           modelMatrix = mMat,
                                           viewMatrix = self.viewMatrix,
                                           projectionMatrix = self.projectionMatrix,
                                           vpMatrix = self.vpMatrix)
                    if vertCount == 4:
                        v3 = self.vertexShader(v3, modelMatrix = mMat,
                                           viewMatrix = self.viewMatrix,
                                           projectionMatrix = self.projectionMatrix,
                                           vpMatrix = self.vpMatrix)
                transformedVerts.append(v0)
                transformedVerts.append(v1)
                transformedVerts.append(v2)
                if vertCount == 4:
                    transformedVerts.append(v0)
                    transformedVerts.append(v2)
                    transformedVerts.append(v3)

                vt0 = model.texcoords[face[0][1] - 1]
                vt1 = model.texcoords[face[1][1] - 1]
                vt2 = model.texcoords[face[2][1] - 1]
                if vertCount == 4:
                    vt3 = model.texcoords[face[3][1] - 1]
                    
                texCoords.append(vt0)
                texCoords.append(vt1)
                texCoords.append(vt2)
                if vertCount == 4:
                    texCoords.append(vt0)
                    texCoords.append(vt2)
                    texCoords.append(vt3)

        primitives = self.glPrimitiveAssembly(transformedVerts, texCoords, normals)       

        for prim in primitives:
            if self.primitiveType ==  TRIANGLES:
                self.glTriangle(prim[0], prim[1], prim[2],
                                prim[3], prim[4], prim[5],
                                prim[6])
        
    def glFinish(self, filename):
        with open(filename, "wb") as file:
            # Header
            file.write(char("B"))
            file.write(char("M"))
            file.write(dword(14 + 40 + (self.width * self.height * 3)))
            file.write(dword(0))
            file.write(dword(14 + 40))

            # InfoHeader
            file.write(dword(40))
            file.write(dword(self.width))
            file.write(dword(self.height))
            file.write(word(1))
            file.write(word(24))
            file.write(dword(0))
            file.write(dword(self.width * self.height * 3))
            file.write(dword(0))
            file.write(dword(0))
            file.write(dword(0))
            file.write(dword(0))

            # Color table
            for y in range(self.height):
                for x in range(self.width):
                    file.write(self.pixels[x][y])