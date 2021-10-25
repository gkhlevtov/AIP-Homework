import math as m
x1, y1, r1 = map(float, input().split(' '))
x2, y2, r2 = map(float, input().split(' '))


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


circle1 = Circle(Point(x1, y1), r1)
circle2 = Circle(Point(x2, y2), r2)

if circle1.check_common_point(circle2):
    print('YES')
else:
    print('NO')