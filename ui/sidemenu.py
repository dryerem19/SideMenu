from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter
from PySide6.QtWidgets import QMdiSubWindow, QWidget, QGraphicsDropShadowEffect, QStyleOption, QStyle

class SideMenuWidget(QWidget):
    def __init__(self):
        super(SideMenuWidget, self).__init__()
        self.setStyleSheet("background: red;")

    def paintEvent(self, event):
        opt = QStyleOption()
        opt.initFrom(self)
        p = QPainter(self)
        self.style().drawPrimitive(QStyle.PE_Widget, opt, p, self)

class SideMenu(QMdiSubWindow):
    def __init__(self):
        super(SideMenu, self).__init__()
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.shadow = QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(50)
        self.setGraphicsEffect(self.shadow)

        self.widget = SideMenuWidget()
        self.setWidget(self.widget)
        self.hide()

