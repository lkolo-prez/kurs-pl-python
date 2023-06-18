import pyautogui
import time

def porusz_myszka():
    while True:
        # Pobierz aktualne współrzędne kursora myszy
        x, y = pyautogui.position()
        
        # Przesuń kursor myszy o 100 pikseli w prawo i 100 pikseli w dół
        pyautogui.moveTo(x + 10, y + 10, duration=0.5)

        # Odczekaj 15 sekund
        time.sleep(15)
        # Przesuń kursor myszy o 100 pikseli w lewo i 100 pikseli w góre
        pyautogui.moveTo(x - 10, y - 10, duration=0.5)
         # Odczekaj 15 sekund
        time.sleep(15)
if __name__ == "__main__":
    try:
        porusz_myszka()
    except KeyboardInterrupt:
        print("Program zakończony przez użytkownika")