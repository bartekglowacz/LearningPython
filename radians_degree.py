"""
Transform Radians into Degrees
Write a function in Python that accepts a numeric parameter and this parameter will be the measure of an angel in radius.
The function converts the radius into degree and returns the value.
You might find a Python library to do this but you must write the function by yourself.
One hint we can give you is that you will need to use Pi to solve the problem.
You can also import the value of Pi from Python’s math module.
"""
import math

print("""Podaj wartość kąta w radianach w któreś z poniższych postaci:\n- 2.0pi\n- 2\n- 1/2pi\n- 1/2 """)
radian = input()
radian_partition = radian.partition("pi")
print(radian_partition, type(radian_partition))
print(f"Element 0 ma wartość: {radian_partition[0]}, typ: {type(radian_partition[0])}")
print(f"Element 1 ma wartość: {radian_partition[1]}, typ: {type(radian_partition[1])}")
# print(float(radian_partition[0]))

#

if radian_partition[0].find(".") == True and radian_partition[1] == ("pi"):
    print("Ułamek dziesiętny")
    degrees = float(radian_partition[0]) * 180
    print(f"{radian} w mierze kątowej jest równe {degrees}")
if radian_partition[0].find(".") == True and radian_partition[1] != ("pi"):
    print("Ułamek dziesiętny")
    degrees = float(radian_partition[0]) * 180/math.pi
    print(f"{radian} w mierze kątowej jest równe {degrees}")
if radian_partition[0].find("/") == True and radian_partition[1] == ("pi"):
    print("Ułamek zwykły")
    fraction = radian_partition[0].partition("/")
    division = float(fraction[0]) / float(fraction[2])
    degrees = division * 180
    print(f"{radian} w mierze kątowej jest równe {degrees}")
if radian_partition[0].find("/") == True and radian_partition[1] != ("pi"):
    print("Ułamek zwykły")
    fraction = radian_partition[0].partition("/")
    division = float(fraction[0]) / float(fraction[2])
    degrees = division * 180/math.pi
    print(f"{radian} w mierze kątowej jest równe {degrees}")