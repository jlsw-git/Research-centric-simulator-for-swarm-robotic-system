import math
import random


class Firefly:
    def __init__(self, x, y):
        self.position = [x, y]
        self.velocity = [random.uniform(-10, 10), random.uniform(-10, 10)]
        self.intensity = None

    def move(self):
        self.position[0] += random.uniform(-10, 10)
        self.position[1] += random.uniform(-10, 10)

    """ #use kwargss here?"""
    def update_position(self, other_firefly, attractiveness):
        distance = math.sqrt((self.position[0] - other_firefly.position[0])**2 + (self.position[1] - other_firefly.position[1])**2)
        attractiveness_factor = attractiveness / (1 + distance**2)
        random_step = random.uniform(-0.5, 0.5)

        self.position[0] = self.position[0] + attractiveness_factor * (other_firefly.position[0] - self.position[0]) + random_step
        self.position[1] = self.position[1] + attractiveness_factor * (other_firefly.position[1] - self.position[1]) + random_step

    def evaluate_intensity(self, target):
        # distance = self.intensity = 1 / (1 + (math.sqrt((self.position[0] - target[0])**2 + (self.position[1] - target[1])**2)))
        distance = math.sqrt((self.position[0] - target[0])**2 + (self.position[1] - target[1])**2)
        self.intensity = 1 / (1 + distance)  # Inverse of distance as intensity


# def firefly_algorithm(population_size, target, attractiveness, max_iterations):
#     population = []
#     global_best_firefly = None
#     global_best_intensity = 0
#
#     # Initialize population
#     for _ in range(population_size):
#         x = random.uniform(-10, 10)
#         y = random.uniform(-10, 10)
#         firefly = Firefly(x, y)
#         population.append(firefly)
#
#     # Main loop
#     for iteration in range(max_iterations):
#         # Evaluate intensity of each firefly
#         for firefly in population:
#             firefly.evaluate_intensity(target)
#
#             # Update global best firefly
#             if firefly.intensity > global_best_intensity:
#                 global_best_intensity = firefly.intensity
#                 global_best_firefly = firefly
#
#         # Move fireflies and update positions
#         for firefly in population:
#             for other_firefly in population:
#                 if firefly.intensity < other_firefly.intensity:
#                     firefly.update_position(other_firefly, attractiveness)
#
#         # Randomly move fireflies to explore new areas
#         for firefly in population:
#             firefly.move()
#
#     return global_best_firefly.position


# # Example usage
# target_position = [5, 5]
# best_position = firefly_algorithm(population_size=50, target=target_position, attractiveness=1, max_iterations=100)
# print("Best position:", best_position)
