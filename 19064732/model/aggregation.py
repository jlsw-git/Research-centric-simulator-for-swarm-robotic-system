import sys
import random
import math
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsView, QGraphicsEllipseItem
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPainter, QBrush, QColor

# Particle class representing a robot
class Particle:
    def __init__(self, x, y):
        self.position = [x, y]
        self.velocity = [random.uniform(-1, 1), random.uniform(-1, 1)]
        self.radius = 10

    def move(self):
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]

    def distance_to(self, other_particle):
        dx = self.position[0] - other_particle.position[0]
        dy = self.position[1] - other_particle.position[1]
        return math.sqrt(dx ** 2 + dy ** 2)


# PSOVisualizer class for visualizing the swarm behavior
class PSOVisualizer(QMainWindow):
    def __init__(self, num_particles):
        super().__init__()

        self.setWindowTitle("Aggregation Swarm Behavior")
        self.setGeometry(100, 100, 600, 600)

        self.scene = QGraphicsScene(self)
        self.view = QGraphicsView(self.scene, self)
        self.view.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.view.setGeometry(0, 0, 600, 600)

        self.num_particles = num_particles
        self.particles = []

        for _ in range(self.num_particles):
            x = random.randint(0, 600)
            y = random.randint(0, 600)
            particle = Particle(x, y)
            self.particles.append(particle)
            ellipse_item = QGraphicsEllipseItem(
                x - particle.radius, y - particle.radius, particle.radius * 2, particle.radius * 2
            )
            self.scene.addItem(ellipse_item)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_particles)
        self.timer.start(5000)

    def update_particles(self):
        for particle in self.particles:
            self.update_velocity(particle)
            particle.move()

        self.draw_scene()

    def update_velocity(self, particle):
        aggregation_strength = 0.5
        alignment_strength = 0.2
        separation_distance = 50

        aggregation_vector = [0, 0]
        alignment_vector = [0, 0]
        separation_vector = [0, 0]

        for other_particle in self.particles:
            if other_particle != particle:
                distance = particle.distance_to(other_particle)

                if distance < separation_distance:
                    dx = particle.position[0] - other_particle.position[0]
                    dy = particle.position[1] - other_particle.position[1]
                    separation_vector[0] += dx
                    separation_vector[1] += dy

                alignment_vector[0] += other_particle.velocity[0]
                alignment_vector[1] += other_particle.velocity[1]

                aggregation_vector[0] += other_particle.position[0]
                aggregation_vector[1] += other_particle.position[1]

        aggregation_vector[0] /= (self.num_particles - 1)
        aggregation_vector[1] /= (self.num_particles - 1)

        particle.velocity[0] = (aggregation_strength * (aggregation_vector[0] - particle.position[0]) +
                                alignment_strength * alignment_vector[0] +
                                separation_vector[0])
        particle.velocity[1] = (aggregation_strength * (aggregation_vector[1] - particle.position[1]) +
                                alignment_strength * alignment_vector[1] +
                                separation_vector[1])

    def draw_scene(self):
        self.scene.clear()
        for particle in self.particles:
            ellipse_item = QGraphicsEllipseItem(
                particle.position[0] - particle.radius,
                particle.position[1] - particle.radius,
                particle.radius * 2,
                particle.radius * 2,
            )
            self.scene.addItem(ellipse_item)

        self.view.fitInView(self.scene.sceneRect(), Qt.AspectRatioMode(1))
        self.scene.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    num_particles = 10

    window = PSOVisualizer(num_particles)

    window.show()
    sys.exit(app.exec_())
