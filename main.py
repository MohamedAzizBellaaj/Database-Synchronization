import sys

import qdarkstyle
from PySide6.QtWidgets import QApplication

from bo.main_window import MainWindow

if __name__ == "__main__":
    app = QApplication([])
    app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api="pyside6"))
    window = MainWindow(sys.argv[1])
    window.show()
    app.exec()
