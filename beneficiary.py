beneficiaries = {}

# Function to add a beneficiary
def add_beneficiary(id, name):
    if id in beneficiaries:
        return "Already exists"
    beneficiaries[id] = name
    return "Beneficiary added"
