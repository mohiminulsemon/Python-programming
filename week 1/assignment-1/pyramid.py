import pyautogui

x = int(input())
for i in range(x):
    for j in range(0,i+1):
        pyautogui.write("#",interval=0.25)
    pyautogui.write("\n")
