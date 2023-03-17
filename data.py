import mysql.connector
import coordinate as co

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="dofus_500"
)
mycursor = mydb.cursor()

# ne pas mettre de characters spéciaux ou d'accents 'Ailes de Moskito', , 'bois de kaerlier'
listName = ['ble']


if co.multiX == 2560 and co.multiY == 1440:
    regionScreen = {"1": (1250, 336), "10": (1250, 400), "100": (
        1250, 465)}
    clicks = {"ini": (116, 8), "croixDelete": (730, 255), "barreDeRecherche": (
        538, 248), "openItem": (860, 273)}
    dimensionScreenPrix = co.Coordinate(122, 32)
    dimensionScreenNom = co.Coordinate(315, 36)

elif co.multiX == 1920 and co.multiY == 1200:
    regionScreen = {"1": (922, 279), "10": (922, 337), "100": (922, 385)}
    clicks = {"ini": (116, 8), "croixDelete": (502, 209), "barreDeRecherche": (
        362, 208), "openItem": (611, 222)}
    dimensionScreenPrix = co.Coordinate(112, 28)
    dimensionScreenNom = co.Coordinate(255, 33)


count = 0
color = 0


dataKamas = []

noSpaceListName = []
# creation noSpaceListName
for i in listName:
    noSpaceListName.append(i.replace(" ", "_"))

[i.strip() for i in listName]


listCoo = {}
# creation listCoo
for i in clicks:
    listCoo[i] = co.Coordinate(clicks[i][0], clicks[i][1])


listRegion = {}
# creation listRegion
for i in regionScreen:
    listRegion[i] = co.Coordinate(regionScreen[i][0], regionScreen[i][1])
