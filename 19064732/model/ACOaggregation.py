import sys
import random
import math
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsView
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPainter, QBrush, QColor, QPen
from PyQt5.QtCore import QLineF

# Ant class representing an ant
class Ant:
    def __init__(self, x, y):
        self.position = [x, y]
        self.path = []
        self.path_length = 0.0

    def move_to(self, node):
        self.path.append(node)
        self.path_length += node.distance_to(self.path[-2]) if len(self.path) > 1 else 0

    def has_visited(self, node):
        return node in self.path


# Node class representing a graph node
class Node:
    def __init__(self, x, y):
        self.position = [x, y]

    def distance_to(self, other_node):
        dx = self.position[0] - other_node.position[0]
        dy = self.position[1] - other_node.position[1]
        return math.sqrt(dx ** 2 + dy ** 2)


# ACOVisualizer class for visualizing the ACO algorithm
class ACOVisualizer(QMainWindow):
    def __init__(self, num_ants):
        super().__init__()

        self.setWindowTitle("Ant Colony Optimization")
        self.setGeometry(100, 100, 600, 600)

        self.scene = QGraphicsScene(self)
        self.view = QGraphicsView(self.scene, self)
        self.view.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.view.setGeometry(0, 0, 600, 600)

        self.num_ants = num_ants
        self.ants = []

        self.nodes = []
        self.num_nodes = 10
        for _ in range(self.num_nodes):
            x = random.randint(0, 600)
            y = random.randint(0, 600)
            node = Node(x, y)
            self.nodes.append(node)
            self.scene.addItem(node)

        self.start_node = self.nodes[0]  # Start node
        self.target_node = self.nodes[-1]  # Target node

        self.pheromone_matrix = [[1.0 for _ in range(self.num_nodes)] for _ in range(self.num_nodes)]
        self.evaporation_rate = 0.1

        for _ in range(self.num_ants):
            x = random.randint(0, 600)
            y = random.randint(0, 600)
            ant = Ant(x, y)
            self.ants.append(ant)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_ants)
        self.timer.start(100)

    def update_ants(self):
        for ant in self.ants:
            if ant.position == self.target_node.position:
                continue

            next_node = self.select_next_node(ant)
            ant.move_to(next_node)

        self.update_pheromone()

        self.draw_scene()

    def select_next_node(self, ant):
        current_node = self.get_current_node(ant)
        unvisited_nodes = [node for node in self.nodes if not ant.has_visited(node)]

        probabilities = []
        total = 0.0

        for node in unvisited_nodes:
            pheromone_level = self.pheromone_matrix[self.nodes.index(current_node)][self.nodes.index(node)]
            distance = current_node.distance_to(node)
            attractiveness = 1.0 / distance if distance > 0 else 0.0

            probabilities.append(pheromone_level * attractiveness)
            total += probabilities[-1]

        selection = random.uniform(0, total)
        accumulative = 0.0

        for i, node in enumerate(unvisited_nodes):
            accumulative += probabilities[i]
            if accumulative >= selection:
                return node

    def get_current_node(self, ant):
        if len(ant.path) == 0:
            return self.start_node
        else:
            return ant.path[-1]

    def update_pheromone(self):
        for i in range(self.num_nodes):
            for j in range(self.num_nodes):
                self.pheromone_matrix[i][j] *= (1 - self.evaporation_rate)

        for ant in self.ants:
            for i in range(len(ant.path) - 1):
                node1 = ant.path[i]
                node2 = ant.path[i + 1]
                self.pheromone_matrix[self.nodes.index(node1)][self.nodes.index(node2)] += 1 / ant.path_length

    def draw_scene(self):
        self.scene.clear()

        for node in self.nodes:
            self.scene.addItem(node)

        pen = QPen(Qt.black)
        pen.setWidth(2)
        for ant in self.ants:
            for i in range(len(ant.path) - 1):
                node1 = ant.path[i]
                node2 = ant.path[i + 1]
                self.scene.addLine(QLineF(node1.position[0], node1.position[1], node2.position[0], node2.position[1]), pen)

        self.view.setScene(self.scene)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    num_ants = 10

    window = ACOVisualizer(num_ants)

    window.show()
    sys.exit(app.exec_())
