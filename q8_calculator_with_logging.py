#!/usr/bin/env python3
# Import required modules
import argparse
import logging
from datetime import datetime

# Configure logging
# Set up logging to write to a file with timestamp in the name
# Format: calculator_YYYY-MM-DD.log
logging.basicConfig(
    filename=f'calculator_{datetime.now().strftime("%Y-%m-%d")}.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def calculate(num1: float, num2: float, operation: str) -> float:
    """
    Perform the requested calculation and log the operation.
    
    Args:
        num1: First number for the calculation
        num2: Second number for the calculation
        operation: The operation to perform (add, subtract, or multiply)
    
    Returns:
        float: The result of the calculation
    
    Raises:
        ValueError: If an invalid operation is provided
    """
    # Log the start of the calculation
    logging.info(f"Starting calculation: {num1} {operation} {num2}")
    
    # Perform the requested operation
    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2
    else:
        # Log error for invalid operation
        error_msg = f"Invalid operation: {operation}"
        logging.error(error_msg)
        raise ValueError(error_msg)
    
    # Log the result
    logging.info(f"Calculation result: {result}")
    return result

def main():
    """
    Main function that sets up the command-line interface and handles user input.
    Uses argparse to parse command-line arguments and logging to record operations.
    """
    # Create the argument parser with a description
    parser = argparse.ArgumentParser(description='Calculator with logging')
    
    # Add required arguments:
    # num1: First number for the calculation
    # num2: Second number for the calculation
    # operation: The operation to perform (add, subtract, or multiply)
    parser.add_argument('num1', type=float, help='First number')
    parser.add_argument('num2', type=float, help='Second number')
    parser.add_argument('operation', choices=['add', 'subtract', 'multiply'],
                       help='Operation to perform (add, subtract, multiply)')
    
    # Parse the command-line arguments
    args = parser.parse_args()
    
    try:
        # Perform the calculation and get the result
        result = calculate(args.num1, args.num2, args.operation)
        # Print the result
        print(f"Result: {result}")
    except ValueError as e:
        # Log and print any errors that occur
        logging.error(str(e))
        print(f"Error: {e}")

if __name__ == '__main__':
    main()

# Example usage:
# python q8_calculator_with_logging.py 5 3 add
# Result: 8.0
# (Logs to calculator_YYYY-MM-DD.log)
#
# python q8_calculator_with_logging.py 10 4 subtract
# Result: 6.0
# (Logs to calculator_YYYY-MM-DD.log)
#
# python q8_calculator_with_logging.py 6 7 multiply
# Result: 42.0
# (Logs to calculator_YYYY-MM-DD.log)
#
# Example log file contents (calculator_YYYY-MM-DD.log):
# 2024-02-14 10:30:15,123 - INFO - Starting calculation: 5 add 3
# 2024-02-14 10:30:15,124 - INFO - Calculation result: 8.0
