from data import *

mycursor.execute("DROP TABLE item_prices")
mycursor.execute(
    "CREATE TABLE item_prices (name varchar(255) ,price1 int , price10 int , price100 int ,date_registered TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP)")
