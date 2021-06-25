import numpy as np
from PIL import Image
from cayley_dickson import cayley_dickson_algebra

scale = 10
level = 5

algebra = cayley_dickson_algebra(level)
table = algebra.e_matrix(table=False, e="")
array = [[int(cell) for cell in row] for row in table]

# array = np.array(array) * 4
# img = Image.fromarray(array, 'L') # not working
# img = img.resize((scale * img.width, scale * img.height), Image.NEAREST)
# img.show()

img = Image.new('RGB', (len(array), len(array)))
data = img.load()
smallest = 2**(level - 1) - 1
for x in range(img.width):
    for y in range(img.height):
        val = array[y][x] + smallest
        val *= 256 // (2**(level))
        r, g, b = 0, 0, 0
        if val >= 0:
            r = val
        else:
            b = -val
        data[x, y] = val, val, val

img = img.resize((scale * img.width, scale * img.height), Image.NEAREST)
img.save('out.png')
img.show()
