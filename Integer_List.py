"""
List with Integers
Create a function in Python accepting a list of any length containing a mix of non-negative strings and integers.
The function must return a list with only integers in the original list in the same order.
"""


def mix_list(lista):
    for x in range(0, len(lista), 1):
        if isinstance(lista[x], int):
            integer_list.append(lista[x])
    print(f"mix_list: {integer_list}")
    return integer_list


def mix_list2(lista):
    for x in lista:
        if type(x) == int:
            integer_list.append(x)
        if type(x) == str:
            break
    print(f"mix_list2: {integer_list}")
    return integer_list


integer_list = []
mixed_list = ["kra", 1, "as", 3, 2, "tram", 55, "mama", 5]
print(f"Lista oryginalna: {mixed_list}")

mix_list(mixed_list)
mix_list2(mixed_list)
