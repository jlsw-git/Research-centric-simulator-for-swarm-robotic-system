import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsView, QGraphicsItem
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPainter, QBrush, QColor
import math
import random


class Robot(QGraphicsItem):
    def __init__(self, x, y):
        super().__init__()
        self.setPos(x, y)
        self.radius = 10

    def boundingRect(self):
        return QtCore.QRectF(-self.radius, -self.radius, 2 * self.radius, 2 * self.radius)

    def paint(self, painter, option, widget):
        painter.setBrush(QBrush(Qt.blue))
        painter.drawEllipse(-self.radius, -self.radius, 2 * self.radius, 2 * self.radius)


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
            robot = Robot(x, y)
            self.particles.append(robot)
            self.scene.addItem(robot)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_particles)
        self.timer.start(50)

    def update_particles(self):
        global_best_fitness = float('inf')
        global_best_position = None

        for particle in self.particles:
            x = particle.pos().x()
            y = particle.pos().y()

            fitness = self.evaluate_fitness(x, y)
            if fitness < global_best_fitness:
                global_best_fitness = fitness
                global_best_position = [x, y]

            self.update_velocity(particle, global_best_position, 0.7, 1.4, 1.4)
            particle.moveBy(particle.velocity[0], particle.velocity[1])

        self.draw_scene()

    def evaluate_fitness(self, x, y):
        distance = math.sqrt((x - self.target[0]) ** 2 + (y - self.target[1]) ** 2)
        return distance

    def update_velocity(self, particle, global_best_position, inertia_weight, cognitive_weight, social_weight):
        r1 = random.random()
        r2 = random.random()

        dx = cognitive_weight * r1 * (particle.pos().x() - particle.best_position[0])
        dy = cognitive_weight * r1 * (particle.pos().y() - particle.best_position[1])
        sx = social_weight * r2 * (particle.pos().x() - global_best_position[0])
        sy = social_weight * r2 * (particle.pos().y() - global_best_position[1])

        vx = inertia_weight * particle.velocity[0] + dx + sx
        vy = inertia_weight * particle.velocity[1] + dy + sy

        particle.velocity = [vx, vy]

    def draw_scene(self):
        self.view.fitInView(self.scene.sceneRect(), Qt.AspectRatioMode(1))

    def closeEvent(self, event):
        self.timer.stop()
        event.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PSOVisualizer()
    window.show()
    sys.exit(app.exec_())
