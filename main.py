import pyautogui
import time

from process.paste import paste
from process import grabber
from process import modifier
from process.checker import bandit

print("Let's Find The Bandits...")
auto = pyautogui

time.sleep(2)
auto.moveTo(86,664)
auto.click()
time.sleep(3)

def followers():
    time.sleep(1)
    auto.moveTo(1042,234)
    auto.click()
    time.sleep(3)

    auto.moveTo(1115, 757)
    time.sleep(3)
    auto.mouseDown(button='left')
    time.sleep(330)
    auto.mouseUp(button='left')
    time.sleep(3)

    auto.hotkey("ctrl", "a")
    time.sleep(2)
    auto.hotkey("ctrl", "c")

    time.sleep(2)
    paste()
    grabber.grabFollowers()
    modifier.modFollowers()

    auto.moveTo(1099, 396)
    auto.click()

def following():
    time.sleep(1)
    auto.moveTo(1175, 233)
    auto.click()
    time.sleep(3)

    auto.moveTo(1115, 757)
    time.sleep(3)
    auto.mouseDown(button='left')
    time.sleep(240)
    auto.mouseUp(button='left')
    time.sleep(3)

    auto.hotkey("ctrl", "a")
    time.sleep(2)
    auto.hotkey("ctrl", "c")

    time.sleep(2)
    paste()
    grabber.grabFollowing()
    modifier.modFollowing()

    auto.moveTo(1099, 396)
    auto.click()

followers()
auto.moveTo(1296,413)
auto.click()
following()
auto.moveTo(1888,16)
auto.click()
bandit()

print("Process done...")