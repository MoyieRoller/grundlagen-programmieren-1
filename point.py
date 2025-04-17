class Point:
    def __init__(self, x: float, y: float):

        if (not isinstance(x, float)) or (not isinstance(y, float)):
            print(f'Deine Argumente, x: {type(x)} und/oder x: {type(y)} sind nicht floats.')
        else:
            self.x = x
            self.y = y

if __name__ == "__main__":
    p1 = Point(3.0, 5.0)
    print(f'x: {p1.x}, y: {p1.y}')