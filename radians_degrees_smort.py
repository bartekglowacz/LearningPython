import math
import fractions

print("Wprowadź miarę kąta w radianach: ")

radius = input()
radius_split = radius.partition("pi")
# print(radius_split)
radius_digit = radius_split[0]
radius_pi = radius_split[1]
# print(f"Część liczbowa: {radius_digit}, część pi: {radius_pi}")
index_pi = int(radius.find("pi"))
# print(f"Indeks PI: {index_pi}, typ: {type(index_pi)}")

if index_pi != -1:
    degrees_result = fractions.Fraction(radius_digit)*180
    print(f"{radius} [rad] = {degrees_result} [deg]")
if index_pi == -1:
    degrees_result = fractions.Fraction(radius_digit)*180/math.pi
    print(f"{radius} [rad] = {degrees_result} [deg]")