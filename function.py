# Funkcja nr 1 - wyciagajaca z ciagu znakow imie
# Funkcja nr 2 - wyciagajaca z ciagu znakow nazwisko

data = "Adam Nowak"
x = 0

# Pętla idąca tak długo aż zastanie znak spacji
while data[x] != ascii(32):
   print(data)
   x += 1