name = []
surname = []

print("Ile osób chcesz wpisać?")
number_of_people = int(input())
print("Wpisz imie i nazwisko dla osoby nr ")
for x in range (0, number_of_people):
    name.append(input())
    surname.append(input())
    print(f"{x+1} to {name}, {surname}")
