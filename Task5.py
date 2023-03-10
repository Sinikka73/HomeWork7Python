"""
Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса
Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов метод должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод
для каждого экземпляра.
"""


class Stationery:
    """
    Канцтовары
    """

    def __init__(self, title):
        self.title = title

    def draw(self):
        """
        :return: отрисовка
        """
        print("Отрисовка")


class Pen(Stationery):
    def draw(self):
        """
        :return: text
        """
        return "pen - ручка"


class Pencil(Stationery):
    def draw(self):
        """
        :return: text
        """
        return "pencil - карандаш"


class Handle(Stationery):
    def draw(self):
        """
        :return: text
        """
        return "Handle - маркер"


pen = Pen('Pen')
pencil = Pencil('Pencil')
handle = Handle('Handle')
print(pen.draw())
print(pencil.draw())
print(handle.draw())