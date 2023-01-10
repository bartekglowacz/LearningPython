# Użytkownik wprowadza liczby z klawiatury, a program wypisuje tylko te z zadanego przedziału

print("Podaj zbiór liczb\nAby potwierdzić zakończenie wprowadzania naciśnij 'k'")

liczby = []
liczby_int = []
liczby_przedzial = []

liczba = 0

while liczba != "k":
    liczba = input()
    liczby.append(liczba)
liczby.remove("k")

print("Wpisany zbiór stringów to: ", liczby)
print("Wpisany zbiór zawiera ", len(liczby), "elementów")

liczby_int = [int(x) for x in liczby]  # zamiana stringów na inty w liście
print("Lista z liczbami po przekonwertowaniu do integer: ", liczby_int)
# print("typ: ", type(liczby_int[0])) # sprawdzenie czy w liście na pewno są inty

"""for i in range (0, len(liczby_int)):
    print("Element ", i, " tablicy wynosi: ", liczby_int[i])"""  # indeksowanie elementów listy

print("Liczby z jakiego zakresu chcesz wypisać?\nPodaj dolny zakres: ")
zakres_dol = int(input())
print("Podaj górny zakres: ")
zakres_gora = int(input())

for x in range(0, len(liczby_int)):
    if zakres_gora > liczby_int[x] > zakres_dol:
        # print("Liczby z zadanego zakresu to: ", liczby_int[x])
        liczby_przedzial.append(liczby_int[x])
print("Lista z liczbami z zadanego zakresu: ", liczby_przedzial)
