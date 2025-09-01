import numpy as np
i, j = np.indices((8, 8))
# `np.indices((8, 8))` creates a pair of arrays `i` and `j` where `i` contains the row indices and `j`
# contains the column indices for an 8x8 grid. Each element in `i` and `j` corresponds to the row and
# column index of a cell in the grid.

chessboard = (i + j) % 2

print(chessboard)