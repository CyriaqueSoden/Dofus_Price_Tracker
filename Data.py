import mysql.connector
import coordinate as co
from screeninfo import get_monitors


multiX = get_monitors()[0].width
multiY = get_monitors()[0].height

if multiX == 2560 and multiY == 1440:
    regionScreen = {"1": 336, "10": 400, "100": 465}
    clicks = {"ini": (116, 8), "croixDelete": (666, 255), "barreDeRecherche": (
        538, 248), "openItem": (913, 284), "KamasLoadItem": (1030, 276)}
    dimensionScreen = co.Coordinate(122, 32)


elif multiX == 1920 and multiY == 1200:
    regionScreen = {"1": 279, "10": 337, "100": 385}
    clicks = {"ini": (116, 8), "croixDelete": (502, 209), "barreDeRecherche": (
        362, 208), "openItem": (611, 222), "KamasLoadItem": (850, 237)}
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
listName = ['galet rutilant', 'galet brasillant',
            'dolomite', 'substrat de bosquet', 'saphir', 'diamant']

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
    if multiX == 2560 and multiY == 1440:
        listRegion[i] = co.Coordinate(1250, regionScreen[i])
    else:
        listRegion[i] = co.Coordinate(922, regionScreen[i])
+55
