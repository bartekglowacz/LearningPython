print("Wyświetla tabliczkę mnożenia: \nDla jakiej cyfry wyświetlić?")

i = int(input())
j = 1
while i <= 10:
    while j <= 10:
        print(i, "*", j, "=", i*j)
        j += 1
    i += 1