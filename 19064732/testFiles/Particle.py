import math
import random


class Particle:
    def __init__(self, x, y):
        self.position = [x, y]
        self.velocity = [random.uniform(-1, 1), random.uniform(-1, 1)]
        self.bestPosition = self.position.copy()
        self.bestFitness = float('inf')
        self.parameters = ['Inertia', 'Cognitive', 'Social']

    def move(self):
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]

    def updatePosition(self, globalBestPosition, inertiaWeight, cognitiveWeight, socialWeight):
        r1 = random.random()
        r2 = random.random()

        # Cognitive component based on best position and current position
        cognitiveComponent = [cognitiveWeight * r1 * (bp - p) for bp, p in zip(self.bestPosition, self.position)]

        # Social component based on global best position and current position
        socialComponent = [socialWeight * r2 * (gbp - p) for gbp, p in zip(globalBestPosition, self.position)]

        """ 
        Velocity update equation for PSO:
        New velocity = Inertia weight * Old velocity + Cognitive component + Social component 
        """
        self.velocity = [(inertiaWeight * v) + c + s for v, c, s in zip(self.velocity, cognitiveComponent, socialComponent)]

    def evaluateFitness(self, target):
        # Fitness based on Euclidean distance from position robot to target, closer means better fitness
        fitness = math.sqrt((self.position[0] - target[0])**2 + (self.position[1] - target[1])**2)
        return fitness

    def updateBestPosition(self, fitness):
        if fitness < self.bestFitness:
            self.bestFitness = fitness
            self.bestPosition = self.position.copy()