import tools.Tools as tl
import subprocess

def UPLOAD(Port,Type_Carte):
    
    absolute_path = tl.GET_ABSOLUTE_PATH("arduino")

    commands = [
        f"cd /d {absolute_path}",
        f"arduino-cli core install {Type_Carte}",
        f"arduino-cli compile --fqbn {Type_Carte} {absolute_path}\\Arduino.ino",
        f"arduino-cli upload -p {Port} --fqbn {Type_Carte} {absolute_path}\\Arduino.ino"
    ]

    command_string = ' & '.join(commands)
    result = subprocess.run(command_string, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if result.returncode == 0:
        return 1
    else: 
        print("Sortie de la commande :")
        print(result.stdout)
        print("Erreur de la commande :")
        print(result.stderr)
        return 0