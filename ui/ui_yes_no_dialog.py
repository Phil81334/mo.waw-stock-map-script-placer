# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'yes_no_dialogAKsiDR.ui'
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

class Ui_YesNoDialog(object):
    def setupUi(self, YesNoDialog):
        if not YesNoDialog.objectName():
            YesNoDialog.setObjectName(u"YesNoDialog")
        YesNoDialog.setWindowModality(Qt.WindowModality.ApplicationModal)
        YesNoDialog.resize(328, 128)
        YesNoDialog.setMinimumSize(QSize(328, 128))
        YesNoDialog.setStyleSheet(u"QToolTip {\n"
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
"    color: #ffffff;\n"
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
"\n"
"/*\n"
"red: ff050d\n"
"green: 0dce1d\n"
"*/")
        YesNoDialog.setModal(True)
        self.verticalLayout = QVBoxLayout(YesNoDialog)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(6, 3, 6, 3)
        self.title_label = QLabel(YesNoDialog)
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

        self.frame = QFrame(YesNoDialog)
        self.frame.setObjectName(u"frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(9)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.msg_label = QLabel(self.frame)
        self.msg_label.setObjectName(u"msg_label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.msg_label.sizePolicy().hasHeightForWidth())
        self.msg_label.setSizePolicy(sizePolicy2)
        self.msg_label.setWordWrap(True)

        self.horizontalLayout.addWidget(self.msg_label)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(YesNoDialog)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"QFrame {\n"
"	background: transparent;\n"
"	border-bottom-left-radius: 9px;\n"
"	border-bottom-right-radius: 9px;\n"
"}")
        self.frame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setSpacing(1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.yes_btn = QPushButton(self.frame_2)
        self.yes_btn.setObjectName(u"yes_btn")
        self.yes_btn.setMinimumSize(QSize(0, 0))
        self.yes_btn.setStyleSheet(u"QPushButton {\n"
"	border-bottom-right-radius: 0px;\n"
"	border-top-left-radius: 0px;\n"
"	border-top-right-radius: 0px;\n"
"}")

        self.horizontalLayout_2.addWidget(self.yes_btn)

        self.no_btn = QPushButton(self.frame_2)
        self.no_btn.setObjectName(u"no_btn")
        self.no_btn.setMinimumSize(QSize(0, 0))
        self.no_btn.setStyleSheet(u"QPushButton {\n"
"	border-bottom-left-radius: 0px;\n"
"	border-top-left-radius: 0px;\n"
"	border-top-right-radius: 0px;\n"
"}")

        self.horizontalLayout_2.addWidget(self.no_btn)


        self.verticalLayout.addWidget(self.frame_2)


        self.retranslateUi(YesNoDialog)

        QMetaObject.connectSlotsByName(YesNoDialog)
    # setupUi

    def retranslateUi(self, YesNoDialog):
        YesNoDialog.setWindowTitle(QCoreApplication.translate("YesNoDialog", u"Yes/No Dialog", None))
        self.title_label.setText(QCoreApplication.translate("YesNoDialog", u"TextLabel", None))
        self.msg_label.setText(QCoreApplication.translate("YesNoDialog", u"Yes/No Dialog...", None))
        self.yes_btn.setText(QCoreApplication.translate("YesNoDialog", u"YES", None))
        self.no_btn.setText(QCoreApplication.translate("YesNoDialog", u"NO", None))
    # retranslateUi

