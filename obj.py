class Obj(object):
    def __init__(self, filename):
        try:
            with open(filename, "r") as file:
                self.lines = file.read().splitlines()

            self.vertices = []
            self.normals = []
            self.texcoords = []
            self.faces = []

            for line in self.lines:
                if line:
                    prefix, value = line.split(' ', 1)

                    if prefix == 'v': # Vertex
                        self.vertices.append(list(map(float, value.split(' '))))
                    elif prefix == 'vn': # Normal
                        self.normals.append(list(map(float, value.split(' '))))
                    elif prefix == 'vt': # Texture Coordinate
                        self.texcoords.append(list(map(float, value.split(' '))))
                    elif prefix == 'f': # Face
                        if '//' in value:
                            self.faces.append([list(map(int, vert.split('//'))) for vert in value.split(' ')])
                        else:
                            self.faces.append([list(map(int, vert.split('/'))) for vert in value.split(' ')])
        except:
            raise Exception(f"The file {filename} can't be opened. Please check the path")