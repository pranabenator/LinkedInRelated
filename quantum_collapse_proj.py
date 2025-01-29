import re
from sympy import Matrix, sqrt, conjugate, I, Abs, N, eye, ZeroMatrix

def parse_superposition_state(state_str):
    """
    Parses superposition state inputs such as '1|0> + 2j|1>' into a vector representation.
    """
    vec = {0: 0+0j, 1: 0+0j}  # Dictionary to hold complex values for a 1-qubit system
    # Regular expression to find all matches of the form (Coef|Base>)
    matches = re.finditer(r'([\+\-]?[\d\.]+j?[\+\-]?[\d\.]*j?)\|(\d+)\>', state_str)
    for match in matches:
        coefficient = match.group(1)
        basis = int(match.group(2))
        # Append 'j' if needed to form a valid complex number
        if 'j' not in coefficient and any(char.isdigit() for char in coefficient[-1]):
            coefficient += '+0j'
        coefficient = coefficient.replace('+-', '-')
        vec[basis] += complex(coefficient)

    return Matrix([vec[0], vec[1]])

def normalize_vector(vector):
    norm = sqrt(sum(abs(v)**2 for v in vector))
    return vector / norm if norm != 0 else vector

def inner_product(vec1, vec2):
    return (vec1.T.conjugate() * vec2)[0]

def express_in_basis(vec, basis_index=0):
    """
    Expresses the given quantum state in terms of the basis vector corresponding to `basis_index`
    and its orthogonal complement within a 1-qubit system.
    """
    # Construct the standard basis for a 1-qubit system
    standard_basis = Matrix([[1, 0], [0, 1]])

    # Define the new basis using the specified basis vector and calculate the orthogonal vector
    new_basis = Matrix(2, 1, lambda i, j: standard_basis[i, basis_index])
    orthogonal_basis = Matrix(2, 1, lambda i, j: 0)
    orthogonal_basis[0, 0] = -new_basis[1, 0]
    orthogonal_basis[1, 0] = new_basis[0, 0]

    # Normalize the new basis vectors
    new_basis = normalize_vector(new_basis)
    orthogonal_basis = normalize_vector(orthogonal_basis)

    # Project the vector onto the new basis
    proj_b1 = (inner_product(new_basis, vec) / inner_product(new_basis, new_basis)) * new_basis
    proj_b2 = (inner_product(orthogonal_basis, vec) / inner_product(orthogonal_basis, orthogonal_basis)) * orthogonal_basis

    # Sum the projections to express vec in the new basis
    expressed_vec = proj_b1 + proj_b2

    print("\nExpressed in new basis:")
    print(f"Basis vector |{basis_index}>: {new_basis}")
    print(f"Orthogonal to |{basis_index}>: {orthogonal_basis}")
    print("Decomposed vector:")
    print(expressed_vec)

    return expressed_vec    

def main():
    print("Enter two superposition states for a 1-qubit system:")
    state1 = input("First state (e.g., '1|0> + 2j|1>'): ")
    state2 = input("Second state (e.g., '3|0> - 1j|1>'): ")

    try:
        vec1 = parse_superposition_state(state1)
        vec2 = parse_superposition_state(state2)
        
        normalized_vec1 = normalize_vector(vec1)
        normalized_vec2 = normalize_vector(vec2)
        
        ip = inner_product(normalized_vec1, normalized_vec2)
        prob_amplitude = Abs(ip)**2
        
        print(f"\nNormalized Vector 1: {normalized_vec1}")
        print(f"Normalized Vector 2: {normalized_vec2}")
        print(f"Inner Product: {ip}")
        print(f"Probability Amplitude: {prob_amplitude}")

        # Additional functionality to express the register in a basis
        express_in_basis(normalized_vec2, basis_index=0)
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()