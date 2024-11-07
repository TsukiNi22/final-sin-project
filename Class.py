import serial.tools.list_ports as liste_des_ports 
import tools.Tools as tl
import keyboard as kb
import Redirect as re
from customtkinter import *
from fractions import *
from tools.langages import *
from copy import *
from screeninfo import get_monitors
from time import sleep
from PIL import Image
import threading
import serial
import sys
import os

Widht ,Height = tl.GET_SCREEN_DIMENSION()

Ratio = Height/1080
Ratio_Percent = (Ratio-480/1080)*1/(1-(480/1080))
Char_Limite = 25

with open('txt\\Dev_Parametre.txt', 'r') as file:
    Dico = eval(file.read())

Boutton_Factice_List = Dico['Boutton_Factice']
if Dico['Ratio_Force'] != None:
    Ratio = Dico['Ratio_Force']
    Ratio_Percent = (Ratio-480/1080)*1/(1-(480/1080))

class Error:

    def __del__(self):
        pass

    def __init__(self, Master, H, L):
        self.Master = Master
        self.Msg = ''
        self.L = L
        self.H = H
        self.Open = False

    def POP_UP(self, Msg):
        
        if not self.Open:
            self.Open = True
            self.Msg = Msg

            def CLOSE():
                self.Close_Button.destroy()
                self.Frame.destroy()
                self.Open = False

            Police = 'Arial'

            self.Frame = CTkFrame(self.Master,fg_color='black',border_color='White',border_width=2*Ratio,width=300*Ratio,height=150*Ratio,corner_radius=5)
            self.Frame.place(x=self.L/2-300*Ratio/2,y=self.H/2-150*Ratio/2)
            self.Txt = CTkLabel(self.Frame,fg_color='transparent',text=self.Msg,text_color='red',height=25*Ratio,width=75*Ratio,corner_radius=10,font=(Police,round(30*Ratio)))
            self.Txt.place(x=32.5*Ratio,y=20*Ratio)
            self.Close_Button = CTkButton(self.Master,fg_color='red',text='X',hover_color='#870909',bg_color='transparent',height=15*Ratio,width=15*Ratio,corner_radius=10,font=(Police,round(25*Ratio)-(5-5*(Ratio_Percent))),command=CLOSE)
            self.Close_Button.place(x=self.L/2+300*Ratio/2-32.5*Ratio,y=self.H/2-150*Ratio/2-35*Ratio)

    def RESIZE(self, Widht_Ratio, Height_Ratio):
        if Widht_Ratio < Height_Ratio:
            Mult = Widht_Ratio
        else:
            Mult = Height_Ratio
        Police = 'Arial'
        self.Frame.configure(width=300*Ratio*Widht_Ratio,height=150*Ratio*Height_Ratio)
        self.Frame.place(x=(self.L/2-300*Ratio/2)*Widht_Ratio,y=(self.H/2-150*Ratio/2)*Height_Ratio)
        self.Txt.configure(height=25*Ratio*Widht_Ratio,width=75*Ratio*Height_Ratio,font=(Police,round(30*Ratio*Mult)))
        self.Txt.place(x=32.5*Ratio*Widht_Ratio,y=20*Ratio*Height_Ratio)
        self.Close_Button.configure(height=15*Ratio*Widht_Ratio,width=15*Ratio*Height_Ratio,font=(Police,round(30*Ratio*Mult)))
        self.Close_Button.place(x=(self.L/2+300*Ratio/2-32.5*Ratio)*Widht_Ratio,y=(self.H/2-150*Ratio/2-35*Ratio)*Height_Ratio)

class Operation_Is_Running:

    def __del__(self):
        pass

    def __init__(self, Master, H, L):
        self.Master = Master
        self.H = H
        self.L = L
        self.Open = False

    def CREATE_FRAME(self):
        if not self.Open:
            self.Open = True
            def WHILE():
                try:
                    Time_Delay = 0.5
                    while True:
                        sleep(Time_Delay)
                        self.Txt.configure(text=Phrase_Chargement + '.')
                        sleep(Time_Delay)
                        self.Txt.configure(text=Phrase_Chargement + '..')
                        sleep(Time_Delay)
                        self.Txt.configure(text=Phrase_Chargement + '...')
                        sleep(Time_Delay)
                        self.Txt.configure(text=Phrase_Chargement)
                except:
                    pass
            While = threading.Thread(target=WHILE)

            self.Txt = CTkLabel(self.Master,fg_color='#2D2D2D',bg_color='#2D2D2D',text=Phrase_Chargement,text_color='white',height=25*Ratio,width=75*Ratio,font=('Arial',round(40*Ratio)))
            self.Txt.place(x=(self.L/2-100)*Ratio,y=(self.H/2)*Ratio)

            While.start()

    def DESTROY_FRAME(self):
        self.Txt.destroy()
        self.Open = False

    def RESIZE(self, Widht_Ratio, Height_Ratio):
        if Widht_Ratio < Height_Ratio:
            Mult = Widht_Ratio
        else:
            Mult = Height_Ratio
        self.Txt.configure(height=25*Ratio*Widht_Ratio,width=75*Ratio*Height_Ratio,font=('Arial',round(40*Ratio*Mult)))
        self.Txt.place(x=((self.L/2-100)*Ratio)*Widht_Ratio,y=((self.H/2)*Ratio)*Height_Ratio)

class Save_Preset:

    def __del__(self):
        pass

    def __init__(self, Master, H, L):
        self.Master = Master
        self.H = H
        self.L = L
        self.Name = 'None'
        self.Open = False

    def CREATE_FRAME(self):

        if not self.Open:
            self.Open = True
            
            def CLOSE():
                self.Frame.destroy()
                self.Close_Button.destroy()
                self.Open = False

            def SAVE():
                self.Name = self.File_Name.get("0.0", "end")[:-1]
                Fuck_It = False
                if not os.path.isfile(tl.GET_ABSOLUTE_PATH(f'setting\\{self.Name}.txt')):
                    try:
                        with open(tl.GET_ABSOLUTE_PATH(f'setting\\{self.Name}.txt'), 'w') as fichier:
                            pass
                        os.remove(tl.GET_ABSOLUTE_PATH(f'setting\\{self.Name}.txt'))
                    except:
                        self.File_Name.delete("0.0", "end")
                        self.File_Name.insert("0.0", Phrase_Nom_Invalide)
                        Fuck_It = True
                if not Fuck_It:
                    if self.Name == 'Actual':
                        self.File_Name.delete("0.0", "end")
                        self.File_Name.insert("0.0", Phrase_Prenez_Un_Autre_Nom)
                    elif '\n' in self.Name or self.Name == '': #Si le nom du fichier n'existe pas ou contient un retour a la ligne
                        self.File_Name.delete("0.0", "end")
                        self.File_Name.insert("0.0", Phrase_Nom_Invalide)
                    elif os.path.isfile(tl.GET_ABSOLUTE_PATH(f'setting\\{self.Name}.txt')): #Si le nom du fichier est deja pris
                        self.File_Name.delete("0.0", "end")
                        self.File_Name.insert("0.0", Phrase_Fichier_Existe_Deja)
                    else:
                        with open(tl.GET_ABSOLUTE_PATH('setting\\Actual.txt'), 'r') as fichier:
                            Ligne = fichier.readlines()
                        with open(tl.GET_ABSOLUTE_PATH(f'setting\\{self.Name}.txt'), 'w') as fichier:
                            fichier.writelines(Ligne)
                        CLOSE()

            Txt_Size = round(20*Ratio)
            Police = 'Arial'

            self.Frame = CTkFrame(self.Master,fg_color='black',border_color='White',border_width=2*Ratio,width=300*Ratio,height=150*Ratio,corner_radius=5)
            self.Frame.place(x=self.L/2-300*Ratio/2,y=self.H/2-150*Ratio/2)
            self.File_Name = CTkTextbox(self.Frame,fg_color='white',height=25*Ratio,width=250*Ratio,corner_radius=10,font=(Police,round(17.5*Ratio)))
            self.File_Name.place(x=300*Ratio/2-250*Ratio/2,y=(10+20*Ratio_Percent)*Ratio)
            self.File_Name.insert("0.0", Phrase_Ici_Nom_Du_Fichier)
            self.Save_Button = CTkButton(self.Frame,fg_color='green',text=f'{Phrase_Sauvegarder}',hover_color='#0A6B17',bg_color='transparent',height=25*Ratio,width=75*Ratio,corner_radius=10,font=(Police,Txt_Size),command=SAVE)
            self.Save_Button.place(x=300*Ratio/2-90*Ratio/2,y=90*Ratio)
            self.Close_Button = CTkButton(self.Master,fg_color='red',text='X',hover_color='#870909',bg_color='transparent',height=15*Ratio,width=15*Ratio,corner_radius=10,font=(Police,round(25*Ratio)-(5-5*(Ratio_Percent))),command=CLOSE)
            self.Close_Button.place(x=self.L/2+300*Ratio/2-32.5*Ratio,y=self.H/2-150*Ratio/2-35*Ratio)

    def RESIZE(self, Widht_Ratio, Height_Ratio):
        if Widht_Ratio < Height_Ratio:
            Mult = Widht_Ratio
        else:
            Mult = Height_Ratio
        Txt_Size = round(20*Ratio*Mult)
        Police = 'Arial'
        self.Frame.configure(width=300*Ratio*Widht_Ratio,height=150*Ratio*Height_Ratio)
        self.Frame.place(x=(self.L/2-300*Ratio/2)*Widht_Ratio,y=(self.H/2-150*Ratio/2)*Height_Ratio)
        self.File_Name.configure(height=25*Ratio*Height_Ratio,width=250*Ratio*Widht_Ratio,font=(Police,round(17.5*Ratio*Mult)))
        self.File_Name.place(x=(300*Ratio/2-250*Ratio/2)*Widht_Ratio,y=(10+20*Ratio_Percent)*Ratio*Height_Ratio)
        self.Save_Button.configure(height=25*Ratio*Height_Ratio,width=75*Ratio*Widht_Ratio,font=(Police,Txt_Size))
        self.Save_Button.place(x=(300*Ratio/2-90*Ratio/2)*Widht_Ratio,y=90*Ratio*Height_Ratio)
        self.Close_Button.configure(height=15*Ratio*Height_Ratio,width=15*Ratio*Widht_Ratio,font=(Police,round((round(25*Ratio)-(5-5*(Ratio_Percent))))*Mult))
        self.Close_Button.place(x=(self.L/2+300*Ratio/2-32.5*Ratio)*Widht_Ratio,y=(self.H/2-150*Ratio/2-35*Ratio)*Height_Ratio)
    
