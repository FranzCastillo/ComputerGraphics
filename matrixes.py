# https://www.geeksforgeeks.org/python-program-multiply-two-matrices/
"""Multiplication of two matrixes

Args:
    A (list): First matrix
    B (list): Second matrix

Returns:
    list: Result of multiplication
"""
import math


def multiplyMatrices(A, B):
    if len(A[0]) != len(B):
        raise ValueError("The number of columns in the first matrix must be equal to the number of rows in the second matrix")
    
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    
    return result

"""Multiplication of a matrix and a vector

Args:
    M (list): Matrix
    v (list): Vector

Returns:
    list: Result of multiplication
"""
def multiplyMatrixVector(M, v):
    result = [0 for _ in range(len(M))]
    
    for i in range(len(M)):
        for j in range(len(v)):
            result[i] += M[i][j] * v[j]
    
    return result

"""
Chat GPT: How can I get the inverse matrix in python without a library?
"""

def identity_matrix(n):
    """
    Creates an identity matrix of size n x n.
    """
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]

def swap_rows(matrix, row1, row2):
    """
    Swaps two rows in a matrix.
    """
    matrix[row1], matrix[row2] = matrix[row2], matrix[row1]

def scale_row(matrix, row, factor):
    """
    Scales a row in a matrix by a factor.
    """
    for i in range(len(matrix[row])):
        matrix[row][i] *= factor

def add_scaled_row(matrix, source_row, target_row, factor):
    """
    Adds a scaled row to another row in a matrix.
    """
    for i in range(len(matrix[source_row])):
        matrix[target_row][i] += factor * matrix[source_row][i]

def inverse(matrix):
    """
    Calculates the inverse of a square matrix using Gauss-Jordan elimination.
    """
    n = len(matrix)
    augmented_matrix = [row + identity_matrix(n)[i] for i, row in enumerate(matrix)]

    for col in range(n):
        # Scale the pivot row to make the pivot element equal to 1
        pivot_row = col
        while augmented_matrix[pivot_row][col] == 0:
            pivot_row += 1
            if pivot_row == n:
                raise ValueError("Matrix is singular, inverse does not exist.")
        swap_rows(augmented_matrix, col, pivot_row)
        scale_row(augmented_matrix, col, 1 / augmented_matrix[col][col])

        # Eliminate other elements in the column
        for row in range(n):
            if row != col:
                factor = -augmented_matrix[row][col]
                add_scaled_row(augmented_matrix, col, row, factor)

    # Extract the inverse matrix from the augmented matrix
    inverse_matrix = [row[n:] for row in augmented_matrix]

    return inverse_matrix

def subtract(arr1, arr2):
    if arr1.shape != arr2.shape:
        raise ValueError("Input arrays must have the same shape")

    # Perform element-wise subtraction
    result = arr1 - arr2
    return result

def crossProduct(arr1, arr2):
    if len(arr1) != 3 or len(arr2) != 3:
        raise ValueError("Input arrays must have 3 elements each")

    # Calculate the cross product
    cross_product = [
        (arr1[1] * arr2[2] - arr1[2] * arr2[1]),
        (arr1[2] * arr2[0] - arr1[0] * arr2[2]),
        (arr1[0] * arr2[1] - arr1[1] * arr2[0])
    ]
    return cross_product

def norm(arr):
    if len(arr.shape) != 1:
        raise ValueError("Input array must be 1D")

    # Calculate the sum of squares
    sum_of_squares = sum(x ** 2 for x in arr)

    # Calculate the square root of the sum of squares to get the norm
    norm = math.sqrt(sum_of_squares)
    return norm