# Funkcja nr 1 - wyciagajaca z ciagu znakow imie
# Funkcja nr 2 - wyciagajaca z ciagu znakow nazwisko


person = "                                        "
print("Podaj imię i nazwisko osoby: ")
data = input()
x = len(data)-1

# Pętla idąca tak długo aż zastanie znak spacji
for x in range (0, x, 1):
    if data[x] == " ":
        break
    else:
        #print(data[x], end="")
        person = person.lstrip(" ") + data[x]
print(f"Imię: {person}")
