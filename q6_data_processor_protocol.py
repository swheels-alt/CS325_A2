# Import Protocol from typing module
# Protocol is used for structural typing (duck typing with type hints)
from typing import Protocol

class DataProcessor(Protocol):
    """
    A Protocol that defines the interface for data processors.
    Any class that has a process() method taking a list of integers and returning a list of integers
    conforms to this protocol, even without explicitly inheriting from it.
    """
    def process(self, data: list[int]) -> list[int]:
        """
        Process a list of integers and return a new processed list.
        This is the only method required to conform to the DataProcessor protocol.
        
        Args:
            data: List of integers to process
            
        Returns:
            Processed list of integers
        """
        pass

class EvenFilter:
    """
    A class that filters a list to keep only even numbers.
    This class conforms to the DataProcessor protocol by implementing process(),
    but doesn't explicitly inherit from DataProcessor.
    """
    
    def process(self, data: list[int]) -> list[int]:
        """
        Filter the input list to keep only even numbers.
        
        Args:
            data: List of integers to filter
            
        Returns:
            List containing only the even numbers from the input
        """
        return [x for x in data if x % 2 == 0]

class SquareProcessor:
    """
    A class that squares each number in a list.
    This class also conforms to the DataProcessor protocol by implementing process(),
    without explicitly inheriting from DataProcessor.
    """
    
    def process(self, data: list[int]) -> list[int]:
        """
        Square each number in the input list.
        
        Args:
            data: List of integers to square
            
        Returns:
            List containing the squares of the input numbers
        """
        return [x * x for x in data]

def apply_processor(processor: DataProcessor, input_data: list[int]) -> list[int]:
    """
    Apply a data processor to the input data.
    This function demonstrates how to use the protocol for type hints.
    
    Args:
        processor: Any object that has a process() method
        input_data: List of integers to process
        
    Returns:
        Processed list of integers
    """
    return processor.process(input_data)

# Test the implementation
if __name__ == "__main__":
    # Test data
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Test EvenFilter
    even_filter = EvenFilter()
    even_numbers = apply_processor(even_filter, numbers)
    print("Even numbers:", even_numbers)
    
    # Test SquareProcessor
    square_processor = SquareProcessor()
    squared_numbers = apply_processor(square_processor, numbers)
    print("Squared numbers:", squared_numbers)
    
    # Example output:
    # Even numbers: [2, 4, 6, 8, 10]
    # Squared numbers: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
