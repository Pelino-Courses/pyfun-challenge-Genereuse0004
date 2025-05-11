def calculate(operation: str, *args, **kwargs):
   
    
    # Ensure there are at least two numbers for most operations
    if len(args) < 2:
        raise ValueError("At least two numbers are required for calculation.")
    
    # Extract precision from kwargs, if provided
    precision = kwargs.get('precision', None)
    
    # Process based on the operation type
    if operation == 'add':
        result = sum(args)
    elif operation == 'subtract':
        result = args[0]
        for num in args[1:]:
            result -= num
    elif operation == 'multiply':
        result = 1
        for num in args:
            result *= num
    elif operation == 'divide':
        result = args[0]
        for num in args[1:]:
            if num == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            result /= num
    else:
        raise ValueError("Invalid operation. Valid options are 'add', 'subtract', 'multiply', 'divide'.")
    
    # Round result to the specified precision, if provided
    if precision is not None:
        try:
            result = round(result, precision)
        except TypeError:
            raise ValueError("Precision must be an integer.")
    
    return result


def add(*args, **kwargs):
    
    return calculate('add', *args, **kwargs)


def subtract(*args, **kwargs):
    
    return calculate('subtract', *args, **kwargs)


def multiply(*args, **kwargs):
    
    return calculate('multiply', *args, **kwargs)


def divide(*args, **kwargs):
    
    return calculate('divide', *args, **kwargs)


# Example usage and demonstration

if __name__ == "__main__":
    try:
        print("Addition Result:", add(1, 2, 3, 4, precision=2))  # Example with precision
        print("Subtraction Result:", subtract(10, 2, 3))
        print("Multiplication Result:", multiply(2, 3, 4))
        print("Division Result:", divide(10, 2))
        
        
        print("Division by Zero Result:", divide(10, 0))

    except Exception as e:
        print(f"Error: {e}")
