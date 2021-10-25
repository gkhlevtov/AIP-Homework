class Point(object):
    """Класс для обозначения точки"""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __copy__(self):
        return Point(self.x, self.y)

    def distance_to(self, other):
        x2 = other.x - self.x
        y2 = other.y - self.y
        v_len = (x2 ** 2 + y2 ** 2) ** 0.5
        return v_len


class Vector:
    """Класс для обозначения вектора"""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def length(self):
        length = (self.x ** 2 + self.y ** 2) ** 0.5
        return length

    def vector_plus(self, other):
        x = other.x + self.x
        y = other.y + self.y
        return Vector(x, y)

    def vector_minus(self, other):
        x = other.x - self.x
        y = other.y - self.y
        return Vector(x, y)

    def vector_number_multiply(self, number):
        if number == 0:
            return 0
        else:
            return Vector(self.x * number, self.y * number)

    def vector_vector_multiply(self, other):
        x = other.x * self.x
        y = other.y * self.y
        return sum([x, y])


v = Vector(3, 5)
v2 = v.vector_number_multiply(-3)
v3 = v2.vector_minus(v)
summ = v.vector_vector_multiply(v3)

print(v2.x, v2.y)
print(v3.x, v3.y)
print(summ)
