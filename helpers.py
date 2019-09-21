fibs = {0: 0, 1: 1}

def GetFibValue(idx):
    if idx in fibs:
        print("Base case, returning: idx {} val {}".format(idx, fibs[idx]))
        return fibs[idx]

    fibs[idx] = GetFibValue(idx-1) + GetFibValue(idx-2)
    print("fibs[{}] = fibs[{}] + fibs[{}]".format(idx, idx-1, idx-2))
    return fibs[idx]