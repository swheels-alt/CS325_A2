# Import functools to use the wraps decorator, which preserves the metadata of the original function
import functools

# Define a decorator that logs function calls and their results
def log_function_call(func):
    """
    A decorator that logs:
    1. When a function is called
    2. The arguments passed to the function
    3. The value returned by the function
    
    Args:
        func: The function to be decorated
        
    Returns:
        wrapper: A new function that wraps the original function with logging
    """
    @functools.wraps(func)  # Preserve the original function's metadata (name, docstring, etc.)
    def wrapper(*args, **kwargs):
        # Log the function call with its arguments
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        
        # Call the original function and store its result
        result = func(*args, **kwargs)
        
        # Log the function's return value
        print(f"{func.__name__} returned: {result}")
        
        # Return the original function's result
        return result
    return wrapper

# Example function that uses the decorator
@log_function_call  # This is equivalent to: greet = log_function_call(greet)
def greet(name, greeting="Hello"):
    """
    A simple greeting function that demonstrates the decorator.
    
    Args:
        name: The name to greet
        greeting: The greeting message (defaults to "Hello")
        
    Returns:
        str: The complete greeting message
    """
    print(f"Inside the function Greet: {greeting} {name}!")
    return f"{greeting}, {name}!"

# Test the implementation
if __name__ == "__main__":
    # Test the decorated function
    result = greet("Sam", greeting="Hi")
    print(f"Final result: {result}")
    
    # The output will show:
    # 1. When the function is called (with its arguments)
    # 2. What the function returns
    # 3. The final result
    
    # Example output:
    # Calling greet with args: ('Sam',), kwargs: {'greeting': 'Hi'}
    # greet returned: Hi, Sam!
    # Final result: Hi, Sam!
