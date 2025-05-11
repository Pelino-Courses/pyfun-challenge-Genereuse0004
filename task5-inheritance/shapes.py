# shapes.py

import math

class Shape:
  

    def __init__(self, name: str):
       
        self.name = name

    def area(self) -> float:
       
        return 0.0

    def __str__(self) -> str:
        
        return f"{self.name} with area: {self.area():.2f}"


class Circle(Shape):
    

    def __init__(self, radius: float):
        
        if radius <= 0:
            raise ValueError("Radius must be positive.")
        super().__init__("Circle")
        self.radius = radius

    def area(self) -> float:
        
        return math.pi * self.radius ** 2

    def __str__(self) -> str:
        return f"{self.name} (radius: {self.radius}) with area: {self.area():.2f}"

    @classmethod
    def from_diameter(cls, diameter: float):
       
        return cls(diameter / 2)


class Rectangle(Shape):
    

    def __init__(self, width: float, height: float):
        
        
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive.")
        super().__init__("Rectangle")
        self.width = width
        self.height = height

    def area(self) -> float:
       
        return self.width * self.height

    def __str__(self) -> str:
        return f"{self.name} (width: {self.width}, height: {self.height}) with area: {self.area():.2f}"


class Triangle(Shape):
    

    def __init__(self, base: float, height: float):
        
        if base <= 0 or height <= 0:
            raise ValueError("Base and height must be positive.")
        super().__init__("Triangle")
        self.base = base
        self.height = height

    def area(self) -> float:
        
        return 0.5 * self.base * self.height

    def __str__(self) -> str:
        return f"{self.name} (base: {self.base}, height: {self.height}) with area: {self.area():.2f}"
# shapes_demo.py

from shapes import Circle, Rectangle, Triangle

def main():
    shapes = [
        Circle(3),
        Circle.from_diameter(10),
        Rectangle(4, 5),
        Triangle(6, 7)
    ]

    for shape in shapes:
        print(shape)

if __name__ == "__main__":
    main()
