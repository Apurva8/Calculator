def addition(a: int, b: int) -> int:
    return a + b

def subtraction(a: int, b: int) -> int:
    return a - b

def multiplication(a: int, b: int) -> int:
    return a * b

def division(a: int, b: int) -> float:
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b
