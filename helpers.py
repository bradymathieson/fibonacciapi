from flask import session

"""
GetBaseCases()

Requires : none
Modifies : none
Effects  : returns the default base cases for the Fibonacci recursion
"""
def GetBaseCases():
    return [0, 1]

"""
GetFibValue(idx)

Requires : idx is a non-negative integer
Modifies : session
Effects  : retrieves a fibonacci value, or calculates one recursively if not already found
"""
def GetFibValue(idx):

    if "fibs" not in session:
        session["fibs"] = GetBaseCases()

    # Base case: we already know what this fibonacci value is
    if idx < len(session["fibs"]):
        return session["fibs"][idx]

    # Otherwise, recurse!
    session["fibs"].append(GetFibValue(idx-1) + GetFibValue(idx-2))

    if idx >= len(session["fibs"]):
        pass

    return session["fibs"][idx]