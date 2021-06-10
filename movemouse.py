import win32api, win32con
import time
import keyboard  # using module keyboard

def poker():
    pos = win32api.GetCursorPos()
    print(pos)
    print('Width:', win32api.GetSystemMetrics(0))
    maxwidth = win32api.GetSystemMetrics(0)
    print('Height:', win32api.GetSystemMetrics(1))
    maxheight = win32api.GetSystemMetrics(1)
    x = pos[0]
    print('x = ',x)
    while True:

        x += 100
        print(x)
        if x >= maxwidth:
            x = 0
        time.sleep(3)
        win32api.SetCursorPos((x, pos[1]))
        if keyboard.is_pressed('q'):  # if key 'q' is pressed
            print('You Pressed A Key!')
            break  # finishing the loop
    #


poker()