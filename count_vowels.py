"""
Count Vowels in The String
Write a function in Python that accepts a single word and also returns the number of vowels in that word.
In this function, only the A, E, I, O, and U will be counted as vowels.
"""
print("Wprowadź słowo. Liczę ile występuje w nim samogłosek")
word = input()
word = word.upper()


def count_a(word):
    if "A" in word:
        counter_a = word.count("A")
        print("Ilość wystąpień litery A: ", counter_a)
    else:
        print("Brak wystąpień litery A")
        counter_a = 0
    return counter_a


def count_e(word):
    if "E" in word:
        counter_e = word.count("E")
        print("Ilość wystąpień litery E: ", counter_e)
    else:
        print("Brak wystąpień litery E")
        counter_e = 0
    return counter_e


def count_i(word):
    if "I" in word:
        counter_i = word.count("I")
        print("Ilość wystąpień litery I: ", counter_i)
    else:
        print("Brak wystąpień litery I")
        counter_i = 0
    return counter_i


def count_o(word):
    if "O" in word:
        counter_o = word.count("O")
        print("Ilość wystąpień litery O: ", counter_o)
    else:
        print("Brak wystąpień litery O")
        counter_o = 0
    return counter_o


def count_u(word):
    if "U" in word:
        counter_u = word.count("U")
        print("Ilość wystąpień litery U: ", counter_u)
    else:
        print("Brak wystąpień litery U")
        counter_u = 0
    return counter_u

def count_y(word):
    if "Y" in word:
        counter_y = word.count("Y")
        print("Ilość wystąpień litery Y: ", counter_y)
    else:
        print("Brak wystąpień litery Y")
        counter_y = 0
    return counter_y


counter_a = count_a(word)
counter_e = count_e(word)
counter_i = count_i(word)
counter_o = count_o(word)
counter_u = count_u(word)
counter_y = count_y(word)

print(f"Poza funkcją:\ncounter_a = {counter_a}\ncounter_e = {counter_e}\ncounter_i = {counter_i}\n"
      f"counter_o = {counter_o}\ncounter_u = {counter_u}\ncounter_y = {counter_y}")


def count_vowels(word):
    counter_vowels = counter_a + counter_e + counter_i + counter_o + counter_u + counter_y
    print(f"W ciele funkcji - Ilość samogłosek we wpisanym wyrazie: {counter_vowels}")
    return counter_vowels

print("Poza ciałęm funkcji - Wywołanie funkcji count_vowels: ")
print(count_vowels(word))