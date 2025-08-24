# https://www.deep-ml.com/problems/1

import numpy as np

def matrix_dot_vector_np(a: list[list[int|float]], b: list[int|float]):

    matrix = np.array(a)
    vector = np.array(b)

    if matrix.shape[1] != vector.shape[0]:
        return -1

    result = np.dot(matrix, vector)

    return result


print(matrix_dot_vector_np([[1, 2, 3], [2, 4, 5], [6, 8, 9]], [1, 2, 3])) # [14, 25, 49]
print(matrix_dot_vector_np([[1, 2], [2, 4], [6, 8], [12, 4]], [1, 2, 3])) # -1
print(matrix_dot_vector_np([[1.5, 2.5], [3.0, 4.0]], [2, 1])) # [5.5, 10.0]