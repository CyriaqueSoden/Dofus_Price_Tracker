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

mycursor.execute(
    "SELECT * FROM item_price WHERE name = '" + noSpaceListName[0] + "'")
