# https://www.geeksforgeeks.org/python-program-multiply-two-matrices/
"""Multiplication of two matrixes

Args:
    A (list): First matrix
    B (list): Second matrix

Returns:
    list: Result of multiplication
"""
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