class Guitar:
    def __init__(self, n_strings=6):
        self.n_strings = n_strings
        self.play()
        self.__cost = 50

    def play(self):
        print("pam pam pam pam pam pam pam")


class ElectricGuitar(Guitar):
    def __init__(self, n_strings):
        super().__init__()
        self.colour = ("#000000", "#FFFFFF")
        self.n_strings = n_strings

    def playLouder(self):
        print("pam pam pam pam pam pam pam".upper())

    def __secret(self):
        print("This guitar actually cost me $", self._Guitar__cost, "only!")


class BassGuitar(Guitar):
    pass


my_classicGuitar = Guitar(2)
my_guitar = ElectricGuitar(55)
my_guitar._ElectricGuitar__secret()
print(f"my bass guitar has {BassGuitar(4).n_strings} strings")
print(f"my electric guitar has {my_guitar.n_strings} strings")
print(f"my guitar has {my_classicGuitar.n_strings} strings")
