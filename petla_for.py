"""
lista = []
i = 97
while i < 107:
    lista.append(chr(i))
    i += 1
print("Utworzona lista: ", lista)
"""

print("Wpisz swoje imię: ")
imie_in=input()
if len(imie_in) == 1:
    print("Imię składa się z: ", len(imie_in), " litery")
else:
    print("Imię składa się z: ", len(imie_in), " liter")

for i in range (0, len(imie_in)):
    print("Litera nr ", i+1, "to ", imie_in[i])
