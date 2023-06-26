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

    def update_velocity(self, global_best_position, inertia_weight, cognitive_weight, social_weight):
        r1 = random.random()
        r2 = random.random()

        cognitive_component = [cognitive_weight * r1 * (bp - p) for bp, p in zip(self.best_position, self.position)]
        social_component = [social_weight * r2 * (gbp - p) for gbp, p in zip(global_best_position, self.position)]

        self.velocity = [inertia_weight * v + c + s for v, c, s in zip(self.velocity, cognitive_component, social_component)]


    def evaluate_fitness(self, target):
        distance = math.sqrt((self.position[0] - target[0])**2 + (self.position[1] - target[1])**2)

        return distance

    def update_best_position(self, fitness):
        if fitness < self.best_fitness:
            self.best_fitness = fitness
            self.best_position = self.position.copy()