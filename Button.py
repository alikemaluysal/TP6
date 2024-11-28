import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtGui import QColor, QPainter
from PyQt5.QtCore import QRect, QPoint


class CanvasButton(QWidget):
    defaultCol = QColor(0, 100, 200)  # Varsayılan renk (mavi tonları)

    def __init__(self):
        super().__init__()
        self.bbox = QRect(50, 50, 100, 100)  # Rastgele bir boyut
        self.cursorOver = False  # Başlangıçta False olarak ayarla

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(self.defaultCol)
        painter.setPen(self.defaultCol)
        painter.drawEllipse(self.bbox)  # Bounding box kullanarak elips çiz

    def mouseMoveEvent(self, event):
        print("Mouse Move Event")  # Debug için
        if self.cursorOnEllipse(event.pos()):
            print("Cursor over ellipse")
            self.cursorOver = True
        else:
            self.cursorOver = False
        self.update()

    def mousePressEvent(self, event):
        print("Mouse Press Event")

    def mouseReleaseEvent(self, event):
        print("Mouse Release Event")

    def cursorOnEllipse(self, point):
        # Elips içindeki noktayı kontrol et
        rx = self.bbox.width() / 2  # Elips yarıçapı (x ekseni)
        ry = self.bbox.height() / 2  # Elips yarıçapı (y ekseni)
        center = QPoint(self.bbox.x() + rx, self.bbox.y() + ry)  # Elips merkezi

        # Noktanın elipsin içinde olup olmadığını kontrol etmek için matematiksel formül
        dx = (point.x() - center.x()) / rx
        dy = (point.y() - center.y()) / ry
        return dx**2 + dy**2 <= 1  # Elips denklemi

def main(args):
    app = QApplication(args)
    main_window = QMainWindow()
    canvas_button = CanvasButton()
    main_window.setCentralWidget(canvas_button)
    main_window.setGeometry(100, 100, 400, 400)  # Ana pencere boyutları
    main_window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main(sys.argv)
