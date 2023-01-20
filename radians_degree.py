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
# print(f"Długość 0 elementu: {len(radian_partition[0])}")

digit_part = radian_partition[0]

print(f"Sama część liczbowa: {digit_part}, typ: {type(digit_part)}, długość: {len(digit_part)}")

# print(digit_part[0].isdigit())
# print("Czy wpisano pi?", radian.find("pi")) sprawdzenie występowania PI we wpisanym stringu "radian"
for x in range(0, len(digit_part)):
    if digit_part[x] == "/":
        parts = digit_part.partition("/") #oddzielam z części liczbowej liczbę, "/" i drugą liczbę
        print(f"Podzielona część liczbowa: {(parts)}")
        digit_part_1 = parts[0]
        digit_part_2 = parts[2]
        division_result = int(digit_part_1)/int(digit_part_2)
        print(f"Wpisany ułamek w postaci dziesiętnej: {division_result}")

        if radian.find("pi") == -1:
            radius_result = division_result*180/math.pi
            print(f"{digit_part} rad wyrażone w stopniach: {radius_result}")
        if radian.find("pi") != -1:
            radius_result = division_result * 180
            print(f"{radian} rad wyrażone w stopniach: {radius_result}")


    if digit_part[x] == ".":
        decimal_fraction = float(digit_part)

        if radian.find("pi") == -1:
            radius_result = decimal_fraction*180/math.pi
            print(f"{digit_part} rad wyrażone w stopniach: {radius_result}")
        if radian.find("pi") != -1:
            radius_result = decimal_fraction * 180
            print(f"{radian} rad wyrażone w stopniach: {radius_result}")
