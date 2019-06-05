from PyQt5.QtWidgets import QApplication

import sys
from app.Main import Main

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = Main()
    sys.exit(app.exec_())


#sajkdask