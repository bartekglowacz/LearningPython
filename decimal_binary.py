"""
Convert Any Decimal Number to Binary
In Python write a function that accepts a decimal number and also return an equivalent binary number.
To keep it simple, the decimal number will always be less than 1,024, hence the binary number returned will be less than ten digits long.
"""

import math

print("Podaj liczbę w systemie dziesiętnym, którą chcesz przekonwertować na system binarny: ")
decimal_input = int(input())

whole = math.floor(decimal_input / 2)
rest = decimal_input % 2
result = []

print(f"Liczba {decimal_input} podzielona przez 2 to {whole} i {rest} reszty")
# whole ma być nowym decimal input

while decimal_input > 0:
    whole = math.floor(decimal_input / 2)
    rest = decimal_input % 2
    if rest == 1:
        print("".join("1"), end="")
        result.append("1")
        decimal_input = whole
    if rest == 0:
        print("".join("0"), end="")
        result.append("0")
        decimal_input = whole
print(f"Result list: {result}")