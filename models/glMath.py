import math as m


def MultiplyMatrix(M1, M2):
    matrix = []
    for i in range(len(M1)):
        matrix.append([])
        for j in range(len(M2[0])):
            matrix[i].append(0)

    for i in range(len(M1)):
        for j in range(len(M2[0])):
            for k in range(len(M1[0])):
                matrix[i][j] += M1[i][k] * M2[k][j]
    return matrix


def IdentityOp(a):
    matrix = []
    for i in range(0, a):
        matrix.append([])
        for j in range(0, a):
            if (i == j):
                matrix[i].append(1)
            else:
                matrix[i].append(0)
    return matrix


def MV(M, V):
    matriz = []
    for fila in M:
        res = 0
        for col in range(len(fila)):
            res += (fila[col]*V[col])
        matriz.append(res)
    return matriz


def Cross(A, B):
    R = []
    R.append(A[1]*B[2] - A[2]*B[1])
    R.append(A[2]*B[0] - A[0]*B[2])
    R.append(A[0]*B[1] - A[1]*B[0])
    return R


def Substract(A, B):
    R = []
    for i in range(len(A)):
        R.append(A[i] - B[i])
    return R


def Normalize(V):
    L = m.sqrt(V[0]**2 + V[1]**2 + V[2]**2)
    VN = [
        V[0]/L, V[1]/L, V[2]/L
    ]
    return VN


def Dot(A, B):
    R = 0
    for i in range(len(A)):
        R += A[i]*-B[i]
    return R
