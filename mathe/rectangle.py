from polygon import Polygon

class Rectangle(Polygon):

    def __init__(self, width: float, height: float):
        super().__init__(numPoints=4)
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

if __name__ == "__main__":
    rectangle1 = Rectangle(width=2, height=5)
    print(rectangle1.area())
    print(rectangle1.innerAngleSum())