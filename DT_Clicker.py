import pyautogui
import time
import keyboard
print("Choose point A")
while True:
    if keyboard.is_pressed('enter'):
        point_a = pyautogui.position()
        print(f"Coordinates for A: {point_a}")
        break

time.sleep(2)

print("Choose point B")
while True:
    if keyboard.is_pressed('enter'):
        point_b = pyautogui.position()
        print(f"Coordinates for B: {point_b}")
        break

while True:
    if keyboard.is_pressed('q'):
        break

    pyautogui.moveTo(point_a[0], point_a[1])
    pyautogui.click()

    pyautogui.moveTo(point_b[0], point_b[1])
    pyautogui.click()

    if keyboard.is_pressed('q'):
        break
