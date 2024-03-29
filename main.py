from unidecode import unidecode
import re
from data import *
from PIL import Image
from pyautogui import *
import pyautogui
import time
import keyboard
import win32api
import win32con
import os
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    time.sleep(0.1)


def screenShot(y):
    if whatNumber(y) != y:
        dataKamas.append("0")
        return
    im = pyautogui.screenshot(
        region=(*listRegion[y].getCoordinates(), *dimensionScreenPrix.getCoordinates()))
    im.save(r'C:\Users\maste\Pictures\bot\scsc' + y + '.png')
    analyse = pytesseract.image_to_string(im).replace(" ", "").replace(",", "")
    if analyse == "":
        dataKamas.append("1")
    else:
        dataKamas.append(analyse)


def uploadData(i):
    mycursor.execute("INSERT INTO item_prices (name ,price1 ,price10 ,price100 ) VALUES ('" + noSpaceListName[i] + "'," +
                     dataKamas[0] + "," + dataKamas[1] + "," + dataKamas[2] + ")")


def didItemLoad(what, dim):
    analyse = ""
    count = 0
    while analyse == "":
        im = pyautogui.screenshot(
            region=(*what, *dim))
        analyse = pytesseract.image_to_string(im)
        time.sleep(0.05)
        count = + 1
        if count > 200:
            return False


def whatNumber(i):
    im = pyautogui.screenshot(
        region=(*listRegion[i].getRegOcrNumber(), *dimensionScreenPrix.getCoordinates()))
    analyse = pytesseract.image_to_string(im)
    analysePost = re.sub(r"\D", "", analyse)
    return str(analysePost)


def isItRightItem(i):
    count = 0
    while True:
        if count > 14:
            listCoo["openItem"].reset()
            for y in listRegion:
                listRegion[y].reset()
            return False
        im = pyautogui.screenshot(
            region=(*listCoo["openItem"].getCoordinates(), *dimensionScreenNom.getCoordinates()))
        analyse = pytesseract.image_to_string(im)
        if unidecode(analyse.lower().strip()) == i.lower().strip():
            return
        listCoo["openItem"].next()
        for y in listRegion:
            listRegion[y].next()
        count += 1


if __name__ == "__main__":
    for idi, i in enumerate(listName):
        click(*listCoo["ini"].getCoordinates())
        click(*listCoo["croixDelete"].getCoordinates())
        click(*listCoo["barreDeRecherche"].getCoordinates())
        keyboard.write(i)
        didItemLoad(listCoo["openItem"].getCoordinates(),
                    dimensionScreenNom.getCoordinates())
        isItRightItem(i)
        click(*listCoo["openItem"].getCoordinates())
        didItemLoad(listRegion["1"].getCoordinates(),
                    dimensionScreenPrix.getCoordinates())
        for idy, y in enumerate(listRegion):
            screenShot(y)
        uploadData(idi)
        click(*listCoo["croixDelete"].getCoordinates())
        dataKamas.clear()
        listCoo["openItem"].reset()
