import numpy as np
from tensor_prod import tensor_product_step_by_step, convert_vector_to_ket
def test_tensor_product():
    """
    Test the tensor product function for 2-qubit and 3-qubit registers.
    Compares the results with expected outputs and prints pass/fail.
    """
    # Test cases
    test_cases = [
        # Format: (input qubits, expected vector result, expected ket result)
        # 2-Qubit Test Cases
        (["|0>", "|0>"], [1, 0, 0, 0], "|00>"),
        (["|0>", "|1>"], [0, 1, 0, 0], "|01>"),
        (["|1>", "|0>"], [0, 0, 1, 0], "|10>"),
        (["|1>", "|1>"], [0, 0, 0, 1], "|11>"),
        
        # 3-Qubit Test Cases
        (["|0>", "|0>", "|0>"], [1, 0, 0, 0, 0, 0, 0, 0], "|000>"),
        (["|0>", "|1>", "|0>"], [0, 0, 1, 0, 0, 0, 0, 0], "|010>"),
        (["|1>", "|0>", "|1>"], [0, 0, 0, 0, 0, 1, 0, 0], "|101>"),
        (["|1>", "|1>", "|1>"], [0, 0, 0, 0, 0, 0, 0, 1], "|111>"),
    ]

    # Results collection
    all_passed = True  # Track overall test status

    for i, (input_qubits, expected_vector, expected_ket) in enumerate(test_cases, start=1):
        print(f"Running Test Case {i}: Input = {input_qubits}")
        try:
            # Step 1: Compute the tensor product's intermediate steps and final result
            intermediate_steps, result_vector = tensor_product_step_by_step(*input_qubits)

            # Step 2: Convert the result vector to ket notation
            result_ket = convert_vector_to_ket(result_vector)

            # Step 3: Compare results with expected values
            vector_match = np.array_equal(result_vector, expected_vector)
            ket_match = result_ket == expected_ket

            # Determine pass/fail
            if vector_match and ket_match:
                print(f"  Test Case {i} PASSED ✅\\n")
            else:
                print(f"  Test Case {i} FAILED ❌")
                print(f"    Expected Vector: {expected_vector}")
                print(f"    Actual Vector:   {result_vector.tolist()}")
                print(f"    Expected Ket:    {expected_ket}")
                print(f"    Actual Ket:      {result_ket}\\n")
                all_passed = False

        except Exception as e:
            print(f"  Test Case {i} FAILED with exception ❌")
            print(f"    Error: {str(e)}\\n")
            all_passed = False

    # Final result summary
    if all_passed:
        print("All test cases PASSED! 🎉")
    else:
        print("Some test cases FAILED. Please review the details above.")

# Execute the test suite
if __name__ == "__main__":
    test_tensor_product()