class Manage_Preset:

    def __del__(self):
        pass
    
    def __init__(self, Master, H, L, Pin):
        self.Master = Master
        self.H = H
        self.L = L
        self.Pin = Pin
        self.Name = 'None'
        self.Setting_Name_List = []
        self.Open = False
        self.Mult = 1
        
    def CREATE_FRAME(self,Pin,Upd):

        def CHOICE(Choice): #Fonction pour executer le choix de l'utilisateur
            self.Name = self.File_Name.get("0.0", "end")[:-1]
            Fuck_It = False
            if not os.path.isfile(tl.GET_ABSOLUTE_PATH(f'setting\\{self.Name}.txt')):
                try:
                    with open(tl.GET_ABSOLUTE_PATH(f'setting\\{self.Name}.txt'), 'w') as fichier:
                        pass
                    os.remove(tl.GET_ABSOLUTE_PATH(f'setting\\{self.Name}.txt'))
                except:
                    self.File_Name.delete("0.0", "end")
                    self.File_Name.insert("0.0", Phrase_Nom_Invalide)
                    Fuck_It = True
            if not Fuck_It:
                self.Name = self.Name.replace("\\", "")
                if Choice == 'Destroy' and os.path.isfile(tl.GET_ABSOLUTE_PATH(f'setting\\{self.Name}.txt')) and self.Name != 'Actual':
                    List_Os_file = os.listdir('setting')
                    List_Os_file.pop(List_Os_file.index('Actual.txt'))
                    for Script in List_Os_file:
                        if Script[:-4] == self.Name:
                            Item = self.Setting_Name_List.pop(List_Os_file.index(Script))
                            Item.destroy()
                    os.remove(tl.GET_ABSOLUTE_PATH(f'setting\\{self.Name}.txt'))
                    self.Name = 'Actual'
                    self.File_Name.delete("0.0", "end")
                    self.File_Name.insert("0.0", Phrase_Ici_Nom_Du_Fichier)
                elif Choice == 'Destroy' and self.Name == 'Actual':
                    self.File_Name.delete("0.0", "end")
                    self.File_Name.insert("0.0", "🖕")
                    def WAIT():
                        self.File_Name.configure(font=(Police,round(350*Ratio*self.Mult)))
                        sleep(1.5)
                        self.File_Name.configure(font=(Police,round(17.5*Ratio*self.Mult)))
                        self.File_Name.delete("0.0", "end")
                        self.File_Name.insert("0.0", "Bruh!!!")
                    Wait = threading.Thread(target=WAIT)
                    Wait.start()
                elif '\n' in self.Name or not os.path.isfile(tl.GET_ABSOLUTE_PATH(f'setting\\{self.Name}.txt')) or self.Name == '':
                    self.File_Name.delete("0.0", "end")
                    self.File_Name.insert("0.0", Phrase_Nom_Invalide)
                    self.Name = 'Actual'
                elif self.Name == "Actual": #Si le nom du fichier a ouvrir est Actual
                    self.File_Name.delete("0.0", "end")
                    self.File_Name.insert("0.0", Phrase_Prenez_Un_Autre_Nom)
                else: #Si le choix est correcte
                    with open(tl.GET_ABSOLUTE_PATH(f'setting\\{self.Name}.txt'), 'r') as fichier:
                        Ligne = fichier.readlines()
                    with open(tl.GET_ABSOLUTE_PATH('setting\\Actual.txt'), 'w') as fichier:
                        Tempo = deepcopy(self.Pin)
                        for Item in Ligne:
                            Item_Split = Item.split(':')
                            if Item_Split[1] in self.Pin:
                                if os.path.isfile(tl.GET_ABSOLUTE_PATH(f'script\\{Item_Split[2][:-1]}.txt')):
                                    fichier.write(Item)
                                    Tempo.pop(Tempo.index(Item_Split[1]))
                        for Item in Tempo:
                            if 'A' in Item:
                                fichier.write(f'A:{Item}:None\n')
                            else:
                                fichier.write(f'N:{Item}:None\n')
                    CLOSE()

        def SET_NAME(Name):
            self.File_Name.delete("0.0", "end")
            self.File_Name.insert("0.0", Name)

        def CLOSE():
            self.Close_Button.destroy()
            self.Frame_Manage.destroy()
            self.Open = False

        if not self.Open and not Upd:

            self.Open = True
            self.Pin = Pin

            Txt_Size = round(25*Ratio)
            Police = 'Arial'
            Decal = 225*Ratio

            #Creation des frame, button et text box permettant le choix
            self.Frame_Manage = CTkFrame(self.Master,fg_color='black',border_color='White',border_width=2*Ratio,width=self.L,height=self.H,corner_radius=5)
            self.Frame_Manage.place(x=((self.L*1.25)-self.L)/2,y=((self.H*1.25)-self.H)/2)
            self.Frame_File_Name = CTkScrollableFrame(self.Frame_Manage,fg_color='#222222',width=self.L/2.5,height=self.H*0.925,corner_radius=5)
            self.Frame_File_Name.place(x=(self.L-(self.L/2.5)*2.25)/2,y=(self.H-self.H*0.95)/2)
            self.Open_File = CTkButton(self.Frame_Manage,fg_color='#2F64B4',text=Phrase_Ouvrir_Le_Fichier,height=25*Ratio,width=75*Ratio,corner_radius=10,font=(Police,Txt_Size),command=lambda:CHOICE('Open'))
            self.Open_File.place(x=self.L/2-75*Ratio/2-110*Ratio+Decal,y=self.H/2-(35+40*Ratio_Percent)*Ratio/2)
            self.Destroy_File = CTkButton(self.Frame_Manage,fg_color='#2F64B4',text=Phrase_Supprimer_Le_Fichier,height=25*Ratio,width=75*Ratio,corner_radius=10,font=(Police,Txt_Size),command=lambda:CHOICE('Destroy'))
            self.Destroy_File.place(x=self.L/2-75*Ratio/2+40*Ratio+Decal,y=self.H/2-(35+40*Ratio_Percent)*Ratio/2)
            self.File_Name = CTkTextbox(self.Frame_Manage,fg_color='white',height=25*Ratio,width=335*Ratio,corner_radius=10,font=(Police,round(17.5*Ratio)))
            self.File_Name.place(x=self.L/2-75*Ratio/2-125*Ratio+Decal,y=self.H/2-75*Ratio/2-(100-40*Ratio_Percent)*Ratio)
            self.File_Name.insert("0.0", Phrase_Ici_Nom_Du_Fichier)
            self.Setting_Name_List = []
            for Script in os.listdir(tl.GET_ABSOLUTE_PATH('setting')):
                if Script[:-4] != 'Actual':
                    if len(Script[:-4]) > Char_Limite:
                        Name = str(Script[:Char_Limite] + '...')
                    else:
                        Name = Script[:-4].encode('utf-8').decode('utf-8')
                    Txt = CTkButton(self.Frame_File_Name,fg_color='#222222',hover_color='#222222',text=Name,text_color='white',height=25*Ratio,width=75*Ratio,corner_radius=10,font=('Arial',round(25*Ratio)),command=lambda Name=deepcopy(Script[:-4]):SET_NAME(Name))
                    Txt.grid(row=len(self.Setting_Name_List),column=0,pady=5*Ratio)
                    self.Setting_Name_List.append(Txt)
            self.Close_Button = CTkButton(self.Master,fg_color='red',text='X',hover_color='#870909',bg_color='transparent',height=15*Ratio,width=15*Ratio,corner_radius=10,font=(Police,Txt_Size-(5-5*(Ratio_Percent))),command=CLOSE)
            self.Close_Button.place(x=((self.L*1.25)-self.L)/2-32.5*Ratio+self.L,y=((self.H*1.25)-self.H)/2-35*Ratio)
            
        elif Upd != 'None' and not f'{Upd}.txt' in os.listdir(tl.GET_ABSOLUTE_PATH('setting')):
            
            if len(Upd) > Char_Limite:
                Name = str(Upd[:Char_Limite] + '...')
            else:
                Name = Upd.encode('utf-8').decode('utf-8')
            Txt = CTkButton(self.Frame_File_Name,fg_color='#222222',hover_color='#222222',text=Name,text_color='white',height=25*Ratio,width=75*Ratio,corner_radius=10,font=('Arial',round(25*Ratio)),command=lambda Name=deepcopy(Upd):SET_NAME(Name))
            Txt.grid(row=len(self.Setting_Name_List),column=0,pady=5*Ratio)
            def WAIT():
                while not f'{Upd}.txt' in os.listdir(tl.GET_ABSOLUTE_PATH('setting')):
                    sleep(0.1)
                List_Os_file = os.listdir(tl.GET_ABSOLUTE_PATH('setting'))
                List_Os_file.pop(List_Os_file.index('Actual.txt'))
                self.Setting_Name_List.insert(List_Os_file.index(f'{Upd}.txt'),Txt)
                for Item in self.Setting_Name_List:
                    Item.grid(row=self.Setting_Name_List.index(Item))
            Wait = threading.Thread(target=WAIT)
            Wait.start()

    def RESIZE(self, Widht_Ratio, Height_Ratio):
        if Widht_Ratio < Height_Ratio:
            Mult = Widht_Ratio
        else:
            Mult = Height_Ratio
        self.Mult = Mult
        Txt_Size = round(25*Ratio*Mult)
        Police = 'Arial'
        Decal = 225*Ratio
        self.Frame_Manage.configure(width=self.L*Widht_Ratio,height=self.H*Height_Ratio)
        self.Frame_Manage.place(x=(((self.L*1.25)-self.L)/2)*Widht_Ratio,y=(((self.H*1.25)-self.H)/2)*Height_Ratio)
        self.Frame_File_Name.configure(width=(self.L/2.5)*Widht_Ratio,height=self.H*0.925*Height_Ratio)
        self.Frame_File_Name.place(x=((self.L-(self.L/2.5)*2.25)/2)*Widht_Ratio,y=((self.H-self.H*0.95)/2)*Height_Ratio)
        self.Open_File.configure(height=25*Ratio*Height_Ratio,width=75*Ratio*Widht_Ratio,font=(Police,Txt_Size))
        self.Open_File.place(x=(self.L/2-75*Ratio/2-110*Ratio+Decal)*Widht_Ratio,y=(self.H/2-(35+40*Ratio_Percent)*Ratio/2)*Height_Ratio)
        self.Destroy_File.configure(height=25*Ratio*Height_Ratio,width=75*Ratio*Widht_Ratio,font=(Police,Txt_Size))
        self.Destroy_File.place(x=(self.L/2-75*Ratio/2+40*Ratio+Decal)*Widht_Ratio,y=(self.H/2-(35+40*Ratio_Percent)*Ratio/2)*Height_Ratio)
        self.File_Name.configure(height=25*Ratio*Height_Ratio,width=335*Ratio*Widht_Ratio,font=(Police,round(17.5*Ratio*Mult)))
        self.File_Name.place(x=(self.L/2-75*Ratio/2-125*Ratio+Decal)*Widht_Ratio,y=(self.H/2-75*Ratio/2-(100-40*Ratio_Percent)*Ratio)*Height_Ratio)
        for Item in self.Setting_Name_List:
            Item.configure(height=25*Ratio*Height_Ratio,width=75*Ratio*Widht_Ratio,font=(Police,Txt_Size))
            Item.grid(pady=5*Ratio*Height_Ratio)
        self.Close_Button.configure(height=15*Ratio*Height_Ratio,width=15*Ratio*Widht_Ratio,font=(Police,Txt_Size))
        self.Close_Button.place(x=(((self.L*1.25)-self.L)/2-32.5*Ratio+self.L)*Widht_Ratio,y=(((self.H*1.25)-self.H)/2-35*Ratio)*Height_Ratio)

