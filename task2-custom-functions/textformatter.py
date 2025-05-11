def add(*args):
    if not all(isinstance(arg, (int, float)) for arg in args):
        raise ValueError("All arguments must be numbers (int or float).")
    return sum(args)
def multiply(*args):
    if not all(isinstance(arg, (int, float)) for arg in args):
        raise ValueError("All arguments must be numbers (int or float).")
    
    result = 1
    for num in args:
        result *= num
    return result


def subtract(*args):
    if not all(isinstance(arg, (int, float)) for arg in args):
        raise ValueError("All arguments must be numbers (int or float).")
    
    result = args[0]
    for num in args[1:]:
        result -= num
    return result


def divide(*args):
    if not all(isinstance(arg, (int, float)) for arg in args):
        raise ValueError("All arguments must be numbers (int or float).")
    if len(args) < 2:
        raise ValueError("At least two numbers are required for division.")
    
    result = args[0]
    for num in args[1:]:
        if num == 0:
            raise ValueError("Division by zero is not allowed.")
        result /= num
    return result


def calculate(*args, **kwargs):
    if not args:
        raise ValueError("At least one number is required for calculation.")
    
    if not any(kwargs.values()):
        raise ValueError("At least one operation must be provided as a keyword argument (e.g., add=True, multiply=True).")
    
    result = args[0]
    
    
    for operation, is_enabled in kwargs.items():
        if is_enabled:
            if operation == "add":
                result = add(result, *args[1:])
            elif operation == "subtract":
                result = subtract(result, *args[1:])
            elif operation == "multiply":
                result = multiply(result, *args[1:])
            elif operation == "divide":
                result = divide(result, *args[1:])
            else:
                raise ValueError(f"Unsupported operation: '{operation}'")
    
    return result


if __name__ == "__main__":
    
    try:
        print("Addition and Multiplication:", calculate(2, 3, 4, add=True, multiply=True))
        print("Subtraction and Division:", calculate(100, 20, 5, subtract=True, divide=True))
        print("Only Addition:", calculate(10, 20, 30, add=True))
       
    except Exception as e:
        print(f"Error: {e}")