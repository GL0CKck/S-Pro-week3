from math import sqrt


class Point2D:
    __count_obj = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.__class__.__count_obj += 1

    def distance(self, obj2):
        distance = sqrt(((obj2.x - self.x)**2) + ((obj2.y - self.y)**2))
        return distance

    @property
    def get_count(self):
        return self.__count_obj


class Point3D(Point2D):

    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def distance(self, obj2):
        distance = super(self.__class__, self).distance(obj2) + ((obj2.z - self.z)**2)
        return distance


p1 = Point2D(3, 6)
p2 = Point2D(9, 10)
print(p1.distance(p2))
print(p1.get_count)
p3 = Point3D(1, 5, 9)
p4 = Point3D(5, 6, 9)
print(p3.distance(p4))
print(p4.get_count)
print(p1.get_count)
