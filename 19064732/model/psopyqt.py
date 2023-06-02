import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsView
from PyQt5.QtCore import Qt, QTimer
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


class PSOVisualizer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PSO Visualizer")
        self.setGeometry(100, 100, 600, 600)

        self.scene = QGraphicsScene(self)
        self.view = QGraphicsView(self.scene, self)
        self.view.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.view.setGeometry(0, 0, 600, 600)

        self.num_particles = 10
        self.target = [300, 300]
        self.particles = []

        for _ in range(self.num_particles):
            x = random.randint(0, 600)
            y = random.randint(0, 600)
            particle = Particle(x, y)
            self.particles.append(particle)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_particles)
        self.timer.start(50)

    def update_particles(self):
        global_best_fitness = float('inf')
        global_best_position = None

        for particle in self.particles:
            fitness = particle.evaluate_fitness(self.target)
            particle.update_best_position(fitness)

            if fitness < global_best_fitness:
                global_best_fitness = fitness
                global_best_position = particle.position.copy()

            particle.update_velocity(global_best_position, 0.7, 1.4, 1.4)
            particle.move()

        self.draw_scene()

    def draw_scene(self):
        self.scene.clear()

        for particle in self.particles:
            x = particle.position[0]
            y = particle.position[1]
            self.scene.addEllipse(x, y, 5, 5)

        self.scene.addEllipse(self.target[0], self.target[1], 10, 10, Qt.red)

        self.view.fitInView(self.scene.sceneRect(), Qt.AspectRatioMode(1))

    def closeEvent(self, event):
        self.timer.stop()
        event.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PSOVisualizer()
    window.show()  # Add this line to display the GUI window
    sys.exit(app.exec())

