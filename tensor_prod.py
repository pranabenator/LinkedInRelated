import numpy as np

def parse_ket(ket_str):
    """
    Parse a single qubit state in ket notation into its vector representation.
    |0> -> [1, 0], |1> -> [0, 1].
    
    Parameters:
        ket_str (str): Input string denoting the ket state (e.g., "|0>" or "|1>"). 

    Returns:
        numpy.ndarray: Vector representing the state [1, 0] or [0, 1].
    """
    ket_map = {'|0>': np.array([1, 0]), '|1>': np.array([0, 1])}
    if ket_str not in ket_map:
        raise ValueError(f"Invalid ket input '{ket_str}'. Allowed values are '|0>' and '|1>'.")
    return ket_map[ket_str]

def tensor_product(*kets):
    """
    Compute the tensor product of multiple qubit states.

    Parameters:
        kets (str): Variable number of states in ket notation (e.g., "|0>", "|1>", etc.).

    Returns:
        numpy.ndarray: Vector representing the full tensor product of the input qubit states.
    """
    state_vectors = [parse_ket(ket) for ket in kets]
    result = state_vectors[0]
    for vector in state_vectors[1:]:
        result = np.kron(result, vector)
    return result

def tensor_product_step_by_step(*kets):
    """
    Compute the tensor product step by step, logging intermediate results.

    Parameters:
        kets (str): Variable number of states in ket notation.

    Returns:
        tuple: 
            - List of intermediate states during tensor product computation.
            - Final tensor product result as a NumPy array.
    """
    state_vectors = [parse_ket(ket) for ket in kets]
    intermediate_results = []
    result = state_vectors[0]

    intermediate_results.append(result)
    for vector in state_vectors[1:]:
        result = np.kron(result, vector)
        intermediate_results.append(result)
    return intermediate_results, result

def convert_vector_to_ket(tensor_vector):
    """
    Convert a tensor product vector to its corresponding quantum state in ket notation.

    Parameters:
        tensor_vector (numpy.ndarray): Vector in NumPy array format.

    Returns:
        str: Ket notation representing the vector.
    """
    n_qubits = int(np.log2(len(tensor_vector)))

    ket_terms = []
    for idx, amplitude in enumerate(tensor_vector):
        if not np.isclose(amplitude, 0):  # Ignore zero amplitudes
            binary_state = f"{idx:0{n_qubits}b}"  # Convert index to binary string
            ket_terms.append(f"|{binary_state}>")
    return " + ".join(ket_terms)

def pretty_print_steps(intermediate_results):
    """
    Pretty-print intermediate results of a tensor product computation.

    Parameters:
        intermediate_results (list): List of intermediate tensor product vectors.

    Returns:
        str: A nicely formatted string showing each step.
    """
    formatted_steps = []
    for i, step in enumerate(intermediate_results, start=1):
        formatted_steps.append(f"Step {i}: {np.array2string(step, separator=', ')}")
    return "\n".join(formatted_steps)

# CLI Usage Example
if __name__ == "__main__":
    try:
        # Input: Get qubits in ket notation
        qubits = []
        print("Enter qubits in ket notation (e.g., |0>, |1>). Type 'done' to finish:")
        while True:
            inp = input("Enter qubit: ").strip()
            if inp.lower() == "done":
                break
            if inp not in ["|0>", "|1>"]:
                print("Invalid input! Please enter '|0>' or '|1>' or type 'done'.")
                continue
            qubits.append(inp)

        # Step-by-step computation
        intermediate_steps, result_vector = tensor_product_step_by_step(*qubits)

        # Print results
        print("\nIntermediate Steps:")
        print(pretty_print_steps(intermediate_steps))

        print("\nFinal Tensor Product (Vector Representation):")
        print(result_vector)

        print("\nFinal Result (Ket Representation):")
        print(convert_vector_to_ket(result_vector))

    except Exception as e:
        print(f"Error: {e}")