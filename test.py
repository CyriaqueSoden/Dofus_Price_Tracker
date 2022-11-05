from screeninfo import get_monitors
import csv
import mysql.connector
import pyautogui
import pipreqs

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="dofus_500"
)
mycursor = mydb.cursor()


print(pipreqs.__path__)
