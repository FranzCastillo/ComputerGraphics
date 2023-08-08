from matrixes import *

def vertexShader(vertex, **kwargs):
    modelMatrix = kwargs["modelMatrix"]
    viewMatrix = kwargs["viewMatrix"]
    projectionMatrix = kwargs["projectionMatrix"]
    vpMatrix = kwargs["vpMatrix"]

    vt = [vertex[0],
          vertex[1],
          vertex[2],
          1]

    # vt = vpMatrix * projectionMatrix * viewMatrix * modelMatrix @ vt
    temp = multiplyMatrices(vpMatrix, projectionMatrix)
    temp = multiplyMatrices(temp, viewMatrix)
    temp = multiplyMatrices(temp, modelMatrix)
    vt = multiplyMatrixVector(temp, vt)
    vt = [vt[0]/vt[3],
          vt[1]/vt[3],
          vt[2]/vt[3]]

    return vt

def fragmentShader(**kwargs):
    texCoords = kwargs["texCoords"]
    texture = kwargs["texture"]
    if texture != None:
        color = texture.getColor(texCoords[0], texCoords[1])
    else:
        color = (1,1,1)
    return color
