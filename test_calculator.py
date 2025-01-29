# Importing NumPy to use the matrix functions from the calculator
import numpy as np

# Import the functions from the matrix calculator program
from matrix_calculator import read_matrix, is_hermitian

def test_calculator():
    """
    Test all features of the matrix calculator:
    - Summation of matrices
    - Multiplication of matrices
    - Dot products
    - Checking if matrices are Hermitian
    """

    print("\n=== TESTING MATRIX CALCULATOR ===\n")

    # Test 1: Real Matrices (Addition, Multiplication, Hermitian Check)
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])

    print("\nTest 1: Real Matrices")
    print("Matrix A:\n", A)
    print("Matrix B:\n", B)

    # Addition
    try:
        print("\nA + B:\n", A + B)
    except ValueError as e:
        print("Addition failed:", e)

    # Multiplication
    try:
        print("\nA x B:\n", A @ B)
    except ValueError as e:
        print("Multiplication failed:", e)

    # Hermitian Check for A and B
    print("\nIs Matrix A Hermitian?:", is_hermitian(A))
    print("Is Matrix B Hermitian?:", is_hermitian(B))

    # Test 2: Complex Matrices (Addition, Multiplication, Hermitian Check)
    C = np.array([[1, 2 + 3j], [2 - 3j, 4]])
    D = np.array([[1, 1], [1, 1]])

    print("\nTest 2: Complex Matrices")
    print("Matrix C:\n", C)
    print("Matrix D:\n", D)

    # Addition
    try:
        print("\nC + D:\n", C + D)
    except ValueError as e:
        print("Addition failed:", e)

    # Multiplication
    try:
        print("\nC x D:\n", C @ D)
    except ValueError as e:
        print("Multiplication failed:", e)

    # Hermitian Check for C and D
    print("\nIs Matrix C Hermitian?:", is_hermitian(C))
    print("Is Matrix D Hermitian?:", is_hermitian(D))

    # Test 3: Incompatible Dimensions for Multiplication
    E = np.array([[1, 2, 3], [4, 5, 6]])
    F = np.array([[1, 2], [3, 4]])

    print("\nTest 3: Incompatible Dimensions")
    print("Matrix E:\n", E)
    print("Matrix F:\n", F)

    # Attempt Multiplication
    try:
        print("\nE x F:\n", E @ F)
    except ValueError as e:
        print("Multiplication failed:", e)

    # Attempt Addition (Should fail due to shape mismatch)
    try:
        print("\nE + F:\n", E + F)
    except ValueError as e:
        print("Addition failed:", e)

    # Test 4: 1D Vectors for Dot Product
    G = np.array([1, 2, 3])
    H = np.array([4, 5, 6])

    print("\nTest 4: 1D Vectors")
    print("Vector G:", G)
    print("Vector H:", H)

    # Dot Product
    try:
        print("\nDot Product (G · H):", np.dot(G, H))
    except ValueError as e:
        print("Dot product failed:", e)

    # Test 5: 1D Vector and Matrix Combination (Should fail for dot/mult)
    try:
        print("\nG + A:\n", G + A)
    except ValueError as e:
        print("Addition of 1D vector and 2D matrix failed:", e)

    # Confirm Hermitian property for a symmetric real matrix:
    I = np.array([[2, 1], [1, 2]])
    print("\nTest 5: Symmetric Real Matrix")
    print("Matrix I:\n", I)
    print("\nIs Matrix I Hermitian?:", is_hermitian(I))

    print("\n=== TESTING COMPLETE ===")

# Run the test program
if __name__ == "__main__":
    test_calculator()