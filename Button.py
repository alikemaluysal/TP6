# Button.py

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

def main(args):
    app = QApplication(args)
    main_window = QMainWindow()
    main_window.show()
    
    sys.exit(app.exec_())

if __name__ == "__main__":
    main(sys.argv)
