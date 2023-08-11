import numpy as np

def vertexShader(vertex, **kwargs):
    modelMatrix = kwargs["modelMatrix"]
    viewMatrix = kwargs["viewMatrix"]
    projectionMatrix = kwargs["projectionMatrix"]
    vpMatrix = kwargs["vpMatrix"]

    vt = [vertex[0],
          vertex[1],
          vertex[2],
          1]

    vt = vpMatrix * projectionMatrix * viewMatrix * modelMatrix @ vt
    vt = vt.tolist()[0]
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


def flatShader(**kwargs):
    texCoords = kwargs["texCoords"]
    texture = kwargs["texture"]
    normal = kwargs["triangleNormal"]
    
    dLight = kwargs["dLight"]
    dLight = np.array(dLight)
    
    color = [1, 1, 1]
    
    if texture != None:
        color = texture.getColor(texCoords[0], texCoords[1])
    
    intensity = np.dot(normal, -dLight)
    
    color = [max(0, min(1, c * intensity)) for c in color]
    
    return color
    
    