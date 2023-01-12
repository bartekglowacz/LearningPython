"""import time

timer = time.time()
timer2 = time.time()
while True:
    if time.time()-timer > 1:
        print("bam")
        timer = time.time()

    if time.time()-timer2 > 5:
        break;"""
import datetime

now = datetime.datetime.now()
print(now.strftime("%H:%M,%d.%m.%y"))

