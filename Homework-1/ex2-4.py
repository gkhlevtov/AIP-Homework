x1, y1 = map(float, input().split(' '))
x2, y2 = map(float, input().split(' '))
x3, y3 = map(float, input().split(' '))
x4, y4 = map(float, input().split(' '))


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

pntin = Point(x4, y4)

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
        if a >= 0 and b >= 0 and c >= 0:
            return True
        else:
            return False


t = Triangle(x1, y1, x2, y2, x3, y3)
if t.contains(pntin):
    print('In')
else:
    print('Out')