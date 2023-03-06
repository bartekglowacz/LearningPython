import random

print("Poraj zakres losowania liczb\nstart:")
start = int(input())
print("stop: ")
stop = int(input())

print(f"losuję z zakresu od {start} do {stop}")
level = random.randint(start, stop)
print(level)