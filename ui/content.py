from PySide6.QtCore import Qt, QPropertyAnimation, QSize
from PySide6.QtGui import QPainter
from PySide6.QtWidgets import QMdiSubWindow, QWidget, QHBoxLayout, QPushButton, QStyleOption, QStyle

class WidgetContent(QWidget):
    def __init__(self, mdi):
        super(WidgetContent, self).__init__()
        self.mdi = mdi
        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        self.setLayout(self.layout)

        self.menu_btn = QPushButton("Menu")
        self.menu_btn.clicked.connect(self.show_menu)
        self.layout.addWidget(self.menu_btn)

    def show_menu(self):
        self.animation = QPropertyAnimation(self.mdi.menu, b"size")
        self.animation.setDuration(150)
        self.animation.setStartValue(QSize(0, self.mdi.height()))
        self.animation.setEndValue(QSize(270, self.mdi.height()))
        self.animation.start()

        self.mdi.menu.show()
        self.mdi.overlay.show()
        self.mdi.setActiveSubWindow(self.mdi.menu)
        self.mdi.setActiveSubWindow(self.mdi.overlay)

    def paintEvent(self, event):
        opt = QStyleOption()
        opt.initFrom(self)
        p = QPainter(self)
        self.style().drawPrimitive(QStyle.PE_Widget, opt, p, self)

class Content(QMdiSubWindow):
    def __init__(self, parent):
        super(Content, self).__init__()
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        self.widget = WidgetContent(parent)
        self.setWidget(self.widget)