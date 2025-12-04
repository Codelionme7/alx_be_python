# main.py
from polymorphism_demo import Shape, Rectangle, Circle
import math

def main():
    shapes = [
        Rectangle(10, 5),
        Circle(7)
    ]

    for shape in shapes:
        # This is Polymorphism in action:
        # We call .area() on generic 'shape', but the specific
        # class (Rectangle or Circle) handles the logic.
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")

if __name__ == "__main__":
    main()