class Frame_Potence: #Instance de la frame du pin analogique

    def __del__(self):
        pass

    def __init__(self, Master, Pin, X, Y, H, L, N, Parametre, Id): #Initialisation des variables Hauteur, Largeur et autre
        self.Master = Master
        self.Pin = Pin
        self.X = X
        self.Y = Y
        self.H = H
        self.L = L
        self.N = N 
        self.Id = Id
        self.Value = 0
        self.Parametre_Instance = Parametre
        self.Open = True

    def CREATE_FRAME(self): #Creation de la frame du pin
        global Boutton_Factice_List

        def PARAMETRE():
            self.Parametre_Instance.OPEN_PARAMETRE()

        def ACTIVATE(Value):
            re.REDIRECT(self.Id,int(Value))
            self.UPDATE(str(int(Value)))

        self.Frame = CTkFrame(self.Master,fg_color='black',width=self.L,height=self.H,corner_radius=10)
        self.Frame.grid(column=self.X,row=self.Y,padx=10*Ratio,pady=10*Ratio)
        
        Txt_Size = round(20*Ratio)
        Police = 'Arial'
        
        Img = CTkImage(light_image=Image.open(tl.GET_ABSOLUTE_PATH("img\\Potentiometre.png")),dark_image=Image.open(tl.GET_ABSOLUTE_PATH("img\\Potentiometre.png")),size=(75*Ratio/1.25, 125*Ratio/1.25))
        self.Image_Button = CTkLabel(self.Frame, image=Img, text="", fg_color='transparent')
        self.Image_Button.place(x=self.L/2-(75*Ratio/1.25)/2,y=self.H/2-125*Ratio/5)
        if self.Id not in Boutton_Factice_List:
            self.Name = CTkLabel(self.Frame, text=f"{Phrase_Potentiometre} n°{self.Id}", fg_color='transparent',text_color='#FFFFFF',font=(Police,Txt_Size))
            self.Name.place(x=self.L/2-self.L/2.5-(5-5*Ratio_Percent),y=self.H/2-self.H/2.25)
            self.Stats = CTkLabel(self.Frame, text=f"{self.Value}%",height=1,width=1,fg_color='transparent',text_color='#FFFFFF',font=(Police,Txt_Size*1.1))
            self.Stats.place(x=self.L/2-self.L/(15*Ratio-7.75*Ratio*(1/3)),y=self.H/2-self.H/4-(0-0*Ratio_Percent))
        else:
            self.Name = CTkLabel(self.Frame, text=f"{Phrase_PB_PT} n°{self.Id.replace('f','')}", fg_color='transparent',text_color='red',font=(Police,Txt_Size))
            self.Name.place(x=self.L/2-self.L/4,y=self.H/2-self.H/2.25)
            self.Stats = CTkLabel(self.Frame, text="50%",height=1,width=1,fg_color='transparent',text_color='red',font=(Police,Txt_Size))
            self.Stats.place(x=self.L/2-self.L/(15-7.75*2/3),y=self.H/2-self.H/4-(0-0*Ratio_Percent))
            self.Activate = CTkSlider(self.Frame,from_=0,to=100,number_of_steps=100,bg_color='transparent',height=(15+5*Ratio_Percent)*Ratio,width=150*Ratio,corner_radius=10,command=ACTIVATE)
            self.Activate.place(x=self.L/2-self.L/2.75,y=self.H/2-self.H/3)
        self.Parametre = CTkButton(self.Frame,fg_color='#2F64B4',text=Phrase_Parametres,height=(15+5*Ratio_Percent)*Ratio,width=75*Ratio,corner_radius=10,font=(Police,Txt_Size),command=PARAMETRE)
        self.Parametre.place(x=self.L/2-self.L/3.25,y=self.H/2+self.H/(3.175-0.225*Ratio_Percent))

    def UPDATE(self,Val): #Fonction pour update l'etat du pin sur la frame et l'alignement du texte
        ValA = -1
        ValB = 0
        with open('setting\\Actual.txt', 'r') as fichier:
            Ligne = fichier.readlines()
        for Item in Ligne:
            Item_Split = Item.split(':')
            if Item_Split[2][:-1] != 'None' and 'A' in self.Id and Item_Split[1] == self.Id:
                with open(f'script\\{Item_Split[2][:-1]}.txt', 'r') as fichier:
                    Ligne_1 = fichier.readlines()
                    Ligne_1.pop(0)
                for Item_1 in Ligne_1:
                    if eval(Item_1)['Name'].encode('latin-1').decode('utf-8') == 'Inverser le potentiometre':
                        ValA = 1
                        ValB = 100
        try:
            Val = str(ValB-int(Val)*ValA)
            self.Value = Val
            Div = (15-7.75*len(Val)/3)
            self.Stats.place(x=self.L/2-self.L/Div)
            self.Stats.configure(text=f"{Val}%")
        except:
            pass

    def RESIZE(self, Widht_Ratio, Height_Ratio):        
        if Widht_Ratio < Height_Ratio:
            Mult = Widht_Ratio
        else:
            Mult = Height_Ratio
        Txt_Size = round(20*Ratio*Mult)
        Police = 'Arial'
        Img = CTkImage(light_image=Image.open(tl.GET_ABSOLUTE_PATH("img\\Potentiometre.png")),dark_image=Image.open(tl.GET_ABSOLUTE_PATH("img\\Potentiometre.png")),size=((75*Ratio/1.25)*Widht_Ratio, (125*Ratio/1.25)*Height_Ratio))
        self.Frame.configure(width=self.L*Widht_Ratio,height=self.H*Height_Ratio)
        self.Frame.grid(padx=10*Ratio*Widht_Ratio,pady=10*Ratio*Height_Ratio)
        self.Image_Button.configure(image=Img)
        self.Image_Button.place(x=(self.L/2-(75*Ratio/1.25)/2)*Widht_Ratio,y=(self.H/2-125*Ratio/5)*Height_Ratio)
        self.Name.configure(font=(Police,Txt_Size))
        self.Name.place(x=(self.L/2-self.L/2.5-(5-5*Ratio_Percent))*Widht_Ratio+80*Ratio*(1-Mult),y=(self.H/2-self.H/2.25)*Height_Ratio)
        print('Beforeeqdsfhgfzsj')
        self.Stats.configure(font=(Police,Txt_Size*1.1))
        print((self.L/2-self.L/(15-7.75*(len(str(self.Stats.cget('text')))-1)/3))*Widht_Ratio+500*Ratio*(1-Mult),(self.L/2-self.L/(15-7.75*(len(str(self.Stats.cget('text')))-1)/3))*Widht_Ratio,500*Ratio*(1-Mult),Ratio*(1-Mult))
        self.Stats.place(x=(self.L/2-self.L/(15-7.75*(2)-1)/3)*Widht_Ratio+500*Ratio*(1-Mult),y=(self.H/2-self.H/4-(0-0*Ratio_Percent))*Height_Ratio)
        try:
            self.Activate.configure(height=(15+5*Ratio_Percent)*Ratio*Height_Ratio,width=150*Ratio*Widht_Ratio)
            self.Activate.place(x=(self.L/2-self.L/2.75)*Widht_Ratio,y=(self.H/2-self.H/3)*Height_Ratio)
        except:
            pass
        self.Parametre.configure(height=(15+5*Ratio_Percent)*Ratio*Height_Ratio,width=75*Ratio*Widht_Ratio,font=(Police,Txt_Size))
        self.Parametre.place(x=(self.L/2-self.L/3.25)*Widht_Ratio+40*Ratio*(1-Mult),y=(self.H/2+self.H/(3.175-0.225*Ratio_Percent))*Height_Ratio)

class Frame_Bp: #Instance de la frame du pin numerique

    def __del__(self):
        pass

    def __init__(self, Master, Pin, X, Y, H, L, N, Parametre, Id): #Initialisation des variables Hauteur, Largeur et autre
        self.Master = Master
        self.Pin = Pin
        self.X = X
        self.Y = Y
        self.H = H
        self.L = L
        self.N = N
        self.Id = Id
        self.Value = 'Low'
        self.Parametre_Instance = Parametre
        self.Open = True

    def CREATE_FRAME(self): #Creation de la frame du pin
        global Boutton_Factice_List

        def PARAMETRE():
            self.Parametre_Instance.OPEN_PARAMETRE()
        
        def ACTIVATE():
            if self.Activate.cget('fg_color') == '#2F64B4':
                self.Activate.configure(fg_color='grey')
                re.REDIRECT(self.Id,1)
                self.UPDATE('1')
            else:
                self.Activate.configure(fg_color='#2F64B4')
                re.REDIRECT(self.Id,0)
                self.UPDATE('0')
            
        self.Frame = CTkFrame(self.Master,fg_color='black',width=self.L,height=self.H,corner_radius=10)
        self.Frame.grid(column=self.X,row=self.Y,padx=10*Ratio,pady=10*Ratio)

        Txt_Size = round(20*Ratio)
        Police = 'Arial'

        Img = CTkImage(light_image=Image.open(tl.GET_ABSOLUTE_PATH("img\\Button.PNG")),dark_image=Image.open(tl.GET_ABSOLUTE_PATH("img\\Button.PNG")),size=(75*Ratio, 75*Ratio))
        self.Image_Button = CTkLabel(self.Frame, image=Img, text="", fg_color='transparent')
        self.Image_Button.place(x=self.L/2-75*Ratio/2,y=self.H/2)
        if self.Id not in Boutton_Factice_List:
            self.Name = CTkLabel(self.Frame, text=f"{Phrase_Bouton} n°{self.Id}",fg_color='transparent',text_color='#FFFFFF',font=(Police,Txt_Size))
            self.Stats = CTkLabel(self.Frame, text=f"{self.Value}",height=1,width=1,fg_color='transparent',text_color='#FFFFFF',font=(Police,Txt_Size))
        else:
            self.Name = CTkLabel(self.Frame, text=f"{Phrase_PB_PT} n°{self.Id.replace('f','')}",fg_color='transparent',text_color='red',font=(Police,Txt_Size))
            self.Stats = CTkLabel(self.Frame, text="Low",height=1,width=1,fg_color='transparent',text_color='red',font=(Police,Txt_Size))
            self.Activate = CTkButton(self.Frame,fg_color='#2F64B4',bg_color='transparent',hover=False,text=Phrase_Activate,height=(15+5*Ratio_Percent)*Ratio,width=75*Ratio,corner_radius=10,font=(Police,Txt_Size),command=ACTIVATE)
            self.Activate.place(x=self.L/2-self.L/4.4,y=self.H/2-self.H/3.25)
        self.Name.place(x=self.L/2-self.L/4,y=self.H/2-self.H/2.25)
        self.Stats.place(x=self.L/2-self.L/10,y=self.H/2-self.H/6-(5-5*Ratio_Percent))
        self.Parametre = CTkButton(self.Frame,fg_color='#2F64B4',text=Phrase_Parametres,height=(15+5*Ratio_Percent)*Ratio,width=75*Ratio,corner_radius=10,font=(Police,Txt_Size),command=PARAMETRE)
        self.Parametre.place(x=self.L/2-self.L/3.25,y=self.H/2+self.H/(3.175-0.225*Ratio_Percent))

    def UPDATE(self,Val): #Fonction pour update l'etat du pin sur la frame et l'alignement du texte
        try:
            if Val == "1":
                self.Value = f'{Phrase_Haut}'
                self.Stats.place(x=self.L/2-self.L/9)
            elif Val == "0":
                self.Value = f'{Phrase_Bas}'
                self.Stats.place(x=self.L/2-self.L/10)
            self.Stats.configure(text=f"{self.Value}")
        except:
            pass    

    def RESIZE(self, Widht_Ratio, Height_Ratio):
        if Widht_Ratio < Height_Ratio:
            Mult = Widht_Ratio
            Size_Correction = [500,500,500]
        else:
            Mult = Height_Ratio
            Size_Correction = [100,25,40]
        Txt_Size = round(20*Ratio*Mult)
        Police = 'Arial'
        Img = CTkImage(light_image=Image.open(tl.GET_ABSOLUTE_PATH("img\\Button.PNG")),dark_image=Image.open(tl.GET_ABSOLUTE_PATH("img\\Button.PNG")),size=(75*Ratio*Widht_Ratio, 75*Ratio*Height_Ratio))
        print(self.Frame.configure(),'____________________________________________________________________________________________________________________')
        self.Frame.configure(width=int(self.L*Widht_Ratio),height=int(self.H*Height_Ratio))
        self.Frame.grid(padx=10*Ratio*Widht_Ratio,pady=10*Ratio*Height_Ratio)
        self.Image_Button.configure(image=Img)
        self.Image_Button.place(x=(self.L/2-75*Ratio/2)*Widht_Ratio,y=(self.H/2)*Height_Ratio)
        self.Name.configure(font=(Police,Txt_Size))
        self.Name.place(x=(self.L/2-self.L/4)*Widht_Ratio+Size_Correction[0]*Ratio*(1-Mult),y=(self.H/2-self.H/2.25)*Height_Ratio)
        self.Stats.configure(font=(Police,Txt_Size*1.1))
        if self.Stats.cget('text') == 'High':
            self.Stats.place(x=(self.L/2-self.L/9)*Widht_Ratio+Size_Correction[1]*Ratio*(1-Mult),y=(self.H/2-self.H/6-(5-5*Ratio_Percent))*Height_Ratio)
        else:
            self.Stats.place(x=(self.L/2-self.L/10)*Widht_Ratio+Size_Correction[1]*Ratio*(1-Mult),y=(self.H/2-self.H/6-(5-5*Ratio_Percent))*Height_Ratio)
        try:
            self.Activate.configure(height=(15+5*Ratio_Percent)*Ratio*Height_Ratio,width=150*Ratio*Widht_Ratio)
            self.Activate.place(x=(self.L/2-self.L/2.75)*Widht_Ratio,y=(self.H/2-self.H/3)*Height_Ratio)
        except:
            pass
        self.Parametre.configure(height=(15+5*Ratio_Percent)*Ratio*Height_Ratio,width=75*Ratio*Widht_Ratio,font=(Police,Txt_Size))
        self.Parametre.place(x=(self.L/2-self.L/3.25)*Widht_Ratio+Size_Correction[2]*Ratio*(1-Mult),y=(self.H/2+self.H/(3.175-0.225*Ratio_Percent))*Height_Ratio)

