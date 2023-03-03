file = open("frequencies.txt", "r")
frequencies = file.readlines()
frequencies = [float(x) for x in frequencies]
print(frequencies)