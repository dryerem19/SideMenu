from PySide6.QtCore import Qt, QPropertyAnimation, QSize
from PySide6.QtWidgets import QMdiSubWindow


class Overlay(QMdiSubWindow):
    def __init__(self, parent):
        super(Overlay, self).__init__()
        self.parent = parent
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        self.setStyleSheet("background: rgba(0, 0, 0, 15%);")
        self.hide()

    def mousePressEvent(self, event):
        self.animation = QPropertyAnimation(self.parent.menu, b"size")
        self.animation.setDuration(150)
        self.animation.setStartValue(QSize(270, self.parent.height()))
        self.animation.setEndValue(QSize(0, self.parent.height()))
        self.animation.start()
        self.animation.finished.connect(self.animation_end)
        self.hide()

    def animation_end(self):
        self.parent.menu.hide()