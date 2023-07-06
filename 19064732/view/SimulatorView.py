"""Reserve 3rd line to write import statement"""
try:
    from model.Firefly import Firefly
except ModuleNotFoundError:
    pass

import random
import os
import sys
import cv2
import shutil
import numpy as np
import pyautogui
import matplotlib.pyplot as plt
from datetime import date
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QBrush, QColor, QFont
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMainWindow, QGraphicsScene, QGraphicsView, QMessageBox


class SimulatorView(QMainWindow):
    def setupUi(self, mainWindow):
        """ mainWindow """
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(1280, 755)
        mainWindow.setMinimumSize(QtCore.QSize(1280, 755))
        mainWindow.setMaximumSize(QtCore.QSize(1280, 755))
        mainWindow.setAcceptDrops(True)

        """ centralWidget """
        self.centralWidget = QtWidgets.QWidget(mainWindow)
        self.centralWidget.setObjectName("centralWidget")

        self.scene = QGraphicsScene(self)
        self.simulationGraphicsView = QGraphicsView(self.scene, self)
        self.simulationGraphicsView.setGeometry(QtCore.QRect(370, 10, 901, 721))
        self.simulationGraphicsView.setObjectName("simulationGraphicsView")
        self.simulationGraphicsView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.simulationGraphicsView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        # Apply grid pattern to graphics view
        brush = QBrush()
        brush.setStyle(Qt.CrossPattern)
        brush.setColor(Qt.lightGray)
        self.simulationGraphicsView.setBackgroundBrush(brush)

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

        """ parametersGroupBox """
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
        self.agentNumberSpinBox.setMinimum(1)
        self.agentNumberSpinBox.setMaximum(1000)
        self.agentNumberSpinBox.setValue(100)
        self.horizontalLayout.addWidget(self.agentNumberSpinBox)

        self.formLayout_2.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.iterationLabel = QtWidgets.QLabel(self.parametersGroupBox)
        self.iterationLabel.setObjectName("iterationLabel")
        self.horizontalLayout_2.addWidget(self.iterationLabel)

        self.iterationSpinBox = QtWidgets.QSpinBox(self.parametersGroupBox)
        self.iterationSpinBox.setObjectName("iterationSpinBox")
        self.iterationSpinBox.setMinimum(1)
        self.iterationSpinBox.setMaximum(100000)
        self.iterationSpinBox.setValue(500)
        self.horizontalLayout_2.addWidget(self.iterationSpinBox)

        self.formLayout_2.setLayout(1, QtWidgets.QFormLayout.LabelRole, self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        self.velocityLabel = QtWidgets.QLabel(self.parametersGroupBox)
        self.velocityLabel.setObjectName("velocityLabel")
        self.horizontalLayout_3.addWidget(self.velocityLabel)

        self.velocityDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.parametersGroupBox)
        self.velocityDoubleSpinBox.setObjectName("velocityDoubleSpinBox")
        self.velocityDoubleSpinBox.setMinimum(10)
        self.velocityDoubleSpinBox.setMaximum(1000)
        self.horizontalLayout_3.addWidget(self.velocityDoubleSpinBox)

        self.formLayout_2.setLayout(2, QtWidgets.QFormLayout.LabelRole, self.horizontalLayout_3)

        """ mapGroupBox """
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

        """ simulationGroupBox """
        self.simulationGroupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.simulationGroupBox.setGeometry(QtCore.QRect(0, 450, 331, 371))
        self.simulationGroupBox.setMinimumSize(QtCore.QSize(331, 371))
        self.simulationGroupBox.setAutoFillBackground(True)
        self.simulationGroupBox.setObjectName("simulationGroupBox")

        self.simSpeedLabel = QtWidgets.QLabel(self.simulationGroupBox)
        self.simSpeedLabel.setGeometry(QtCore.QRect(10, 30, 91, 16))
        self.simSpeedLabel.setObjectName("simSpeedLabel")

        self.videoRecLabel = QtWidgets.QLabel(self.simulationGroupBox)
        self.videoRecLabel.setGeometry(QtCore.QRect(10, 120, 81, 20))
        self.videoRecLabel.setObjectName("videoRecLabel")

        self.simSpeedHoriSlider = QtWidgets.QSlider(self.simulationGroupBox)
        self.simSpeedHoriSlider.setGeometry(QtCore.QRect(80, 60, 160, 22))
        self.simSpeedHoriSlider.setOrientation(QtCore.Qt.Horizontal)
        self.simSpeedHoriSlider.setObjectName("simSpeedHoriSlider")
        self.simSpeedHoriSlider.setMinimum(50)
        self.simSpeedHoriSlider.setMaximum(250)
        self.simSpeedHoriSlider.setValue(250)
        self.simSpeedHoriSlider.setInvertedAppearance(True)

        self.xFirstLabel = QtWidgets.QLabel(self.simulationGroupBox)
        self.xFirstLabel.setGeometry(QtCore.QRect(80, 90, 20, 20))
        self.xFirstLabel.setObjectName("xFirstLabel")

        self.xSecondLabel = QtWidgets.QLabel(self.simulationGroupBox)
        self.xSecondLabel.setGeometry(QtCore.QRect(160, 90, 20, 20))
        self.xSecondLabel.setObjectName("xSecondLabel")

        self.xThirdLabel = QtWidgets.QLabel(self.simulationGroupBox)
        self.xThirdLabel.setGeometry(QtCore.QRect(230, 90, 21, 20))
        self.xThirdLabel.setObjectName("xThirdLabel")

        self.layoutWidget_13 = QtWidgets.QWidget(self.simulationGroupBox)
        self.layoutWidget_13.setGeometry(QtCore.QRect(50, 150, 241, 96))
        self.layoutWidget_13.setObjectName("layoutWidget_13")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget_13)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")

        self.startPushButton = QtWidgets.QPushButton(self.layoutWidget_13)
        self.startPushButton.setObjectName("startPushButton")

        self.stopPushButton = QtWidgets.QPushButton(self.layoutWidget_13)
        self.stopPushButton.setObjectName("stopPushButton")
        self.stopPushButton.setDisabled(True)
        self.horizontalLayout_4.addWidget(self.startPushButton)
        self.horizontalLayout_4.addWidget(self.stopPushButton)

        self.viewRecPushButton = QtWidgets.QPushButton(self.layoutWidget_13)
        self.viewRecPushButton.setObjectName("viewRecPushButton")
        self.horizontalLayout_4.addWidget(self.viewRecPushButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.horizontalLine = QtWidgets.QFrame(self.layoutWidget_13)
        self.horizontalLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.horizontalLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.horizontalLine.setObjectName("horizontalLine")
        self.verticalLayout_4.addWidget(self.horizontalLine)

        self.startSimPushButton = QtWidgets.QPushButton(self.layoutWidget_13)
        self.startSimPushButton.setObjectName("startSimPushButton")
        self.startSimPushButton.setDisabled(True)
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

        self.currentIterationLabel = QtWidgets.QLabel(self.simulationGroupBox)
        self.currentIterationLabel.setGeometry(QtCore.QRect(10, 260, 80, 13))
        self.currentIterationLabel.setObjectName("currentIterationLabel")

        self.iterationSlider = QtWidgets.QSlider(self.simulationGroupBox)
        self.iterationSlider.setGeometry(QtCore.QRect(80, 280, 160, 22))
        self.iterationSlider.setOrientation(QtCore.Qt.Horizontal)
        self.iterationSlider.setObjectName("iterationSlider")
        self.iterationSlider.setMinimum(0)
        self.iterationSlider.setValue(0)
        self.iterationSlider.setDisabled(True)

        self.firstIterationLabel = QtWidgets.QLabel(self.simulationGroupBox)
        self.firstIterationLabel.setGeometry(QtCore.QRect(80, 300, 21, 20))
        self.firstIterationLabel.setObjectName("firstIterationLabel")

        self.finalIterationLabel = QtWidgets.QLabel(self.simulationGroupBox)
        self.finalIterationLabel.setGeometry(QtCore.QRect(230, 300, 81, 20))
        self.finalIterationLabel.setObjectName("finalIterationLabel")

        self.iterationSpinBox_2 = QtWidgets.QSpinBox(self.simulationGroupBox)
        self.iterationSpinBox_2.setGeometry(QtCore.QRect(260, 280, 42, 22))
        self.iterationSpinBox_2.setObjectName("iterationSpinBox_2")
        self.iterationSpinBox_2.setMinimum(0)
        self.iterationSpinBox_2.setDisabled(True)

        """ swarmDesignGroupBox """
        self.swarmDesignGroupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.swarmDesignGroupBox.setGeometry(QtCore.QRect(0, 0, 331, 151))
        self.swarmDesignGroupBox.setMinimumSize(QtCore.QSize(331, 151))
        self.swarmDesignGroupBox.setAutoFillBackground(True)
        self.swarmDesignGroupBox.setObjectName("swarmDesignGroupBox")

        self.dropFrame = QtWidgets.QFrame(self.swarmDesignGroupBox)
        self.dropFrame.setGeometry(QtCore.QRect(190, 70, 91, 71))
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
        self.algorithmLabel.setGeometry(QtCore.QRect(150, 31, 55, 20))
        self.algorithmLabel.setMinimumSize(QtCore.QSize(100, 20))
        self.algorithmLabel.setMaximumSize(QtCore.QSize(100, 20))
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
        mainWindow.setTabOrder(self.stopPushButton, self.viewRecPushButton)
        mainWindow.setTabOrder(self.viewRecPushButton, self.startSimPushButton)
        mainWindow.setTabOrder(self.startSimPushButton, self.loadPushButton)
        mainWindow.setTabOrder(self.loadPushButton, self.resetPushButton)
        mainWindow.setTabOrder(self.resetPushButton, self.scrollArea)
        mainWindow.setTabOrder(self.scrollArea, self.simulationGraphicsView)

        """ Button Connections """
        # startPushButton - Start Video Recording
        self.startPushButton.clicked.connect(self.startRecord)

        # viewRecPushButton - View Video Recording
        self.viewRecPushButton.clicked.connect(self.viewRecording)

        # startSimPushButton - Start Simulation
        self.startSimPushButton.clicked.connect(self.startSimulation)

        # algorithmToolButton - Select Algorithm from Local Files
        self.algorithmToolButton.clicked.connect(self.selectAlgorithm)

        # resetPushButton - Reset simulation
        self.resetPushButton.clicked.connect(self.resetScene)

        # iterationSlider - Adjust visualization according to iteration slider
        self.iterationSlider.valueChanged.connect(self.displayPosition)

        # iterationSpinBox_2 - Sync iteration spinbox to current slider value
        self.iterationSpinBox_2.valueChanged.connect(self.adjustIterationSlider)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Swarm Robotics Simulator"))
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
        self.simulationGroupBox.setTitle(_translate("mainWindow", "Simulation"))
        self.simSpeedLabel.setText(_translate("mainWindow", "Simulation speed:"))
        self.videoRecLabel.setText(_translate("mainWindow", "Video recording:"))
        self.xFirstLabel.setText(_translate("mainWindow", "1x"))
        self.xSecondLabel.setText(_translate("mainWindow", "5x"))
        self.xThirdLabel.setText(_translate("mainWindow", "10x"))
        self.startPushButton.setText(_translate("mainWindow", "Start Rec"))
        self.stopPushButton.setText(_translate("mainWindow", "Stop Rec"))
        self.viewRecPushButton.setText(_translate("mainWindow", "View Rec"))
        self.startSimPushButton.setText(_translate("mainWindow", "Start Simulation"))
        self.loadPushButton.setText(_translate("mainWindow", "Load"))
        self.resetPushButton.setText(_translate("mainWindow", "Reset"))
        self.currentIterationLabel.setText(_translate("mainWindow", "Load Iteration:"))
        self.firstIterationLabel.setText(_translate("mainWindow", "0"))
        self.finalIterationLabel.setText(_translate("mainWindow", "-"))
        self.swarmDesignGroupBox.setTitle(_translate("mainWindow", "Swarm Design"))
        self.dropAlgoLabel.setText(_translate("mainWindow", " Drop .py here"))
        self.dropAlgoLabel.setAlignment(Qt.AlignCenter)
        self.taskLabel.setText(_translate("mainWindow", "Task:"))
        self.taskComboBox.setItemText(0, _translate("mainWindow", "Aggregation"))
        self.taskComboBox.setItemText(1, _translate("mainWindow", "Exploration"))
        self.taskComboBox.setItemText(2, _translate("mainWindow", "Foraging"))
        self.algorithmLabel.setText(_translate("mainWindow", "Selected Algorithm:"))
        self.selectedAlgoLabel.setText(_translate("mainWindow", "Please select an algorithm."))
        self.algorithmToolButton.setText(_translate("mainWindow", "..."))

    """ Object Event Functions """
    # To start recording of current screen
    def startRecord(self):

        self.startPushButton.setDisabled(True)
        self.stopPushButton.setDisabled(False)

        # Specify resolution of video
        width, height = pyautogui.size()
        res = (width, height)

        # Specify video codec
        codec = cv2.VideoWriter_fourcc(*"mp4v")

        # Create new filename with incrementing number
        counter = 0
        current_date = str(date.today())
        clean_date = current_date.replace("-", "")
        filename = "VID%s_%s.mp4" % (clean_date, counter)
        filepath = "./recordings/" + filename

        while os.path.exists(filepath):
            counter += 1
            filename = "VID%s_%s.mp4" % (clean_date, counter)
            filepath = "./recordings/" + filename

        # Specify frame rate
        fps = 20.0

        # Create VideoWriter object
        out = cv2.VideoWriter(filepath, codec, fps, res)

        # Create empty window
        cv2.namedWindow("Recording.. ('Q' to stop)", cv2.WINDOW_NORMAL)

        # Resize window
        cv2.resizeWindow("Recording.. ('Q' to stop)", 300, 200)

        # Move window to top left corner
        cv2.moveWindow("Recording.. ('Q' to stop)", 0, 0)

        while True:
            # Take screenshot using PyAutoGUI
            img = pyautogui.screenshot()

            # Convert the screenshot to numpy array
            frame = np.array(img)

            # Convert from BGR(Blue, Green, Red) to RGB(Red, Green, Blue)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Write to the output file
            out.write(frame)

            # Display recording screen
            cv2.imshow("Recording.. ('Q' to stop)", frame)

            # Wait for keystroke 'q' or stopPushButton to be clicked
            if cv2.waitKey(1) == ord('q') or self.stopPushButton.isDown():
                self.startPushButton.setDisabled(False)
                self.stopPushButton.setDisabled(True)
                break

        # Release VideoWriter
        out.release()

        # Close all windows
        cv2.destroyAllWindows()

    def viewRecording(self):
        path, ftype = QFileDialog.getOpenFileName(None, "View Video Recording", "./recordings/",
                                                  "Video Files (*.mp4)")

        if path != "":
            os.startfile(path)

    # To select algorithm from system files
    def selectAlgorithm(self):
        path, ftype = QFileDialog.getOpenFileName(None, "Select a Swarm Algorithm", "./model/", "PY Files (*.py)")

        if path != '':
            # Get file name
            fname = path.split("/")[-1]       # Particle.py
            fname_only = fname.split('.')[0]  # Particle
            ext = fname.split('.')[-1]        # py
            to_path = "./model/%s" % fname
            import_statement = '    from model.%s import %s\n' % (fname_only, fname_only)

            # Check if file exists in model folder
            if not (os.path.exists(to_path)):
                # If file type is .py, add to model folder
                if ext == 'py':
                    # Check if file name already exists
                    if os.path.exists(to_path):
                        self.selectedAlgoLabel.setText("Error! File already exists.")

                    # Check if file is empty
                    elif os.path.getsize(path) == 0:
                        self.selectedAlgoLabel.setText("Error! File is empty.")

                    else:
                        self.selectedAlgoLabel.setText("Added %s!" % fname)
                        shutil.copyfile(path, to_path)

                else:
                    self.selectedAlgoLabel.setText("Error! Invalid file type.")

            # Read the contents of the file
            with open('./view/SimulatorView.py', 'r') as file:
                lines = file.readlines()

            # Check if the import already exists
            if import_statement not in lines:
                lines[2] = import_statement

                # Write import statement into this file
                with open('./view/SimulatorView.py', 'w') as file:
                    file.writelines(lines)

                # Display dialog to restart program
                restart_dialog = QMessageBox()
                restart_dialog.setText("Restart is required. App will restart minimised.")
                restart_dialog.setWindowTitle("Swarm Robotics Simulator")
                restart_dialog.setStandardButtons(QMessageBox.Ok)

                result = restart_dialog.exec_()
                if result == QMessageBox.Ok:
                    # Close program
                    # exit()
                    os.execl(sys.executable, sys.executable, *sys.argv)

            else:
                self.startSimPushButton.setDisabled(False)
                self.selectedAlgoLabel.setText(fname)

    # To get path of dragged algorithm files
    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    # To accept path of dropped algorithm files
    def dropEvent(self, event):
        files = [u.toLocalFile() for u in event.mimeData().urls()]
        from_path = files[0]  # C:/Users/user/Desktop/19064732/model/sample.py
        fname = from_path.split('/')[-1]  # sample.py
        ext = fname.split('.')[-1]  # py
        to_path = "./model/%s" %fname

        # If file type is .py, add to model folder
        if ext == 'py':
            # Check if file name already exists
            if os.path.exists(to_path):
                self.selectedAlgoLabel.setText("Error! File already exists.")

            # Check if file is empty
            elif os.path.getsize(from_path) == 0:
                self.selectedAlgoLabel.setText("Error! File is empty.")

            else:
                self.selectedAlgoLabel.setText("Added %s!" % fname)
                shutil.copyfile(from_path, to_path)

        else:
            self.selectedAlgoLabel.setText("Error! Invalid file type.")

        """ Incomplete section
        # Apply selected algorithm into simulation
        """

    def startSimulation(self):
        self.adjustButtonBeforeSim()

        fname = self.selectedAlgoLabel.text().split('.')[0]
        startSimFunction = eval("self.startSimulation_%s" % fname)
        startSimFunction()

    """User-defined"""
    def startSimulation_Particle(self):
        # Apply parameter values
        self.num_robots = self.agentNumberSpinBox.value()
        self.num_iterations = self.iterationSpinBox.value()

        self.current_iteration = 0
        self.target = [300, 300]
        self.robots = []
        self.fitness_list = []
        self.fitness_threshold = 0.005

        self.pos_list = []

        for _ in range(self.num_robots):
            x = random.randint(0, 600)
            y = random.randint(0, 600)
            robot = Particle(x, y)
            self.robots.append(robot)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_robots_PSO)
        self.timer.start(self.simSpeedHoriSlider.value())

    def startSimulation_Firefly(self):
        # Apply parameter values
        self.num_robots = self.agentNumberSpinBox.value()
        self.num_iterations = self.iterationSpinBox.value()

        self.current_iteration = 0
        self.target = [300, 300]
        self.robots = []
        self.fitness_list = []
        self.fitness_threshold = 0.2

        self.pos_list = []

        # Initialize population
        for _ in range(self.num_robots):
            x = random.uniform(-10, 10)
            y = random.uniform(-10, 10)
            robot = Firefly(x, y)
            self.robots.append(robot)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_robots_FA)
        self.timer.start(self.simSpeedHoriSlider.value())

    def update_robots_PSO(self):
        global_best_fitness = float('inf')
        global_best_position = None

        for robot in self.robots:
            fitness = robot.evaluate_fitness(self.target)
            robot.update_best_position(fitness)

            if fitness < global_best_fitness:
                global_best_fitness = fitness
                global_best_position = robot.position.copy()

            robot.update_position(global_best_position, 0.7, 1.2, 1)
            robot.move()

        self.savePositions()
        self.draw_scene()
        self.simulationGraphicsView.viewport().update()
        self.fitness_list.append(global_best_fitness)

        # Check termination criteria - Stop if fitness threshold or max number of iterations is reached
        if global_best_fitness < self.fitness_threshold or self.current_iteration >= self.num_iterations:
            self.adjustButtonAfterSim()
            self.plotGraphs()

        self.displayCurrentIteration()
        self.current_iteration += 1

    def update_robots_FA(self):
        global_best_fitness = 0

        for robot in self.robots:
            robot.evaluate_fitness(self.target)

            if robot.fitness > global_best_fitness:
                global_best_fitness = robot.fitness

        for robot in self.robots:
            for other_firefly in self.robots:
                if robot.fitness < other_firefly.fitness:
                    robot.update_position(other_firefly, attractiveness=1, step_size=0.5)

        for robot in self.robots:
            robot.move()

        self.savePositions()
        self.draw_scene()
        self.simulationGraphicsView.viewport().update()
        self.fitness_list.append(global_best_fitness)

        # Check termination criteria - Stop if fitness threshold or max number of iterations is reached
        if global_best_fitness > self.fitness_threshold or self.current_iteration >= self.num_iterations:
            self.adjustButtonAfterSim()
            self.plotGraphs()

        self.displayCurrentIteration()
        self.current_iteration += 1

    """"""

    def draw_scene(self):
        self.scene.clear()
        self.simulationGraphicsView.viewport().update()

        model_size = 15

        for robot in self.robots:
            x = robot.position[0]
            y = robot.position[1]

            self.drawRobot(model_size, x, y)

        self.drawTarget(model_size)

    def savePositions(self):
        pos = [robot.position.copy() for robot in self.robots]
        self.pos_list.append(pos)

    def displayPosition(self):
        self.scene.clear()
        self.simulationGraphicsView.viewport().update()
        self.iterationSpinBox_2.setValue(self.iterationSlider.sliderPosition())

        model_size = 15

        for iterationNo in range(self.num_robots):
            x = self.pos_list[self.iterationSlider.sliderPosition()][iterationNo][0]
            y = self.pos_list[self.iterationSlider.sliderPosition()][iterationNo][1]

            self.displayCurrentIteration()

            self.drawRobot(model_size, x, y)

        self.drawTarget(model_size)

    def adjustIterationSlider(self):
        self.iterationSlider.setSliderPosition(self.iterationSpinBox_2.value())

    def resetScene(self):
        self.finalIterationLabel.setText("-")
        self.iterationSpinBox_2.setValue(0)
        self.scene.clear()
        self.simulationGraphicsView.update()
        self.simulationGraphicsView.viewport().update()
        self.iterationSlider.setDisabled(True)
        self.iterationSpinBox_2.setDisabled(True)

        plt.close()

        """ Incomplete - implement stop running simulation """
        # self.startSimPushButton.setDisabled(False)

    def adjustButtonBeforeSim(self):
        self.scene.clear()

        self.swarmDesignGroupBox.setDisabled(True)
        self.parametersGroupBox.setDisabled(True)

        self.startSimPushButton.setDisabled(True)
        self.finalIterationLabel.setText("-")
        self.iterationSpinBox_2.setValue(0)
        self.simSpeedHoriSlider.setDisabled(True)

        self.iterationSlider.setDisabled(True)
        self.iterationSpinBox_2.setDisabled(True)

    def adjustButtonAfterSim(self):
        self.timer.stop()

        self.swarmDesignGroupBox.setDisabled(False)
        self.parametersGroupBox.setDisabled(False)

        self.simSpeedHoriSlider.setDisabled(False)

        self.iterationSlider.setDisabled(False)
        self.iterationSpinBox_2.setDisabled(False)

        self.startSimPushButton.setDisabled(False)
        self.finalIterationLabel.setText(str(self.current_iteration))
        self.iterationSlider.setMaximum(self.current_iteration)
        self.iterationSpinBox_2.setMaximum(self.current_iteration)
        self.iterationSlider.setValue(self.current_iteration)
        self.iterationSpinBox_2.setValue(self.current_iteration)
        self.iterationSlider.setDisabled(False)
        self.iterationSpinBox_2.setDisabled(False)

    def plotGraphs(self):
        # Plot graphs
        iteration_list = list(range(0, self.current_iteration + 1))

        plt.plot(iteration_list, self.fitness_list)
        plt.xlabel('Iterations')
        plt.ylabel('Fitness value')
        plt.title('Swarm Fitness vs. Iteration')
        plt.get_current_fig_manager().window.setGeometry(320, 190, 500, 500)
        plt.grid(linestyle='dotted')
        plt.show()

    # Display current iteration
    def displayCurrentIteration(self):
        iterationText = self.scene.addText("Iteration: %s" % str(self.current_iteration))
        font = QFont()
        font.setPointSize(20)
        iterationText.setFont(font)
        iterationText.setPos(0, 0)

    # Draw robot as a blue circle
    def drawRobot(self, size, x, y):
        robot_color = QColor(Qt.blue)
        robot_brush = QBrush(robot_color)

        self.scene.addEllipse(x - size / 2, y - size / 2, size, size, brush=robot_brush)

    # Draw target as a red circle
    def drawTarget(self, size):
        target_brush = QBrush(Qt.red)
        self.scene.addEllipse(self.target[0] - size / 2, self.target[1] - size / 2, size, size, brush=target_brush)