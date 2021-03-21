from PySide6.QtWidgets import QApplication, QMainWindow, QMdiArea

from ui.sidemenu import SideMenu
from ui.content import Content
from ui.overlay import Overlay


class MdiArea(QMdiArea):
    def __init__(self):
        super(MdiArea, self).__init__()
        self.menu = SideMenu()
        self.content= Content(self) 
        self.overlay = Overlay(self)

        self.addSubWindow(self.menu)
        self.addSubWindow(self.content)
        self.addSubWindow(self.overlay)

    def resizeEvent(self, event):
        self.content.resize(self.width(), self.height())
        self.overlay.resize(self.width(), self.height())
        self.menu.resize(270, self.height())

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.mdi = MdiArea()
        self.setCentralWidget(self.mdi)

if __name__ == "__main__":
    import sys 

    app = QApplication([])
    w = MainWindow()
    w.resize(800, 600)
    w.show()

    sys.exit(app.exec_())