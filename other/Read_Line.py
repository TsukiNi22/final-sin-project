from serial import *

#initialisation des listes
liste_distance = []

# Fonction pour la récupération des données série venant de la carte Arduino
ser = Serial('COM3', 9600)
print("Reset Arduino")

# Essai pour une succession de 20 lignes de données
line1 = ser.readline() 
print(line1)

ser.close()