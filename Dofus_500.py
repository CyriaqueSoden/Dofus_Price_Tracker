from data import *
from PIL import Image
from pyautogui import *
import pyautogui
import time
import keyboard
import win32api
import win32con
import pytesseract
import os
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
        time.sleep(0.2)
    analyse = pytesseract.image_to_string(
        Image.open(pathImg)).replace(" ", "")
    time.sleep(0.1)
    if analyse == "":
        dataKamas.append("0")
    else:
        dataKamas.append(analyse)
    if os.path.exists(pathImg):
        os.remove(pathImg)


def uploadData(i):
    mycursor.execute("INSERT INTO item_price (name ,price1 ,price10 ,price100 ) VALUES ('" + noSpaceListName[i] + "'," +
                     dataKamas[0] + "," + dataKamas[1] + "," + dataKamas[2] + ")")


def didItemLoad():
    while color == pyautogui.pixel(*listCoo["KamasLoadItem"].getCoordinates())[0]:
        count = + 1
        time.sleep(0.2)
        if count > 20:
            return
    else:
        time.sleep(0.1)
        return


def isItRightItem(i):
    while True:
        im = pyautogui.screenshot(
            region=(*listCoo["openItem"].getCoordinates(), *dimensionScreen2.getCoordinates()))
        pathImg = r'C:\Users\maste\Pictures\bot\verif.png'
        im.save(pathImg)
        while not os.path.exists(pathImg):
            time.sleep(0.2)
        analyse = pytesseract.image_to_string(Image.open(pathImg))
        time.sleep(0.1)
        print(analyse.lower())
        print(listCoo["openItem"].getCoordinates())
        if analyse.lower().strip() == i.lower().strip():
            return
        else:
            listCoo["openItem"].next()
            # for i in listRegion:
            #     listRegion[i].next()


if __name__ == "__main__":
    for idi, i in enumerate(listName):
        click(*listCoo["ini"].getCoordinates())
        click(*listCoo["croixDelete"].getCoordinates())
        click(*listCoo["barreDeRecherche"].getCoordinates())
        color = pyautogui.pixel(*listCoo["KamasLoadItem"].getCoordinates())[0]
        keyboard.write(i)
        didItemLoad()
        isItRightItem(i)
        click(*listCoo["openItem"].getCoordinates())
        time.sleep(0.1)
        for idy, y in enumerate(listRegion):
            screenShot(idy, y, idi)
        uploadData(idi)
        click(*listCoo["croixDelete"].getCoordinates())
        for n in range(len(dataKamas)):
            dataKamas = []
        listCoo["openItem"].reset()
