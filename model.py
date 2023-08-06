from obj import Obj
from texture import Texture

class Model(object):
    def __init__(self, filename, translate = (0,0,0), rotate = (0,0,0), scale = (1,1,1)):
        model = Obj(filename)
        self.vertices = model.vertices
        self.texcoords = model.texcoords
        self.normals = model.normals
        self.faces = model.faces

        self.translate = translate
        self.rotate = rotate
        self.scale = scale

    def LoadTexture(self, textureName):
        self.texture = Texture(textureName)