class Pin_Parametre: #Instance des parametre 

    def __del__(self):
        pass

    def __init__(self, Master, Id, H, L):
        self.Master = Master
        self.Id = str(Id)
        self.H = H
        self.L = L
        self.Stat = False
        self.Option = 'Nothing'
        self.Frame_Choice = None
        self.Close_Button = None
        self.List_Frame = []
        self.Open = True

    def OPEN_PARAMETRE(self):
        
        if self.Stat == False:
            self.Stat = True

            def UPDATE(Choice):
                Attention = False
                Validation = True
                End = True
                Msg = []
                if Choice != '三 Script...':
                    with open(tl.GET_ABSOLUTE_PATH(f'script\\{Choice}.txt'), 'r') as fichier:
                        Ligne = fichier.readlines()
                        Ligne.pop(0)
                        for Item in Ligne:
                            if Item != Ligne[-1]:
                                Item = Item[:-1]
                            Item = eval(Item)
                            if Item['Attention'] != None:
                                Attention = True
                                if Item['Attention'] not in Msg:
                                    Msg.append(Item['Attention'])

                if Attention:
                    End = False
                    Validation = False
                    Edit = 0
                    for Message in Msg:
                        def POP_UP(Message):
                            nonlocal self
                            def CLOSE(n):
                                nonlocal End
                                nonlocal Edit
                                nonlocal Validation
                                if n == 1 and Edit == 0:
                                    Edit = 1
                                    Validation = True
                                elif n == 0:
                                    Edit = 1
                                    Validation = False
                                self.List_Frame[-1].destroy()
                                self.List_Frame.pop(-1)
                                if Message == Msg[0]:
                                    End = True
                                if End != True and Validation == False:
                                    for Sous_Item in self.List_Frame:
                                        self.List_Frame[-1].destroy()
                                        self.List_Frame.pop(-1)
                                    End = True
 
                            Police = 'Arial'

                            Frame = CTkFrame(self.Master,fg_color='black',border_color='White',border_width=2*Ratio,width=300*Ratio,height=175*Ratio,corner_radius=5)
                            Frame.place(x=self.L/2-300*Ratio/2,y=self.H/2-150*Ratio/2)
                            self.List_Frame.append(Frame)

                            Txt = CTkLabel(self.List_Frame[-1],fg_color='transparent',text=Message,text_color='red',height=25*Ratio,width=75*Ratio,corner_radius=10,font=(Police,round(30*Ratio)))
                            Txt.place(x=50*Ratio,y=15*Ratio)
                            
                            Clear = CTkButton(self.List_Frame[-1],fg_color='#741010',text=Phrase_Annuler_2,hover_color='#550E0E',bg_color='transparent',height=25*Ratio,width=75*Ratio,corner_radius=10,font=(Police,Txt_Size),command=lambda:CLOSE(0))
                            Clear.place(x=300*Ratio/2-90*Ratio/2-75*Ratio/1.75,y=125*Ratio)
                            Save = CTkButton(self.List_Frame[-1],fg_color='green',text=Phrase_Sauvegarder,hover_color='#0A6B17',bg_color='transparent',height=25*Ratio,width=75*Ratio,corner_radius=10,font=(Police,Txt_Size),command=lambda:CLOSE(1))
                            Save.place(x=300*Ratio/2-90*Ratio/2+75*Ratio/1.75,y=125*Ratio)
                        
                        POP_UP(Message)

                def WAIT():
                    while not End:
                        sleep(0.1)
                    if Validation:
                        if Choice == "三 Script...":
                            self.Short_List.set(f"{Choice}")
                        else:
                            self.Short_List.set(f"三 {Choice}")
                        self.Option = Choice
                        with open(tl.GET_ABSOLUTE_PATH('setting\\Actual.txt'), 'r') as fichier:
                            Ligne = fichier.readlines()
                        with open(tl.GET_ABSOLUTE_PATH('setting\\Actual.txt'), 'w') as fichier:
                            for Item in Ligne:
                                Item_Split = Item[:-1].split(':')
                                if Item_Split[1] == self.Id:
                                    if Choice == "三 Script...":
                                        Item = f"{Item_Split[0]}:{Item_Split[1]}:None\n"
                                    else:
                                        Item = f"{Item_Split[0]}:{Item_Split[1]}:{Choice}\n"
                                    fichier.writelines(Item)
                                else:
                                    fichier.writelines(Item)
                    else:
                        self.Short_List.set("三 Script...")
                Wait = threading.Thread(target=WAIT)
                Wait.start()

            def CLOSE():
                try:
                    self.Frame.destroy()
                except:
                    pass
                self.Frame_Choice.destroy()
                self.Close_Button.destroy()
                self.Frame_Choice = None
                self.Close_Button = None
                self.Stat = False

            Txt_Size = round(20*Ratio)
            Police = 'Arial'

            self.Frame_Choice = CTkFrame(self.Master,fg_color='black',border_color='White',border_width=2*Ratio,width=300*Ratio,height=150*Ratio,corner_radius=5)
            self.Frame_Choice.place(x=self.L/2-300*Ratio/2,y=self.H/2-150*Ratio/2)
            self.Txt = CTkLabel(self.Frame_Choice,fg_color='transparent',text=f'{Phrase_Script_Pour_Le} n°{self.Id}',text_color='white',height=25*Ratio,width=75*Ratio,corner_radius=10,font=(Police,round(22.5*Ratio)))
            self.Txt.place(x=(7.5+7.5*Ratio_Percent)*Ratio,y=20*Ratio)
            self.Short_List_Var = StringVar()
            self.OptionList = ["三 Script..."]
            for Script in os.listdir(tl.GET_ABSOLUTE_PATH('script')):
                with open(tl.GET_ABSOLUTE_PATH(f'script\\{Script}'),'r') as fichier:
                    Ligne = fichier.readlines()
                if 'A' in self.Id and Ligne[0][:-1] == 'Potentiometre':
                    self.OptionList.append(Script[:-4])
                elif not 'A' in self.Id and Ligne[0][:-1] == 'Boutton':
                    self.OptionList.append(Script[:-4])
            self.Short_List = CTkOptionMenu(self.Frame_Choice,hover=False,fg_color='#222222',button_color='#222222',values=self.OptionList,height=20*Ratio,width=50*Ratio,corner_radius=10,font=(Police,Txt_Size),dynamic_resizing=True,command=UPDATE,variable=self.Short_List_Var)
            Define = False
            with open(tl.GET_ABSOLUTE_PATH('setting\\Actual.txt'), 'r') as fichier:
                Ligne = fichier.readlines()
            for Item in Ligne:
                if Item.split(':')[1] == self.Id and Item[:-1].split(':')[2] != 'None':
                    self.Short_List.set(f"三 {Item[:-1].split(':')[2]}")
                    Define = True
            if not Define:
                self.Short_List.set("三 Script...")
            self.Short_List.place(x=10*Ratio,y=75*Ratio)
            self.Close_Button = CTkButton(self.Master,fg_color='red',text='X',hover_color='#870909',bg_color='transparent',height=15*Ratio,width=15*Ratio,corner_radius=10,font=(Police,round(25*Ratio-(5-5*(Ratio_Percent)))),command=CLOSE)
            self.Close_Button.place(x=self.L/2+300*Ratio/2-32.5*Ratio,y=self.H/2-150*Ratio/2-35*Ratio)
        
    def RESIZE(self, Widht_Ratio, Height_Ratio):
        if Widht_Ratio < Height_Ratio:
            Mult = Widht_Ratio
        else:
            Mult = Height_Ratio
    
