# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(450, 670)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(450, 670))
        MainWindow.setMaximumSize(QtCore.QSize(450, 670))
        MainWindow.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setBold(False)
        font.setWeight(50)
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 280, 431, 101))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 6)
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.cubeButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.cubeButton.setEnabled(True)
        self.cubeButton.setObjectName("cubeButton")
        self.gridLayout.addWidget(self.cubeButton, 1, 3, 1, 1)
        self.squareButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.squareButton.setObjectName("squareButton")
        self.gridLayout.addWidget(self.squareButton, 0, 2, 1, 1)
        self.trapezoidButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.trapezoidButton.setObjectName("trapezoidButton")
        self.gridLayout.addWidget(self.trapezoidButton, 1, 1, 1, 1)
        self.rombButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.rombButton.setObjectName("rombButton")
        self.gridLayout.addWidget(self.rombButton, 1, 0, 1, 1)
        self.triangleButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.triangleButton.setObjectName("triangleButton")
        self.gridLayout.addWidget(self.triangleButton, 0, 1, 1, 1)
        self.circleButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.circleButton.setObjectName("circleButton")
        self.gridLayout.addWidget(self.circleButton, 0, 0, 1, 1)
        self.sphereButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.sphereButton.setEnabled(True)
        self.sphereButton.setObjectName("sphereButton")
        self.gridLayout.addWidget(self.sphereButton, 1, 2, 1, 1)
        self.rectangleButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.rectangleButton.setObjectName("rectangleButton")
        self.gridLayout.addWidget(self.rectangleButton, 0, 3, 1, 1)
        self.parallelepipedButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.parallelepipedButton.setEnabled(True)
        self.parallelepipedButton.setObjectName("parallelepipedButton")
        self.gridLayout.addWidget(self.parallelepipedButton, 2, 0, 1, 1)
        self.pyramidButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pyramidButton.setEnabled(True)
        self.pyramidButton.setObjectName("pyramidButton")
        self.gridLayout.addWidget(self.pyramidButton, 2, 1, 1, 1)
        self.cylinderButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.cylinderButton.setEnabled(True)
        self.cylinderButton.setObjectName("cylinderButton")
        self.gridLayout.addWidget(self.cylinderButton, 2, 2, 1, 1)
        self.coneButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.coneButton.setEnabled(True)
        self.coneButton.setObjectName("coneButton")
        self.gridLayout.addWidget(self.coneButton, 2, 3, 1, 1)
        self.inputBox = QtWidgets.QGroupBox(self.centralwidget)
        self.inputBox.setGeometry(QtCore.QRect(10, 380, 211, 281))
        self.inputBox.setObjectName("inputBox")
        self.formLayoutWidget = QtWidgets.QWidget(self.inputBox)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 50, 191, 191))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.optionsFormLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.optionsFormLayout.setContentsMargins(0, 0, 0, 0)
        self.optionsFormLayout.setObjectName("optionsFormLayout")
        self.optionsBox = QtWidgets.QComboBox(self.inputBox)
        self.optionsBox.setGeometry(QtCore.QRect(10, 20, 189, 20))
        self.optionsBox.setObjectName("optionsBox")
        self.calculateButton = QtWidgets.QPushButton(self.inputBox)
        self.calculateButton.setEnabled(False)
        self.calculateButton.setGeometry(QtCore.QRect(14, 250, 181, 23))
        self.calculateButton.setObjectName("calculateButton")
        self.outputBox = QtWidgets.QGroupBox(self.centralwidget)
        self.outputBox.setGeometry(QtCore.QRect(230, 380, 211, 281))
        self.outputBox.setObjectName("outputBox")
        self.outputTextBrowser = QtWidgets.QTextBrowser(self.outputBox)
        self.outputTextBrowser.setEnabled(True)
        self.outputTextBrowser.setGeometry(QtCore.QRect(10, 20, 191, 251))
        self.outputTextBrowser.setAcceptDrops(True)
        self.outputTextBrowser.setLineWidth(1)
        self.outputTextBrowser.setMidLineWidth(3)
        self.outputTextBrowser.setPlaceholderText("")
        self.outputTextBrowser.setObjectName("outputTextBrowser")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 431, 261))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.drawingLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.drawingLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.drawingLayout.setContentsMargins(0, 0, 0, 0)
        self.drawingLayout.setSpacing(6)
        self.drawingLayout.setObjectName("drawingLayout")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Geometry++"))
        self.cubeButton.setText(_translate("MainWindow", "Куб"))
        self.squareButton.setText(_translate("MainWindow", "Квадрат"))
        self.trapezoidButton.setText(_translate("MainWindow", "Трапеция"))
        self.rombButton.setText(_translate("MainWindow", "Ромб"))
        self.triangleButton.setText(_translate("MainWindow", "Треугольник"))
        self.circleButton.setText(_translate("MainWindow", "Круг"))
        self.sphereButton.setText(_translate("MainWindow", "Сфера"))
        self.rectangleButton.setText(_translate("MainWindow", "Прямоугольник"))
        self.parallelepipedButton.setText(_translate("MainWindow", "Параллелепипед"))
        self.pyramidButton.setText(_translate("MainWindow", "Пирамида"))
        self.cylinderButton.setText(_translate("MainWindow", "Цилиндр"))
        self.coneButton.setText(_translate("MainWindow", "Конус"))
        self.inputBox.setTitle(_translate("MainWindow", "Параметры"))
        self.calculateButton.setText(_translate("MainWindow", "Расчитать"))
        self.outputBox.setTitle(_translate("MainWindow", "Результат"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
