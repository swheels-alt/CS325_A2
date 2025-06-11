# Import Protocol from typing module
# Protocol is used for structural typing (duck typing with type hints)
from typing import Protocol

class Printable(Protocol):
    """
    A Protocol that defines the interface for printable objects.
    Any class that has a to_string() method conforms to this protocol,
    even without explicitly inheriting from it.
    """
    def to_string(self) -> str:
        """
        Convert the object to a string representation.
        This is the only method required to conform to the Printable protocol.
        """
        pass

class Book:
    """
    A class representing a book.
    This class conforms to the Printable protocol by implementing to_string(),
    but doesn't explicitly inherit from Printable.
    """
    
    def __init__(self, title, author):
        """
        Initialize a book with title and author.
        
        Args:
            title: The title of the book
            author: The author of the book
        """
        self.title = title
        self.author = author
    
    def to_string(self) -> str:
        """
        Convert the book to a string representation.
        This method makes the class conform to the Printable protocol.
        """
        return f"Book: {self.title} by {self.author}"

class Movie:
    """
    A class representing a movie.
    This class also conforms to the Printable protocol by implementing to_string(),
    without explicitly inheriting from Printable.
    """
    
    def __init__(self, title, director):
        """
        Initialize a movie with title and director.
        
        Args:
            title: The title of the movie
            director: The director of the movie
        """
        self.title = title
        self.director = director
    
    def to_string(self) -> str:
        """
        Convert the movie to a string representation.
        This method makes the class conform to the Printable protocol.
        """
        return f"Movie: {self.title} directed by {self.director}"

def print_item(item: Printable) -> None:
    """
    Print any object that conforms to the Printable protocol.
    This function demonstrates how to use the protocol for type hints.
    
    Args:
        item: Any object that has a to_string() method
    """
    print(item.to_string())

# Test the implementation
if __name__ == "__main__":
    # Test Book
    book = Book("The Great Gatsby", "F. Scott Fitzgerald")
    print_item(book)
    
    # Test Movie
    movie = Movie("The Godfather", "Francis Ford Coppola")
    print_item(movie)
    
    # Example output:
    # Book: The Great Gatsby by F. Scott Fitzgerald
    # Movie: The Godfather directed by Francis Ford Coppola
