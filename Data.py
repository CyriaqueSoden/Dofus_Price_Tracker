import mysql.connector
import coordinate as co

count = 0
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="dofus_500"
)
mycursor = mydb.cursor()

dataKamas = []
regionScreen = [336, 400, 465]
listName = ['galet rutilant', 'galet brasillant',
            'dolomite', 'substrat de bosquet', 'saphir', 'diamant']

noSpaceListName = []

for i in listName:
    noSpaceListName.append(i.replace(" ", "_"))

listCoo = {}
listRegion = {}
clicks = {"ini": (116, 8), "croixDelete": (730, 255), "barreDeRecherche": (
    538, 248), "openItem": (913, 284), "KamasLoadItem": (1030, 276)}

for i in clicks:
    listCoo[i] = co.Coordinate(clicks[i][0], clicks[i][1])

for i in regionScreen:
    listRegion[i] = co.Coordinate(1250, i)
