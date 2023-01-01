"""
 Создать класс TrafficLight (светофор) и определить у него один атрибут
 color (цвет) и метод running (запуск). Атрибут реализовать как приватный.
 В рамках метода реализовать переключение светофора в режимы:
 красный, желтый, зеленый. Продолжительность первого состояния (красный)
 составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
 на ваше усмотрение. Переключение между режимами должно осуществляться только
 в указанном порядке (красный, желтый, зеленый). Проверить работу примера,
 создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов,
и при его нарушении выводить соответствующее сообщение и завершать скрипт.
"""

import time


class TrafficLight:
    """
    Светофор
    """
    # атрибут
    __color = ["Red", "Yellow", "Green"]

    def __init__(self, red_time, yellow_time, green_time, num_time):
        self.red_time = red_time
        self.yellow_time = yellow_time
        self.green_time = green_time
        self.num_time = num_time

    # метод
    def running(self):
        """
        Метод работы светофора:
        красный - 7сек.,
        желтый - 2сек.,
        зелёный - 8сек

        """
        col = [red_t, yellow_t, green_t]
        colors = dict(zip(TrafficLight.__color, col))
        i = 0
        while i < num_t:
            print("Красный")
            time.sleep(colors.get("Red"))
            print("Жёлтый")
            time.sleep(colors.get("Yellow"))
            print("Зелёный")
            time.sleep(colors.get("Green"))
            print("-------")
            i = i + 1
        print("Программа завершена")


red_t = int(input("Введите время работы красного сигнала: "))
yellow_t = int(input("Введите время работы жёлтого сигнала: "))
green_t = int(input("Введите время работы зелёного сигнала: "))
num_t = int(input("Введите количество циклов работы светофора: "))
a = TrafficLight(red_t, yellow_t, green_t, num_t)
a.running()
