# napisz funkcję, która będzie przyjmować dwa parametry:
# - listę liczb
# - string desc, asc, none, który poinstruuje funkcję czy sortowanie ma być w kolejności rosnącej (asc) czy malejącej (desc) czy też bez zmian (none)

tab = []
tab_asc = []
tab_desc = []
tab_none = []

print("""Wprowadź elemnty tablicy\nNaciśnięcie "k" kończy sekwencję""")
x = 0
while x != "k":
    x = input()
    tab.append(x)
tab.remove("k")
tab = [int(x) for x in tab]

print("Jak posortować tablicę? Wpisz\nasc - rosnąco\ndesc - malejąco\nnone - bez zmian")
mode = input()


def sort_list(tab, mode):
    n = len(tab)

    if mode == "asc":
        while n > 1:
            zamien = False
            for l in range(0, n - 1):
                if tab[l] > tab[l + 1]:
                    tab[l], tab[l + 1] = tab[l + 1], tab[l]
                    zamien = True

            n -= 1
            tab
            if not zamien: break
        print(tab)
        return tab

    if mode == "desc":
        while n > 1:
            zamien = False
            for l in range(0, n - 1):
                if tab[l] < tab[l + 1]:
                    tab[l], tab[l + 1] = tab[l + 1], tab[l]
                    zamien = True

            n -= 1
            tab
            if not zamien: break
        print(tab)
        return tab

    if mode == "none":
        for l in range(0, n - 1):
            tab
        print(tab)
        return tab

sort_list(tab, mode)
