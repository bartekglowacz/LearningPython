"""
Convert Any Decimal Number to Binary
In Python write a function that accepts a decimal number and also return an equivalent binary number.
To keep it simple, the decimal number will always be less than 1,024, hence the binary number returned will be less than ten digits long.
"""

import math

print("Podaj liczbę w systemie dziesiętnym, którą chcesz przekonwertować na system binarny: ")
decimal_input = int(input())
decimal_input_global = decimal_input

whole = math.floor(decimal_input / 2)
rest = decimal_input % 2
result = []

while decimal_input > 0:
    whole = math.floor(decimal_input / 2)
    rest = decimal_input % 2
    if rest == 1:
        result.append("1")
        decimal_input = whole
    if rest == 0:
        result.append("0")
        decimal_input = whole

result2 = result[::-1]
# print(f"\nResult list: {result2}")
string_result = "".join(result2)
print(f"Decimal form: {decimal_input_global}\nBinary form: {string_result}")
