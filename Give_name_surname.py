person = "                                                                     "
print("Podaj imię i nazwisko: ")
data = input()
x = len(data) - 1


def function_name(data, y=len(data)):
    global person
    for y in range(0, y, 1):
        if data[y] == " ":
            break
        else:
            # print(data[x], end="")
            person = person.lstrip(" ") + data[y]
    #print(f"Imię: {person}")
    return person


def function_surname(data):
    for i in range(x, -1, -1):
        if data[i] == " ":
            break
        else:
            person = data[i::+1]
    #print(f"Nazwisko: {person}")
    return person


print(f"Imię osoby to: {function_name(data)}")
print(f"Nazwisko osoby to: {function_surname(data)}")