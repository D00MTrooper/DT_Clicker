import pyautogui
import time
import keyboard
print("Kliknij w miejsce A")
while True:
    if keyboard.is_pressed('enter'):
        point_a = pyautogui.position()
        print(f"Współrzędne punktu A: {point_a}")
        break

time.sleep(2)

print("Kliknij w miejsce B")
while True:
    if keyboard.is_pressed('enter'):
        point_b = pyautogui.position()
        print(f"Współrzędne punktu B: {point_b}")
        break

while True:
    if keyboard.is_pressed('q'):
        break
    # przesunięcie kursora na punkt A
    pyautogui.moveTo(point_a[0], point_a[1])
    # kliknięcie lewego przycisku myszy
    pyautogui.click()
    # przesunięcie kursora na punkt B
    pyautogui.moveTo(point_b[0], point_b[1])
    # kliknięcie lewego przycisku myszy
    pyautogui.click()
    if keyboard.is_pressed('q'):
        break
