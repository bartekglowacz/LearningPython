"""
Napisz klasę FunkcjaKwadratowa, która przechowuje funkcje typu $ax^2$+bx+c. Klasa powinna zawierać trzy pola: a,
b, c, które są przypisywane w konstruktorze. Główną metodą powinna być Rozwiaz(), która zwraca miejsca zerowe podanej
funkcji. Należy zwrócić uwagę na przypadki gdy a=0, b=0 lub c=0, a także obmyślić sposób informowania o nieskończonej
liczbie, jednym lub zerze rozwiązań.
"""
import math


class FunkcjaKwadratowa:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def rozwiaz(self):
        delta = self.b ** 2 - 4 * self.a * self.c
        if delta > 0:
            x1 = (-self.b - math.sqrt(delta)) / (2 * self.a)
            x2 = (-self.b + math.sqrt(delta)) / (2 * self.a)
            print(f"{x1 = }\n{x2 = }")
        if delta == 0:
            x0 = -self.b / (2 * self.a)
            print(f"{x0 = }")
        else:
            print("brak rozwiązań rzeczywistych")


funkcja = FunkcjaKwadratowa(-2, 10, -2)
funkcja.rozwiaz()
