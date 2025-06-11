import functools
import logging
import time
from typing import Any, Callable

# Configure logging
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

def cache_result(verbose=False):
    """
    A decorator that caches function results based on their arguments.
    If the same arguments are used again, returns the cached result instead of recomputing.
    
    Args:
        verbose (bool): If True, prints messages about cache hits and misses
    
    Returns:
        decorator: A function that wraps the original function with caching
    """
    def decorator(func):
        # Dictionary to store cached results
        # Keys are function arguments, values are function results
        cache = {}
        
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Create a key from the function arguments
            # This allows us to cache results for different argument combinations
            key = str(args) + str(kwargs)
            
            # Check if we have a cached result for these arguments
            if key in cache:
                if verbose:
                    print(f"Cache hit for {func.__name__} with args: {args}, kwargs: {kwargs}")
                return cache[key]
            
            # If no cached result, compute it
            if verbose:
                print(f"Cache miss for {func.__name__} with args: {args}, kwargs: {kwargs}")
            result = func(*args, **kwargs)
            
            # Store the result in cache
            cache[key] = result
            return result
        
        return wrapper
    return decorator

# Example 1: Fibonacci function with caching
@log_function
@time_it
@cache_result(verbose=True)
def fibonacci(n):
    """
    Calculate the nth Fibonacci number.
    Without caching, this would be very inefficient for large n.
    With caching, each value is computed only once.
    """
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Example 2: Power function with caching
@log_function
@time_it
@cache_result(verbose=True)
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
