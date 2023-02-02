"""
Repeat Characters
Create a function in Python that accepts a string
and the python must return a string with each character in the original string doubled.
If you send the “now” function as a parameter it must return “nnooww,”.
If you send “123a!”, it must return “112233aa!!”.
"""

print("Napisz słowo")
some_string = input()


def double_characters1(str: some_string):
    splitted_string = list(some_string)
    double_string = []
    print(f"{splitted_string}")
    for x in some_string:
        double_string.append("".join(x + x))

    return "".join(double_string)


def double_characters2(some_string):
    return "".join([char * 2 for char in some_string])


print("Funkcja 1: ", double_characters1(some_string))
print("Funkcja 2: ", double_characters2(some_string))
