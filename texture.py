import struct

# Reads a texture from a file (only works with bmp files and color depth of 24 bits)
class Texture(object):
    def __init__(self, filename):
        with open(filename, 'rb') as image:
            image.seek(10)
            headerSize = struct.unpack('=l', image.read(4))[0]
            
            image.seek(18)
            self.width = struct.unpack('=l', image.read(4))[0]
            self.height = struct.unpack('=l', image.read(4))[0]
            
            image.seek(headerSize)
            
            self.pixels = []
            
            for _ in range(self.height):
                pixelRow = []
                for _ in range(self.width):
                    b = ord(image.read(1)) / 255
                    g = ord(image.read(1)) / 255
                    r = ord(image.read(1)) / 255
                    pixelRow.append([r, g, b])
                self.pixels.append(pixelRow)
                
                
    def getColor(self, tx, ty):
        if 0 <= tx < 1 and 0 <= ty < 1:
            x = int(tx * self.width)
            y = int(ty * self.height)
            
            return self.pixels[y][x]
        else:
            return None