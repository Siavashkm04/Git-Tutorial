def multiplier(a, b):
    return a * b

def addition(a, b):
    return a + b

def divider(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b