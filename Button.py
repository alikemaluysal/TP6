import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from CanvasButton import CanvasButton

def main(args):
    app = QApplication(args)
    main_window = QMainWindow()
    canvas_button = CanvasButton()
    main_window.setCentralWidget(canvas_button)
    main_window.setWindowTitle("Canvas Button Example")
    main_window.resize(400, 300)
    main_window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main(sys.argv)
