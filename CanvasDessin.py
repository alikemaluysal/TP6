from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QPainterPath, QColor
from PyQt5.QtCore import QMouseEvent

class CanvasDessin(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumSize(400, 300)
        self.traces = []
        self.current_trace = None
        self.current_color = QColor(0, 0, 0)
        self.current_width = 1

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        for trace in self.traces:
            painter.setPen(trace["color"])
            painter.drawPath(trace["path"])

        if self.current_trace:
            painter.setPen(self.current_trace["color"])
            painter.drawPath(self.current_trace["path"])

    def mousePressEvent(self, event: QMouseEvent):
        self.current_trace = {
            "path": QPainterPath(),
            "color": self.current_color
        }
        self.current_trace["path"].moveTo(event.pos())

    def mouseMoveEvent(self, event: QMouseEvent):
        if self.current_trace:
            self.current_trace["path"].lineTo(event.pos())
        self.update()

    def mouseReleaseEvent(self, event: QMouseEvent):
        if self.current_trace:
            self.traces.append(self.current_trace)
            self.current_trace = None
        self.update()
