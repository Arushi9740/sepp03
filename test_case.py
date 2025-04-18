from sepp03.beneficiary import add_beneficiary, beneficiaries

def test_add_beneficiary():
    # Reset the beneficiaries dictionary before each test
    beneficiaries = {}

    # Test case 1: Add a new beneficiary
    result = add_beneficiary("B001", "Alice")
    assert result == "Beneficiary added", f"Expected 'Beneficiary added', but got {result}"
    assert beneficiaries == {"B001": "Alice"}, f"Expected {{'B001': 'Alice'}}, but got {beneficiaries}"

    # Test case 2: Try adding an existing beneficiary
    result = add_beneficiary("B001", "Alice")
    assert result == "Already exists", f"Expected 'Already exists', but got {result}"
    assert beneficiaries == {"B001": "Alice"}, f"Expected {{'B001': 'Alice'}}, but got {beneficiaries}"

    print("All test cases passed!")

# Run the test case function
test_add_beneficiary()
