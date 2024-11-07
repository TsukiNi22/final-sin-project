import string
import random as rd
import base64
import lzma
import ast

All_Characters = string.printable
exclude_chars = '\n\r'
All_Characters = ''.join(char for char in All_Characters if char not in exclude_chars)

def CHAR_GENERATEUR():
    Char = ''
    for i in range(rd.randint(1000,2500)):
        rdm = rd.choice(All_Characters)
        Char += rdm
    with open('Key_Encode.txt','w') as f:
        f.write(base64.b64encode(lzma.compress(bytes(Char, 'utf-8'))).decode('utf-8'))

def CLE_GENERATEUR():
    with open('Key_Encode.txt','r') as f:
        Ligne = f.read()
    Char = lzma.decompress(base64.b64decode(Ligne)).decode('utf-8')
    Join_Char = ''
    for Sous_Char in Char:
        if not Sous_Char in Join_Char:
            Join_Char += Sous_Char
    Len = len(Join_Char)
    Cle = [Join_Char]
    for i in range(rd.randint(50,100)):
        Random_Characters = ''
        while len(Random_Characters) != Len:
            rdm = rd.choice(All_Characters)
            if not rdm in Random_Characters:
                Random_Characters += rdm
                rdm = rd.randint(0,Len-1)
        Cle.append(Random_Characters)
    with open('Key.txt','w') as f:
        for Ligne in Cle:
            if Ligne != Cle[-1]:
                f.write(str(Ligne)+'\n')
            else:
                f.write(str(Ligne))

def ENCODE(Char,Cle):
    for h in range(len(Cle)):
        List = Cle[h]
        List_Emplacement = {}
        Join_Char = ''
        for Sous_Char in Char:
            if not Sous_Char in Join_Char:
                Join_Char += Sous_Char
        for j in range(len(List)):
            Sous_List = []
            for i in range(len(Char)):
                if Char[i] == Join_Char[j]:
                    Sous_List.append(i)
            List_Emplacement[List[j]] = Sous_List
        for Key in list(List_Emplacement.keys()):
            for i in range(len(List_Emplacement[Key])):
                Char = Char[:List_Emplacement[Key][i]] + Key + Char[List_Emplacement[Key][i]+1:]
        #print(Char,List_Emplacement,Join_Char,List,'_____________encode')
    return Char

def DECODE(Char,Cle):
    for h in range(len(Cle)):
        List = Cle[-(h+1)]
        List_Emplacement = {}
        Join_Char = ''
        for Sous_Char in Char:
            if not Sous_Char in Join_Char:
                Join_Char += Sous_Char
        for j in range(len(List)):
            Sous_List = []
            for i in range(len(Char)):
                if Char[i] == Join_Char[j]:
                    Sous_List.append(i)
            List_Emplacement[List[j]] = Sous_List
        for Key in list(List_Emplacement.keys()):
            for i in range(len(List_Emplacement[Key])):
                Char = Char[:List_Emplacement[Key][i]] + Key + Char[List_Emplacement[Key][i]+1:]
        #print(Char,List_Emplacement,Join_Char,List,'_____________decode')
    return Char

def GET_KEY():
    with open('Key.txt','r') as f:
        Cle = list(f.readlines())
    for i in range(len(Cle)):
        Cle[i] = Cle[i].replace('\n','')
    return Cle

def GET_CHAR():
    with open('Key_Encode.txt','r') as f:
        Ligne = f.read()
    Char = lzma.decompress(base64.b64decode(Ligne)).decode('utf-8')
    return Char

def WRITE_KEY(Char):
    with open('Key_Encode.txt','w') as f:
        f.write(base64.b64encode(lzma.compress(bytes(Char, 'utf-8'))).decode('utf-8'))

def ENCODE_CHAR():
    Char = GET_CHAR()
    with open('Key_Encode.txt','w') as f:
        f.write(base64.b64encode(lzma.compress(bytes(ENCODE(Char,GET_KEY()), 'utf-8'))).decode('utf-8'))

#CHAR_GENERATEUR()
#CLE_GENERATEUR()
#ENCODE_CHAR()
