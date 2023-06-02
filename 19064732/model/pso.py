import math
import random
import matplotlib.pyplot as plt


class Obstacle:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Particle:
    def __init__(self, x, y):
        self.position = [x, y]
        self.velocity = [random.uniform(-1, 1), random.uniform(-1, 1)]
        self.best_position = self.position.copy()
        self.best_fitness = float('inf')
        self.x = x
        self.y = y

    def move(self):
        self.x += self.velocity[0]
        self.y += self.velocity[1]
        self.position = [self.x, self.y]

    def update_velocity(self, global_best_position, inertia_weight, cognitive_weight, social_weight):
        r1 = random.random()
        r2 = random.random()

        cognitive_component = [cognitive_weight * r1 * (bp - p) for bp, p in zip(self.best_position, self.position)]
        social_component = [social_weight * r2 * (gbp - p) for gbp, p in zip(global_best_position, self.position)]

        self.velocity = [inertia_weight * v + c + s for v, c, s in
                         zip(self.velocity, cognitive_component, social_component)]

    def evaluate_fitness(self, target):
        distance = math.sqrt((self.position[0] - target[0]) ** 2 + (self.position[1] - target[1]) ** 2)
        return distance

    def update_best_position(self, fitness):
        if fitness < self.best_fitness:
            self.best_fitness = fitness
            self.best_position = self.position.copy()


def particle_swarm_optimization(robots, target, num_iterations=100):
    # num_particles = len(robots)
    inertia_weight = 0.7
    cognitive_weight = 1.4
    social_weight = 1.4
    global_best_fitness = float('inf')
    global_best_position = None

    # Initialize particles
    particles = []
    for robot in robots:
        particle = Particle(robot.x, robot.y)
        particles.append(particle)

    plt.figure()
    plt.xlim(0, 100)
    plt.ylim(0, 100)
    plt.title("Particle Swarm Optimization")

    for _ in range(num_iterations):
        plt.clf()
        for i, particle in enumerate(particles):
            fitness = particle.evaluate_fitness(target)
            particle.update_best_position(fitness)

            if fitness < global_best_fitness:
                global_best_fitness = fitness
                global_best_position = particle.position.copy()

            particle.update_velocity(global_best_position, inertia_weight, cognitive_weight, social_weight)
            particle.move()
            robots[i].x = particle.position[0]
            robots[i].y = particle.position[1]

        # Plot robots and target
        for robot in robots:
            plt.plot(robot.x, robot.y, 'bo')
        plt.plot(target[0], target[1], 'ro')

        plt.pause(0.01)

    # Plot final positions
    plt.clf()
    for robot in robots:
        plt.plot(robot.x, robot.y, 'bo')
    plt.plot(target[0], target[1], 'ro')
    plt.show()


def main():
    # Create robots and obstacles
    num_robots = 10
    robots = []
    obstacles = []
    target = [50, 50]

    for _ in range(num_robots):
        x = random.randint(0, 100)
        y = random.randint(0, 100)
        robot = Particle(x, y)
        robots.append(robot)

    for _ in range(5):
        x = random.randint(0, 100)
        y = random.randint(0, 100)
        obstacle = Obstacle(x, y)
        obstacles.append(obstacle)

    # Apply Particle Swarm Optimization
    particle_swarm_optimization(robots, target)

    # Print the final positions of robots
    print("Final Robot positions:")
    for robot in robots:
        print(f"({robot.x}, {robot.y})")


if __name__ == '__main__':
    main()

