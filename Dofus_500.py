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


def screenShot(nb, y, i):
    im = pyautogui.screenshot(
        region=(*listRegion[y].getCoordinates(), *dimensionScreen.getCoordinates()))
    pathImg = r'C:\Users\maste\Pictures\bot\screen' + str(i) + str(nb) + '.png'
    im.save(pathImg)
    while not os.path.exists(pathImg):
        time.sleep(0.01)
    analyse = pytesseract.image_to_string(
        Image.open(pathImg)).replace(" ", "")
    time.sleep(0.1)
    if analyse == "":
        dataKamas.append("0")
    else:
        dataKamas.append(analyse)
    # if os.path.exists(pathImg):
    #     os.remove(pathImg)


def uploadData(i):
    mycursor.execute("INSERT INTO item_price (name ,price1 ,price10 ,price100 ) VALUES ('" + noSpaceListName[i] + "'," +
                     dataKamas[0] + "," + dataKamas[1] + "," + dataKamas[2] + ")")


def didItemLoad(where):
    while color == pyautogui.pixel(*where)[0]:
        count = + 1
        time.sleep(0.01)
        if count > 20000:
            return
    else:
        time.sleep(0.1)
        print(color)
        return


def isItRightItem(i):
    while True:
        im = pyautogui.screenshot(
            region=(*listCoo["openItem"].getCoordinates(), *dimensionScreen2.getCoordinates()))
        pathImg = r'C:\Users\maste\Pictures\bot\verif.png'
        im.save(pathImg)
        while not os.path.exists(pathImg):
            time.sleep(0.01)
        analyse = pytesseract.image_to_string(Image.open(pathImg))
        time.sleep(0.1)
        if analyse.lower().strip() == i.lower().strip():
            return
        else:
            listCoo["openItem"].next()
            for y in listRegion:
                listRegion[y].next()


if __name__ == "__main__":
    for idi, i in enumerate(listName):
        click(*listCoo["ini"].getCoordinates())
        click(*listCoo["croixDelete"].getCoordinates())
        click(*listCoo["barreDeRecherche"].getCoordinates())
        color = pyautogui.pixel(*listCoo["KamasLoadItem"].getCoordinates())[0]
        keyboard.write(i)
        didItemLoad(listCoo["KamasLoadItem"].getCoordinates())
        isItRightItem(i)
        color = pyautogui.pixel(*listRegion["1"].getCoordinates())[0]
        print(color)
        click(*listCoo["openItem"].getCoordinates())
        didItemLoad(listRegion["1"].getCoordinates())
        for idy, y in enumerate(listRegion):
            screenShot(idy, y, idi)
        uploadData(idi)
        click(*listCoo["croixDelete"].getCoordinates())
        for n in range(len(dataKamas)):
            dataKamas = []
        listCoo["openItem"].reset()
