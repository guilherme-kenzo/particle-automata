import numpy as np

class GameMatrix:
    
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.matrix = np.zeros((self.height, self.width), dtype=int)

    def slice_square_around(self, x: int, y: int, radius: int):
        left_limit = max(0, x - radius)
        right_limit = min(self.matrix.shape[1], x + radius + 1)
        down_limit = max(0, y - radius)
        up_limit = min(self.matrix.shape[0], y + radius + 1)
        return self.matrix[down_limit:up_limit, left_limit:right_limit]
