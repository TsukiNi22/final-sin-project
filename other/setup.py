from cx_Freeze import setup, Executable
import Tools as tl
import sys

include_files = [tl.GET_ABSOLUTE_PATH('Arduino.py'),tl.GET_ABSOLUTE_PATH('Class.py'),tl.GET_ABSOLUTE_PATH('Redirect.py'),tl.GET_ABSOLUTE_PATH('TkVideoPlayer.py'),tl.GET_ABSOLUTE_PATH('Tools.py')
                 ,tl.GET_ABSOLUTE_PATH('Commande_Boutton.txt'),tl.GET_ABSOLUTE_PATH('Commande_Potentiometre.txt'),tl.GET_ABSOLUTE_PATH('Script_Save.txt')
                 ,tl.GET_ABSOLUTE_PATH('arduino'),tl.GET_ABSOLUTE_PATH('img'),tl.GET_ABSOLUTE_PATH('script'),tl.GET_ABSOLUTE_PATH('setting'),tl.GET_ABSOLUTE_PATH('video')]

setup(
    name='MAGIC',
    version='0.1',
    description='Multimedia et Application Gere par Interraction et Clavier',
    executables=[Executable('Main.py')],
    options={'build_exe': {'include_files': include_files}},
)

Base = None
if sys.platform == 'win32':
    Base = 'Win32GUI'

setup(
    name='MAGIC',
    version='0.1',
    description='Multimedia et Application Gere par Interraction et Clavier',
    executables=[Executable('Main.py', base=Base, icon=tl.GET_ABSOLUTE_PATH('img\\Magic_3_-removebg-preview.ico'))],
    options={'build_exe': {'include_files': include_files}},
)

#python setup.py build
#Ca marche a moitier