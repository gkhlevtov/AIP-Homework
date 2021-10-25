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

    def distance_to(self, other):
        x3 = other.x - self.x
        y3 = other.y - self.y
        v_len = (x3 ** 2 + y3 ** 2) ** 0.5
        return v_len


def side_length(point1, point2):
    x = point2.coordinates()[0] - point1.coordinates()[0]
    y = point2.coordinates()[1] - point1.coordinates()[1]
    v_len = (x ** 2 + y ** 2) ** 0.5
    return v_len


class Circle:
    """Класс для обозначения окружности"""

    def __init__(self, center, r):
        self.x = center.x
        self.y = center.y
        self.r = r
        self.center = center

    def __contains__(self, point):
        return self.center.distance_to(point) <= self.r

    def circle_length(self):
        l = m.pi * self.r * 2
        return l

    def circle_area(self):
        s = m.pi * self.r ** 2
        return s

    def check_common_point(self, circle2):
        distance = self.center.distance_to(circle2.center.coordinates()[0], circle2.center.coordinates()[1])
        return self.r + circle2.r >= distance and distance + circle2.r >= self.r and distance + self.r >= circle2.r


class Operator:
    def __init__(self, name):
        self.name = name
        self.towers = []
        self.available = 0

    def __str__(self):
        return f'{self.name} {self.available}'


n = int(input())
operators = {}

for i in range(n):
    name = input()
    x, y, r = map(float, input().split())
    tower = Circle(Point(x, y), r)
    if name not in operators:
        operators[name] = Operator(name)
    operators[name].towers.append(tower)

user = Point(*map(float, input().split()))

for op in operators.values():
    for tower in op.towers:
        if user in tower:
            op.available += 1

print(len(operators))
for op in operators.values():
    print(op)
