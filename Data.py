import mysql.connector
import coordinate as co


if co.multiX == 2560 and co.multiY == 1440:
    regionScreen = {"1": (1250, 336), "10": (1250, 400), "100": (
        1250, 465), "lot1": (1087, 333), "lot10": (1087, 399), "lot100": (1087, 465)}
    clicks = {"ini": (116, 8), "croixDelete": (730, 255), "barreDeRecherche": (
        538, 248), "openItem": (860, 273)}
    dimensionScreen = co.Coordinate(122, 32)
    dimensionScreen2 = co.Coordinate(315, 36)
    dimensionScreen3 = co.Coordinate(111, 42)

elif co.multiX == 1920 and co.multiY == 1200:
    regionScreen = {"1": 279, "10": 337, "100": 385}
    clicks = {"ini": (116, 8), "croixDelete": (502, 209), "barreDeRecherche": (
        362, 208), "openItem": (611, 222)}
    dimensionScreen = co.Coordinate(112, 28)
    dimensionScreen2 = co.Coordinate(255, 33)


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="dofus_500"
)
mycursor = mydb.cursor()

count = 0
color = 0

dataKamas = []
listName = ['diamant', 'saphir']
# 'galet brasillant'
noSpaceListName = []
# creation noSpaceListName
for i in listName:
    noSpaceListName.append(i.replace(" ", "_"))


listCoo = {}
# creation listCoo
for i in clicks:
    listCoo[i] = co.Coordinate(clicks[i][0], clicks[i][1])


listRegion = {}
# creation listRegion
for i in regionScreen:
    listRegion[i] = co.Coordinate(clicks[i][0], regionScreen[i])
