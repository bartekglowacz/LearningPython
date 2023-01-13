person = []
print("Podaj imię i nazwisko osoby: ")
data = input()
x = len(data)-1
print(f"Długość imienia: {x}")
print(f"ostatni znak to: {data[x]}")
#print(data[len(data)-1])
# Pętla idąca tak długo aż zastanie znak spacji
while data[x] != " ":
    print(data[x])
    if data[x].isspace:
        break
    x -= 1