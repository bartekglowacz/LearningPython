import random
import time
import matplotlib.pyplot as draw

draw.ion()

print("Poraj zakres losowania liczb\nstart:")
start = int(input())
print("stop: ")
stop = int(input())

print(f"losuję z zakresu od {start} do {stop}")

frequency = [float(x) for x in range(6000, 18000, 1000)]
# print(frequency)
# level = random.randint(start, stop)
# print(level)
print("Wprowadź najniższą spodziewaną wartość: ")
error_condition_value = int(input())

level_list = []
frequency_list = []

draw.grid()
draw.xlabel("f [MHz]")
draw.ylabel("Level [dBuV]")
draw.plot(frequency_list, level_list)

for x in frequency:
    level = random.randint(start, stop)
    if level < error_condition_value:
        print("You are in if!")
        while level < error_condition_value:
            print("You are in while nested in if!")
            level = random.randint(start, stop)
            print(f"f = {x} MHz")
            print(f"Level = {level} dBuV")
            time.sleep(2)
        level_list.append(level)
        frequency_list.append(x)
    else:
        print("You are in for!")
        print(f"f = {x} MHz")
        print(f"Level = {level} dBuV")
        level_list.append(level)
        frequency_list.append(x)
    draw.plot(frequency_list, level_list, color='b')
    draw.pause(1)
draw.ioff()
draw.show()

print(frequency_list)
print(level_list)
