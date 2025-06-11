from abc import ABC, abstractmethod
import json

class DataSource(ABC):
    """
    Abstract Base Class for data sources.
    This class defines the interface that all data sources must implement.
    """
    
    @abstractmethod
    def fetch_data(self):
        """
        Fetch data from the source.
        This is an abstract method that must be implemented by all concrete data source classes.
        Returns:
            The fetched data (format depends on the implementation)
        """
        pass

class FileDataSource(DataSource):
    """
    Concrete implementation of DataSource for reading from JSON files.
    Implements the required fetch_data() method to read and parse JSON data.
    """
    
    def __init__(self, file_path):
        """
        Initialize a file data source with a given file path.
        
        Args:
            file_path: Path to the JSON file to read from
        """
        self.file_path = file_path
    
    def fetch_data(self):
        """
        Read and parse data from the JSON file.
        
        Returns:
            The parsed JSON data (typically a list or dictionary)
        """
        with open(self.file_path, 'r') as file:
            return json.load(file)

class APIDataSource(DataSource):
    """
    Concrete implementation of DataSource for fetching from APIs.
    Implements the required fetch_data() method to simulate API responses.
    """
    
    def __init__(self, endpoint):
        """
        Initialize an API data source with a given endpoint.
        
        Args:
            endpoint: The API endpoint URL to fetch from
        """
        self.endpoint = endpoint
    
    def fetch_data(self):
        """
        Simulate fetching data from an API endpoint.
        
        Returns:
            Simulated API response data
        """
        # Simulate API response
        if "users" in self.endpoint:
            return [
                {"id": 1, "name": "John Doe"},
                {"id": 2, "name": "Jane Smith"}
            ]
        return [{"error": "Unknown endpoint"}]

# Test the implementation
if __name__ == "__main__":
    # Create a sample JSON file for testing
    sample_data = [
        {"id": 1, "name": "Test Item 1"},
        {"id": 2, "name": "Test Item 2"}
    ]
    
    # Write test data to a file
    with open("sample_data.json", "w") as f:
        json.dump(sample_data, f)
    
    # Test FileDataSource
    print("Testing FileDataSource:")
    file_source = FileDataSource("sample_data.json")
    print(file_source.fetch_data())
    
    # Test APIDataSource
    print("\nTesting APIDataSource:")
    api_source = APIDataSource("https://api.example.com/users")
    print(api_source.fetch_data())
    
    # Clean up test file
    import os
    os.remove("sample_data.json")
    
    # Example output:
    # Testing FileDataSource:
    # [{'id': 1, 'name': 'Test Item 1'}, {'id': 2, 'name': 'Test Item 2'}]
    #
    # Testing APIDataSource:
    # [{'id': 1, 'name': 'John Doe'}, {'id': 2, 'name': 'Jane Smith'}] 