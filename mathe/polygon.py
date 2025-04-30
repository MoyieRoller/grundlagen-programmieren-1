class Polygon:

    def __init__(self, numPoints: int):
        self.numPoints = numPoints

    def innerAngleSum(self):
        return (self.numPoints - 2) * 180

if __name__ == "__main__":
    poly1 = Polygon(numPoints=15)

    print(poly1)
    print(poly1.numPoints)