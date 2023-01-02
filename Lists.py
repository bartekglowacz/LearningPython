i = 0
# x = [1, 2, 3, 4, 5]
# print("Liczby przed pętlą: ", x)
liczby1 = []
while i < 5:
    liczby1.append(i)
    i += 1
print("Liczby z pętli 0-4: ", liczby1)

i = 5
liczby2 = []
while i <= 10:
    liczby2.append(i)
    i += 1
print("Liczby z pętli 5-10: ", liczby2)

liczby = liczby1 + liczby2
print("Połączone listy: ", liczby)
# print(liczby.index(0))
# print(liczby.index(1))
liczby_parzyste = []
liczby_nieparzyste = []
i = 0
while i <= 10:
    if liczby.index(i) % 2 == 0:
        # print(i, "parzysta")
        liczby_parzyste.append(i)
    else:
        liczby_nieparzyste.append(i)
    i += 1
print("Liczby parzyste: ", liczby_parzyste)
print("Liczby nieparzyste: ", liczby_nieparzyste)
