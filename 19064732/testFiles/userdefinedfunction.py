# import random
#
# """User-defined functions - **algorithmName"""
# def startSimulation_algorithmName(self):
#     # Set values
#     targetLocation = [300, 300]
#     fitnessThreshold = 0.005
#
#     self.applyParameter()
#
#     self.currentIteration = 0
#     self.robots = []
#     self.fitnessList = []
#     self.posList = []
#
#     self.target = targetLocation
#     self.fitnessThreshold = fitnessThreshold
#
#     for _ in range(self.numRobots):
#         # Set range of random values for robot movement
#         x = random.randint(0, 600)
#         y = random.randint(0, 600)
#
#         fname = self.selectedAlgoLabel.text().split('.')[0]
#         robotString = "%s(x, y)" % fname
#         robot = eval(robotString)
#         self.robots.append(robot)
#
#     # Start timer and update according to updateRobot function
#     self.startSimTimer()
#
# def updateRobots_algorithmName(self):
#     # Initialize values
#     lowerFitnessIsBetter = True
#
#     globalBestFitness = 0
#
#     self.parameterWeightList = self.getDynamicParameterValues()
#
#     # Update robot positions
#     for robot in self.robots:
#         fitness = robot.evaluateFitness(self.target)
#         robot.fitness = fitness
#
#         if robot.fitness > globalBestFitness:
#             globalBestFitness = robot.fitness
#
#     # Update robot positions
#     for robot in self.robots:
#         for otherFirefly in self.robots:
#             if robot.fitness < otherFirefly.fitness:
#                 robot.updatePosition(otherFirefly, attractiveness=self.parameterWeightList[0],
#                                      stepSize=self.parameterWeightList[1])
#         robot.move()
#
#     self.savePositions()
#     self.drawScene()
#     self.fitnessList.append(globalBestFitness)
#
#     # Check termination criteria - Stop if fitness threshold or max number of iterations is reached
#     self.terminationCriteriaLowerFitnessIsBetter(lowerFitnessIsBetter)
#
#     self.displayCurrentIteration()
#     self.currentIteration += 1
# """------------------------"""