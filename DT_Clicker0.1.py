import pyautogui
import time
import keyboard


while True:
#Functions
#__________________________________________________________________________
#Multipoint clicker
    def case_1():
        time.sleep(1)
        print("Choose point A")
        while True:
            if keyboard.is_pressed('enter'):
                point_a = pyautogui.position()
                print(f"Coordinates for A: {point_a}")
                break

        time.sleep(1)

        print("Choose point B")
        while True:
            if keyboard.is_pressed('enter'):
                point_b = pyautogui.position()
                print(f"Coordinates for B: {point_b}")
                break

        while True:
            if keyboard.is_pressed('F5'):
                break

            pyautogui.moveTo(point_a[0], point_a[1])
            pyautogui.click()

            if keyboard.is_pressed('F5'):
                break

            pyautogui.moveTo(point_b[0], point_b[1])
            pyautogui.click()

            if keyboard.is_pressed('F5'):
                break
#Single point clicker
    def case_2():
        while True:
            if keyboard.is_pressed('F5'):
                break

            pyautogui.click()

            if keyboard.is_pressed('F5'):
                break
#Quit
    def case_3():
        quit()
#______________________________________________________________________________
#Main code
    print(f"______ _____ _____ _ _      _             ")
    print(f"|  _  \_   _/  __ \ (_)    | |            ")
    print(f"| | | | | | | /  \/ |_  ___| | _____ _ __ ")
    print(f"| | | | | | | |   | | |/ __| |/ / _ \ '__|")
    print(f"| |/ /  | | | \__/\ | | (__|   <  __/ |   ")
    print(f"|___/   \_/  \____/_|_|\___|_|\_\___|_|   ")
    print(f"")
    print(f"1: Multipoint clicker")
    print(f"2:  Single point clicker")
    print(f"3: Quit")

    options = {
        1: case_1,
        2: case_2,
        3: case_3
    }

    selected_option = int(input("Choose option: "))

    options[selected_option]()