class Script_Editor: #Instance du scipt editor

    def __del__(self):
        pass

    def __init__(self, Master, Name_Script, H, L): #Initialisation des variables Hauteur, Largeur, etat frame et autre

        self.Master = Master
        self.Name_Script = Name_Script
        self.H = H
        self.L = L 
        self.Frame_Open = False
        self.Frame = False
        self.Save_Button = False
        self.Frame_Choice = False
        self.Name = 'None'
        self.Script_Line_List = []
        self.Commande_Line_List = []
        self.Script_Name_List = []
        self.Choice = None

    def CREATE_FRAME_CHOICE(self): #Fonction pour cree la frame pour choisir d'ouvrir un acient fichier / nouveau avec son nom
        
        def CHOICE(Choice): #Fonction pour executer le choix de l'utilisateur
            self.Name = self.File_Name.get("0.0", "end")[:-1]
            Fuck_It = False
            if not os.path.isfile(tl.GET_ABSOLUTE_PATH(f'script\\{self.Name}.txt')):
                try:
                    with open(tl.GET_ABSOLUTE_PATH(f'script\\{self.Name}.txt'), 'w') as fichier:
                        pass
                    os.remove(tl.GET_ABSOLUTE_PATH(f'script\\{self.Name}.txt'))
                except:
                    self.File_Name.delete("0.0", "end")
                    self.File_Name.insert("0.0", Phrase_Nom_Invalide)
                    Fuck_It = True
            if not Fuck_It:
                if Choice == 'Destroy' and os.path.isfile(tl.GET_ABSOLUTE_PATH(f'script\\{self.Name}.txt')):
                    for Script in os.listdir(tl.GET_ABSOLUTE_PATH('script')):
                        if Script[:-4] == self.Name:
                            Item = self.Script_Name_List.pop(os.listdir(tl.GET_ABSOLUTE_PATH('script')).index(Script))
                            Item.destroy()
                    os.remove(tl.GET_ABSOLUTE_PATH(f'script\\{self.Name}.txt'))
                    self.Name = 'None'
                    self.File_Name.delete("0.0", "end")
                    self.File_Name.insert("0.0", Phrase_Ici_Nom_Du_Fichier)
                    with open(tl.GET_ABSOLUTE_PATH('setting\\Actual.txt'), 'r') as fichier:
                        Ligne = fichier.readlines()
                    with open(tl.GET_ABSOLUTE_PATH('setting\\Actual.txt'), 'w') as fichier:
                        for Item in Ligne:
                            Item_Split = Item.split(':')
                            if os.path.isfile(f'script\\{Item_Split[2][:-1]}.txt'):
                                fichier.write(Item)
                            else:
                                fichier.write(f'{Item_Split[0]}:{Item_Split[1]}:None\n')
                elif Choice == 'Destroy' and not os.path.isfile(tl.GET_ABSOLUTE_PATH(f'script\\{self.Name}.txt')):
                    self.File_Name.delete("0.0", "end")
                    self.File_Name.insert("0.0", Phrase_Nom_Invalide)
                    self.Name = 'None'
                elif self.Name == "None": #Si le nom du fichier a ouvrir est None
                    self.File_Name.delete("0.0", "end")
                    self.File_Name.insert("0.0", Phrase_Prenez_Un_Autre_Nom)
                elif '\n' in self.Name or (not Choice and not os.path.isfile(tl.GET_ABSOLUTE_PATH(f'script\\{self.Name}.txt'))) or self.Name == '': #Si le nom du fichier n'existe pas
                    self.File_Name.delete("0.0", "end")
                    self.File_Name.insert("0.0", Phrase_Nom_Invalide)
                elif Choice and os.path.isfile(tl.GET_ABSOLUTE_PATH(f'script\\{self.Name}.txt')): #Si le nom du fichier est deja pris
                    self.File_Name.delete("0.0", "end")
                    self.File_Name.insert("0.0", Phrase_Fichier_Existe_Deja)
                else: #Si le choix est correcte
                    self.Frame_Choice.destroy()
                    self.CREATE_FRAME()
                    self.CREATE_OPEN_FILE(Choice)
                    
        # [Editeurs de Scripts] Récupérer et afficher le type du fichier + [ON/OFF - Bouton/Potentiometre]
        def SET_NAME(Name):
            self.File_Name.delete("0.0", "end")
            self.File_Name.insert("0.0", Name)
            with open(tl.GET_ABSOLUTE_PATH(f'script\\{Name}.txt'),'r') as fichier:
                Ligne = fichier.readlines()
                if Ligne[0][:-1] == 'Boutton':
                    self.Switch.deselect() # Déplace le bouton à gauche (Bouton)
                    Type_Du_Fichier = f'{Phrase_Bouton}' # Applique la conversion
                    self.Choice = 'Boutton'
                elif Ligne[0][:-1] == 'Potentiometre':
                    self.Switch.select() # Déplace le bouton à droite (Potentiometre)
                    Type_Du_Fichier = f'{Phrase_Potentiometre}' # Applique la conversion
                    self.Choice = 'Potentiometre'

                self.Text.configure(text=f'{Phrase_Type_De_Fichier}: {Type_Du_Fichier}') # Renvoie "Type de Fichier: Bouton/Potentiometre"

        # [Editeurs de Scripts] Bouton horizontal pour changer le type de fichier
        def SWITCH(): 
            self.Choice = self.Switch_Var.get()
            if self.Choice == "Potentiometre":
                self.Text.configure(text=f'{Phrase_Type_De_Fichier}: {Phrase_Potentiometre}')
            else:
                self.Text.configure(text=f'{Phrase_Type_De_Fichier}: {Phrase_Bouton}')

        Txt_Size = round(25*Ratio)
        Police = 'Arial'
        Decal = 225*Ratio
        
        #Fenêtre Editeurs de Script

        # [Editeurs de Scripts] Fenêtre
        self.Frame_Choice = CTkFrame(self.Master,fg_color='black',border_color='White',border_width=2*Ratio,width=self.L,height=self.H,corner_radius=5)
        self.Frame_Choice.place(x=((self.L*1.25)-self.L)/2,y=((self.H*1.25)-self.H)/2)

        # [Editeurs de Scripts] Liste des fichiers existants
        self.Frame_File_Name= CTkScrollableFrame(self.Frame_Choice,fg_color='#222222',width=self.L/2.5,height=self.H*0.925,corner_radius=5)
        self.Frame_File_Name.place(x=(self.L-(self.L/2.5)*2.25)/2,y=(self.H-self.H*0.95)/2)
        self.Script_Name_List = []
        for Script in os.listdir(tl.GET_ABSOLUTE_PATH('script')):
            if len(Script[:-4]) > Char_Limite:
                Name = Script[:Char_Limite] + '...'
            else:
                Name = Script[:-4].encode('utf-8').decode('utf-8')
            Txt = CTkButton(self.Frame_File_Name,fg_color='#222222',hover_color='#222222',text=Name,text_color='white',height=25*Ratio,width=75*Ratio,corner_radius=10,font=('Arial',round(25*Ratio)),command=lambda Name=deepcopy(Script[:-4]):SET_NAME(Name))
            Txt.grid(row=len(self.Script_Name_List),column=0,pady=5*Ratio)
            self.Script_Name_List.append(Txt)

        # [Editeurs de Scripts] Texte et Bouton pour choisir/afficher le type de fichier (Bouton/Potentiometre)
        self.Text = CTkLabel(self.Frame_Choice,fg_color='transparent',text_color='white',text=f'{Phrase_Bouton}                   {Phrase_Potentiometre}',corner_radius=5,font=(Police,Txt_Size))
        self.Text.place(x=self.L/2-75*Ratio/2-125*Ratio+Decal,y=self.H/2-215*Ratio)
        self.Text = CTkLabel(self.Frame_Choice,fg_color='transparent',text_color='white',text=f'{Phrase_Type_De_Fichier}: {Phrase_Bouton}',corner_radius=5,font=(Police,Txt_Size))
        self.Text.place(x=self.L/2-75*Ratio/2-60*Ratio+Decal,y=self.H/2-175*Ratio)
        self.Switch_Var = StringVar(value="off")
        self.Switch = CTkSwitch(self.Frame_Choice,fg_color='white',progress_color='white',text='',switch_width=(90+10*Ratio_Percent)*Ratio,switch_height=25*Ratio,width=1,command=SWITCH,variable=self.Switch_Var, onvalue="Potentiometre", offvalue="Boutton")
        self.Switch.place(x=self.L/2-75*Ratio/2-(25+5*Ratio_Percent)*Ratio+Decal,y=self.H/2-207.5*Ratio)
        self.Choice = 'Boutton'

        # [Editeurs de Scripts] Zone de texte pour le nom du fichier
        self.File_Name = CTkTextbox(self.Frame_Choice,fg_color='white',height=25*Ratio,width=335*Ratio,corner_radius=10,font=(Police,round(17.5*Ratio)))
        self.File_Name.place(x=self.L/2-75*Ratio/2-125*Ratio+Decal,y=self.H/2-75*Ratio/2-(85-25*Ratio_Percent)*Ratio)
        self.File_Name.insert("0.0", Phrase_Ici_Nom_Du_Fichier)
        
        # [Editeurs de Scripts] Bouton pour ouvrir/modifier/supprimer un fichier existant
        self.New_File = CTkButton(self.Frame_Choice,fg_color='#2F64B4',text=Phrase_Nouveau_Fichier,height=25*Ratio,width=75*Ratio,corner_radius=10,font=(Police,Txt_Size),command=lambda:CHOICE(True))
        self.New_File.place(x=self.L/2-75*Ratio/2-100*Ratio+Decal,y=self.H/2-(35+40*Ratio_Percent)*Ratio/2)
        self.Ancient_File = CTkButton(self.Frame_Choice,fg_color='#2F64B4',text=Phrase_Modifier_Le_Fichier,height=25*Ratio,width=75*Ratio,corner_radius=10,font=(Police,Txt_Size),command=lambda:CHOICE(False))
        self.Ancient_File.place(x=self.L/2-75*Ratio/2+50*Ratio+Decal,y=self.H/2-(35+40*Ratio_Percent)*Ratio/2)
        self.Delete_File = CTkButton(self.Frame_Choice,fg_color='#2F64B4',text=Phrase_Supprimer_Le_Fichier,height=25*Ratio,width=75*Ratio,corner_radius=10,font=(Police,Txt_Size),command=lambda:CHOICE('Destroy'))
        self.Delete_File.place(x=self.L/2-75*Ratio/2-35*Ratio+Decal,y=self.H/2+(45-35*Ratio_Percent)*Ratio)
        

    def CREATE_FRAME(self):
        
        self.Frame_Open = True

        def SAVE():
            with open(tl.GET_ABSOLUTE_PATH(f'script\\{self.Name}.txt'), 'w') as fichier:
                with open(tl.GET_ABSOLUTE_PATH('File_Editor_Temporaire.txt'), 'r') as fichier_1:
                    Ligne = fichier_1.readlines()
                    Item_Pop = Ligne.pop(0)
                    New_Ligne = []
                    for i in range(len(Ligne)):
                        Item = eval(Ligne[i])
                        List = self.Script_Line_List[i]
                        if len(List) > 1:
                            for i in range(1,len(List)-1):
                                Sous_Item = List[i+1]
                                if Item['_'][i-1] == 'Text_Box':
                                    try:
                                        Item['Parametre'][i-1] = Sous_Item.get("0.0", "end")[:-1]
                                    except:
                                        Item['Parametre'][i-1] = None
                                elif 'Menu' in Item['_'][i-1]:
                                    if not '三' in Sous_Item.get():
                                        Item['Parametre'][i-1] = Sous_Item.get()
                                    else:
                                        Item['Parametre'][i-1] = None
                                elif Item['_'][i-1] == 'Boutton':
                                    if not 'Select Touch' in Sous_Item.cget("text") and not 'Press a Touch' in Sous_Item.cget("text"):
                                        Item['Parametre'][i-1] = Sous_Item.cget("text")
                                    else:
                                        Item['Parametre'][i-1] = None
                            Name = Item['Name']
                            for i in range(len(Item['_'])):
                                if Item['Parametre'][i] != None:
                                    Name = Name.replace('_',"\""+Item['Parametre'][i]+"\"",1)
                                else:
                                    Name = Name.replace('_',"WHYDIDYOUCHOSETHISFUKINGWORLD",1)
                            Name = Name.replace('WHYDIDYOUCHOSETHISFUKINGWORLD',"_")
                            if Item['Type'] != 'Title' and len(Name) > Char_Limite:
                                Tempo = Name.split(' ')
                                j = 0
                                while j < len(Tempo):
                                    if len(Tempo[j]) > Char_Limite:
                                        i = 1
                                        First = Tempo[j][:Char_Limite]
                                        Second = Tempo[j][Char_Limite:]
                                        if len(Second) < Char_Limite+1:
                                            Tempo.insert(j+1,First)
                                            Tempo.insert(j+2,Second)
                                            Tempo.pop(j)
                                        else:
                                            while len(Second) > Char_Limite:
                                                First = Tempo[j][Char_Limite*(i-1):Char_Limite*i]
                                                Tempo.insert(j+i,First)
                                                Second = Tempo[j][Char_Limite*i:]
                                                i += 1
                                            Tempo.insert(j+i,Second)
                                            Tempo.pop(j)
                                    j += 1
                                Name = ''
                                j = 0
                                while j < len(Tempo):
                                    Tempo_Name = ''
                                    if not len(' ' + Tempo[j]) < Char_Limite+1:
                                        Tempo_Name = ' ' + Tempo[j]
                                        j += 1
                                    else:
                                        while j < len(Tempo) and len(Tempo_Name + ' ' + Tempo[j]) < Char_Limite+1:
                                            Tempo_Name += ' ' + Tempo[j]
                                            j += 1
                                    Space = ''
                                    if j < len(Tempo):
                                        Space = '\n'
                                    Name += Tempo_Name + Space
                            List[0].configure(text=Name.replace('Ã©','é'))
                        New_Ligne.append(str(Item)+'\n')
                    New_Ligne.insert(0,Item_Pop)
                    self.File = fichier.writelines(New_Ligne)

        Txt_Size = round(25*Ratio)
        Police = 'Arial'

        self.Frame = CTkFrame(self.Master,fg_color='black',border_color='White',border_width=2*Ratio,width=self.L,height=self.H,corner_radius=5)
        self.Frame.place(x=((self.L*1.25)-self.L)/2,y=((self.H*1.25)-self.H)/2)
        self.Frame_Editor_Option = CTkScrollableFrame(self.Frame,fg_color='#222222',width=self.L/2.5,height=self.H*0.925,corner_radius=5)
        self.Frame_Editor_Option.place(x=(self.L-(self.L/2.5)*2.25)/2,y=(self.H-self.H*0.95)/2)
        self.Frame_Visualizeur = CTkScrollableFrame(self.Frame,fg_color='#222222',width=self.L/2.5,height=self.H*0.925,corner_radius=5)
        self.Frame_Visualizeur.place(x=(self.L-(self.L/2.5)*2.25)/2+self.L/2.5+((self.L-(self.L/2.5)*2)/2-(self.L-(self.L/2.5)*2.5)/2),y=(self.H-self.H*0.95)/2)
        self.Save_Button = CTkButton(self.Master,fg_color='green',text=Phrase_Sauvegarder,hover_color='#0A6B17',bg_color='transparent',height=25*Ratio,width=75*Ratio,corner_radius=10,font=(Police,Txt_Size),command=SAVE)
        self.Save_Button.place(x=((self.L*1.25)-self.L)/2+self.L-75,y=((self.H*1.25)-self.H)/2+self.H)

    def CREATE_OPEN_FILE(self,Choice):
        
        def BUTTON_TOUCH(Button):
            Button.configure(text='Press a Touch')
            def WAIT():
                try:
                    Touch_Name = ''
                    Touch_Name = kb.read_key()
                    Button.configure(text=Touch_Name)
                except:
                    print('Error: This boutton no longer exist')
            Wait = threading.Thread(target=WAIT)
            Wait.start()

        def CHOICE(Var):
            Choice = Var.get()
            if "三 Select n°" in Choice:
                Var.set(f"{Choice}")
            else:
                Var.set(f"三 {Choice}")

        def ADD_LIGNE(Item):
            with open(tl.GET_ABSOLUTE_PATH('File_Editor_Temporaire.txt'), 'a') as fichier:
                Name = Item['Name']
                if Item['Type'] != 'Title' and len(Name) > 30:
                    Tempo = Name.split(' ')
                    Name = ''
                    i = 0
                    while i < len(Tempo):
                        Tempo_Name = ''
                        while i < len(Tempo) and len(Tempo_Name + ' ' + Tempo[i]) < 30:
                            Tempo_Name += ' ' + Tempo[i]
                            i += 1
                        Space = ''
                        if i < len(Tempo):
                            Space = '\n'
                        Name += Tempo_Name + Space
                Txt = CTkButton(self.Frame_Visualizeur,fg_color='#222222',hover_color='#222222',text=Name.encode('latin-1').decode('utf-8'),text_color='white',height=25*Ratio,width=75*Ratio,corner_radius=10,font=('Arial',round(25*Ratio)))
                Txt.grid(row=len(self.Script_Line_List)*2,column=0,pady=5*Ratio)
                L = [Txt]
                if '_' in list(Item.keys()):
                    Frame = CTkFrame(self.Frame_Visualizeur,fg_color='black',corner_radius=10)
                    Frame.grid(row=len(self.Script_Line_List)*2+1,column=0,pady=5*Ratio)
                    L.append(Frame)
                    for List_Item in Item['_']:
                        if List_Item == 'Text_Box':
                            Created_Item = CTkTextbox(Frame,fg_color='white',height=20*Ratio,width=100*Ratio,corner_radius=10,font=('Arial',round(15*Ratio)))
                            Created_Item.grid(row=0,column=len(L)-2,padx=5*Ratio,pady=5*Ratio)
                            Created_Item.insert("0.0", f"Value n°{len(L)-2}")
                        elif 'Menu' in List_Item:
                            Var = StringVar()
                            OptionList = deepcopy(Item[List_Item])
                            OptionList.insert(0,f"三 Select n°{len(L)-2}")
                            Created_Item = CTkOptionMenu(Frame,hover=False,fg_color='#222222',button_color='#222222',width=50*Ratio,values=OptionList,dynamic_resizing=True,variable=Var,height=35*Ratio,corner_radius=10,font=('Arial',round(15*Ratio)))
                            Created_Item.grid(row=0,column=len(L)-2,padx=5*Ratio,pady=5*Ratio)
                            Created_Item.set(f"三 Select n°{len(L)-2}")
                            Created_Item.configure(command=lambda Variable=Var:CHOICE(Variable))
                        elif List_Item == 'Boutton':
                            Created_Item = CTkButton(Frame,fg_color='#2F64B4',text=f'Select Touch n°{len(L)-2}',height=35*Ratio,width=50*Ratio,corner_radius=10,font=('Arial',round(15*Ratio)))
                            Created_Item.grid(row=0,column=len(L)-2,padx=5*Ratio,pady=5*Ratio)
                            Created_Item.configure(command=lambda Boutton=Created_Item:BUTTON_TOUCH(Boutton))
                        if Created_Item:
                            L.append(Created_Item)
                self.Script_Line_List.append(L)
                Txt.configure(command=lambda Item=L:DELETE_LIGNE(Item))
                fichier.write(f'{Item}\n')

        def DELETE_LIGNE(Item):
            Index = self.Script_Line_List.index(Item)
            Item = self.Script_Line_List.pop(Index)
            for Item_L in Item:
                try:
                    Item_L.destroy()
                except:
                    pass
            for Item in self.Script_Line_List:
                Item[0].grid(row=self.Script_Line_List.index(Item)*2)
                try:
                    Item[1].grid(row=int(self.Script_Line_List.index(Item))*2+1)
                except:
                    pass
            with open(tl.GET_ABSOLUTE_PATH('File_Editor_Temporaire.txt'), 'r') as fichier:
                Ligne = fichier.readlines()
                Ligne.pop(Index+1)
            with open(tl.GET_ABSOLUTE_PATH('File_Editor_Temporaire.txt'), 'w') as fichier:
                fichier.writelines(Ligne)

        self.Script_Line_List = []
        with open(tl.GET_ABSOLUTE_PATH('File_Editor_Temporaire.txt'), 'w') as fichier:
            if Choice:
                fichier.write(f'{self.Choice}\n')
                with open(tl.GET_ABSOLUTE_PATH(f'script\\{self.Name}.txt'), 'w') as fichier_1:
                    fichier_1.write(f'{self.Choice}\n')
            else:
                with open(tl.GET_ABSOLUTE_PATH(f'script\\{self.Name}.txt'), 'r') as fichier_1:
                    Ligne = fichier_1.readlines()
                    self.Choice = Ligne[0][:-1]
                    self.File = fichier.writelines(Ligne)
                    for Item in Ligne[1:]:
                        if Item != Ligne[-1]:
                            Item = Item[:-1]
                        Item = eval(Item)
                        Name = Item['Name']
                        if Item['Type'] != 'Title' and len(Name) > 30:
                            Tempo = Name.split(' ')
                            Name = ''
                            i = 0
                            while i < len(Tempo):
                                Tempo_Name = ''
                                while i < len(Tempo) and len(Tempo_Name + ' ' + Tempo[i]) < 30:
                                    Tempo_Name += ' ' + Tempo[i]
                                    i += 1
                                Space = ''
                                if i < len(Tempo):
                                    Space = '\n'
                                Name += Tempo_Name + Space
                        Txt = CTkButton(self.Frame_Visualizeur,fg_color='#222222',hover_color='#222222',text=Name.encode('latin-1').decode('utf-8'),text_color='white',height=25*Ratio,width=75*Ratio,corner_radius=10,font=('Arial',round(25*Ratio)))
                        Txt.grid(row=len(self.Script_Line_List)*2,column=0,pady=5*Ratio)
                        L = [Txt]
                        if '_' in list(Item.keys()):
                            Frame = CTkFrame(self.Frame_Visualizeur,fg_color='black',corner_radius=10)
                            Frame.grid(row=len(self.Script_Line_List)*2+1,column=0,pady=5*Ratio)
                            L.append(Frame)
                            i = 0
                            for List_Item in Item['_']:
                                if List_Item == 'Text_Box':
                                    if Item['Parametre'][i] != None:
                                        Name = str(Item['Parametre'][i])
                                    else:
                                        Name = f"Value n°{len(L)-2}"
                                    Created_Item = CTkTextbox(Frame,fg_color='white',height=20*Ratio,width=100*Ratio,corner_radius=10,font=('Arial',round(15*Ratio)))
                                    Created_Item.grid(row=0,column=len(L)-2,padx=5*Ratio,pady=5*Ratio)
                                    Created_Item.insert("0.0", Name)
                                elif 'Menu' in List_Item:
                                    if Item['Parametre'][i] != None:
                                        Name = Item['Parametre'][i]
                                    else:
                                        Name = f"三 Select n°{len(L)-2}"
                                    Var = StringVar()
                                    OptionList = deepcopy(Item[List_Item])
                                    OptionList.insert(0,f"三 Select n°{len(L)-2}")
                                    Created_Item = CTkOptionMenu(Frame,hover=False,fg_color='#222222',button_color='#222222',width=50*Ratio,values=OptionList,dynamic_resizing=True,variable=Var,height=35*Ratio,corner_radius=10,font=('Arial',round(15*Ratio)))
                                    Created_Item.grid(row=0,column=len(L)-2,padx=5*Ratio,pady=5*Ratio)
                                    Created_Item.set(Name)
                                elif List_Item == 'Boutton':
                                    if Item['Parametre'][i] != None:
                                        Name = Item['Parametre'][i]
                                    else:
                                        Name = f'Select Touch n°{len(L)-2}'
                                    Created_Item = CTkButton(Frame,fg_color='#2F64B4',text=Name,height=35*Ratio,width=50*Ratio,corner_radius=10,font=('Arial',round(15*Ratio)))
                                    Created_Item.grid(row=0,column=len(L)-2,padx=5*Ratio,pady=5*Ratio)
                                    Created_Item.configure(command=lambda Boutton=Created_Item:BUTTON_TOUCH(Boutton))
                                if Created_Item:
                                    L.append(Created_Item)
                                i += 1
                            Name = Item['Name']
                            for i in range(len(Item['_'])):
                                if Item['Parametre'][i] != None:
                                    Name = Name.replace('_',"\""+Item['Parametre'][i]+"\"",1)
                                else:
                                    Name = Name.replace('_',"¤WHYDIDYOUCHOSETHISFUKINGWORLDANDWHATTHEFUKINGPROBABILITIEOFWRITETHISPHRASETHISMEANINTHEMOON月にANDRAAAAAAAA�¤",1)
                            Name = Name.replace('¤WHYDIDYOUCHOSETHISFUKINGWORLDANDWHATTHEFUKINGPROBABILITIEOFWRITETHISPHRASETHISMEANINTHEMOON月にANDRAAAAAAAA�¤',"_")
                            if Item['Type'] != 'Title' and len(Name) > Char_Limite:
                                Tempo = Name.split(' ')
                                j = 0
                                while j < len(Tempo):
                                    if len(Tempo[j]) > Char_Limite:
                                        i = 1
                                        First = Tempo[j][:Char_Limite]
                                        Second = Tempo[j][Char_Limite:]
                                        if len(Second) < Char_Limite+1:
                                            Tempo.insert(j+1,First)
                                            Tempo.insert(j+2,Second)
                                            Tempo.pop(j)
                                        else:
                                            while len(Second) > Char_Limite:
                                                First = Tempo[j][Char_Limite*(i-1):Char_Limite*i]
                                                Tempo.insert(j+i,First)
                                                Second = Tempo[j][Char_Limite*i:]
                                                i += 1
                                            Tempo.insert(j+i,Second)
                                            Tempo.pop(j)
                                    j += 1
                                Name = ''
                                j = 0
                                while j < len(Tempo):
                                    Tempo_Name = ''
                                    if not len(' ' + Tempo[j]) < Char_Limite+1:
                                        Tempo_Name = ' ' + Tempo[j]
                                        j += 1
                                    else:
                                        while j < len(Tempo) and len(Tempo_Name + ' ' + Tempo[j]) < Char_Limite+1:
                                            Tempo_Name += ' ' + Tempo[j]
                                            j += 1
                                    Space = ''
                                    if j < len(Tempo):
                                        Space = '\n'
                                    Name += Tempo_Name + Space
                            L[0].configure(text=Name.replace('Ã©','é'))
                        self.Script_Line_List.append(L)
                        Txt.configure(command=lambda Item=L:DELETE_LIGNE(Item))
        
        with open(tl.GET_ABSOLUTE_PATH(f'txt\\Commande_{self.Choice}.txt'), 'r') as fichier:
            Ligne = fichier.readlines()
            for Item in Ligne:
                if Item != Ligne[-1]:
                    Item = Item[:-1]
                Item = eval(Item)
                Name = Item['Name']
                if Item['Type'] != 'Title' and len(Name) > 30:
                    Tempo = Name.split(' ')
                    Name = ''
                    i = 0
                    while i < len(Tempo):
                        Tempo_Name = ''
                        while i < len(Tempo) and len(Tempo_Name + ' ' + Tempo[i]) < 30:
                            Tempo_Name += ' ' + Tempo[i]
                            i += 1
                        Space = ''
                        if i < len(Tempo):
                            Space = '\n'
                        Name += Tempo_Name + Space
                if Item['Type'] == 'Button':
                    Txt = CTkButton(self.Frame_Editor_Option,fg_color='black',text=Name.encode('latin-1').decode('utf-8'),text_color='white',height=25*Ratio,width=75*Ratio,corner_radius=10,font=('Arial',round(25*Ratio)),command=lambda item=deepcopy(Item):ADD_LIGNE(item))
                    Txt.grid(row=len(self.Commande_Line_List),column=0,pady=5*Ratio)
                elif Item['Type'] == 'Title':
                    Txt = CTkLabel(self.Frame_Editor_Option,fg_color='transparent',text=Name.encode('latin-1').decode('utf-8'),text_color='white',height=25*Ratio,width=75*Ratio,corner_radius=10,font=('Arial',round(25*Ratio)))
                    Txt.grid(row=len(self.Commande_Line_List),column=0,pady=7.5*Ratio)
                self.Commande_Line_List.append(Txt)

    def RESIZE(self, Widht_Ratio, Height_Ratio):
        if Widht_Ratio < Height_Ratio:
            Mult = Widht_Ratio
        else:
            Mult = Height_Ratio
    
