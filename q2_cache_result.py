import functools
import logging
import time
from typing import Any, Callable, Dict, Hashable, TypeVar, cast

# Configure logging
# This sets up the Python logging system with the following parameters:
# - level=logging.INFO: Only messages of level INFO and above will be shown
#   (DEBUG < INFO < WARNING < ERROR < CRITICAL)
# - format: Specifies how each log message should be formatted:
#   %(asctime)s: Timestamp of when the log was created
#   %(levelname)s: The logging level (INFO, WARNING, etc.)
#   %(message)s: The actual log message
# This configuration will be used by all logging calls in the program
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def time_it(func: Callable) -> Callable:
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        logging.info(f"Function {func.__name__} took {end_time - start_time:.2f} seconds to execute")
        return result
    return wrapper

def log_function(func: Callable) -> Callable:
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        logging.info(f"Calling function: {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"Function {func.__name__} completed")
        return result
    return wrapper

# Type variable for the decorated function
F = TypeVar('F', bound=Callable[..., Any])

def cache_result(func: F) -> F:
    """
    Decorator that caches function results based on input arguments.
    
    Args:
        func: The function to be decorated
        
    Returns:
        The decorated function that caches results
    """
    # Dictionary to store cached results
    cache: Dict[Hashable, Any] = {}
    
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        # Create a cache key from function arguments
        key = (func.__name__, args, tuple(sorted(kwargs.items())))
        
        # Return cached result if available
        if key in cache:
            return cache[key]
            
        # Compute and cache new result
        result = func(*args, **kwargs)
        cache[key] = result
        return result
        
    return cast(F, wrapper)

# Example 1: Fibonacci function with caching
@log_function
@time_it
@cache_result
def fibonacci(n: int) -> int:
    """
    Calculate the nth Fibonacci number.
    
    Args:
        n: The position in the Fibonacci sequence
        
    Returns:
        The nth Fibonacci number
    """
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Example 2: Power function with caching
@log_function
@time_it
@cache_result
def power(base, exponent):
    """
    Calculate base raised to the power of exponent.
    Simple example to show caching with multiple arguments.
    """
    return base ** exponent

# Test the implementation
if __name__ == "__main__":
    # Test Fibonacci with caching
    print("\nTesting Fibonacci:")
    print(f"fibonacci(5) = {fibonacci(5)}")  # First call: computes all values
    print(f"fibonacci(5) = {fibonacci(5)}")  # Second call: uses cache
    
    # Test Power with caching
    print("\nTesting Power:")
    print(f"power(2, 3) = {power(2, 3)}")    # First call: computes result
    print(f"power(2, 3) = {power(2, 3)}")    # Second call: uses cache
    print(f"power(3, 2) = {power(3, 2)}")    # Different arguments: computes new result
