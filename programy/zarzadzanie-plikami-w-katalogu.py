import os

def wyswietl_menu():
    print("Wybierz operację:")
    print("1. Wyświetl zawartość katalogu")
    print("2. Utwórz nowy plik")
    print("3. Odczytaj zawartość pliku")
    print("4. Edytuj plik")
    print("5. Usuń plik")
    print("6. Wyjdź z programu")

def wyswietl_zawartosc():
    path = os.getcwd()
    print(f"Zawartość katalogu {path}:")
    for file in os.listdir(path):
        print(file)

def utworz_plik():
    nazwa_pliku = input("Podaj nazwę pliku: ")
    with open(nazwa_pliku, 'w') as f:
        print(f"Plik {nazwa_pliku} został utworzony.")

def odczytaj_plik():
    nazwa_pliku = input("Podaj nazwę pliku: ")
    try:
        with open(nazwa_pliku, 'r') as f:
            print(f"Zawartość pliku {nazwa_pliku}:")
            print(f.read())
    except FileNotFoundError:
        print("Plik nie istnieje")

def edytuj_plik():
    nazwa_pliku = input("Podaj nazwę pliku: ")
    try:
        with open(nazwa_pliku, 'a') as f:
            tresc = input("Wpisz tekst, który chcesz dodać do pliku: ")
            f.write(tresc + '\n')
            print(f"Tekst został dodany do pliku {nazwa_pliku}.")
    except FileNotFoundError:
        print("Plik nie istnieje")

def usun_plik():
    nazwa_pliku = input("Podaj nazwę pliku: ")
    try:
        os.remove(nazwa_pliku)
        print(f"Plik {nazwa_pliku} został usunięty.")
    except FileNotFoundError:
        print("Plik nie istnieje")

def main():
    while True:
        wyswietl_menu()
        wybor = input("Wprowadź numer operacji (1/2/3/4/5/6): ")

        if wybor == '1':
            wyswietl_zawartosc()
        elif wybor == '2':
            utworz_plik()
        elif wybor == '3':
            odczytaj_plik()
        elif wybor == '4':
            edytuj_plik()
        elif wybor == '5':
            usun_plik()
        elif wybor == '6':
            print("Koniec programu")
            break
        else:
            print("Niepoprawny wybór")

if __name__ == "__main__":
    main()