class Card_Manual:

    def __del__(self):
        pass

    def __init__(self, Master, H, L): #Initialisation des variables Hauteur, Largeur, etat frame et autre
        self.Master = Master
        self.H = H
        self.L = L 
        self.Port_Selec = None
        self.Open = False
        self.Port_Selec_Tempo = -1
        self.Close_By = 0

    def CREATE_FRAME(self):
        
        if not self.Open:
            self.Open = True
            
            def CLOSE(n):
                self.Close_By = n
                self.Frame.destroy()
                self.Close_Button.destroy()
                self.Open = False

            def CLEAR():
                self.Short_List.set("三 Port...")
                self.Port_Selec = None
                self.Port_Selec_Tempo = -1

            def SAVE():
                if self.Port_Selec_Tempo == -1:
                    CLOSE(0)
                else:
                    self.Port_Selec = self.Port_Selec_Tempo
                    CLOSE(1)

            def UPDATE(Choice):
                if Choice == "三 Port...":
                    self.Short_List.set(f"{Choice}")
                else:
                    self.Short_List.set(f"三 {Choice}")
                if Choice == 'Auto':
                    self.Port_Selec_Tempo = None
                elif Choice == "三 Port...":
                    self.Port_Selec_Tempo = -1
                else:
                    for p in list(liste_des_ports.comports()):
                        if p.description == Choice:
                            self.Port_Selec_Tempo = p.device
                
            Txt_Size = round(20*Ratio)
            Police = 'Arial'

            self.Frame = CTkFrame(self.Master,fg_color='black',border_color='White',border_width=2*Ratio,width=400*Ratio,height=150*Ratio,corner_radius=5)
            self.Frame.place(x=self.L/2-400*Ratio/2,y=self.H/2-150*Ratio/2)
            
            self.Short_List_Var = StringVar()
            self.OptionList = ['三 Port...','Auto']
            for p in list(liste_des_ports.comports()):
                if not 'COM1'  in p.description and not 'COM2' in p.description:
                    self.OptionList.append(p.description)
            self.Short_List = CTkOptionMenu(self.Frame,hover=False,fg_color='#222222',button_color='#222222',values=self.OptionList,height=20*Ratio,width=50*Ratio,corner_radius=10,font=(Police,Txt_Size),dynamic_resizing=True,command=UPDATE,variable=self.Short_List_Var)
            self.Short_List.set("三 Port...")
            self.Short_List.place(x=25*Ratio,y=32.5*Ratio)

            self.Clear = CTkButton(self.Frame,fg_color='#741010',text=Phrase_Annuler,hover_color='#550E0E',bg_color='transparent',height=25*Ratio,width=75*Ratio,corner_radius=10,font=(Police,Txt_Size),command=CLEAR)
            self.Clear.place(x=400*Ratio/2-90*Ratio/2-75*Ratio/1.75,y=90*Ratio)
            self.Save = CTkButton(self.Frame,fg_color='green',text=Phrase_Sauvegarder,hover_color='#0A6B17',bg_color='transparent',height=25*Ratio,width=75*Ratio,corner_radius=10,font=(Police,Txt_Size),command=SAVE)
            self.Save.place(x=400*Ratio/2-90*Ratio/2+75*Ratio/1.75,y=90*Ratio)
            self.Close_Button = CTkButton(self.Master,fg_color='red',text='X',hover_color='#870909',bg_color='transparent',height=15*Ratio,width=15*Ratio,corner_radius=10,font=(Police,round((25-(5-5*(Ratio_Percent)))*Ratio)),command=lambda:CLOSE(0))
            self.Close_Button.place(x=self.L/2+400*Ratio/2-32.5*Ratio,y=self.H/2-150*Ratio/2-35*Ratio)

    def RESIZE(self, Widht_Ratio, Height_Ratio):
        if Widht_Ratio < Height_Ratio:
            Mult = Widht_Ratio
        else:
            Mult = Height_Ratio
    
