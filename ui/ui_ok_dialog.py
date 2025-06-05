# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ok_dialogqvqaCu.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_OkDialog(object):
    def setupUi(self, OkDialog):
        if not OkDialog.objectName():
            OkDialog.setObjectName(u"OkDialog")
        OkDialog.setWindowModality(Qt.WindowModality.ApplicationModal)
        OkDialog.resize(328, 128)
        OkDialog.setMinimumSize(QSize(328, 128))
        OkDialog.setStyleSheet(u"QToolTip {\n"
"    background-color: #2e2e2e;\n"
"    color: #ffffff;\n"
"    border: 1px solid #5b5e60;\n"
"    padding: 4px;\n"
"    border-radius: 4px;\n"
"    opacity: 200;\n"
"    font-size: 12px;\n"
"}\n"
"\n"
"QLabel {\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"QFrame {\n"
"    background-color: #2e2e2e;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #3c3f41;\n"
"    color: #fff;\n"
"    border: 1px solid #5b5e60;\n"
"    border-radius: 4px;\n"
"	padding: 0px 0px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border-color: #4a90e2;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #3d78b2;\n"
"    border-color: #2a5f92;\n"
"}\n"
"")
        OkDialog.setModal(True)
        self.verticalLayout = QVBoxLayout(OkDialog)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(6, 3, 6, 3)
        self.title_label = QLabel(OkDialog)
        self.title_label.setObjectName(u"title_label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title_label.sizePolicy().hasHeightForWidth())
        self.title_label.setSizePolicy(sizePolicy)
        self.title_label.setMinimumSize(QSize(0, 18))
        self.title_label.setStyleSheet(u"QLabel {\n"
"	background-color: #3c3f41;\n"
"	border-top-left-radius: 4px;\n"
"	border-top-right-radius: 4px;\n"
"	padding-left: 5px;\n"
"}")
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout.addWidget(self.title_label)

        self.frame = QFrame(OkDialog)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(9, -1, 6, -1)
        self.msg_label = QLabel(self.frame)
        self.msg_label.setObjectName(u"msg_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.msg_label.sizePolicy().hasHeightForWidth())
        self.msg_label.setSizePolicy(sizePolicy1)
        self.msg_label.setWordWrap(True)

        self.horizontalLayout.addWidget(self.msg_label)


        self.verticalLayout.addWidget(self.frame)

        self.ok_btn = QPushButton(OkDialog)
        self.ok_btn.setObjectName(u"ok_btn")
        self.ok_btn.setMinimumSize(QSize(0, 0))
        self.ok_btn.setStyleSheet(u"QPushButton {\n"
"	border-top-left-radius: 0px;\n"
"	border-top-right-radius: 0px;\n"
"}")

        self.verticalLayout.addWidget(self.ok_btn)


        self.retranslateUi(OkDialog)

        QMetaObject.connectSlotsByName(OkDialog)
    # setupUi

    def retranslateUi(self, OkDialog):
        OkDialog.setWindowTitle(QCoreApplication.translate("OkDialog", u"Ok Dialog", None))
        self.title_label.setText(QCoreApplication.translate("OkDialog", u"TextLabel", None))
        self.msg_label.setText(QCoreApplication.translate("OkDialog", u"Ok Dialog...", None))
        self.ok_btn.setText(QCoreApplication.translate("OkDialog", u"OK", None))
    # retranslateUi

