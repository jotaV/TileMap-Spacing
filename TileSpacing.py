#TileSpacing.py

from scipy import ndimage
from scipy import misc

import numpy as np
import matplotlib.pyplot as plt

TILE_WIDTH = 32
TILE_HEIGHT = 16
TILE_SPACING_1 = 0

def main():
    tileset = misc.imread('cave_tiles_exodia.png')

    tiles
    x = 0 * TILE_WIDTH
    y = 1 * TILE_HEIGHT
    tile = np.array(tileset[y:y+16, x:x+32], dtype=tileset.dtype)




    misc.imsave('tile.png', tile)
    plt.imshow(tile)
    plt.show()

if __name__ == '__main__':
    main()
