from PyQt5.QtWidgets import QMainWindow, QApplication, QToolBar, QAction, QColorDialog, QSlider
from PyQt5.QtCore import Qt
from CanvasDessin import CanvasDessin
import sys

class Dessin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.canvas = CanvasDessin()
        self.setCentralWidget(self.canvas)
        self.setWindowTitle("Drawing Canvas")
        self.resize(600, 400)
        self.create_toolbar()

    def create_toolbar(self):
        toolbar = QToolBar("Tools")
        self.addToolBar(toolbar)

        # Renk seçici
        color_action = QAction("Color", self)
        color_action.triggered.connect(self.select_color)
        toolbar.addAction(color_action)

        # Kalınlık kaydırıcısı
        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.setRange(1, 20)
        self.slider.setValue(1)
        self.slider.valueChanged.connect(self.change_width)
        toolbar.addWidget(self.slider)

        # Temizleme düğmesi
        clear_action = QAction("Clear", self)
        clear_action.triggered.connect(self.clear_canvas)
        toolbar.addAction(clear_action)

    def select_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.canvas.current_color = color

    def change_width(self, value):
        self.canvas.current_width = value

    def clear_canvas(self):
        self.canvas.traces = []
        self.canvas.update()

def main(args):
    app = QApplication(args)
    window = Dessin()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main(sys.argv)
