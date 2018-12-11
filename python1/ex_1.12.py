import random

matrixSize = 128
a = [[random.randint(0,9) for i in range(matrixSize)] for j in range(matrixSize)]
b = [[random.randint(0,9) for i in range(matrixSize)] for j in range(matrixSize)]

matrix3 = [[0 for i in range(matrixSize)] for j in range(matrixSize)]

def add(matrix1,matrix2):
    for i in range(matrixSize):
        for j in range(matrixSize):
            matrix3[i][j]= matrix1[i][j]+matrix2[i][j]

    return matrix3

print a
print b
print (add(a,b))