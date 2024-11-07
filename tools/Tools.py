import os
from screeninfo import get_monitors

def GET_ABSOLUTE_PATH(Relative_Path):
    Current_Dir = os.path.abspath(os.path.dirname(__file__)).replace('\\tools','')
    Absolute_Path = os.path.join(Current_Dir, Relative_Path)
    return Absolute_Path

def GET_SCREEN_DIMENSION():
    for m in get_monitors():
        if m.is_primary:
         return m.width, m.height
        
def GET_ACTUAL_FENETRE_WIDHT_HEIGHT(Fenetre):
    return Fenetre.winfo_width(), Fenetre.winfo_height()

def GET_ACTUAL_FENETRE_WIDHT_HEIGHT_RATIO(Fenetre,Start_Widht,Start_Height):
    return Fenetre.winfo_width() / Start_Widht, Fenetre.winfo_height() / Start_Height