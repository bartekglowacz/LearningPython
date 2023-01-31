"""
Are Xs Equal to Os?
Create a function in Python that accepts a string.
This function must count the number of Xs and Os in the string.
And then it should return a boolean value of either True or False.
If the Xs and Os count is equal then the function must return true.
If the count isn’t the same then it must return false.
And if there are no Xs and Os in the string then also it must return true because 0 equals 0.
"""
print("Wpisz słowo lub zdanie")
napis = input()


def Xs_Equal_oS(napis):
    counterXs = 0
    counterOs = 0
    for x in range(0, len(napis)):
        if napis[x].upper() == "X":
            counterXs += 1
        elif napis[x].upper() == "O":
            counterOs += 1
    print(f"{counterXs = }")
    print(f"{counterOs = }")
    if counterXs == counterOs:
        return print(f"Czy tyle samo Xs i Os?\n{bool(counterXs == counterOs)}")
    if counterXs != counterOs:
        return print(f"Czy tyle samo Xs i Os?\n{bool(counterXs == counterOs)}")


Xs_Equal_oS(napis)
