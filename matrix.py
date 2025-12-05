import numpy as np

# ------------------------------
# 1. Create a random matrix A
# ------------------------------
n = 4   # size of the matrix (4x4)
A = np.random.randint(-10, 10, size=(n, n))
print("Matrix A:")
print(A)

# ------------------------------
# 2. Create another random matrix B
# ------------------------------
B = np.random.randint(-10, 10, size=(n, n))
print("\nMatrix B:")
print(B)

# ------------------------------
# 3. Matrix multiplication C = A * B
# ------------------------------
C = A @ B   # or np.matmul(A, B)
print("\nMatrix C = A @ B:")
print(C)

# ------------------------------
# 4. Transpose of A
# ------------------------------
A_T = A.T
print("\nTranspose of A:")
print(A_T)

# ------------------------------
# 5. Determinant of A
# ------------------------------
detA = np.linalg.det(A)
print("\nDeterminant of A:", detA)

# ------------------------------
# 6. Inverse of A (if possible)
# ------------------------------
if abs(detA) > 1e-8:
    invA = np.linalg.inv(A)
    print("\nInverse of A:")
    print(invA)
else:
    print("\nA is singular, inverse cannot be computed.")

# ------------------------------
# 7. Eigenvalues of A
# ------------------------------
eigenvalues = np.linalg.eigvals(A)
print("\nEigenvalues of A:")
print(eigenvalues)
