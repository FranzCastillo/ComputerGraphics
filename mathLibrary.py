def getBarycentricCoordinates(A, B, C, P):
    pcbArea = (B[1] - C[1]) * (P[0] - C[0]) + (C[0] - B[0]) * (P[1] - C[1])
    acpArea = (C[1] - A[1]) * (P[0] - C[0]) + (A[0] - C[0]) * (P[1] - C[1])
    abcArea = (B[1] - C[1]) * (A[0] - C[0]) + (C[0] - B[0]) * (A[1] - C[1])
    
    u = pcbArea / abcArea
    v = acpArea / abcArea
    w = 1 - u - v

    return u, v, w