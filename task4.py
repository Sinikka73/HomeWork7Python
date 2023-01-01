"""
 Реализуйте базовый класс Car. У данного класса должны быть следующие
 атрибуты: speed, color, name, is_police (булево).
 А также методы: go, stop, turn(direction), которые должны сообщать,
 что машина поехала, остановилась, повернула (куда). Опишите несколько
 дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
 Добавьте в базовый класс метод show_speed, который должен показывать
 текущую скорость автомобиля. Для классов TownCar и WorkCar
 переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
 и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:
    """
    Характеристики авто и его состояний
    """

    def __init__(self, name, speed, color, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = bool(is_police)

    def auto_go(self):
        """
        :return:авто в движении
        """
        return "Автомобиль движется."

    def auto_stop(self):
        """
        :return: остановка
        """
        return "Автомобиль остановился."

    def auto_turn(self, direction):
        """
        :return: поворот направо или налево
        """
        return "Автомобиль поворачивает " + direction + "."

    def show_speed(self):
        """
        :return: скорость
        """
        print(
            f"Автомобиль {self.name} движется со скоростью {self.speed} км.ч")


class TownCar(Car):
    """
    семейный автомобиль
    """
    def show_speed(self):
        """
        :return: превышена скорость или нет
        """
        if self.speed < 60:
            return "Автомобиль движется с нормальной скоростью."
        return "Превышение скорости."


class WorkCar(Car):
    """
    служебный автомобиль
    """
    def show_speed(self):
        """
        :return: превышена скорость или нет
        """
        if self.speed < 40:
            return "Автомобиль движется с нормальной скоростью"
        return "Превышение скорости."


class SportCar(Car):
    """
    спортивный автомобиль
    """
    def get_class_info_1(self):
        """
        :return: описание
        """
        print(f"{self.name} - спортивная машина.")


class PolisCar(Car):
    """
    полиция
    """
    def get_class_info_2(self):
        """
        :return: описание
        """
        print(f"{self.name} - полицейская машина.")


nissan = TownCar("Nissan", 80, "grey", False)
print(f"{nissan.name}, цвет: {nissan.color}, "
      f"движется со скоростью: {nissan.speed} км.ч")
print(nissan.show_speed(), nissan.auto_go(), nissan.auto_turn("налево"))
nissan.speed = 50
print(f"скорость: {nissan.speed} км.ч")
print(nissan.show_speed(), nissan.auto_go(), nissan.auto_stop())
print()
ford = SportCar("Ford", 120, "red", False)
ford.get_class_info_1()
print(f"цвет: {ford.color}")
print(ford.auto_turn("налево"))
print()
bmw = PolisCar("BMW", 75, "белый", True)
print(f"{bmw.name}, цвет: {bmw.color}")
print(bmw.auto_turn("направо"), bmw.auto_go(), bmw.auto_stop())
print()
bmw = WorkCar("BMW", 35, "black", False)
print(
    f"{bmw.name}, цвет: {bmw.color}, движется со скоростью: {bmw.speed} км/ч")
print(bmw.show_speed(), bmw.auto_turn("направо"))
bmw.speed = 90
print(bmw.show_speed())
