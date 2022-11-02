import mysql.connector
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


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="dofus_500"
)
mycursor = mydb.cursor()

dataKamas = []
regionScreen = [336, 400, 465]
listName = ['galet rutilant', 'galet brasillant',
            'dolomite', 'substrat de foret', 'substrat du bosquet', 'saphir', 'diamant']

noSpaceListName = []

for i in range(len(listName)):
    noSpaceListName.append((listName[i]).replace(" ", "_"))


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    time.sleep(0.5)


def screenShot(nb, y, i):
    im = pyautogui.screenshot(region=(1250, y, 122, 32))
    pathImg = r'C:\Users\maste\Pictures\bot\screen' + str(i) + str(nb) + '.png'
    im.save(pathImg)
    time.sleep(0.5)
    analyse = pytesseract.image_to_string(
        Image.open(pathImg)).replace(" ", "")
    if analyse == "":
        dataKamas.append("0")
    else:
        dataKamas.append(analyse)
    if os.path.exists(pathImg):
        os.remove(pathImg)


def uploadData(i):
    mycursor.execute("INSERT INTO item_price (name ,price1 ,price10 ,price100 ) VALUES ('" + noSpaceListName[i] + "'," +
                     dataKamas[0] + "," + dataKamas[1] + "," + dataKamas[2] + ")")


if __name__ == "__main__":
    for i in range(2):
        click(116, 8)
        click(730, 255)
        click(538, 248)
        keyboard.write(listName[i])
        time.sleep(2)
        click(913, 284)
        for y in range(len(regionScreen)):
            screenShot(y, regionScreen[y], i)
        uploadData(i)
        click(730, 255)
        for n in range(len(dataKamas)):
            dataKamas = []
