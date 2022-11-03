import csv
import mysql.connector
from Dofus_500 import *

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="dofus_500"
)
mycursor = mydb.cursor()


clicks = {"ini": (116, 8), "croixDelete": (730, 255), "barreDeRecherche": (
    538, 248), "openItem": (913, 284), "KamasLoadItem": (1030, 276)}

for i in clicks:
    print(clicks[i])
