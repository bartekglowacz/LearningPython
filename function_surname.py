print("Podaj imię i nazwisko osoby: ")
data = input()
person = "                                                                     "
x = len(data)-1
#print(f"Imię i nazwisko skłąda się z: {x} liter")
#print(f"ostatni znak to: {data[x]}")


for i in range(x, -1, -1):
    if data[i] == " ":
        break
    else:
        # print(f"Element {i} = {data[i]}")
        # print(f"{data[i]}", end="")
        # print(data[i::+1]) # prawie działa!
        person = data[i::+1]
print(f"Nazwisko: {person}")






