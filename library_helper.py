"""
Treść wyzwania rekrutacyjnego: Zaprogramuj robota, który będzie pomagał Paniom w bibliotece w odkładaniu książek
przyniesionych przez czytelników na odpowiednie półki. Dla uproszczenia zakładamy, że jest to biblioteka
specjalizująca się w 3-ech gatunkach książek. Książka może być: naukowa, biograficzna lub przygodowa. Ponieważ
książka sama w sobie nie jest gatunkiem, dlatego do sprawdzenia jakiego jest rodzaju mamy specjalną funkcję o nazwie:

sprawdz_gatunek_ksiazki(ksiazka);

Aby zoptymalizować pracę robota tak, aby nie musiał chodzić odkładać każdą pojedynczą pozycję, kiedy tylko ją
otrzyma, to dajemy mu do dyspozycji 3 pudełka na 3 różne gatunki książek. W każdym z tych pudełek może zmieścić się
maksymalnie 5 książek. Zakładamy, że jeśli jakieś pudełko jest pełne, to należy uruchomić odpowiednią funkcję,
aby robot odniósł książki z tego pudełka na odpowiednią półkę. Ilość książek w danym pudełku oznaczamy odpowiednią
zmienną – tym razem mamy do dyspozycji następujące zmienne: naukowe, biograficzne, przygodowe. Pamiętaj, że zmienne
„naukowa” i „naukowe” są różne i przechowują różne informacje!

Oto lista wszystkich zmiennych i funkcji jakie masz do dyspozycji:


1. ksiazka; gatunek; naukowa; biograficzna; przygodowa; naukowe; biograficzne; przygodowe;
2. ksiazka = odbierz_ksiazke( );
3. gatunek = sprawdz_gatunek_ksiazki(ksiazka);
4. odloz_na_polke_z_ksiazkami_naukowymi(naukowe);
5. odloz_na_polke_z_ksiazkami_biograficznymi(biografie);
6. odloz_na_polke_z_ksiazkami_przygodowymi(przygodowe);
7. odloz_na_bok(ksiazka);
8. wyswietl_komunikat(”Treść komunikatu.”);

Robot powinien działać dopóki czytelnik podaje mu kolejne książki.
"""


class Book:
    def __init__(self, title, genre):
        self.title = title
        self.genre = genre

    def give_title(self):
        print("Podaj tytuł książki: ")
        self.title = input()

    def give_genre(self):
        print("Podaj gatunek książki: ")
        self.genre = input()


def podaj_tytuł():
    print("Podaj tytuł książki")
    title = input()
    return title


def podaj_gatunek():
    print("Podaj gatunek książki")
    genre = input()
    return genre


def odnies_na_polke_naukowe(naukowe):
    print(f"Na półce z książkami naukowymi znajdują się tytuły: {naukowe}")


def odnies_na_polke_przygodowe(przygodowe):
    print(f"Na półce z książkami przygodowymi znajdują się tytuły: {przygodowe}")


def odnies_na_polke_biograficzne(biograficzne):
    print(f"Na półce z książkami biograficznymi znajdują się tytuły: {biograficzne}")


book_list_naukowe = []
book_list_przygodowe = []
book_list_biograficzne = []

# dodawanie książek do listy
choice = 0
while choice != "NIE":
    print("Czy masz książkę do oddania?\nwpisz tak lub nie")
    choice = input().upper()
    if choice == "tak".upper():
        title = podaj_tytuł()
        genre = podaj_gatunek()
        book = Book(title, genre)
        if genre == "naukowe":
            book_list_naukowe.append(f"{book.title}")
            if len(book_list_naukowe) == 5:
                odnies_na_polke_naukowe(book_list_naukowe)
        if genre == "przygodowe":
            book_list_przygodowe.append(f"{book.title}")
            if len(book_list_przygodowe) == 5:
                odnies_na_polke_przygodowe(book_list_przygodowe)
        if genre == "biograficzne":
            book_list_biograficzne.append(f"{book.title}")
            if len(book_list_biograficzne) == 5:
                odnies_na_polke_biograficzne(book_list_biograficzne)
    if choice == "nie".upper():
        break

print(f"Książki naukowe: {book_list_naukowe}")
print(f"Książki przygodowe: {book_list_przygodowe}")
print(f"Książki biograficzne: {book_list_biograficzne}")
