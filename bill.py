
def get_bill(pid):
    if pid == "P001":
        return {"name": "Alice", "amount": 700}
    return {}

if __name__ == "__main__":
    print(get_bill("P001"))
