# --- Stock Imports ---

from PySide6.QtCore import Signal
from PySide6.QtGui import QCloseEvent
from PySide6.QtWidgets import QMainWindow

# --- Main ---

from ui.ui_main_window import Ui_MainWindow

class MainWindow(QMainWindow):
    close_event = Signal()

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
    
    def closeEvent(self, event: QCloseEvent) -> None:
        self.close_event.emit()
        event.accept()