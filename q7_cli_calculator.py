#!/usr/bin/env python3
# Import argparse for command-line argument parsing
import argparse

def main():
    """
    Main function that sets up and runs the command-line calculator.
    Uses argparse to handle command-line arguments and perform calculations.
    """
    # Create the argument parser with a description
    parser = argparse.ArgumentParser(description='Simple command-line calculator')
    
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
    
    # Perform the requested operation
    if args.operation == 'add':
        result = args.num1 + args.num2
    elif args.operation == 'subtract':
        result = args.num1 - args.num2
    else:  # multiply
        result = args.num1 * args.num2
    
    # Print the result
    print(f"Result: {result}")

if __name__ == '__main__':
    main()

# Example usage:
# python q7_cli_calculator.py 5 3 add
# Result: 8.0
#
# python q7_cli_calculator.py 10 4 subtract
# Result: 6.0
#
# python q7_cli_calculator.py 6 7 multiply
# Result: 42.0
#
# To see help message:
# python q7_cli_calculator.py --help
# usage: q7_cli_calculator.py [-h] num1 num2 {add,subtract,multiply}
#
# Simple command-line calculator
#
# positional arguments:
#   num1                  First number
#   num2                  Second number
#   operation            Operation to perform (add, subtract, multiply)
#
# optional arguments:
#   -h, --help           show this help message and exit 