import os
import time
from datetime import datetime
import pyautogui 

# Screen Size => width=1920, height=1080

while True:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time(work) =", current_time)
    time.sleep(3)
    pyautogui.moveTo(950,910)
    pyautogui.click()
    time.sleep(2)
    pyautogui.moveTo(950,890)
    pyautogui.click()
    time.sleep(2)
    pyautogui.moveTo(850,390)
    pyautogui.click()
    time.sleep(2)
    pyautogui.moveTo(1020,325)
    pyautogui.click()
    time.sleep(2)
    pyautogui.moveTo(950,790)
    pyautogui.click()
    time.sleep(180)   #How long do you want to work
    
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time(wrest) =", current_time)
    time.sleep(3)
    pyautogui.moveTo(950,910)
    pyautogui.click()
    time.sleep(2)
    pyautogui.moveTo(950,890)
    pyautogui.click()
    time.sleep(2)
    pyautogui.moveTo(930,390)
    pyautogui.click()
    time.sleep(2)
    pyautogui.moveTo(1020,325)
    pyautogui.click()
    time.sleep(2)
    pyautogui.moveTo(950,790)
    pyautogui.click()
    time.sleep(720)   #How long do you want to rest
    
