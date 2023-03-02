# Dofus_Price_Tracker

Description :

C'est un script qui permet de stocker dans une base de donnée les prix des items voulus par 1 / 10 / 100 , le but final étant de lier la base de donnée a un front end qui
fait des graphique sur la fluctuation du prix au cours du temps 

Mise en place : 

-Crée une base de donnée mySQL

-DL les requirements de requirements.txt

-DL Pytesseract (https://pypi.org/project/pytesseract/)

-Dans data.py changer 

      mydb = mysql.connector.connect(
          host="localhost",
          user="root",
          password="",
          database="dofus_500"
      )
      
-Lancer le fichier db.py

-Dans data.py ajouter les items qu'on veut traquer dans 

listName = ['Ailes de Moskito', 'Aile de Bourdard', ]

(ne pas mettre d'accents ou de caracteres speciaux)

-Prier que les coordonnées soit les memes sur son pc 

-Ouvrir un hotel de vente en pleine écran 

-Lancer Dofus_500.py

Coordonnées :
Etant donné que les coordonées ne sont pas proportionnelles a la résolution et change en fonction de la taille de l'hud il y a beaucoup de chances qu'elles ne fonctionnent 
pas sur les différentes configues .
