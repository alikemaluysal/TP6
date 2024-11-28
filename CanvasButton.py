from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QColor, QPainter
from PyQt5.QtCore import QRect, QPoint
from ButtonModel import ButtonModel

class CanvasButton(QWidget):
    defaultCol = QColor(100, 150, 200)
    hoverCol = QColor(150, 200, 250)
    pressCol = QColor(200, 100, 150)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.bbox = QRect(100, 100, 100, 50)
        self.cursorOver = False
        self.model = ButtonModel()

    def paintEvent(self, event):
        painter = QPainter(self)
        if self.model.state == ButtonModel.idle:
            color = self.defaultCol
        elif self.model.state == ButtonModel.hover:
            color = self.hoverCol
        elif self.model.state in {ButtonModel.pressIn, ButtonModel.pressOut}:
            color = self.pressCol
        painter.setBrush(color)
        painter.drawEllipse(self.bbox)

    def mouseMoveEvent(self, event):
        if self.cursorOnEllipse(event.pos()):
            if not self.cursorOver:
                self.model.toHover()
            self.cursorOver = True
        else:
            if self.cursorOver:
                self.model.toIdle()
            self.cursorOver = False
        self.update()

    def mousePressEvent(self, event):
        if self.cursorOnEllipse(event.pos()):
            self.model.toPressIn()
        self.update()

    def mouseReleaseEvent(self, event):
        if self.cursorOnEllipse(event.pos()):
            self.model.toPressOut()
            self.model.action()
        else:
            self.model.toIdle()
        self.update()

    def cursorOnEllipse(self, point: QPoint):
        rect_center = self.bbox.center()
        rx = self.bbox.width() / 2
        ry = self.bbox.height() / 2
        dx = (point.x() - rect_center.x()) / rx
        dy = (point.y() - rect_center.y()) / ry
        return dx**2 + dy**2 <= 1
