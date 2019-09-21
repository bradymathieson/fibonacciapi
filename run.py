from flask import Flask, redirect, request, session, url_for

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

fibs = {0: 0, 1: 1}

def GetFibValue(idx):
    if idx in fibs:
        print("Base case, returning: idx {} val {}".format(idx, fibs[idx]))
        return fibs[idx]

    fibs[idx] = GetFibValue(idx-1) + GetFibValue(idx-2)
    print("fibs[{}] = fibs[{}] + fibs[{}]".format(idx, idx-1, idx-2))
    return fibs[idx]

@app.route("/current")
def current():
    if "curridx" not in session:
        session["curridx"] = 0
    return str(GetFibValue(session["curridx"]))

@app.route("/next")
def next():
    if "curridx" not in session:
        pass
    session["curridx"] += 1
    return str(GetFibValue(session["curridx"]))

@app.route("/previous")
def previous():
    if "curridx" not in session:
        pass
    session["curridx"] -= 1
    return str(GetFibValue(session["curridx"]))

@app.route("/clear")
def clear():
    if "curridx" not in session:
        pass
    session["curridx"] = 0
    return redirect(url_for("current"))

app.run(debug=True)