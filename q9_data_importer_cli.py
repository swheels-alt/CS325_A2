#!/usr/bin/env python3
# Import required modules
import argparse
import json
import csv
import sys
from typing import List, Dict, Any

def read_json_file(file_path: str) -> List[Dict[str, Any]]:
    """
    Read and parse a JSON file containing a list of dictionaries.
    
    Args:
        file_path: Path to the JSON file
    
    Returns:
        List[Dict[str, Any]]: List of dictionaries from the JSON file
    
    Raises:
        FileNotFoundError: If the file doesn't exist
        json.JSONDecodeError: If the file contains invalid JSON
    """
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: '{file_path}' contains invalid JSON")
        sys.exit(1)

def read_csv_file(file_path: str) -> List[Dict[str, Any]]:
    """
    Read and parse a CSV file into a list of dictionaries.
    Each row becomes a dictionary with column headers as keys.
    
    Args:
        file_path: Path to the CSV file
    
    Returns:
        List[Dict[str, Any]]: List of dictionaries from the CSV file
    
    Raises:
        FileNotFoundError: If the file doesn't exist
    """
    try:
        with open(file_path, 'r') as f:
            # Use DictReader to automatically create dictionaries from CSV rows
            return list(csv.DictReader(f))
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found")
        sys.exit(1)

def process_data(data: List[Dict[str, Any]], output_format: str) -> None:
    """
    Process the data and output it in the specified format.
    
    Args:
        data: List of dictionaries containing the data
        output_format: Format to output the data ('json' or 'csv')
    """
    if output_format == 'json':
        # Output as JSON with pretty printing
        print(json.dumps(data, indent=2))
    else:  # csv
        if not data:
            print("No data to output")
            return
        
        # Get fieldnames from the first dictionary
        fieldnames = data[0].keys()
        
        # Create CSV writer for stdout
        writer = csv.DictWriter(sys.stdout, fieldnames=fieldnames)
        
        # Write header and data
        writer.writeheader()
        writer.writerows(data)

def main():
    """
    Main function that sets up the command-line interface and processes data files.
    Uses argparse to handle command-line arguments and processes files based on their type.
    """
    # Create the argument parser with a description
    parser = argparse.ArgumentParser(description='Data importer for JSON and CSV files')
    
    # Add required arguments:
    # file: Path to the input file
    # format: Output format (json or csv)
    parser.add_argument('file', help='Input file path (JSON or CSV)')
    parser.add_argument('--format', choices=['json', 'csv'], default='json',
                       help='Output format (default: json)')
    
    # Parse the command-line arguments
    args = parser.parse_args()
    
    # Determine file type from extension
    if args.file.endswith('.json'):
        data = read_json_file(args.file)
    elif args.file.endswith('.csv'):
        data = read_csv_file(args.file)
    else:
        print("Error: Unsupported file format. Use .json or .csv files")
        sys.exit(1)
    
    # Process and output the data
    process_data(data, args.format)

if __name__ == '__main__':
    main()

# Example usage:
# python q9_data_importer_cli.py data.json
# [Outputs JSON data in pretty-printed format]
#
# python q9_data_importer_cli.py data.csv --format csv
# [Outputs CSV data with headers]
#
# Example JSON file (data.json):
# [
#   {"name": "John", "age": 30},
#   {"name": "Jane", "age": 25}
# ]
#
# Example CSV file (data.csv):
# name,age
# John,30
# Jane,25 