"""
Transform Radians into Degrees
Write a function in Python that accepts a numeric parameter and this parameter will be the measure of an angel in radius.
The function converts the radius into degree and returns the value.
You might find a Python library to do this but you must write the function by yourself.
One hint we can give you is that you will need to use Pi to solve the problem.
You can also import the value of Pi from Python’s math module.
"""
import math

print("Podaj wartość kąta w radianach")
radian = input()
radian_left = radian.split(" ")
print(radian_left)
radian_right = radian.split(f"{float}")
print(radian_right)

#def rad_to_deg(radian):
