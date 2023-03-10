"""
Реализовать класс Road (дорога), в котором определить атрибуты:
length (длина), width (ширина). Значения данных атрибутов должны
передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия
всего дорожного полотна. Использовать формулу: длинаширинамасса асфальта
для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см*число см толщины полотна. Проверить работу метода.
Например: 20м*5000м*25кг*5см = 12500 т
"""


class Road:
    """
    Расчёт массы дорожного полотна
    """
    _length = None
    _width = None

    def __init__(self, length, width, thickness):
        self._length = length
        self._width = width
        self.thickness = thickness

    def calculation(self):
        """
        Масса покрытия дороги длиной 5000м, шириной 20м, заданной толщиной
        """
        weigth = 0.025
        print("Принимаем расход асфальта на покрытие 1кв.м - 25кг")
        calc = self._length * self._width * weigth * self.thickness / 100
        print(f'Для покрытия дороги длиной 5000м, шириной 20м, '
              f'толщиной {self.thickness} cм '
              f'необходимо  {round(calc)}т. асфальта')


thick = int(input("Введите толщину дорожного "
                  "полотна в сантиметрах: "))
asphalt_weight = Road(5000, 20, thick)

asphalt_weight.calculation()