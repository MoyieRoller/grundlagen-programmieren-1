from polygon import Polygon

class Triangle(Polygon):

    def __init__(self, base: float, height: float):
        super().__init__(numPoints=3)
        self.base = base
        self.height = height
    
    def area(self) -> float:
        return 0.5 * self.base * self.height

if __name__ == "__main__":
    triangle1 = Triangle(base=3, height=10)
    print(triangle1.area())
    print(triangle1.innerAngleSum())