import keyboard as clavier
import tools.Tools as tl
import pygetwindow as gw
import mouse as souris
from customtkinter import *
from time import *
from screeninfo import get_monitors
import webbrowser
import os
import sys
from pycaw.pycaw import *
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL

# Récupérer la taille de la fenêtre :
Fenetre_Width ,Fenetre_Height = tl.GET_SCREEN_DIMENSION()

# Récupérer l'appareil pour modifier le volume
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

# Déclarer l'état du Volume (Mute/UnMute)
Mute = False

Value_Dico = {}
def REDIRECT(Id,Value):
    global Value_Dico
    global Fenetre_Width
    global Fenetre_Height
    global Mute
    Key = Value_Dico.keys()
    if not Id in Key or Value_Dico[Id] != Value:
        Value_Dico[Id] = Value
        if 'A' in Id or int(Value) > 0:
            Value = int(Value)
            with open('setting\\Actual.txt', 'r') as fichier:
                Ligne = fichier.readlines()
            for Item in Ligne:
                Item_Split = Item.split(':')
                if Item_Split[2][:-1] != 'None' and (('f' in Id and (('A' in Id and Item_Split[1] == Id) or (not 'A' in Id and Item_Split[1] == Id))) or ('A' in Id and Item_Split[1] == Id) or ('N' in Id and Item_Split[1] == Id[1:])):
                    with open(f'script\\{Item_Split[2][:-1]}.txt', 'r') as fichier:
                        Ligne_1 = fichier.readlines()
                        Ligne_1.pop(0)
                    for Item_1 in Ligne_1:
                        if eval(Item_1)['Name'].encode('latin-1').decode('utf-8') == 'Inverser le potentiometre':
                            Value = 100 - Value
                    for Item_1 in Ligne_1:
                        Commande_Item = eval(Item_1)
                        Commande_Name = Commande_Item['Name'].encode('latin-1').decode('utf-8')

# ------------------------ BOUTONS ------------------------

                        #     ------------Clavier------------
                        # Appuyer et Relacher
                        if Commande_Name == 'Appuyer et relacher _':
                            Touche = Commande_Item['Parametre'][0]
                            if Touche != 'None':
                                Appuyer_Et_Relacher(Touche)
                        
                        # Appuyer
                        elif Commande_Name == 'Appuyer _':
                            Touche_A_Appuyer = Commande_Item['Parametre'][0]
                            if Touche_A_Appuyer != 'None':
                                Appuyer(Touche_A_Appuyer)
                        
                        # Relacher
                        elif Commande_Name == 'Relacher _':
                            Touche_A_Relacher = Commande_Item['Parametre'][0]
                            if Touche_A_Relacher != 'None':
                                Relacher(Touche_A_Relacher)

                        # Ecrire
                        elif Commande_Name == 'Ecrire _':
                            Phrase_A_Ecrire = Commande_Item['Parametre'][0]
                            if Phrase_A_Ecrire != 'None':
                                Ecrire(Phrase_A_Ecrire)

                        # Est presser ?
                        elif Commande_Name == '_ est presser':
                            Touche_A_Analyser = Commande_Item['Parametre'][0]
                            if Touche_A_Analyser != 'None':
                                Touche_Pressee(Touche_A_Analyser)
                        #Quand appuyee
                        elif Commande_Name == 'Quand _ est appuyee':
                            Touche_A_Attendre = Commande_Item['Parametre'][0]
                            if Touche_A_Attendre != 'None':
                                Quand_Appuyee(Touche_A_Attendre)

                        #     ------------Souris------------
                        # Clic
                        elif 'Clic' in Commande_Name:
                            cmd = 'left'
                            if Commande_Item['Parametre'][0] == 'Droit':
                                cmd = 'right'                                
                            Clic(cmd)
                            if 'Double' in Commande_Name:
                                Clic(cmd)
                        
                        #     ------------Navigateur------------
                        #Ouvrir une page web
                        elif Commande_Name == 'Ouvrir la page web _':
                            url = Commande_Item['Parametre'][0]
                            if url != 'None':
                                Ouvrir_Une_Page(url)

                        #     ------------OS------------
                        #Ouvrir une application
                        elif Commande_Name == 'Lancer l\'application _':
                            application = Commande_Item['Parametre'][0]
                            if application != 'None':
                                Lancer_Application(application)

                        #Couper le song et remettre le volume
                        elif Commande_Name == 'Activer/Desactiver le volume':
                            Mute = not Mute
                            if Mute:
                                Desactiver_Le_Volume()
                            else:
                                Activer_Le_Volume()

                        #     ------------Instructions------------
                        #Attendre
                        elif Commande_Name == 'Attendre _ secondes':
                            temps = Commande_Item['Parametre'][0]
                            if temps != 'None':
                                Attendre(int(temps))
