from matrixes import multiplyMatrixVector

def vertexShader(vertex, **kwargs):
    modelMatrix = kwargs["modelMatrix"]
    vt = [vertex[0],
          vertex[1],
          vertex[2],
          1]
    vt = multiplyMatrixVector(modelMatrix, vt)
    vt = [vt[0]/vt[3], 
          vt[1]/vt[3], 
          vt[2]/vt[3]]
    return vt

def fragmentShader(**kwargs):
      textureCoords = kwargs["texCoords"]
      texture = kwargs["texture"]
      color = (1, 1, 1)
      if texture != None:
            color = texture.getColor(textureCoords[0], textureCoords[1])
      return color
