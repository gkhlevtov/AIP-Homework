import math as m


class Point(object):
    """Класс для обозначения точки"""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def copy_point(self):
        point = Point(self.x, self.y)
        return point

    def coordinates(self):
        return list([self.x, self.y])

    def distance_to(self, x2, y2):
        x3 = x2 - self.x
        y3 = y2 - self.y
        v_len = (x3 ** 2 + y3 ** 2) ** 0.5
        return v_len


def side_length(point1, point2):
    x = point2.coordinates()[0] - point1.coordinates()[0]
    y = point2.coordinates()[1] - point1.coordinates()[1]
    v_len = (x ** 2 + y ** 2) ** 0.5
    return v_len


class Triangle(object):
    """Класс для обозначения треугольника"""
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.p1 = Point(x1, y1)
        self.p2 = Point(x2, y2)
        self.p3 = Point(x3, y3)

    def perimeter(self):
        a = side_length(self.p1, self.p2)
        b = side_length(self.p2, self.p3)
        c = side_length(self.p3, self.p1)
        return a + b + c

    def area(self):
        a = side_length(self.p1, self.p2)
        b = side_length(self.p2, self.p3)
        c = side_length(self.p3, self.p1)
        p = (a + b + c) / 2
        area = (p*(p-a)*(p-b)*(p-c)) ** 0.5
        return area

    def contains(self, pnt):
        a = (self.p1.x - pnt.x) * (self.p2.y - self.p1.y) - (self.p2.x - self.p1.x) * (self.p1.y - pnt.y)
        b = (self.p2.x - pnt.x) * (self.p3.y - self.p2.y) - (self.p3.x - self.p2.x) * (self.p2.y - pnt.y)
        c = (self.p3.x - pnt.x) * (self.p1.y - self.p3.y) - (self.p1.x - self.p3.x) * (self.p2.y - pnt.y)
        return a >= 0 and b >= 0 and c >= 0


class Circle(Point):
    """Класс для обозначения окружности"""

    def __init__(self, center, r):
        self.x = center.x
        self.y = center.y
        self.r = r
        self.p = center

    def __contains__(self, point):
        return self.center.distance(point) <= self.r

    def circle_length(self):
        l = m.pi * self.r * 2
        return l

    def circle_area(self):
        s = m.pi * self.r ** 2
        return s

    def check_common_point(self, circle2):
        distance = self.p.distance_to(circle2.p.coordinates()[0], circle2.p.coordinates()[1])
        return self.r + circle2.r >= distance and distance + circle2.r >= self.r and distance + self.r >= circle2.r
