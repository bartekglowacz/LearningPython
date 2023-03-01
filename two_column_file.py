import random

frequencies = []
level = []
combine_list = []

for f in range(1, 21, 1):
    x = 10 * f
    y = round(random.random() * random.randint(1, 100), 2)
    frequencies.append(x)
    level.append(y)

print(frequencies)
print(level)

result_file = open("result.txt", "w")
for counter in range(0, len(frequencies)):
    result_file.write(str(frequencies[counter]) + "\t" + str(level[counter]))
    result_file.write("\n")