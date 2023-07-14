import math
import random


class Firefly:
    def __init__(self, x, y):
        self.position = [x, y]
        self.fitness = float('inf')

    def move(self):
        self.position[0] += random.uniform(-10, 10)
        self.position[1] += random.uniform(-10, 10)

    def updatePosition(self, otherFirefly, attractiveness, stepSize):
        distance = math.sqrt((self.position[0] - otherFirefly.position[0])**2 + (self.position[1] - otherFirefly.position[1])**2)
        attractivenessFactor = attractiveness / (1 + distance**2)
        randomStep = random.uniform(-stepSize, stepSize)

        self.position[0] = self.position[0] + attractivenessFactor * (otherFirefly.position[0] - self.position[0]) + randomStep
        self.position[1] = self.position[1] + attractivenessFactor * (otherFirefly.position[1] - self.position[1]) + randomStep

    def evaluateFitness(self, target):
        self.fitness = 1 / (1 + (math.sqrt((self.position[0] - target[0])**2 + (self.position[1] - target[1])**2)))