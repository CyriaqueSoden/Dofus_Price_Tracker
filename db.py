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
    "CREATE TABLE item_price (name varchar(255) ,price1 int , price10 int , price100 int ,date_registered TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP)")
