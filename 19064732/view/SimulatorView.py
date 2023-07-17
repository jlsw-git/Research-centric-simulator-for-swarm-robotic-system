"""Reserve line 3 for program to write import statement, by default set as pass"""
try:
    from model.Particle import Particle
except ModuleNotFoundError:
    pass
""""""

import random
import os
import sys
import cv2
import shutil
import numpy as np
import pyautogui
import matplotlib.pyplot as plt
import json
from datetime import date
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QBrush, QColor, QFont
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMainWindow, QGraphicsScene, QGraphicsView, QMessageBox


class SimulatorView(QMainWindow):
    def setupUi(self, mainWindow):
        """------------mainWindow------------"""
        # Set mainWindow properties
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(1280, 755)
        mainWindow.setMinimumSize(QtCore.QSize(1280, 755))
        mainWindow.setMaximumSize(QtCore.QSize(1280, 755))

        # Allow mainWindow to accept drops
        mainWindow.setAcceptDrops(True)

        """------------centralWidget------------"""
        self.centralWidget = QtWidgets.QWidget(mainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.scene = QGraphicsScene(self)
        self.simulationGraphicsView = QGraphicsView(self.scene, self)
        self.simulationGraphicsView.setGeometry(QtCore.QRect(370, 10, 901, 721))
        self.simulationGraphicsView.setObjectName("simulationGraphicsView")
        self.simulationGraphicsView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.simulationGraphicsView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
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

        # Apply grid pattern to graphics view background
        brush = QBrush()
        brush.setStyle(Qt.CrossPattern)
        brush.setColor(Qt.lightGray)
        self.simulationGraphicsView.setBackgroundBrush(brush)

        """------------parametersGroupBox------------"""
        self.parametersGroupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.parametersGroupBox.setGeometry(QtCore.QRect(0, 170, 331, 201))
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
        self.formLayout_2.setLayout(2, QtWidgets.QFormLayout.LabelRole, self.horizontalLayout_3)

        # Adjust agentNumberSpinBox properties
        self.agentNumberSpinBox.setMinimum(1)
        self.agentNumberSpinBox.setMaximum(1000)
        self.agentNumberSpinBox.setValue(100)
        self.agentNumberSpinBox.setSingleStep(10)

        # Adjust iterationSpinBox properties
        self.iterationSpinBox.setMinimum(1)
        self.iterationSpinBox.setMaximum(100000)
        self.iterationSpinBox.setValue(1000)
        self.iterationSpinBox.setSingleStep(100)

        # Instantiate previous algo as None
        self.prevAlgo = None

        """------------simulationGroupBox------------"""
        self.simulationGroupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.simulationGroupBox.setGeometry(QtCore.QRect(0, 380, 331, 391))
        self.simulationGroupBox.setMinimumSize(QtCore.QSize(331, 391))
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
        self.verticalLayout_4.addWidget(self.startSimPushButton)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.pauseSimPushButton = QtWidgets.QPushButton(self.layoutWidget_13)
        self.pauseSimPushButton.setObjectName("pauseSimPushButton")
        self.horizontalLayout_6.addWidget(self.pauseSimPushButton)
        self.resumeSimPushButton = QtWidgets.QPushButton(self.layoutWidget_13)
        self.resumeSimPushButton.setObjectName("resumeSimPushButton")
        self.horizontalLayout_6.addWidget(self.resumeSimPushButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
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
        self.firstIterationLabel = QtWidgets.QLabel(self.simulationGroupBox)
        self.firstIterationLabel.setGeometry(QtCore.QRect(80, 300, 21, 20))
        self.firstIterationLabel.setObjectName("firstIterationLabel")
        self.finalIterationLabel = QtWidgets.QLabel(self.simulationGroupBox)
        self.finalIterationLabel.setGeometry(QtCore.QRect(230, 300, 81, 20))
        self.finalIterationLabel.setObjectName("finalIterationLabel")
        self.iterationSpinBox_2 = QtWidgets.QSpinBox(self.simulationGroupBox)
        self.iterationSpinBox_2.setGeometry(QtCore.QRect(260, 280, 42, 22))
        self.iterationSpinBox_2.setObjectName("iterationSpinBox_2")

        # Adjust simSpeedHoriSlider properties
        self.simSpeedHoriSlider.setMinimum(10)
        self.simSpeedHoriSlider.setMaximum(250)
        self.simSpeedHoriSlider.setValue(250)
        self.simSpeedHoriSlider.setInvertedAppearance(True)

        # Adjust iterationSlider properties
        self.iterationSlider.setMinimum(0)
        self.iterationSlider.setValue(0)

        # Adjust iterationSpinBox_2 properties
        self.iterationSpinBox_2.setMinimum(0)

        # Set button default as disabled
        self.stopPushButton.setDisabled(True)
        self.resetPushButton.setDisabled(True)
        self.iterationSlider.setDisabled(True)
        self.startSimPushButton.setDisabled(True)
        self.pauseSimPushButton.setDisabled(True)
        self.resumeSimPushButton.setDisabled(True)
        self.loadPushButton.setDisabled(True)
        self.iterationSpinBox_2.setDisabled(True)

        """------------swarmDesignGroupBox------------"""
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
        self.taskLabel2 = QtWidgets.QLabel(self.layoutWidget_15)
        self.taskLabel2.setObjectName("taskLabel")
        self.verticalLayout_5.addWidget(self.taskLabel2)
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

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

        """------------Button Connections------------"""
        # startPushButton - Start video recording
        self.startPushButton.clicked.connect(self.startRecord)

        # viewRecPushButton - View video recording
        self.viewRecPushButton.clicked.connect(self.viewRecording)

        # startSimPushButton - Start simulation
        self.startSimPushButton.clicked.connect(self.startSimulation)

        # pauseSimPushButton - Pause simulation
        self.pauseSimPushButton.clicked.connect(self.pauseSimulation)

        # resumePushButton - Resume simulation
        self.resumeSimPushButton.clicked.connect(self.resumeSimulation)

        # algorithmToolButton - Select algorithm from local files
        self.algorithmToolButton.clicked.connect(self.selectAlgorithm)

        # resetPushButton - Reset simulation canvas and close plots
        self.resetPushButton.clicked.connect(self.resetScene)

        # iterationSlider - Adjust visualization according to iteration slider
        self.iterationSlider.valueChanged.connect(self.displayPosition)

        # iterationSpinBox_2 - Sync iteration spinbox to current slider value
        self.iterationSpinBox_2.valueChanged.connect(self.adjustIterationSlider)

        # loadPushButton - Load saved parameters from json file
        self.loadPushButton.clicked.connect(self.loadParameters)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Swarm Robotics Simulator"))
        self.parametersGroupBox.setTitle(_translate("mainWindow", "Parameters"))
        self.agentNumberLabel.setText(_translate("mainWindow", "Number of agents:"))
        self.iterationLabel.setText(_translate("mainWindow", "Iterations:"))
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
        self.pauseSimPushButton.setText(_translate("mainWindow", "Pause"))
        self.resumeSimPushButton.setText(_translate("mainWindow", "Resume"))
        self.loadPushButton.setText(_translate("mainWindow", "Load"))
        self.resetPushButton.setText(_translate("mainWindow", "Reset"))
        self.currentIterationLabel.setText(_translate("mainWindow", "Load Iteration:"))
        self.firstIterationLabel.setText(_translate("mainWindow", "0"))
        self.finalIterationLabel.setText(_translate("mainWindow", "-"))
        self.swarmDesignGroupBox.setTitle(_translate("mainWindow", "Swarm Design"))
        self.dropAlgoLabel.setText(_translate("mainWindow", " Drop .py here"))
        self.dropAlgoLabel.setAlignment(Qt.AlignCenter)
        self.taskLabel.setText(_translate("mainWindow", "Task:"))
        self.taskLabel2.setText(_translate("mainWindow", "Exploration"))
        self.algorithmLabel.setText(_translate("mainWindow", "Selected Algorithm:"))
        self.selectedAlgoLabel.setText(_translate("mainWindow", "Please select an algorithm."))
        self.algorithmToolButton.setText(_translate("mainWindow", "..."))

    """------------Button Event Functions------------"""
    """User-defined functions - Particle"""
    def startSimulation_Particle(self):
        # Set values
        targetLocation = [300, 300]
        fitnessThreshold = 0.005

        self.applyParameter()

        self.currentIteration = 0
        self.robots = []
        self.fitnessList = []
        self.posList = []

        self.target = targetLocation
        self.fitnessThreshold = fitnessThreshold

        for _ in range(self.numRobots):
            # Set range of random values for robot movement
            x = random.randint(0, 600)
            y = random.randint(0, 600)

            fname = self.selectedAlgoLabel.text().split('.')[0]
            robotString = "%s(x, y)" % fname
            robot = eval(robotString)
            self.robots.append(robot)

        # Start timer and update according to updateRobot function
        self.startSimTimer()

    def updateRobots_Particle(self):
        self.globalBestFitness = float('inf')
        globalBestPosition = None

        self.parameterWeightList = self.getDynamicParameterValues()

        # Update robot positions
        for robot in self.robots:
            fitness = robot.evaluateFitness(self.target)
            robot.updateBestPosition(fitness)

            if fitness < self.globalBestFitness:
                self.globalBestFitness = fitness
                globalBestPosition = robot.position.copy()

            robot.updatePosition(globalBestPosition, inertiaWeight=self.parameterWeightList[0], cognitiveWeight=self.parameterWeightList[1], socialWeight=self.parameterWeightList[2])
            robot.move()

        self.savePositions()
        self.drawScene()
        self.fitnessList.append(self.globalBestFitness)

        # Check termination criteria - Stop if fitness threshold or max number of iterations is reached
        self.terminationCriteriaLowerFitnessIsBetter(True)

        self.displayCurrentIteration()
        self.currentIteration += 1
    """------------------------"""

    """User-defined functions - Firefly"""
    def startSimulation_Firefly(self):
        # Set values
        targetLocation = [300, 300]
        fitnessThreshold = 0.5

        self.applyParameter()

        self.currentIteration = 0
        self.robots = []
        self.fitnessList = []
        self.posList = []

        self.target = targetLocation
        self.fitnessThreshold = fitnessThreshold

        for _ in range(self.numRobots):
            # Set range of random values for robot movement
            x = random.uniform(-10, 10)
            y = random.uniform(-10, 10)

            fname = self.selectedAlgoLabel.text().split('.')[0]
            robotString = "%s(x, y)" % fname
            robot = eval(robotString)
            self.robots.append(robot)

        # Start timer and update according to updateRobot function
        self.startSimTimer()

    def updateRobots_Firefly(self):
        self.globalBestFitness = 0

        self.parameterWeightList = self.getDynamicParameterValues()

        # Update robot positions
        for robot in self.robots:
            fitness = robot.evaluateFitness(self.target)
            robot.fitness = fitness

            if robot.fitness > self.globalBestFitness:
                self.globalBestFitness = robot.fitness

        # Update robot positions
        for robot in self.robots:
            for otherFirefly in self.robots:
                if robot.fitness < otherFirefly.fitness:
                    robot.updatePosition(otherFirefly, attractiveness=self.parameterWeightList[0], stepSize=self.parameterWeightList[1])
            robot.move()

        self.savePositions()
        self.drawScene()
        self.fitnessList.append(self.globalBestFitness)

        self.terminationCriteriaLowerFitnessIsBetter(False)

        self.displayCurrentIteration()
        self.currentIteration += 1
    """------------------------"""

    # To select algorithm from system files
    def selectAlgorithm(self):
        path, ftype = QFileDialog.getOpenFileName(None, "Select a Swarm Algorithm", "./model/", "PY Files (*.py)")

        # Check if user cancelled algorithm selection
        if path != '':
            # Get file name
            fname = path.split("/")[-1]       # Particle.py
            fname_only = fname.split('.')[0]  # Particle
            ext = fname.split('.')[-1]        # py
            to_path = "./model/%s" % fname

            # Initialize import statement
            importStatement = '    from model.%s import %s\n' % (fname_only, fname_only)

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

                    # Copy file to folder
                    else:
                        self.selectedAlgoLabel.setText("Added %s!" % fname)
                        shutil.copyfile(path, to_path)

                # Reject non-Python files
                else:
                    self.selectedAlgoLabel.setText("Error! Invalid file type.")

            # Read each line of the file
            with open('./view/SimulatorView.py', 'r') as file:
                lines = file.readlines()

            # If import statement does not exist, write import statement to file and restart program
            if importStatement not in lines:
                lines[2] = importStatement

                # Write import statement into this file
                with open('./view/SimulatorView.py', 'w') as file:
                    file.writelines(lines)

                # Display dialog to restart program
                restartDialog = QMessageBox()
                restartDialog.setIcon(QMessageBox.Warning)
                restartDialog.setText("Restart is required. App will restart minimised.")
                restartDialog.setWindowTitle("Swarm Robotics Simulator")
                restartDialog.setStandardButtons(QMessageBox.Ok)

                # Restart program in minimized
                result = restartDialog.exec_()
                if result == QMessageBox.Ok:
                    os.execl(sys.executable, sys.executable, *sys.argv)

            # If import already exists, add dynamic parameters to ui
            else:
                # Adjust buttons
                self.startSimPushButton.setDisabled(False)
                self.loadPushButton.setDisabled(False)

                # If algorithm is already selected, return
                if fname == self.prevAlgo:
                    return

                # Set prev algo name to current filename (default is None)
                self.prevAlgo = fname
                self.selectedAlgoLabel.setText(fname)

                # Update parameter ui dynamically
                fname = self.selectedAlgoLabel.text().split('.')[0]
                robotString = "%s(None, None)" %fname
                robot = eval(robotString)

                # Add parameters from row 3 of parameter group box, increment row for each parameter
                row = 3
                for parameter in robot.parameters:
                    # Create horizontal layout
                    hLayout = QtWidgets.QHBoxLayout()
                    setattr(self, "horizontalLayout_%s" % parameter, hLayout)

                    # Create parameter label according to paraneter name
                    parameterLabel = QtWidgets.QLabel(self.parametersGroupBox)
                    setattr(self, "label_%s" % parameter, parameterLabel)


                    # Create double spin box for each parameter label
                    parameterDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.parametersGroupBox)
                    setattr(self, "doubleSpinBox_%s" % parameter, parameterDoubleSpinBox)

                    # Adjust default properties of spin boxes
                    parameterDoubleSpinBox.setMinimum(0.01)
                    parameterDoubleSpinBox.setMaximum(1.50)
                    parameterDoubleSpinBox.setSingleStep(0.10)
                    parameterDoubleSpinBox.setValue(0.80)

                    # Add components to layout
                    hLayout.addWidget(parameterLabel)
                    hLayout.addWidget(parameterDoubleSpinBox)

                    # Add components to respective row
                    self.formLayout_2.setLayout(row, QtWidgets.QFormLayout.LabelRole, hLayout)

                    # Translate label text for main window
                    _translate = QtCore.QCoreApplication.translate
                    parameterLabel.setText(_translate("mainWindow", "%s:" % parameter))

                    # Increment row for next parameter
                    row += 1

    # To get path of dragged algorithm files
    def dragEnterEvent(self, event):
        # Accept drag if path exists, else ignore
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    # To accept path of dragged and dropped algorithm files
    def dropEvent(self, event):
        files = [u.toLocalFile() for u in event.mimeData().urls()]
        fromPath = files[0]  # C:/Users/user/Desktop/19064732/model/sample.py
        fname = fromPath.split('/')[-1]  # sample.py
        ext = fname.split('.')[-1]  # py
        toPath = "./model/%s" %fname

        # If file type is .py, add to model folder
        if ext == 'py':
            # Check if file name already exists
            if os.path.exists(toPath):
                self.selectedAlgoLabel.setText("Error! File already exists.")

            # Check if file is empty
            elif os.path.getsize(fromPath) == 0:
                self.selectedAlgoLabel.setText("Error! File is empty.")

            # Copy file to folder
            else:
                self.selectedAlgoLabel.setText("Added %s!" % fname)
                shutil.copyfile(fromPath, toPath)

        # Reject non-Python files
        else:
            self.selectedAlgoLabel.setText("Error! Invalid file type.")

    # To start simulation based on evaluated name of user-defined function
    def startSimulation(self):
        self.adjustButtonBeforeSim()

        fname = self.selectedAlgoLabel.text().split('.')[0]
        startSimFunction = eval("self.startSimulation_%s" % fname)
        startSimFunction()

    # Timer update function for simulation based on algorithm input
    def startSimTimer(self):
        # Initialize timer
        self.timer = QTimer(self)

        # Get algorithm name and its respective update function
        algoName = self.selectedAlgoLabel.text().split('.')[0]
        self.updateSimFunction = getattr(self, f"updateRobots_{algoName}")      # e.g. self.updateRobots_Particle

        # Connect simulator signal to timer, update signals based on speed value
        self.timer.timeout.connect(self.updateSimFunction)

        # Set speed of simulation according to specified value (e.g. 50 means update function signal every 50ms)
        self.timer.start(self.simSpeedHoriSlider.value())

    def drawScene(self):
        self.scene.clear()
        self.simulationGraphicsView.viewport().update()

        modelSize = 15

        for robot in self.robots:
            x = robot.position[0]
            y = robot.position[1]

            self.drawRobot(modelSize, x, y)

        self.drawTarget(modelSize)

    # To save robot positions from each iteration in a list
    def savePositions(self):
        robotPos = [robot.position.copy() for robot in self.robots]
        self.posList.append(robotPos)

    # To display position of robots according to previous simulation
    def displayPosition(self):
        self.scene.clear()
        self.simulationGraphicsView.viewport().update()
        self.iterationSpinBox_2.setValue(self.iterationSlider.sliderPosition())

        modelSize = 15

        # Draw robot positions based on saved positions with its respective iteration number
        for iterationNo in range(self.numRobots):
            x = self.posList[self.iterationSlider.sliderPosition()][iterationNo][0]
            y = self.posList[self.iterationSlider.sliderPosition()][iterationNo][1]

            self.displayCurrentIterationSlider()

            self.drawRobot(modelSize, x, y)

        self.drawTarget(modelSize)

    # To sync iterationSlider with iterationSpinBox_2
    def adjustIterationSlider(self):
        self.iterationSlider.setSliderPosition(self.iterationSpinBox_2.value())

    # To stop running simulation, remove all items from canvas, and close plots
    def resetScene(self):
        # Stop timer and disconnect function
        self.timer.stop()
        self.timer.timeout.disconnect(self.updateSimFunction)

        # Adjust buttons and values
        self.swarmDesignGroupBox.setDisabled(False)
        self.parametersGroupBox.setDisabled(False)
        self.simSpeedHoriSlider.setDisabled(False)
        self.startSimPushButton.setDisabled(False)
        self.iterationSpinBox_2.setDisabled(False)
        self.resetPushButton.setDisabled(True)
        self.iterationSlider.setDisabled(True)
        self.iterationSpinBox_2.setDisabled(True)
        self.finalIterationLabel.setText("-")
        self.iterationSpinBox_2.setValue(0)

        # Remove all scene items
        self.scene.clear()
        self.simulationGraphicsView.update()
        self.simulationGraphicsView.viewport().update()

        # Close plots
        plt.close()

    # To adjust buttons and scene before simulation starts
    def adjustButtonBeforeSim(self):
        self.scene.clear()

        self.swarmDesignGroupBox.setDisabled(True)
        self.parametersGroupBox.setDisabled(True)
        self.startSimPushButton.setDisabled(True)
        self.pauseSimPushButton.setDisabled(False)
        self.simSpeedHoriSlider.setDisabled(True)
        self.iterationSlider.setDisabled(True)
        self.iterationSpinBox_2.setDisabled(True)
        self.resetPushButton.setDisabled(False)
        self.finalIterationLabel.setText("-")
        self.iterationSpinBox_2.setValue(0)

    # To adjust buttons and scene after simulation ends
    def adjustButtonAfterSim(self):
        self.swarmDesignGroupBox.setDisabled(False)
        self.parametersGroupBox.setDisabled(False)
        self.simSpeedHoriSlider.setDisabled(False)
        self.iterationSlider.setDisabled(False)
        self.iterationSpinBox_2.setDisabled(False)
        self.iterationSlider.setDisabled(False)
        self.iterationSpinBox_2.setDisabled(False)
        self.startSimPushButton.setDisabled(False)
        self.iterationSlider.setMaximum(self.currentIteration)
        self.iterationSpinBox_2.setMaximum(self.currentIteration)
        self.finalIterationLabel.setText(str(self.currentIteration))
        self.iterationSlider.setValue(self.currentIteration)
        self.iterationSpinBox_2.setValue(self.currentIteration)

    # To plot graphs
    def plotGraphs(self):
        iterationList = list(range(0, self.currentIteration + 1))

        plt.plot(iterationList, self.fitnessList)
        plt.xlabel('Iterations')
        plt.ylabel('Fitness value')
        plt.title('Swarm Fitness vs. Iteration')
        plt.get_current_fig_manager().window.setGeometry(320, 190, 500, 500)
        plt.grid(linestyle='dotted')
        plt.show()

    # To display current iteration on scene
    def displayCurrentIteration(self):
        iterationText = self.scene.addText("Iteration: %s" % str(self.currentIteration))
        font = QFont()
        font.setPointSize(20)
        iterationText.setFont(font)
        iterationText.setPos(0, 0)

    # To display current iteration for iterationSlider on scene
    def displayCurrentIterationSlider(self):
        iterationTextSlider = self.scene.addText("Iteration: %s" % str(self.iterationSlider.value()))
        font = QFont()
        font.setPointSize(20)
        iterationTextSlider.setFont(font)
        iterationTextSlider.setPos(0, 0)

    # To draw a blue circle representing robot
    def drawRobot(self, size, x, y):
        robotBrush = QBrush(QColor(Qt.blue))

        self.scene.addEllipse(x - size / 2, y - size / 2, size, size, brush=robotBrush)

    # To draw a red circle representing target
    def drawTarget(self, size):
        targetBrush = QBrush(Qt.red)
        self.scene.addEllipse(self.target[0] - size / 2, self.target[1] - size / 2, size, size, brush=targetBrush)

    # To apply base parameter values from simulator
    def applyParameter(self):
        # Apply parameter values
        self.numRobots = self.agentNumberSpinBox.value()
        self.numIterations = self.iterationSpinBox.value()

    # To get dynamic parameter values in a list
    def getDynamicParameterValues(self):
        fname = self.selectedAlgoLabel.text().split('.')[0]
        robotString = "%s(None,None)" % fname
        robot = eval(robotString)

        parameterWeightList = []
        for parameter in robot.parameters:
            parameterValue = getattr(self, f"doubleSpinBox_{parameter}").value()
            parameterWeightList.append(parameterValue)

        return parameterWeightList

    # To save all parameter values in a JSON file to parameters folder
    def saveParameters(self):
        # Prompt user in dialog if they want to save the parameters
        saveParameterDialog = QMessageBox()
        saveParameterDialog.setIcon(QMessageBox.Question)
        saveParameterDialog.setText("Save current parameters?")
        saveParameterDialog.setWindowTitle("Swarm Robotics Simulator")
        saveParameterDialog.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

        yesNoResult = saveParameterDialog.exec_()
        if yesNoResult == QMessageBox.Yes:
            """Format: parameters = [Agents, Iterations, **any other parameters]"""
            parameters = [self.agentNumberSpinBox.value(), self.iterationSpinBox.value()]
            parameters = parameters + self.parameterWeightList

            # Write to parameters folder as json file, with incrementing filename
            counter = 0
            algoName = self.selectedAlgoLabel.text().split('.')[0]

            filename = "%s_parameters_%s.json" % (algoName, counter)
            toPath = "./parameters/" + filename

            while os.path.exists(toPath):
                counter += 1
                filename = "%s_parameters_%s.json" % (algoName, counter)
                toPath = "./parameters/" + filename

            with open(toPath, 'w') as file:
                json.dump(parameters, file)

    # To load parameters from JSON file into simulator
    def loadParameters(self):
        fromPath, ftype = QFileDialog.getOpenFileName(None, "Select a parameter file", "./parameters/", "JSON Files (*.json)")

        # Check if user cancelled loading parameters
        if fromPath != '':
            # Load JSON parameter file
            with open(fromPath, 'r') as file:
                jsonParameters = json.load(file)

            # Set parameter values
            self.agentNumberSpinBox.setValue(jsonParameters[0])
            self.iterationSpinBox.setValue(jsonParameters[1])

            # Set dynamic parameter values
            counter = 2
            fname = self.selectedAlgoLabel.text().split('.')[0]
            robotString = "%s(None,None)" % fname
            robot = eval(robotString)
            for parameter in robot.parameters:
                getattr(self, f"doubleSpinBox_{parameter}").setValue(jsonParameters[counter])
                counter += 1

    # To start recording of current screen
    def startRecord(self):
        # Adjust recording buttons
        self.startPushButton.setDisabled(True)
        self.stopPushButton.setDisabled(False)

        # Create video filename with incrementing number for new videos
        counter = 0
        current_date = str(date.today())
        clean_date = current_date.replace("-", "")
        filename = "VID%s_%s.mp4" % (clean_date, counter)
        filepath = "./recordings/" + filename

        while os.path.exists(filepath):
            counter += 1
            filename = "VID%s_%s.mp4" % (clean_date, counter)
            filepath = "./recordings/" + filename

        # Specify video codec
        codec = cv2.VideoWriter_fourcc(*"mp4v")

        # Specify frame rate
        fps = 20.0

        # Specify resolution of video
        width, height = pyautogui.size()
        res = (width, height)

        # Create VideoWriter object
        output = cv2.VideoWriter(filepath, codec, fps, res)

        # Create empty window
        cv2.namedWindow("Recording.. ('Q' to stop)", cv2.WINDOW_NORMAL)

        # Resize window
        cv2.resizeWindow("Recording.. ('Q' to stop)", 300, 200)

        # Move window to top left corner
        cv2.moveWindow("Recording.. ('Q' to stop)", 0, 0)

        # Loop to take screenshots and write to file
        while True:
            # Take screenshot using PyAutoGUI
            img = pyautogui.screenshot()

            # Convert the screenshot to numpy array
            frame = np.array(img)

            # Convert from BGR to RGB
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Write output to file
            output.write(frame)

            # Display recording window
            cv2.imshow("Recording.. ('Q' to stop)", frame)

            # Wait for keystroke 'q' or stopPushButton to be clicked
            if cv2.waitKey(1) == ord('q') or self.stopPushButton.isDown():
                self.startPushButton.setDisabled(False)
                self.stopPushButton.setDisabled(True)
                break

        # Release VideoWriter object
        output.release()

        # Close all windows
        cv2.destroyAllWindows()

    # To view saved recordings
    def viewRecording(self):
        path, ftype = QFileDialog.getOpenFileName(None, "View Video Recording", "./recordings/",
                                                  "Video Files (*.mp4)")

        # Open file explorer according to path
        if path != "":
            os.startfile(path)

    def terminationCriteriaLowerFitnessIsBetter(self, status: bool):
        if status:
            # Stop if fitness is low or max iterations is reached
            if self.globalBestFitness < self.fitnessThreshold or self.currentIteration >= self.numIterations:
                self.timer.stop()
                self.saveParameters()
                self.adjustButtonAfterSim()
                self.plotGraphs()
        else:
            # Stop if fitness is high or max iterations is reached
            if self.globalBestFitness > self.fitnessThreshold or self.currentIteration >= self.numIterations:
                self.timer.stop()
                self.saveParameters()
                self.adjustButtonAfterSim()
                self.plotGraphs()

    def pauseSimulation(self):
        self.startSimPushButton.setDisabled(False)
        self.pauseSimPushButton.setDisabled(True)
        self.resumeSimPushButton.setDisabled(False)

        self.timer.stop()

    def resumeSimulation(self):
        self.pauseSimPushButton.setDisabled(False)
        self.resumeSimPushButton.setDisabled(True)

        self.timer.start()