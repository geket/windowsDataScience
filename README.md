# Dependencies

Before running `tryAgain.py`, you will need to install the pyautogui module using pip (pip install pyautogui), and you will also need to save two screenshots to the same directory as the script: move_copy.png, which shows the "Move" or "Copy" button in Windows Explorer, and try_again.png, which shows the "Try Again" button that appears when a move/copy operation fails.

This script uses the pyautogui module to search for the "Move" or "Copy" button and click it to start the process, and then continues to search for the "Try Again" button and click it whenever it appears. It uses a try-except block to catch the TypeError that is raised when locateCenterOnScreen() cannot find the specified image, and simply passes over it to continue searching.
