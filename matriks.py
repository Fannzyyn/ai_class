import numpy as np

ROW_A, COL_A = 2, 3
ROW_B, COL_B = 3, 4


A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])


B = np.array([
    [7, 8, 9, 10],
    [11, 12, 13, 14],
    [15, 16, 17, 18]
])


if A.shape[1] != B.shape[0]:
    raise ValueError("Matriks A dan B tidak memiliki dimensi yang cocok untuk perkalian.")


C = np.dot(A, B)


print("Matriks A:")
print(A)

print("\nMatriks B:")
print(B)

print("\nHasil A * B:")
print(C)


A = [
    [1, 2, 3],
    [4, 5, 6]
]

B = [
    [7, 8, 9, 10],
    [11, 12, 13, 14],
    [15, 16, 17, 18]
]

if len(A[0]) != len(B):
    raise ValueError("Matriks A dan B tidak memiliki dimensi yang cocok untuk perkalian.")

C = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            C[i][j] += A[i][k] * B[k][j]

print("\nMatriks A:")
for row in A:
    print(row)

print("\nMatriks B:")
for row in B:
    print(row)

print("\nHasil A * B:")
for row in C:
    print(row)
