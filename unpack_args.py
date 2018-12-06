def f(val1=3, val2=4, val3=6):
    return val1 + val2 + val3

values = {"val1" : 9, "val3" : -1}

print(f(**values))