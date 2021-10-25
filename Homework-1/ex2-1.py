x1, y1, x2, y2 = map(float, input().split(' '))


class Point(object):
    """Класс для обозначения точки"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __copy__(self):
        return Point(self.x, self.y)

    '''
    def copy_point(self):
        point = Point(self.x, self.y)
        return point
    '''

    def distance_to(self, other):
        x2 = other.x - self.x
        y2 = other.y - self.y
        v_len = (x2 ** 2 + y2 ** 2) ** 0.5
        return v_len


pnt = Point(x1, y1)
pnt2 = Point(x2, y2)
print(pnt.distance_to(pnt2))