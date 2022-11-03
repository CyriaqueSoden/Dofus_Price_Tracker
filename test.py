from screeninfo import get_monitors
import csv
import mysql.connector
import pyautogui

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="dofus_500"
)
mycursor = mydb.cursor()

while not 1 == 2:
    print(pyautogui.displayMousePosition())
