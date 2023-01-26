"""
Convert Any Decimal Number to Binary
In Python write a function that accepts a decimal number and also return an equivalent binary number.
To keep it simple, the decimal number will always be less than 1,024, hence the binary number returned will be less than ten digits long.
"""

import math

print("Podaj liczbę w systemie dziesiętnym, którą chcesz przekonwertować na system binarny: ")
decimal_input = int(input())
TwoPowX = []
exponents = []
exponents_all = []
binary_list = []


def decimal_to_binary(decimal_input):
    loop_counter = 0
    while math.log2(decimal_input) >= 0:
        # 1. Znajdź potęgę liczby 2, która jest najbliższa wpianej wartości, ale mniejsza od niej
        max_2powx = math.log2(decimal_input)
        max_2powx = math.floor(max_2powx)
        # print(f"maksymalny wykładnik liczby 2, przy którym liczba jest mniejsza od zadanej: {max_2powx}")

        # Powtórz operację z punktu 1 i tak do momentu aż log2(x)=0
        pow_temp = math.pow(2, max_2powx)
        # dopisanie wykładnika liczby 2 do listy
        TwoPowX.append(pow_temp)
        exponents.append(math.log2(pow_temp))
        # print(f"Liczba 2 po podniesieniu do tej potęgi: {pow_temp}")
        rest_decimal = decimal_input - pow_temp
        # print(f"Zostało do rozpisania: {rest_decimal}")

        decimal_input = rest_decimal
        loop_counter += 1
        if decimal_input == 0:
            break
    # print(f"\nPętla wykonała się następującą ilość razy: {loop_counter}")


def binary_form(exponents_all_HighToLow_str, exponents_str):
    print(f"Zamieniam {decimal_input} na postać binarną:")

    for x in range(0, len(exponents_all_HighToLow_str), 1):
        if exponents_all_HighToLow_str[x] != exponents_str[x]:
            exponents_str.insert(x, "none")

    for x in range(0, len(exponents_str), 1):
        if exponents_all_HighToLow_str[x] == exponents_str[x]:
            binary_list.insert(x, "1")
        else:
            binary_list.insert(x, "0")
    print("".join(binary_list))

decimal_to_binary(decimal_input)
# print(f"Lista z liczbami: {TwoPowX}")
# print(f"Lista z użytymi wykładnikami liczby 2: {exponents}")
exponents_str = [str(x) for x in exponents]
# print(f"Lista z użytymi wykładnikami liczby 2, ale typu str: {exponents_str}")

# utworzenie listy ze wszystkimi możliwymi wykładnikami, począwszy od największej dla wprowadzonej liczby


# print(f"Max wartość na liście to = {max(TwoPowX)}.\nJest to 2 podniesione do potęgi: {math.log2(max(TwoPowX))}")
for x in range(int(math.log2(max(TwoPowX))), -1, -1):
    exponents_all.append(math.log2(max(TwoPowX)) - x)
# print(f"Wszystkie wykładniki: {exponents_all}")
exponents_all_HighToLow = exponents_all[::-1]
# print(f"Posortowane od największej do najmniejszej: {exponents_all_HighToLow}")
exponents_all_HighToLow_str = [str(x) for x in exponents_all_HighToLow]
print(f"Posortowane od największej do najmniejszej: {exponents_all_HighToLow_str},")

binary_form(exponents_all_HighToLow_str, exponents_str)
print(f"Lista 1: {exponents_str}")
print(f"Lista 2: {exponents_all_HighToLow_str}")

# print(len(exponents_str) == len(exponents_all_HighToLow_str)) # sprawdzenie czy tablice mają takie same długości
print(binary_list)