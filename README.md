Dofus Price Tracker

Ce projet est un bot pour le jeu Dofus. Il permet de suivre les prix des objets dans le marché.
Prérequis

-Python 3.x
-Tesseract OCR : https://github.com/UB-Mannheim/tesseract/wiki

Installation et mise en place

-Clonez le repository
-Installez les bibliothèques Python avec la commande pip install -r requirements.txt
-Créé une base de donnée MySQL
-Dans le fichier config.py mettez les informations de votre base de donnée (4-9) ainsi que les objets que vous souhaitez suivre (13)
-Lancez le fichier db.py avec la commande python db.py
-Changer les coordonées si nécessaire (voir Coordonnées)

Utilisation

Mettre Dofus en plein écran (nécessaire seulement avec les coordonnées que j'ai fait) ,lancer main.py et attendre que le programme boucle sur tous les items de la liste.

Coordonnées

Les coordonnées sont les pixels sur les quels le bot clique ou prend des screenshots. Etant donnée que la position de l'hud de dofus ne change pas de facon proportionnel a la résolution de l'écran(du moins d'apres mes tests) il faut les definire a la mains. Je l'ai fait pour 2 écrans 2560x1440 et 1920x1200.
Deja que pour moi c'était giga chiant alors que je sais a quoi chaque coordonnées correspondents alors pour quelqu'un qui essaie de lire le fichier main HF.
