import sys, os
from PyQt5.QtGui import QIcon

if getattr(sys, 'frozen', False):
    os.chdir(sys._MEIPASS)

MPRUN_WINDOW_ICON = QIcon('assets/logos/mprun_icon.png')