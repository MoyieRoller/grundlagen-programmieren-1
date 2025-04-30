class Point2D:

    def __init__(self, p_x: float = 0., p_y: float = 0.):
        self.x = p_x
        self.y = p_y

    def add_point2d(self, p_other):
        self.x = self.x + p_other.x
        self.y = self.y + p_other.y

    def added_point2d(self, p_other):
        point2d = Point2D()
        point2d.x = self.x + p_other.x
        point2d.y = self.y + p_other.y
        return point2d

    def __add__(self, p_other):
        return self.added_point2d(p_other)

if __name__ != "__main__":
    exit(0)

point2d_0 = Point2D(4., 20.)

point2d_1 = Point2D(6., 9.)