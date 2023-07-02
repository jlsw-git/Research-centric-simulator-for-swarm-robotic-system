import math
import random


class Particle:
    def __init__(self, x, y):
        self.position = [x, y]
        self.velocity = [random.uniform(-1, 1), random.uniform(-1, 1)]
        self.best_position = self.position.copy()
        self.best_fitness = float('inf')

    def move(self):
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]

    def update_position(self, global_best_position, inertia_weight, cognitive_weight, social_weight):
        r1 = random.random()
        r2 = random.random()

        # Cognitive component based on best position and current position
        cognitive_component = [cognitive_weight * r1 * (bp - p) for bp, p in zip(self.best_position, self.position)]

        # Social component based on global best position and current position
        social_component = [social_weight * r2 * (gbp - p) for gbp, p in zip(global_best_position, self.position)]

        """ 
        Velocity update equation for PSO:
        New velocity = Inertia weight * Old velocity + Cognitive component + Social component 
        """
        self.velocity = [(inertia_weight * v) + c + s for v, c, s in zip(self.velocity, cognitive_component, social_component)]

    def evaluate_fitness(self, target):
        # Fitness based on Euclidean distance from position robot to target, closer means better fitness
        fitness = math.sqrt((self.position[0] - target[0])**2 + (self.position[1] - target[1])**2)
        return fitness

    def update_best_position(self, fitness):
        if fitness < self.best_fitness:
            self.best_fitness = fitness
            self.best_position = self.position.copy()