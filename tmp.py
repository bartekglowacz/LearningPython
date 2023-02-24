wzor = "205x^2 + 34x + 91"
wspolczynniki = []
for char in wzor:
    try:
        if float(char):
            wspolczynniki.append(char)
            print(f"{char = }")
    except Exception as e:
        continue
        # print(f"Błąd: {e}")

print(f"{wspolczynniki = }")
a = float(wspolczynniki[0])
b = float(wspolczynniki[2])
c = float(wspolczynniki[3])
print(f"{a = }, {b = }, {c = }")
