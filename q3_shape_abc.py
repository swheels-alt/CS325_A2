from abc import ABC, abstractmethod
import math

class Shape(ABC):
    """
    Abstract Base Class for shapes.
    This class defines the interface that all shapes must implement.
    It cannot be instantiated directly - you must create a concrete shape class.
    """
    
    @abstractmethod
    def area(self):
        """
        Calculate the area of the shape.
        This is an abstract method that must be implemented by all concrete shape classes.
        """
        pass
    
    @abstractmethod
    def perimeter(self):
        """
        Calculate the perimeter of the shape.
        This is an abstract method that must be implemented by all concrete shape classes.
        """
        pass

class Circle(Shape):
    """
    Concrete implementation of Shape for circles.
    Implements the required area() and perimeter() methods.
    """
    
    def __init__(self, radius):
        """
        Initialize a circle with a given radius.
        
        Args:
            radius: The radius of the circle
        """
        if radius <= 0:
            raise ValueError("Radius must be positive")
        self.radius = radius
    
    def area(self):
        """
        Calculate the area of the circle using the formula: πr²
        """
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        """
        Calculate the perimeter (circumference) of the circle using the formula: 2πr
        """
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    """
    Concrete implementation of Shape for rectangles.
    Implements the required area() and perimeter() methods.
    """
    
    def __init__(self, width, height):
        """
        Initialize a rectangle with given width and height.
        
        Args:
            width: The width of the rectangle
            height: The height of the rectangle
        """
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive")
        self.width = width
        self.height = height
    
    def area(self):
        """
        Calculate the area of the rectangle using the formula: width × height
        """
        return self.width * self.height
    
    def perimeter(self):
        """
        Calculate the perimeter of the rectangle using the formula: 2(width + height)
        """
        return 2 * (self.width + self.height)

# Test the implementation
if __name__ == "__main__":
    # Test Circle
    circle = Circle(5)
    print(f"Circle area: {circle.area():.2f}")
    print(f"Circle perimeter: {circle.perimeter():.2f}")
    
    # Test Rectangle
    rectangle = Rectangle(4, 6)
    print(f"\nRectangle area: {rectangle.area()}")
    print(f"Rectangle perimeter: {rectangle.perimeter()}")
    
    # Try to instantiate Shape (should raise error)
    try:
        shape = Shape()  # This will fail because Shape is abstract
    except TypeError as e:
        print(f"\nAttempting to instantiate Shape raises: {e}")
    
    # Example output:
    # Circle area: 78.54
    # Circle perimeter: 31.42
    #
    # Rectangle area: 24
    # Rectangle perimeter: 20
    #
    # Attempting to instantiate Shape raises: Can't instantiate abstract class Shape with abstract methods area, perimeter
