from flask import jsonify, session

"""
GetFibValue(idx)

Requires : idx is a non-negative integer
Modifies : session
Effects  : retrieves a fibonacci value, or calculates one recursively if not already found
"""
def GetFibValue(idx):

    # Base case: we already know what this fibonacci value is
    if idx < len(session["fibs"]):
        return session["fibs"][idx]

    # Otherwise, recurse!
    session["fibs"].append(GetFibValue(idx-1) + GetFibValue(idx-2))

    return session["fibs"][idx]

"""
GetJson()

Requires : an initialized session
Modifies : none
Effects  : returns the json of the current Fibonacci value
"""
def GetJson():
    return jsonify({
        "index": session["idx"],
        "value": GetFibValue(session["idx"])
    })