def add(a, b):
    """Addition"""
    return a + b

def sub(a, b):
    """Subtraction"""
    return a - b

def mul(a, b):
    """Multiplication"""
    return a * b

def div(a, b):
    """Division with zero check"""
    if b == 0:
        return "Cannot divide by zero"
    return a / b

def sq(x):
    """Square"""
    return x * x

def cube(x):
    """Cube"""
    return x * x * x

def swap(a, b):
    """Swap two values"""
    return b, a