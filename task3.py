"""
 Реализовать базовый класс Worker (работник), в котором определить атрибуты:
 name, surname, position (должность), income (доход). Последний атрибут
 должен быть защищенным и ссылаться на словарь, содержащий элементы:
 оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс
 Position (должность) на базе класса Worker. В классе Position реализовать
 методы получения полного имени сотрудника (get_full_name) и дохода
 с учетом премии (get_total_income). Проверить работу примера на реальных
 данных (создать экземпляры класса Position, передать данные, проверить
 значения атрибутов, вызвать методы экземпляров).
"""


class Worker:
    """
    Создание атрибутов работника
    """
    name = None
    surname = None
    position = None
    _income = None

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    """
    Определние дохода заданного работника
    """

    def get_full_name(self):
        """
        :return: полное имя
        """
        return self.name + " " + self.surname

    def get_total_income(self):
        """
        :return: полный доход
        """
        return self._income.get("wage") + self._income.get("bonus")


person = Position("Александр", "Козырев", "директор", 50000, 5000)
print(person.get_full_name(), end=", ")
print(f"должность:  {person.position}", end=", ")
print(f"доход за период: {person.get_total_income()}")