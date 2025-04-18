beneficiaries = {}

def add_beneficiary(bid, name):
    if bid not in beneficiaries:
        beneficiaries[bid] = name
        return "Beneficiary added"
    return "Already exists"
