import random
import math

class Particle:
    def __init__(self, position):
        self.position = position
        self.velocity = [random.uniform(-1, 1) for _ in range(2)]
        self.best_position = position
        self.best_fitness = float('inf')

    def update_velocity(self, global_best_position, omega, phi_p, phi_g):
        for i in range(2):
            r_p = random.uniform(0, 1)
            r_g = random.uniform(0, 1)
            self.velocity[i] = omega * self.velocity[i] + phi_p * r_p * (self.best_position[i] - self.position[i]) \
                               + phi_g * r_g * (global_best_position[i] - self.position[i])

    def update_position(self):
        for i in range(2):
            self.position[i] = self.position[i] + self.velocity[i]

    def evaluate_fitness(self, target_position):
        fitness = math.sqrt((self.position[0] - target_position[0]) ** 2 + (self.position[1] - target_position[1]) ** 2)
        if fitness < self.best_fitness:
            self.best_fitness = fitness
            self.best_position = self.position

class PSO:
    def __init__(self, num_particles, num_iterations):
        self.num_particles = num_particles
        self.num_iterations = num_iterations
        self.particles = []
        self.global_best_position = None
        self.global_best_fitness = float('inf')

    def initialize_particles(self):
        for _ in range(self.num_particles):
            x = random.uniform(-10, 10)
            y = random.uniform(-10, 10)
            position = [x, y]
            particle = Particle(position)
            self.particles.append(particle)

    def update_global_best(self):
        for particle in self.particles:
            if particle.best_fitness < self.global_best_fitness:
                self.global_best_fitness = particle.best_fitness
                self.global_best_position = particle.best_position

    def run(self):
        self.initialize_particles()

        for _ in range(self.num_iterations):
            for particle in self.particles:
                particle.update_velocity(self.global_best_position, 0.5, 0.5, 0.5)
                particle.update_position()
                particle.evaluate_fitness([0, 0])

            self.update_global_best()

        print("Global Best Position:", self.global_best_position)
        print("Global Best Fitness:", self.global_best_fitness)


if __name__ == '__main__':
    num_particles = 20
    num_iterations = 100

    pso = PSO(num_particles, num_iterations)
    pso.run()
