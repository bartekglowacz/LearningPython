def read_current():
    file = open("current.txt", "r")
    current = file.readlines()
    current = [float(x.replace(",", ".")) / 1000 for x in current]
    # print(current)
    return current


current_list = read_current()
print(current_list)
