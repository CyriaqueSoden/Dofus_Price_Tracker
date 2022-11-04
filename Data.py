import mysql.connector
import coordinate as co

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


clicks = {"ini": (116, 8), "croixDelete": (666, 255), "barreDeRecherche": (
    538, 248), "openItem": (913, 284), "KamasLoadItem": (1030, 276)}

listCoo = {}
# creation listCoo
for i in clicks:
    listCoo[i] = co.Coordinate(clicks[i][0], clicks[i][1])


regionScreen = {"1": 336, "10": 400, "100": 465}

listRegion = {}
# creation listRegion
for i in regionScreen:
    listRegion[i] = co.Coordinate(1250, regionScreen[i])

dimensionScreen = co.Coordinate(122, 32)