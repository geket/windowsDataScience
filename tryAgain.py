import time
import pyautogui

# Wait for user to start move/copy process
print("Please start the move/copy process in Windows Explorer")
while True:
    try:
        time.sleep(1)
        x, y = pyautogui.locateCenterOnScreen('move_copy.png')
        pyautogui.click(x, y)
        break
    except TypeError:
        pass

# Monitor the move/copy process
while True:
    try:
        time.sleep(1)
        x, y = pyautogui.locateCenterOnScreen('try_again.png')
        pyautogui.click(x, y)
    except TypeError:
        pass
