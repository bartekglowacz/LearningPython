name_surname = []

print("Ile osób chcesz wpisać?")
number_of_people = int(input())
print("Wpisz imie i nazwisko dla osoby nr ")
for x in range (0, number_of_people):
    print(x+1,":")
    name_surname.append(input())
print(f"{name_surname}")


