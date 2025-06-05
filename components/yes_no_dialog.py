# /*===================================
#     Stock Imports
# ====================================*/

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog, QWidget

# /*===================================
#     Main
# ====================================*/

from ui.ui_yes_no_dialog import Ui_YesNoDialog

class YesNoDialog(QDialog):
    def __init__(self, headless: bool, parent: QWidget) -> None:
        super().__init__(parent)  # Pass parent to base class

        # Set Attributes
        if headless:
            self.setAttribute(Qt.WA_TranslucentBackground, True)
            self.setWindowFlags(Qt.WindowStaysOnTopHint)
            self.setWindowFlags(Qt.FramelessWindowHint)

        # Ui
        self.ui = Ui_YesNoDialog()
        self.ui.setupUi(self)

        # Signals
        self.ui.yes_btn.clicked.connect(self.accept)
        self.ui.no_btn.clicked.connect(self.reject)
    
    def set_title(self, title: str) -> None:
        self.ui.title_label.setText(title)
    
    def set_text(self, message: str) -> None:
        self.ui.msg_label.setText(message)

def displayYesNoDialog(
        title: str = 'Yes/No Dialog',
        message: str = 'Yes/No Dialog',
        headless:bool = True,
        parent: QWidget | None = None) -> None:

    """
    If headless = False, pass the parent as well to take full advantage of the dialog's features.
    Passing parent is always optional.
    """

    msg_box = YesNoDialog(headless, parent)
    msg_box.set_text(message)
    msg_box.set_title(title)
    result = msg_box.exec()  # returns QDialog.Accepted or QDialog.Rejected
    return result == QDialog.Accepted  # returns bool
