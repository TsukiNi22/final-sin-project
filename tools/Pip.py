import os
import threading

User_Name = os.popen("whoami").read()
User_Name = User_Name[User_Name.find("\\")+1:len(User_Name)-1]
Commands = ["C:","python -m ensurepip"]
Cmd_Input = Commands[0]
for Command in Commands[1:]:
    Cmd_Input += " & " + Command

def PIP(Bibliotheque):
    global Cmd_Input
    os.system(f'cmd /C "{Cmd_Input}"')
    Commands = ["C:","cd /",f"cd Users\\{User_Name}\\.local\\bin",f"pip3 install {Bibliotheque}"]
    Cmd_Input = Commands[0]
    for Command in Commands[1:]:
        Cmd_Input += " & " + Command
    os.system(f'cmd /C "{Cmd_Input}"')

if not os.path.isdir(f'C:\\Users\\{User_Name}\\.local\\lib\\python3.9\\site-packages\\pycaw') or not os.path.isdir(f'C:\\Users\\{User_Name}\\.local\\lib\\python3.9\\site-packages\\psutil'):
    os.system('xcopy ' + os.path.abspath(os.path.dirname(__file__)).replace('tools','') + 'file_copy' + f' C:\\Users\\{User_Name}\\.local\\lib\\python3.9\\site-packages /E /Y')

'''
#'pyinstaller','pygame','av','moviepy'
List = ['customtkinter','screeninfo','time','copy','random','sys','threading','requests','fractions','serial','pyserial','pillow','webbrowser','mouse','pygetwindow','gc','logging','tkinter','keyboard']
for Item in List:
    try:
        if Item == 'pillow':
            Biliotheque = __import__('PIL')
        elif Item == 'pyserial':
            Biliotheque = __import__('serial.tools.list_ports')
        else:
            Biliotheque = __import__(Item) 
    except:
        PIP(Item)'''