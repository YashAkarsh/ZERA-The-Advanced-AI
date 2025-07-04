# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setup.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFont,QFontDatabase

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(510, 627)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        QFontDatabase.addApplicationFont(':/Fonts/orbitron.light.ttf')
        QFontDatabase.addApplicationFont(':/Fonts/pdark.ttf')
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("border-image: url(:/Settings_window/setup_page_background.png);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(34, 126, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setStyleSheet("border-image:none;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 20, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_5 = QtWidgets.QFrame(self.frame_2)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 13)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_8 = QtWidgets.QFrame(self.frame_5)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_8)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.frame_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet("border-image: url(:/miccel/border_element.png);\n"
"color:white;\n"
"font: 75 12pt \"Orbitron\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.frame_8)
        self.frame_9 = QtWidgets.QFrame(self.frame_5)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_9)
        self.gridLayout_3.setContentsMargins(-1, -1, 0, -1)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.username = QtWidgets.QLineEdit(self.frame_9)
        self.username.setMinimumSize(QtCore.QSize(0, 50))
        self.username.setStyleSheet("border-image: url(:/miccel/border_element.png);\n"
"color:white;\n"
"font: 75 11pt \"Orbitron\";\n"
"padding-left:10px;\n"
"padding-right:10px;")
        self.username.setAlignment(QtCore.Qt.AlignCenter)
        self.username.setObjectName("username")
        self.gridLayout_3.addWidget(self.username, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.frame_9)
        self.verticalLayout_2.addWidget(self.frame_5)
        self.frame_7 = QtWidgets.QFrame(self.frame_2)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_2.setContentsMargins(-1, 0, 0, 19)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_10 = QtWidgets.QFrame(self.frame_7)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_10)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_2 = QtWidgets.QLabel(self.frame_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setStyleSheet("border-image: url(:/miccel/border_element.png);\n"
"color:white;\n"
"font: 75 12pt \"Orbitron\";")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 0, 0, 1, 1)
        self.horizontalLayout_2.addWidget(self.frame_10)
        self.frame_11 = QtWidgets.QFrame(self.frame_7)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_11)
        self.gridLayout_5.setContentsMargins(11, 0, 0, 0)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.dob = QtWidgets.QDateEdit(self.frame_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dob.sizePolicy().hasHeightForWidth())
        self.dob.setSizePolicy(sizePolicy)
        self.dob.setMinimumSize(QtCore.QSize(0, 50))
        self.dob.setStyleSheet("QDateEdit\n"
"{\n"
"    background-color: transparent;\n"
"    \n"
"    border-image: url(:/miccel/border_element.png);\n"
"    font: 11pt \"orbitron\";\n"
"    border-bottom-left-radius:20px;\n"
"color:white;\n"
"padding-left:20px;\n"
"}\n"
"QDateEdit::up-button{\n"
"width:26px;\n"
"}\n"
"QDateEdit::down-button{\n"
"width:26px;\n"
"}")
        self.dob.setObjectName("dob")
        self.gridLayout_5.addWidget(self.dob, 0, 0, 1, 1)
        self.horizontalLayout_2.addWidget(self.frame_11)
        self.verticalLayout_2.addWidget(self.frame_7)
        self.frame_6 = QtWidgets.QFrame(self.frame_2)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout_8.setContentsMargins(9, 0, 0, 13)
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_3 = QtWidgets.QLabel(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(0, 50))
        self.label_3.setMaximumSize(QtCore.QSize(228, 16777215))
        self.label_3.setStyleSheet("border-image: url(:/miccel/border_element.png);\n"
"color:white;\n"
"font: 75 12pt \"Orbitron\";")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_8.addWidget(self.label_3, 0, 0, 1, 1)
        self.AgeSelection = QtWidgets.QSpinBox(self.frame_6)
        self.AgeSelection.setMinimumSize(QtCore.QSize(0, 50))
        self.AgeSelection.setStyleSheet("QSpinBox\n"
"{\n"
"    background-color: transparent;\n"
"     \n"
"    border-image: url(:/miccel/border_element.png);\n"
"    font: 11pt \"orbitron\";\n"
"border-bottom-left-radius:20px;\n"
"color:white;\n"
"padding-left:20px;\n"
"\n"
"}\n"
"QSpinBox::up-button{\n"
"width:26px;\n"
"}\n"
"QSpinBox::down-button{\n"
"width:26px;\n"
"}")
        self.AgeSelection.setObjectName("AgeSelection")
        self.gridLayout_8.addWidget(self.AgeSelection, 0, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.frame_6)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 71))
        self.frame_3.setStyleSheet("border-image:none;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setContentsMargins(-1, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_12 = QtWidgets.QFrame(self.frame_3)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame_12)
        self.gridLayout_6.setContentsMargins(16, 0, 0, 0)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.male = QtWidgets.QRadioButton(self.frame_12)
        self.male.setMaximumSize(QtCore.QSize(86, 16777215))
        self.male.setStyleSheet("color:white;\n"
"font: 75 14pt \"Orbitron\";\n"
"border-right:2px solid white;")
        self.male.setObjectName("male")
        self.gridLayout_6.addWidget(self.male, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(62, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem, 0, 0, 1, 1)
        self.frame_13 = QtWidgets.QFrame(self.frame_12)
        self.frame_13.setMaximumSize(QtCore.QSize(119, 16777215))
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frame_13)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.female = QtWidgets.QRadioButton(self.frame_13)
        self.female.setMaximumSize(QtCore.QSize(113, 16777215))
        self.female.setStyleSheet("color:white;\n"
"font: 75 14pt \"Orbitron\";")
        self.female.setObjectName("female")
        self.female.adjustSize()
        self.gridLayout_7.addWidget(self.female, 0, 0, 1, 1)
        self.gridLayout_6.addWidget(self.frame_13, 0, 2, 1, 1)
        self.horizontalLayout_4.addWidget(self.frame_12)
        spacerItem1 = QtWidgets.QSpacerItem(87, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setStyleSheet("border-image:none;")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_5.setContentsMargins(13, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frame_14 = QtWidgets.QFrame(self.frame_4)
        self.frame_14.setStyleSheet("border-top:2px solid white;")
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_14)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 13)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_15 = QtWidgets.QFrame(self.frame_14)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_15.sizePolicy().hasHeightForWidth())
        self.frame_15.setSizePolicy(sizePolicy)
        self.frame_15.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_15.setMaximumSize(QtCore.QSize(16777215, 55))
        self.frame_15.setStyleSheet("border:none;")
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.frame_15)
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_9.setSpacing(0)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.label_4 = QtWidgets.QLabel(self.frame_15)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setStyleSheet("border:none;\n"
"border-image: url(:/miccel/border_element.png);\n"
"color:white;\n"
"font: 75 12pt \"Orbitron\";")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_9.addWidget(self.label_4, 0, 0, 1, 1)
        self.horizontalLayout_3.addWidget(self.frame_15)
        self.frame_16 = QtWidgets.QFrame(self.frame_14)
        self.frame_16.setStyleSheet("border:none;")
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.frame_16)
        self.gridLayout_10.setContentsMargins(-1, -1, 14, -1)
        self.gridLayout_10.setSpacing(0)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.email = QtWidgets.QLineEdit(self.frame_16)
        self.email.setMinimumSize(QtCore.QSize(0, 50))
        self.email.setMaximumSize(QtCore.QSize(16777215, 65))
        self.email.setStyleSheet("border-image: url(:/miccel/border_element.png);\n"
"color:white;\n"
"font: 75 11pt \"Orbitron\";\n"
"padding-left:10px;\n"
"padding-right:10px;")
        self.email.setAlignment(QtCore.Qt.AlignCenter)
        self.email.setObjectName("email")
        self.gridLayout_10.addWidget(self.email, 0, 0, 1, 1)
        self.horizontalLayout_3.addWidget(self.frame_16, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout_5.addWidget(self.frame_14, 0, QtCore.Qt.AlignTop)
        spacerItem2 = QtWidgets.QSpacerItem(17, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.verticalLayout.addWidget(self.frame_4, 0, QtCore.Qt.AlignTop)
        self.frame_17 = QtWidgets.QFrame(self.frame)
        self.frame_17.setStyleSheet("border-image:none;")
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.frame_17)
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_11.setSpacing(0)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.finish = QtWidgets.QPushButton(self.frame_17)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.finish.sizePolicy().hasHeightForWidth())
        self.finish.setSizePolicy(sizePolicy)
        self.finish.setMinimumSize(QtCore.QSize(0, 50))
        self.finish.setMaximumSize(QtCore.QSize(200, 16777215))
        self.finish.setStyleSheet("QPushButton{\n"
"border-image: url(:/buttons/proceed_button.png);\n"
"}\n"
"QPushButton::hover{\n"
"border:4px solid transparent;\n"
"}")
        self.finish.setText("")
        self.finish.setObjectName("finish")
        self.gridLayout_11.addWidget(self.finish, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame_17)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Setup"))
        self.label.setText(_translate("MainWindow", "Username"))
        self.label_2.setText(_translate("MainWindow", "D.O.B"))
        self.label_3.setText(_translate("MainWindow", "Age"))
        self.male.setText(_translate("MainWindow", "Male"))
        self.female.setText(_translate("MainWindow", "Female"))
        self.label_4.setText(_translate("MainWindow", "Email Address"))
import res_rc


if __name__ == "__main__":
    import sys
#     QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling,False)
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
