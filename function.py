# Funkcja nr 1 - wyciagajaca z ciagu znakow imie
# Funkcja nr 2 - wyciagajaca z ciagu znakow nazwisko

data = "Kamil Zdun"
people = []
x = 0

# Pętla idąca tak długo aż zastanie znak spacji
while x < len(data):
   # print(f"Element {x} to {data[x]}")
   print(data[x], end="")
   # people.append(data[x])

   if data[x].isspace():
      break
   people.append(data[x])
   x += 1
print(f"\nNa liście: {people}")
print(len(people))