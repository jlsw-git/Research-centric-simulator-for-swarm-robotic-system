import math
import random


class Firefly:
    def __init__(self, x, y):
        self.position = [x, y]
        self.fitness = float('inf')

    def move(self):
        self.position[0] += random.uniform(-10, 10)
        self.position[1] += random.uniform(-10, 10)

    def update_position(self, other_firefly, attractiveness, step_size):
        distance = math.sqrt((self.position[0] - other_firefly.position[0])**2 + (self.position[1] - other_firefly.position[1])**2)
        attractiveness_factor = attractiveness / (1 + distance**2)
        random_step = random.uniform(-step_size, step_size)

        self.position[0] = self.position[0] + attractiveness_factor * (other_firefly.position[0] - self.position[0]) + random_step
        self.position[1] = self.position[1] + attractiveness_factor * (other_firefly.position[1] - self.position[1]) + random_step

    def evaluate_fitness(self, target):
        # fitness = math.sqrt((self.position[0] - target[0])**2 + (self.position[1] - target[1])**2)
        # self.best_fitness = 1 / (1 + fitness)  # Inverse of distance as intensity
        self.fitness = 1 / (1 + (math.sqrt((self.position[0] - target[0])**2 + (self.position[1] - target[1])**2)))