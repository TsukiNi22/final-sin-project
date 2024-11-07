import os

User_Name = os.popen("whoami").read()
User_Name = User_Name[User_Name.find("\\")+1:len(User_Name)-1]
Commands = ["C:","python -m ensurepip"]
Cmd_Input = Commands[0]
for Command in Commands[1:]:
    Cmd_Input += " & " + Command
os.system(f'cmd /C "{Cmd_Input}"')
My_File = open("Pip\\Bibliotheque.txt", "r")
Bibliotheque = My_File.readline()
while Bibliotheque:
    Bibliotheque = Bibliotheque[:len(User_Name)-1]
    Commands = ["C:","cd /",f"cd Users\\{User_Name}\\.local\\bin",f"pip3 install {Bibliotheque}"]
    Cmd_Input = Commands[0]
    for Command in Commands[1:]:
        Cmd_Input += " & " + Command
    os.system(f'cmd /C "{Cmd_Input}"')
    Bibliotheque = My_File.readline()
My_File.close()