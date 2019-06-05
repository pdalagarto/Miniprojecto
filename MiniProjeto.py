from PyQt5.QtWidgets import QApplication
import sys
from app.Main import Main

if __name__ == "__main__": #Corre o programa interiro
    app = QApplication(sys.argv)
    ui = Main()
    sys.exit(app.exec_())
