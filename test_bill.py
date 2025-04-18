from sepp03.bill import get_bill

def test_get_bill_valid():
    assert get_bill("P001") == {"name": "Alice", "amount": 700}

def test_get_bill_invalid():
    assert get_bill("XYZ") == {}

print("test passed")