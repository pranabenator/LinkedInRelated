import numpy as np

def read_matrix(prompt):
    """
    Read a matrix from user input. 
    Rows are separated by `,,` and columns are separated by `,`.
    Supports both real and complex numbers.
    Example: "1,2+3j,4,,5,6,7" -> [[1, (2+3j), 4], [5, 6, 7]]
    """
    while True:
        try:
            user_input = input(prompt)
            # Parse input into rows and columns
            rows = user_input.split(",,")
            matrix = [list(map(eval, row.split(","))) for row in rows]  # Use eval for numbers and complex numbers
            return np.array(matrix)
        except Exception as e:
            print(f"Invalid input! Please try again. ({e})")

def is_hermitian(matrix):
    """
    Check whether a matrix is Hermitian.

    A matrix is Hermitian if it equals its own conjugate transpose:
    M == M.conjugate().T

    This works for both real matrices (checks symmetry)
    and complex matrices.
    """
    try:
        # Compute conjugate transpose
        conjugate_transpose = np.conjugate(matrix.T)
        # Check if matrix equals its conjugate transpose
        return np.array_equal(matrix, conjugate_transpose)
    except Exception as e:
        print(f"Error while checking Hermitian property: {e}")
        return False

def process_matrices():
    """
    Main logical flow for reading matrices, performing operations, and showing results to the user.
    """
    print("Enter two matrices. Use `,,` to separate rows and `,` to separate columns.")
    matrix_A = read_matrix("Matrix A: ")
    matrix_B = read_matrix("Matrix B: ")

    # Show matrix dimensions
    print(f"\nMatrix A ({matrix_A.shape[0]}x{matrix_A.shape[1]}):")
    print(matrix_A)

    print(f"\nMatrix B ({matrix_B.shape[0]}x{matrix_B.shape[1]}):")
    print(matrix_B)

    print("\nPerforming all operations:")

    # Summation
    try:
        print("\nSummation (A + B):")
        print(matrix_A + matrix_B)
    except ValueError as e:
        print("\nSummation not possible: Matrices must have the same dimensions.", e)

    # Multiplication
    try:
        print("\nMultiplication (A x B):")
        print(matrix_A @ matrix_B)
    except ValueError as e:
        print("\nMultiplication not possible: Number of columns in A must match the number of rows in B.", e)

    # Dot (Inner) Product
    try:
        print("\nDot (Inner) Product (A · B):")
        print(np.dot(matrix_A, matrix_B))
    except ValueError as e:
        print("\nDot product not possible: Both inputs must be 1D vectors of the same length.", e)

    # Hermitian Check
    print("\nHermitian Matrix Checks:")
    try:
        if is_hermitian(matrix_A):
            print("Matrix A is Hermitian.")
        else:
            print("Matrix A is NOT Hermitian.")
    except Exception as e:
        print(f"Error while checking if Matrix A is Hermitian: {e}")

    try:
        if is_hermitian(matrix_B):
            print("Matrix B is Hermitian.")
        else:
            print("Matrix B is NOT Hermitian.")
    except Exception as e:
        print(f"Error while checking if Matrix B is Hermitian: {e}")

if __name__ == "__main__":
    print("Welcome to the Matrix Operations Program!")
    process_matrices()
