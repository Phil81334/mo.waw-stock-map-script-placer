# /*===================================
#     Stock Imports
# ====================================*/

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog, QWidget

# /*===================================
#     Main
# ====================================*/

from ui.ui_ok_dialog import Ui_OkDialog

class OKDialog(QDialog):
    def __init__(self, headless: bool, parent: QWidget) -> None:
        super().__init__(parent)  # Pass parent to base class

        # Set Attributes
        if headless:
            self.setAttribute(Qt.WA_TranslucentBackground, True)
            self.setWindowFlags(Qt.WindowStaysOnTopHint)
            self.setWindowFlags(Qt.FramelessWindowHint)

        # Ui
        self.ui = Ui_OkDialog()
        self.ui.setupUi(self)
    
        # Signals
        self.ui.ok_btn.clicked.connect(self.close)
    
    def set_title(self, title: str) -> None:
        self.ui.title_label.setText(title)
    
    def set_text(self, message: str) -> None:
        self.ui.msg_label.setText(message)

def displayOkDialog(
        title: str = 'Ok Dialog',
        message: str = 'Ok Dialog',
        headless:bool = True,
        parent: QWidget | None = None) -> None:
    
    """
    If headless = False, pass the parent as well to take full advantage of the dialog's features.
    Passing parent is always optional.
    """

    msg_box = OKDialog(headless, parent)
    msg_box.set_text(message)
    msg_box.set_title(title)
    msg_box.exec()