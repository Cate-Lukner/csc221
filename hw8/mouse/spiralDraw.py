import pyautogui as pag
import time

time.sleep(5)
pag.click(266, 350)
distance = 300
change = 20

while distance > 0:
    pag.drag(distance, 0, duration=0.2)
    distance = distance - change
    pag.drag(0, distance, duration=0.2)
    pag.drag(-distance, 0, duration=0.2)
    distance = distance - change
    pag.drag(0, -distance, duration=0.2)
    
