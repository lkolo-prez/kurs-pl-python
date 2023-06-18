import sqlite3

def polacz_baza(nazwa_pliku):
    """Funkcja do łączenia się z bazą danych SQLite"""
    conn = sqlite3.connect(nazwa_pliku)
    return conn

def pobierz_dane_zrodlo(conn):
    """Funkcja do pobierania danych z bazy źródłowej"""
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM przykladowa_tabela")
    return cursor.fetchall()

def zapisz_dane_docelowe(conn, dane):
    """Funkcja do zapisywania danych w bazie docelowej"""
    cursor = conn.cursor()
    cursor.executemany("INSERT INTO przykladowa_tabela VALUES (?, ?)", dane)
    conn.commit()

def main():
    # Łączenie z bazą danych źródłową
    zrodlo_conn = polacz_baza("zrodlo.db")

    # Pobieranie danych z bazy źródłowej
    dane = pobierz_dane_zrodlo(zrodlo_conn)

    # Zamykanie połączenia z bazą danych źródłową
    zrodlo_conn.close()

    # Łączenie z bazą danych docelową
    docelowe_conn = polacz_baza("docelowa.db")

    # Zapisywanie danych w bazie docelowej
    zapisz_dane_docelowe(docelowe_conn, dane)

    # Zamykanie połączenia z bazą danych docelową
    docelowe_conn.close()

    print("Migracja danych zakończona pomyślnie.")

if __name__ == "__main__":
    main()
