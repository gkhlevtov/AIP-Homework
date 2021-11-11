class Point(object):
    """Класс для обозначения точки"""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __copy__(self):
        return Point(self.x, self.y)

    def distance(self, other):
        try:
            x2 = other.x - self.x
            y2 = other.y - self.y
            v_len = (x2 ** 2 + y2 ** 2) ** 0.5
            return v_len

        except AttributeError:
            print("Ошибка: Отсутствует необходимый атрибут")
        except ValueError:
            print('Ошибка: В метод необходимо подать другую точку')


p1 = Point(1, 1)
p2 = Point(0, 0)
lst = [0, 2]
n = 2

print(p1.distance(p2))
print(p1.distance(lst))
print(p1.distance(n))
