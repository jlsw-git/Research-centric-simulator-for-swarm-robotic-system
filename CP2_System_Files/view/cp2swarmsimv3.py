# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cp2swarmsimv3.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(1280, 755)
        mainWindow.setMinimumSize(QtCore.QSize(1280, 755))
        mainWindow.setMaximumSize(QtCore.QSize(1280, 755))
        self.centralWidget = QtWidgets.QWidget(mainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.simulationGraphicsView = QtWidgets.QGraphicsView(self.centralWidget)
        self.simulationGraphicsView.setGeometry(QtCore.QRect(370, 10, 901, 721))
        self.simulationGraphicsView.setObjectName("simulationGraphicsView")
        self.timeLcdNumber = QtWidgets.QLCDNumber(self.centralWidget)
        self.timeLcdNumber.setGeometry(QtCore.QRect(1173, 700, 71, 23))
        self.timeLcdNumber.setObjectName("timeLcdNumber")
        self.timeLabel = QtWidgets.QLabel(self.centralWidget)
        self.timeLabel.setGeometry(QtCore.QRect(1110, 700, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.timeLabel.setFont(font)
        self.timeLabel.setObjectName("timeLabel")
        self.layoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 2, 2))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralWidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 10, 351, 721))
        self.scrollArea.setMinimumSize(QtCore.QSize(351, 721))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 332, 791))
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(331, 791))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.parametersGroupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.parametersGroupBox.setGeometry(QtCore.QRect(0, 170, 331, 131))
        self.parametersGroupBox.setMinimumSize(QtCore.QSize(331, 131))
        self.parametersGroupBox.setAutoFillBackground(True)
        self.parametersGroupBox.setObjectName("parametersGroupBox")
        self.formLayout_2 = QtWidgets.QFormLayout(self.parametersGroupBox)
        self.formLayout_2.setObjectName("formLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.agentNumberLabel = QtWidgets.QLabel(self.parametersGroupBox)
        self.agentNumberLabel.setObjectName("agentNumberLabel")
        self.horizontalLayout.addWidget(self.agentNumberLabel)
        self.agentNumberSpinBox = QtWidgets.QSpinBox(self.parametersGroupBox)
        self.agentNumberSpinBox.setObjectName("agentNumberSpinBox")
        self.horizontalLayout.addWidget(self.agentNumberSpinBox)
        self.formLayout_2.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.iterationLabel = QtWidgets.QLabel(self.parametersGroupBox)
        self.iterationLabel.setObjectName("iterationLabel")
        self.horizontalLayout_2.addWidget(self.iterationLabel)
        self.iterationSpinBox = QtWidgets.QSpinBox(self.parametersGroupBox)
        self.iterationSpinBox.setObjectName("iterationSpinBox")
        self.horizontalLayout_2.addWidget(self.iterationSpinBox)
        self.formLayout_2.setLayout(1, QtWidgets.QFormLayout.LabelRole, self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.velocityLabel = QtWidgets.QLabel(self.parametersGroupBox)
        self.velocityLabel.setObjectName("velocityLabel")
        self.horizontalLayout_3.addWidget(self.velocityLabel)
        self.velocityDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.parametersGroupBox)
        self.velocityDoubleSpinBox.setObjectName("velocityDoubleSpinBox")
        self.horizontalLayout_3.addWidget(self.velocityDoubleSpinBox)
        self.formLayout_2.setLayout(2, QtWidgets.QFormLayout.LabelRole, self.horizontalLayout_3)
        self.mapGroupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.mapGroupBox.setGeometry(QtCore.QRect(0, 320, 331, 111))
        self.mapGroupBox.setMinimumSize(QtCore.QSize(331, 111))
        self.mapGroupBox.setAutoFillBackground(True)
        self.mapGroupBox.setObjectName("mapGroupBox")
        self.layoutWidget_12 = QtWidgets.QWidget(self.mapGroupBox)
        self.layoutWidget_12.setGeometry(QtCore.QRect(10, 30, 94, 66))
        self.layoutWidget_12.setObjectName("layoutWidget_12")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget_12)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.mapLabel = QtWidgets.QLabel(self.layoutWidget_12)
        self.mapLabel.setObjectName("mapLabel")
        self.verticalLayout_3.addWidget(self.mapLabel)
        self.mapComboBox = QtWidgets.QComboBox(self.layoutWidget_12)
        self.mapComboBox.setObjectName("mapComboBox")
        self.mapComboBox.addItem("")
        self.mapComboBox.addItem("")
        self.mapComboBox.addItem("")
        self.verticalLayout_3.addWidget(self.mapComboBox)
        self.verticalLayout_2.addLayout(self.verticalLayout_3)
        self.itemCheckBox = QtWidgets.QCheckBox(self.layoutWidget_12)
        self.itemCheckBox.setObjectName("itemCheckBox")
        self.verticalLayout_2.addWidget(self.itemCheckBox)
        self.simulationGoupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.simulationGoupBox.setGeometry(QtCore.QRect(0, 450, 331, 271))
        self.simulationGoupBox.setMinimumSize(QtCore.QSize(331, 271))
        self.simulationGoupBox.setAutoFillBackground(True)
        self.simulationGoupBox.setObjectName("simulationGoupBox")
        self.simSpeedLabel = QtWidgets.QLabel(self.simulationGoupBox)
        self.simSpeedLabel.setGeometry(QtCore.QRect(10, 30, 91, 16))
        self.simSpeedLabel.setObjectName("simSpeedLabel")
        self.videoRecLabel = QtWidgets.QLabel(self.simulationGoupBox)
        self.videoRecLabel.setGeometry(QtCore.QRect(10, 120, 81, 20))
        self.videoRecLabel.setObjectName("videoRecLabel")
        self.simSpeedHoriSlider = QtWidgets.QSlider(self.simulationGoupBox)
        self.simSpeedHoriSlider.setGeometry(QtCore.QRect(80, 60, 160, 22))
        self.simSpeedHoriSlider.setOrientation(QtCore.Qt.Horizontal)
        self.simSpeedHoriSlider.setObjectName("simSpeedHoriSlider")
        self.xFirstLabel = QtWidgets.QLabel(self.simulationGoupBox)
        self.xFirstLabel.setGeometry(QtCore.QRect(80, 90, 20, 20))
        self.xFirstLabel.setObjectName("xFirstLabel")
        self.xSecondLabel = QtWidgets.QLabel(self.simulationGoupBox)
        self.xSecondLabel.setGeometry(QtCore.QRect(160, 90, 20, 20))
        self.xSecondLabel.setObjectName("xSecondLabel")
        self.xThirdLabel = QtWidgets.QLabel(self.simulationGoupBox)
        self.xThirdLabel.setGeometry(QtCore.QRect(230, 90, 21, 20))
        self.xThirdLabel.setObjectName("xThirdLabel")
        self.layoutWidget_13 = QtWidgets.QWidget(self.simulationGoupBox)
        self.layoutWidget_13.setGeometry(QtCore.QRect(50, 150, 241, 96))
        self.layoutWidget_13.setObjectName("layoutWidget_13")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget_13)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.startPushButton = QtWidgets.QPushButton(self.layoutWidget_13)
        self.startPushButton.setObjectName("startPushButton")
        self.horizontalLayout_4.addWidget(self.startPushButton)
        self.stopPushButton = QtWidgets.QPushButton(self.layoutWidget_13)
        self.stopPushButton.setObjectName("stopPushButton")
        self.horizontalLayout_4.addWidget(self.stopPushButton)
        self.savePushButton = QtWidgets.QPushButton(self.layoutWidget_13)
        self.savePushButton.setObjectName("savePushButton")
        self.horizontalLayout_4.addWidget(self.savePushButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.horizontalLine = QtWidgets.QFrame(self.layoutWidget_13)
        self.horizontalLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.horizontalLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.horizontalLine.setObjectName("horizontalLine")
        self.verticalLayout_4.addWidget(self.horizontalLine)
        self.startSimPushButton = QtWidgets.QPushButton(self.layoutWidget_13)
        self.startSimPushButton.setObjectName("startSimPushButton")
        self.verticalLayout_4.addWidget(self.startSimPushButton)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.loadPushButton = QtWidgets.QPushButton(self.layoutWidget_13)
        self.loadPushButton.setObjectName("loadPushButton")
        self.horizontalLayout_5.addWidget(self.loadPushButton)
        self.resetPushButton = QtWidgets.QPushButton(self.layoutWidget_13)
        self.resetPushButton.setObjectName("resetPushButton")
        self.horizontalLayout_5.addWidget(self.resetPushButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.swarmDesignGroupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.swarmDesignGroupBox.setGeometry(QtCore.QRect(0, 0, 331, 151))
        self.swarmDesignGroupBox.setMinimumSize(QtCore.QSize(331, 151))
        self.swarmDesignGroupBox.setAutoFillBackground(True)
        self.swarmDesignGroupBox.setObjectName("swarmDesignGroupBox")
        self.dropFrame = QtWidgets.QFrame(self.swarmDesignGroupBox)
        self.dropFrame.setGeometry(QtCore.QRect(190, 70, 91, 71))
        self.dropFrame.setMouseTracking(True)
        self.dropFrame.setAcceptDrops(True)
        self.dropFrame.setAutoFillBackground(False)
        self.dropFrame.setStyleSheet("background-color: #E0E0E0")
        self.dropFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.dropFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.dropFrame.setObjectName("dropFrame")
        self.dropAlgoLabel = QtWidgets.QLabel(self.dropFrame)
        self.dropAlgoLabel.setGeometry(QtCore.QRect(0, 0, 91, 71))
        self.dropAlgoLabel.setObjectName("dropAlgoLabel")
        self.layoutWidget_15 = QtWidgets.QWidget(self.swarmDesignGroupBox)
        self.layoutWidget_15.setGeometry(QtCore.QRect(10, 30, 87, 41))
        self.layoutWidget_15.setObjectName("layoutWidget_15")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.layoutWidget_15)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.taskLabel = QtWidgets.QLabel(self.layoutWidget_15)
        self.taskLabel.setObjectName("taskLabel")
        self.verticalLayout_5.addWidget(self.taskLabel)
        self.taskComboBox = QtWidgets.QComboBox(self.layoutWidget_15)
        self.taskComboBox.setObjectName("taskComboBox")
        self.taskComboBox.addItem("")
        self.taskComboBox.addItem("")
        self.taskComboBox.addItem("")
        self.verticalLayout_5.addWidget(self.taskComboBox)
        self.algorithmLabel = QtWidgets.QLabel(self.swarmDesignGroupBox)
        self.algorithmLabel.setGeometry(QtCore.QRect(146, 31, 55, 20))
        self.algorithmLabel.setMinimumSize(QtCore.QSize(55, 20))
        self.algorithmLabel.setMaximumSize(QtCore.QSize(55, 20))
        self.algorithmLabel.setObjectName("algorithmLabel")
        self.selectedAlgoLabel = QtWidgets.QLabel(self.swarmDesignGroupBox)
        self.selectedAlgoLabel.setGeometry(QtCore.QRect(150, 50, 135, 20))
        self.selectedAlgoLabel.setMinimumSize(QtCore.QSize(135, 20))
        self.selectedAlgoLabel.setMaximumSize(QtCore.QSize(135, 20))
        self.selectedAlgoLabel.setObjectName("selectedAlgoLabel")
        self.algorithmToolButton = QtWidgets.QToolButton(self.swarmDesignGroupBox)
        self.algorithmToolButton.setGeometry(QtCore.QRect(290, 50, 31, 19))
        self.algorithmToolButton.setObjectName("algorithmToolButton")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        mainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(mainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1280, 21))
        self.menuBar.setObjectName("menuBar")
        mainWindow.setMenuBar(self.menuBar)
        self.statusBar = QtWidgets.QStatusBar(mainWindow)
        self.statusBar.setObjectName("statusBar")
        mainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)
        mainWindow.setTabOrder(self.taskComboBox, self.algorithmToolButton)
        mainWindow.setTabOrder(self.algorithmToolButton, self.agentNumberSpinBox)
        mainWindow.setTabOrder(self.agentNumberSpinBox, self.iterationSpinBox)
        mainWindow.setTabOrder(self.iterationSpinBox, self.velocityDoubleSpinBox)
        mainWindow.setTabOrder(self.velocityDoubleSpinBox, self.mapComboBox)
        mainWindow.setTabOrder(self.mapComboBox, self.itemCheckBox)
        mainWindow.setTabOrder(self.itemCheckBox, self.simSpeedHoriSlider)
        mainWindow.setTabOrder(self.simSpeedHoriSlider, self.startPushButton)
        mainWindow.setTabOrder(self.startPushButton, self.stopPushButton)
        mainWindow.setTabOrder(self.stopPushButton, self.savePushButton)
        mainWindow.setTabOrder(self.savePushButton, self.startSimPushButton)
        mainWindow.setTabOrder(self.startSimPushButton, self.loadPushButton)
        mainWindow.setTabOrder(self.loadPushButton, self.resetPushButton)
        mainWindow.setTabOrder(self.resetPushButton, self.scrollArea)
        mainWindow.setTabOrder(self.scrollArea, self.simulationGraphicsView)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "MainWindow"))
        self.timeLabel.setText(_translate("mainWindow", "Time:"))
        self.parametersGroupBox.setTitle(_translate("mainWindow", "Parameters"))
        self.agentNumberLabel.setText(_translate("mainWindow", "Number of agents:"))
        self.iterationLabel.setText(_translate("mainWindow", "Iterations:"))
        self.velocityLabel.setText(_translate("mainWindow", "Velocity:"))
        self.mapGroupBox.setTitle(_translate("mainWindow", "Map Design"))
        self.mapLabel.setText(_translate("mainWindow", "Map:"))
        self.mapComboBox.setItemText(0, _translate("mainWindow", "Map Design 1"))
        self.mapComboBox.setItemText(1, _translate("mainWindow", "Map Design 2"))
        self.mapComboBox.setItemText(2, _translate("mainWindow", "Map Design 3"))
        self.itemCheckBox.setText(_translate("mainWindow", "Items"))
        self.simulationGoupBox.setTitle(_translate("mainWindow", "Simulation"))
        self.simSpeedLabel.setText(_translate("mainWindow", "Simulation speed:"))
        self.videoRecLabel.setText(_translate("mainWindow", "Video recording:"))
        self.xFirstLabel.setText(_translate("mainWindow", "1x"))
        self.xSecondLabel.setText(_translate("mainWindow", "5x"))
        self.xThirdLabel.setText(_translate("mainWindow", "10x"))
        self.startPushButton.setText(_translate("mainWindow", "Start"))
        self.stopPushButton.setText(_translate("mainWindow", "Stop"))
        self.savePushButton.setText(_translate("mainWindow", "Save"))
        self.startSimPushButton.setText(_translate("mainWindow", "Start Simulation"))
        self.loadPushButton.setText(_translate("mainWindow", "Load"))
        self.resetPushButton.setText(_translate("mainWindow", "Reset"))
        self.swarmDesignGroupBox.setTitle(_translate("mainWindow", "Swarm Design"))
        self.dropAlgoLabel.setText(_translate("mainWindow", " Drop .py file here"))
        self.taskLabel.setText(_translate("mainWindow", "Task:"))
        self.taskComboBox.setItemText(0, _translate("mainWindow", "Aggregation"))
        self.taskComboBox.setItemText(1, _translate("mainWindow", "Exploration"))
        self.taskComboBox.setItemText(2, _translate("mainWindow", "Foraging"))
        self.algorithmLabel.setText(_translate("mainWindow", "Algorithm:"))
        self.selectedAlgoLabel.setText(_translate("mainWindow", "selectedalgo.py"))
        self.algorithmToolButton.setText(_translate("mainWindow", "..."))

    # for debugging purposes
    def clicked(self):
        print("button is clicked")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
