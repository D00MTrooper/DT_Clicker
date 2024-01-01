import pyautogui
import time
import keyboard
import mouse
import os


while True:
    def clear_screen():
        os.system('cls')

    # Call the function to clear the screen
    clear_screen()
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
#Record mouse
    def case_3():
        print("Press 'R' to start recording / press 'P' to end recording")
        keyboard.wait('R')  # Wait for the 'R' key to be pressed
        print('Recording....')

        events = []
        recording = True

        def on_mouse_event(event):
            nonlocal recording
            if recording:
                events.append(event)

        mouse.hook(on_mouse_event)

        while not keyboard.is_pressed('P'):
            pass  # Wait for the right mouse button to be pressed

        recording = False  # Stop recording
        mouse.unhook(on_mouse_event)

        print('Movement has been recorded')

        print('Press Enter to play the record')
        keyboard.wait('enter')  # Wait for the Enter key to be pressed
        mouse.play(events[:-1])  # Play the recorded events, excluding the last one

        events.clear()
        print('Recording cleared')

#Quit
    def case_4():
        quit()
#______________________________________________________________________________
#Main code
    print(f"______ _____ _____ _ _      _             ")
    print(f"|  _  \_   _/  __ \ (_)    | |            ")
    print(f"| | | | | | | /  \/ |_  ___| | _____ _ __ ")
    print(f"| | | | | | | |   | | |/ __| |/ / _ \ '__|")
    print(f"| |/ /  | | | \__/\ | | (__|   <  __/ |   ")
    print(f"|___/   |_|  \____/_|_|\___|_|\_\___|_|   ")
    print(f"")
    print(f"1: Multipoint clicker")
    print(f"2:  Single point clicker")
    print(f"3:  Record mouse ")
    print(f"4: Quit")

    options = {
        1: case_1,
        2: case_2,
        3: case_3,
        4: case_4
    }

    try:
        selected_option = int(input("Choose option: ").strip())
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        continue  # Restart the loop

    if selected_option in options:
        options[selected_option]()
    else:
        print("Invalid option. Please choose a valid option.")
