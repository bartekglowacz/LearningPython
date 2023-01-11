# Użytkownik wprowadza liczby z klawiatury, a program wypisuje tylko te z zadanego przedziału

print("Podaj zbiór liczb\nAby potwierdzić zakończenie wprowadzania naciśnij 'k'")

# 1. dobra praktyka jest od poczatku pisac po angielsku, bo to jest jezyk uzywany w pracy :)
# 2. inputs, numeric_inputs, in_range_inputs = [], [], []  # to jest tzw. tuple unpacking - o ile zmienne nie sa zbyt rozlegle i kod nie traci na przejrzystosci, to mozna zmienne deklarowac w tej samej linii :)
numbers = []
numbers_int = []  # w zasadzie ta deklaracja jest niepotrzebna, bo nie uzywasz tej zmiennej przed
numbers_in_range = []

number = 0  # jezeli bys uzyl przypisania wartosci w tej samej linii co while, to ta linijka jest zbedna

# 3. while (liczba := input()) != "k":  # mozliwe od pythona 3.8 https://peps.python.org/pep-0572/
while number != "k":
    number = input()
    numbers.append(number)
numbers.remove("k")

print(f"Wpisany zbiór stringów to: {numbers}")
print(f"Wielkość zbioru to: , {len(numbers)}")

numbers_int = [int(x) for x in numbers]  # zamiana stringów na inty w liście
print(f"Lista z liczbami po przekonwertowaniu do integer: , {numbers_int}")
print(f"Posortowana: , {sorted(numbers_int)}")
"""for i in range (0, len(liczby_int)):
    print("Element ", i, " tablicy wynosi: ", liczby_int[i])"""  # indeksowanie elementów listy

print("Liczby z jakiego zakresu chcesz wypisać?\nPodaj dolny zakres: ")
lower_range = int(input())
print("Podaj górny zakres: ")
upper_range = int(input())

for x in range(0, len(numbers_int)):
    if upper_range > numbers_int[x] > lower_range:
        # print("Liczby z zadanego zakresu to: ", liczby_int[x])
        numbers_in_range.append(numbers_int[x])
print(f"Lista z liczbami z zadanego zakresu: , {sorted(numbers_in_range)}")

"""
7. wersja dla leniwych
filter przyjmuje nastepujace argumenty filter(condition, collection)
condition to jakas funkcja zwracajaca True lub False - elementy, dla ktorych zwroci True, sa zachowywane w nowej liscie
lambdy to wyzsza szkola magii, o ktora na pozniejszym etapie zahaczysz
Ponizsza lambda mowi: Dla kazdego x sprawdz warunki widoczny po ":"
"""
numbers_in_range = list(filter(lambda x: upper_range > x > lower_range, numbers_int))