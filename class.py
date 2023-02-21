class Fruit:
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour
        self.exp_date = "20.07.2021"

    def details(self):
        print("expires on: " + self.exp_date)


apple = Fruit("apple", "red")
apple.details()
print(f"{apple.name} is {apple.colour} and has expires date on {apple.exp_date}")