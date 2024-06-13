from particle_automata.matrix import GameMatrix
import numpy as np
import pytest

@pytest.fixture
def numpy_matrix():
    matrix = [
        [0, 1, 2, 3, 4],
        [5, 6, 7, 8, 9],
        [10, 11, 12, 13, 14],
        [15, 16, 17, 18, 19],
        [20, 21, 22, 23, 24],
    ]
    return np.array(matrix)

def test_game_matrix():
    matrix = GameMatrix(5, 5)
    assert matrix.width == 5
    assert matrix.height == 5
    assert (matrix.matrix == np.zeros((5, 5), dtype=int)).all()

def test_slice_square_around(numpy_matrix):
    matrix = GameMatrix(5, 5)
    matrix.matrix = numpy_matrix
    assert (matrix.slice_square_around(2, 2, 1) == np.array([[6, 7, 8], [11, 12, 13], [16, 17, 18]])).all()