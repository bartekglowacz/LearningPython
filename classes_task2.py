"""
Napisz klasę FunkcjaKwadratowa, która przechowuje funkcje typu $ax^2$+bx+c. Klasa powinna zawierać pole formula,
które jest przypisywane w konstruktorze. Główną metodą powinna być Rozwiaz(), która zwraca miejsca zerowe podanej
funkcji. Należy zwrócić uwagę na przypadki gdy a=0, b=0 lub c=0, a także obmyślić sposób informowania o nieskończonej
liczbie, jednym lub zerze rozwiązań.
"""
import math
import matplotlib.pyplot as plt


class FunkcjaKwadratowa:
    def __init__(self):
        self.delta = None
        self.x0 = None
        self.x2 = None
        self.x1 = None
        self.partition = None
        self.a = None
        self.b = None
        self.c = None
        self.formula = input()

    def format_formula(self):
        self.formula = self.formula.replace("x", "*x")
        self.formula = self.formula.replace("^", "**")
        return self.formula

    def get_coefficients(self):
        self.partition = self.formula.split("*x**")
        self.a = eval((self.partition[0]))
        self.b = self.partition[1].lstrip("2")
        b_tmp = self.b.split("*x")
        self.b = eval(b_tmp[0])
        self.c = eval(b_tmp[1])
        return [self.a, self.b, self.c]

    def solve(self):
        self.delta = self.b ** 2 - 4 * self.a * self.c
        if self.delta > 0:
            self.x1 = (-self.b - math.sqrt(self.delta)) / (2 * self.a)
            self.x2 = (-self.b + math.sqrt(self.delta)) / (2 * self.a)
            return [self.x1, self.x2]
        if self.delta == 0:
            self.x0 = -self.b / (2 * self.a)
            return [self.x0]
        else:
            return "brak rozwiązań rzeczywistych"

    def drawing_function(self):
        vertex_x = -self.b / (2 * self.a)
        vertex_y = -self.delta / (4 * self.a)
        print(f"Parametry wierzchołka: {vertex_x}, {vertex_y}")
        x_list = []
        y_list = []
        plt.ion()
        plt.xlabel("x")
        plt.ylabel("y")
        plt.grid()
        x = vertex_x - 10
        while x < vertex_x + 10:
            x_list.append(x)
            y = eval(formatted_formula)
            y_list.append(y)
            plt.plot(x_list, y_list, color="red")
            plt.autoscale()
            plt.show()
            plt.pause(0.1)
            x += 0.1
        print(x_list, y_list)
        plt.ioff()
        plt.show()


print("Wprowadź równanie w postaci ax^2+bx+c. Nie musisz pisać znaków mnożenia. Przed x zawsze musisz podać liczbę")
function1 = FunkcjaKwadratowa()
formatted_formula = function1.format_formula()
print(f"Formuła po formatowaniu: {formatted_formula}")
coefficients = function1.get_coefficients()
print(f"Współczynniki: {coefficients}")
solutions = function1.solve()
print(f"Rozwiązanie: {solutions}")
function1.drawing_function()
