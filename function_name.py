# Funkcja nr 1 - wyciagajaca z ciagu znakow imie
# Funkcja nr 2 - wyciagajaca z ciagu znakow nazwisko


person = []
print("Podaj imię i nazwisko osoby: ")
data = input()
x = 0

# Pętla idąca tak długo aż zastanie znak spacji
while data[x] != " ":
    print(data[x],end="")
    x += 1
