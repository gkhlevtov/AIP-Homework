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

    def __str__(self):
        return f'Вектор {self.x}, {self.y}'


class Vehicle:
    """Класс для обозначения траспорта"""

    def __init__(self, x0, y0):
        self.x = x0
        self.y = y0
        self.drive_story = ['Стартовые координаты: 0, 0']
        self.vector = Vector(0, 0)

    def set_vector(self, x, y):
        self.vector = Vector(x, y)

    def drive(self, n, count=True):
        if count:
            for i in range(n):
                self.x += self.vector.x
                self.y += self.vector.y
                self.drive_story.append(f'Перемещение на координаты ({self.x}, {self.y})')
        else:
            for i in range(n):
                self.x += self.vector.x
                self.y += self.vector.y


class Car(Vehicle):
    """Класс для обозначения машины"""

    def __init__(self, x0, y0, fuel, mileage):
        Vehicle.__init__(self, x0, y0)
        self.fuel = fuel
        self.mileage = mileage

    @property
    def fuel(self):
        return self.__fuel

    @fuel.setter
    def fuel(self, fuel):
        if fuel < 0:
            print('Недостаточно топлива')
        else:
            self.__fuel = fuel
            print(f'Текущее топливо {self.fuel}')

    def fuel_usage(self):
        usage = self.mileage * self.vector.length()
        return usage

    def drive(self, n, count=True):
        if count:
            for i in range(n):
                if self.fuel >= self.fuel_usage():
                    self.x += self.vector.x
                    self.y += self.vector.y
                    self.fuel -= self.fuel_usage()
                    self.drive_story.append(f'Перемещение на координаты ({self.x}, {self.y})')
                else:
                    print('Недостаточно топлива')

        else:
            for i in range(n):
                if self.fuel >= self.fuel_usage():
                    self.x += self.vector.x
                    self.y += self.vector.y
                    self.fuel -= self.fuel_usage()
                else:
                    print('Недостаточно топлива')


#  Расход топлива из формулы ед. топлива / вектор длиной (скорость) 1

car = Car(0, 0, 12, 1)
car.set_vector(1, 1)
car.drive(8)
print(car.drive_story)
car.set_vector(-2, -2)
car.fuel += 10
car.drive(4)
print(car.drive_story)