# ------------------------\ FIN BOUTONS \------------------------



# ------------------------ POTENTIOMETRES ------------------------

                        elif Commande_Name == 'Déplacer la souris vers _ de _ px':
                            direction = Commande_Item['Parametre'][0]
                            distance = int(Commande_Item['Parametre'][1])
                            position_du_curseur = list(souris.get_position()) #Récupère la position du curseur sous forme de list [x,y]
                            x = int(position_du_curseur[0])
                            y = int(position_du_curseur[1])

                            if direction != None and distance != None:
                                if direction == "la Gauche":
                                     souris.move(x-distance, y)
                                elif direction == "la Droite":
                                     souris.move(x+distance,y)
                                elif direction == "le Haut":
                                     souris.move(x,y+distance)
                                elif direction == "le Bas":
                                     souris.move(x,y-distance)

                        elif Commande_Name == 'Déplacer la souris _':
                            Axe = Commande_Item['Parametre'][0]
                            position_du_curseur = list(souris.get_position()) #Récupère la position du curseur sous forme de list [x,y]
                            x = int(position_du_curseur[0])
                            y = int(position_du_curseur[1])
                            
                            Largeur = Fenetre_Width/100 * Value
                            Hauteur = Fenetre_Height/100 * Value

                            if Axe == 'Horizontalement':
                                souris.move(Largeur,y)
                            elif Axe == 'Verticalement':
                                souris.move(x,Hauteur)
                        
                        elif Commande_Name == 'Gérer le son':
                            Regler_Le_Volume(Value)
# ------------------------\ FIN DES POTENTIOMETRES \------------------------
# ------------------------ FONCTIONS DES BOUTONS ------------------------

#     ------------Clavier------------

def Appuyer_Et_Relacher(touche): #Presser et Relacher la touche
    clavier.press_and_release(touche)

def Appuyer(touche): # Presser la touche
    clavier.press(touche)

def Relacher(touche): # Relacher la touche
    clavier.release(touche)

def Ecrire(phrase): # Ecrire la phrase
    clavier.write(phrase)  

def Touche_Pressee(touche): # Detecter si la touche est préssée
    clavier.is_pressed(touche)

def Quand_Appuyee(touche): # Quand la touche est appuyée
    on_press_event(touche)

#     ------------Souris------------

def Clic(typeDeClique):
    souris.click(typeDeClique)

def Deplacer_Vers(direction, nombredePX): # Déplacer le curseur de quelques pixels
    position = souris.get_position()


def Deplacer_En(x, y): # Déplacer le curseur à des coordonnées
    souris.move(x, y)

#     ------------Navigateur------------

def Ouvrir_Une_Page(lien): # Ouvrir une page web
    webbrowser.open(lien)

#     ------------OS------------
def Lancer_Application(exe):
    os.startfile(exe)

# Desactiver le volume
def Desactiver_Le_Volume():
    volume.SetMute(1, None)

# Activer le volume
def Activer_Le_Volume():
    volume.SetMute(0, None)
#     ------------Instruction------------

def Tant_Que(variable1, condition, variable2): # while
    return

def Si(): # If
    return

def Attendre(temps): #Attendre
    sleep(temps)
# ------------------------\ FIN DES FONCTIONS DES BOUTONS \------------------------


# ------------------------ FONCTIONS DES POTENTIOMETRES ------------------------

#     ------------Clavier------------

def Deplacer_Vers(direction, nombredePX): # Déplacer le curseur de quelques pixels
    position = souris.get_position()
#     ------------Souris------------

#     ------------Navigateur------------

#     ------------OS------------
# Modifie le volume (de 0 à 100)
def Regler_Le_Volume(nouveau_volume):
    # Convertit la variable de volume en une valeur entre 0 et 1
    new_volume_scalar = nouveau_volume / 100.0

    # Définit le nouveau volume
    volume.SetMasterVolumeLevelScalar(new_volume_scalar, None)
    print(f"Volume set to: {nouveau_volume}%")
#     ------------Instruction------------

# ------------------------\ FIN DES FONCTIONS DES POTENTIOMETRES \------------------------


class Exit_Redirect:
    def init(self):
        sys.exit()