class Card_Type:

    def __del__(self):
        pass

    def __init__(self, Master, H, L): #Initialisation des variables Hauteur, Largeur, etat frame et autre
        self.Master = Master
        self.H = H
        self.L = L 
        self.Open = False
        self.Type_Selec_Tempo = -1
        self.Close_By = 0
        self.Type_Carte = None
        self.List = {
            'Arduino Uno' : 'arduino:avr:uno',
            'Arduino Nano' : 'arduino:avr:nano',
            'Arduino Mega (avec un processeur ATmega1280)' : 'arduino:avr:mega',
            'Arduino Mega (avec un processeur ATmega2560)' : 'arduino:avr:mega:cpu=atmega2560',
            'Arduino Zero' : 'arduino:samd:zero',
            'Arduino MKR Zero' : 'arduino:samd:mkrzero',
            'Arduino MKR1000' : 'arduino:samd:mkr1000',
            'Arduino MKRWiFi1010' : 'arduino:samd:mkrwifi1010',
            'Arduino MKRNB1500' : 'arduino:samd:mkrnb1500',
            'Arduino MKRGSM1400' : 'arduino:samd:mkrgsm1400',
            'Arduino Nano 33 BLE' : 'arduino:mbed:nrf52840',
            'Arduino MKRIoT Carrier' : 'arduino:mbed:nrf52840_mkriota',
            'Arduino Nano 33 BLE' : 'arduino:mbed:nano33ble',
            'Arduino Nano 33 BLE Sense' : 'arduino:mbed:nano33ble_sense',
            'Arduino Portenta H7' : 'arduino:mbed:portenta_h7',
            'Arduino Nicla Vision' : 'arduino:mbed:nicla_vision',

            'ESP32 Dev Module' : 'esp32:esp32:esp32',
            'ESP32 DOIT DevKit V1' : 'esp32:esp32:esp32doit-devkit-v1',
            'NodeMCU ESP32' : 'esp32:esp32:nodemcuv2',
            'Lolin32' : 'esp32:esp32:lolin32',
            'Wemos Lolin32' : 'esp32:esp32:wemos_lolin32',
            'TTGO T-Call Sprite' : 'esp32:esp32:ttgo-t-call-sprite',
            'M5Stack Core ESP32' : 'esp32:esp32:m5stack-core-esp32',
            'M5Stack Fire' : 'esp32:esp32:m5stack-fire',
            'M5Stack Gray' : 'esp32:esp32:m5stack-gray'
        }  

    def CREATE_FRAME(self):

        if not self.Open:
            self.Open = True
            
            def CLOSE(n):
                self.Close_By = n
                self.Frame.destroy()
                self.Close_Button.destroy()
                self.Open = False

            def CLEAR():
                self.Short_List.set("三 Type...")
                self.Type_Carte = None
                self.Type_Selec_Tempo = -1

            def SAVE():
                if self.Type_Selec_Tempo == -1:
                    CLOSE(0)
                else:
                    self.Type_Carte = self.List[self.Type_Selec_Tempo]
                    CLOSE(1)

            def UPDATE(Choice):
                if Choice != "三 Type...":
                    self.Short_List.set(f"三 {Choice}")
                    self.Type_Selec_Tempo = Choice
                else:
                    self.Short_List.set(f"{Choice}")
                    self.Type_Selec_Tempo = -1

            Txt_Size = round(20*Ratio)
            Police = 'Arial'

            self.Frame = CTkFrame(self.Master,fg_color='black',border_color='White',border_width=2*Ratio,width=400*Ratio,height=150*Ratio,corner_radius=5)
            self.Frame.place(x=self.L/2-400*Ratio/2,y=self.H/2-150*Ratio/2)
            self.Short_List_Var = StringVar()
            self.OptionList = list(self.List.keys())
            self.OptionList.insert(0,"三 Type...")
            self.Short_List = CTkOptionMenu(self.Frame,hover=False,fg_color='#222222',button_color='#222222',values=self.OptionList,height=20,width=50,corner_radius=10,font=(Police,Txt_Size),dynamic_resizing=True,command=UPDATE,variable=self.Short_List_Var)
            self.Short_List.set("三 Type...")
            self.Short_List.place(x=25*Ratio,y=32.5*Ratio)
            self.Clear = CTkButton(self.Frame,fg_color='#741010',text=Phrase_Annuler,hover_color='#550E0E',bg_color='transparent',height=25*Ratio,width=75*Ratio,corner_radius=10,font=(Police,Txt_Size),command=CLEAR)
            self.Clear.place(x=400*Ratio/2-90*Ratio/2-75*Ratio/1.75,y=90*Ratio)
            self.Save = CTkButton(self.Frame,fg_color='green',text='Upload',hover_color='#0A6B17',bg_color='transparent',height=25*Ratio,width=75*Ratio,corner_radius=10,font=(Police,Txt_Size),command=SAVE)
            self.Save.place(x=400*Ratio/2-90*Ratio/2+75*Ratio/1.75,y=90*Ratio)
            self.Close_Button = CTkButton(self.Master,fg_color='red',text='X',hover_color='#870909',bg_color='transparent',height=15*Ratio,width=15*Ratio,corner_radius=10,font=(Police,round((25-(5-5*(Ratio_Percent)))*Ratio)),command=lambda:CLOSE(0))
            self.Close_Button.place(x=self.L/2+400*Ratio/2-32.5*Ratio,y=self.H/2-150*Ratio/2-35*Ratio)

    def RESIZE(self, Widht_Ratio, Height_Ratio):
        if Widht_Ratio < Height_Ratio:
            Mult = Widht_Ratio
        else:
            Mult = Height_Ratio
    
class Carte: #Configuration de la Carte

    def __del__(self):
        pass

    Type_Carte = None    

    @staticmethod
    def port(Write): # Sélection automatique du port de la carte
        
        ports = list(liste_des_ports.comports())
        
        # Parcours des ports disponibles
        for p in ports:
            if Write:
                print(p)
            # Vérification de la présence de la carte ESP32
            if "ESP32" in p.description: # Cherche un element dans le nom du port
                if Write:
                    print("Carte ESP32 détectée")
                return p.device # Récupère uniquement le port dans le nom du port

            # Vérification de la présence de la carte Arduino
            elif "Arduino" in p.description:
                if Write:
                    print("Carte Arduino détectée")
                return p.device

        # Aucune carte détectée
        if Write:
            print("Aucune carte disponible")
        return None

class PortSerie: #Configuration du port série

    def __del__(self):
        pass

    ser = None
    initialisation = False
    nombresDePinsNumeriques = ""
    nombresDePinsAnalogiques = ""
    Alive = False
    Port = None

    @classmethod
    def KILL(self):
        self.ser.close()
        self.ser = None
        self.initialisation = False
        self.Alive = False

    @classmethod
    def configuration(self, port): # Défini les caractéristiques du port série pour la lecture série 
    # On utilise cls pour faire référence à la classe à l'intérieur de la méthode (introduit la variable ser = None pour pouvoir l'utiliser (PortSerie.ser == cls.ser))
        if port == None:
            print("ERREUR : Impossible de configurer le port série car le port n'est pas défini")
        else:
            try:
                self.Port = port
                self.ser = serial.Serial(
                    port,\
                    baudrate=115200,\
                    # parity=serial.PARITY_NONE,\
                    # stopbits=serial.STOPBITS_ONE,\
                    # bytesize=serial.EIGHTBITS,\
                    timeout=0.01)
                print("Port Série " + port +  " configuré avec succès")
            except:
                return False
        return True
    
    @classmethod
    def lecture(cls):
        if cls.ser is not None:
            try:
                ligneActuelle = cls.ser.readline().decode('utf-8', errors='ignore').rstrip()
                return ligneActuelle
            except:
                pass
        else:
            print("ERREUR : port série non configurable")
        
    @classmethod
    def traitementInitialisation(cls):
        
        pinsNumeriquesRecupere = False
        pinsAnalogiquesRecupere = False
        
        try:
            Error_Line = 0
            while cls.initialisation == False and Error_Line < 300:

                ligne = cls.lecture() 

                if "[Void Setup]" in ligne:
                    print("Début de l'initialisation :")

                elif "PINS Numerique HIGH :" in ligne:
                    print("Récupération des PINS Numériques :")
                    # Séparer la ligne par les espaces pour obtenir les éléments individuels
                    partitionsDeLaLigneDonneesNumeriques = ligne.split()

                    # Récupérer les IDs
                    cls.identifiantsPinsNumeriques = partitionsDeLaLigneDonneesNumeriques[4:]

                    # Obtenir la quantité d'éléments
                    cls.nombresDePinsNumeriques = len(cls.identifiantsPinsNumeriques)

                    # Scrap les valeurs pins : 0, 0 , 0
                    # A FAIRE MAIS DEMANDE DE MODIFIER LE SCRIPT ARDUINO

                    # Afficher les IDs et leurs quantités
                    print("IDs:", cls.identifiantsPinsNumeriques)
                    print("Quantités:", cls.nombresDePinsNumeriques)

                    pinsNumeriquesRecupere = True

                elif "PINS Analogiques HIGH :" in ligne:
                    print("Récupération des PINS Analogique :")

                    # Séparer la ligne par les espaces pour obtenir les éléments individuels
                    partitionsDeLaLigneDonneesAnalogiques = ligne.split()

                    # Récupérer les IDs
                    cls.identifiantsPinsAnalogiques = partitionsDeLaLigneDonneesAnalogiques[4:]

                    # Obtenir la quantité d'éléments 
                    cls.nombresDePinsAnalogiques = len(cls.identifiantsPinsAnalogiques)
                    
                    # Scrap les valeurs pins : 234, 234
                    # A FAIRE MAIS DEMANDE DE MODIFIER LE SCRIPT ARDUINO

                    # Afficher les IDs et leurs quantités
                    print("IDs:", cls.identifiantsPinsAnalogiques)
                    print("Quantités:", cls.nombresDePinsAnalogiques)
                    
                    pinsAnalogiquesRecupere = True
                elif Error_Line != -1:
                    Error_Line += 1

                if pinsAnalogiquesRecupere and pinsNumeriquesRecupere == True:
                    cls.initialisation = True
            if not Error_Line < 300:
                return -1
            cls.Alive = True
            return True
        except:
            cls.identifiantsPinsNumeriques = []
            cls.nombresDePinsNumeriques = 0
            cls.identifiantsPinsAnalogiques = []
            cls.nombresDePinsAnalogiques = 0
            cls.Port = None
            print('Erreur : Carte debrancher lors de l\'initialisation')
            return False
        
class Value_Pin:

    def __del__(self):
        pass

    def __init__(self):
        self.Setup = True
        self.Last_Id = None
        self.Last_Value = 0
        self.Last_Try = 0
        self.Last = 0

    def LIGNE_EXTRACTION(self,Ligne,Pin_Numerique_Id,Pin_Analogique_Id):
        if not self.Setup:
            try:
                Ligne_Split_1 = Ligne.split(':')
                Id = Ligne_Split_1[0]
                Value = Ligne_Split_1[1]
                if 'A' in Id:
                    self.Pin_Analogique_Value[Id] = int(Value)
                else:
                    self.Pin_Numerique_Value[Id] = int(Value)
            except:
                pass
            '''try:
                Ligne_Split_1 = Ligne.split(']')
                Id = Ligne_Split_1[0][1:]
                Ligne_Split_2 = Ligne.split(':')
                Value = Ligne_Split_2[1][1:]
                if self.Last_Id != Id or self.Last_Try >= 20:
                    if 'A' in Id:
                        self.Pin_Analogique_Value[Id] = int(Value)
                    else:
                        self.Pin_Numerique_Value[Id] = int(Value)
                    if self.Last_Id != None:
                        if 'A' in self.Last_Id:
                            self.Pin_Analogique_Value[self.Last_Id] = self.Last_Value
                        else:
                            self.Pin_Numerique_Value[self.Last_Id] = self.Last_Value
                    self.Last_Id = Id
                    self.Last_Value = int(Value)
                    self.Last_Try = 0
                else:
                    self.Last_Value = int(Value)
                    self.Last_Try += 1
            except:
                if Ligne == '' and self.Last_Id != None:
                    self.Last_Try = 0
                    if 'A' in self.Last_Id:
                        self.Pin_Analogique_Value[self.Last_Id] = self.Last_Value
                    else:
                        self.Pin_Numerique_Value[self.Last_Id] = self.Last_Value'''
                    
        elif Ligne == '[/Void Setup]':
            self.Setup = False
            self.Pin_Numerique_Value = {}
            self.Pin_Analogique_Value = {}
            for Id in Pin_Numerique_Id:
                self.Pin_Numerique_Value[str(Id)] = 0
            for Id in Pin_Analogique_Id:
                self.Pin_Analogique_Value[str(Id)] = 0

class Exit_Class:

    def __del__(self):
        pass
    
    def __init__(self):
        sys.exit()