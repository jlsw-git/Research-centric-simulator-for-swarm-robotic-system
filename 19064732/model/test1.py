import random
import matplotlib.pyplot as plt

class Robot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, direction):
        if direction == "left":
            self.x -= 1
        elif direction == "right":
            self.x += 1
        elif direction == "up":
            self.y += 1
        elif direction == "down":
            self.y -= 1

    def get_position(self):
        return (self.x, self.y)

def main():
    # Create a swarm of 10 robots
    robots = []
    for i in range(10):
        robots.append(Robot(random.randint(0, 100), random.randint(0, 100)))

    # Create a figure and an axes object
    fig, ax = plt.subplots()

    # Let the robots move for 100 steps
    for i in range(100):
        for robot in robots:
            direction = random.choice(["left", "right", "up", "down"])
            robot.move(direction)

            # Plot the current position of the robot
            ax.plot(robot.x, robot.y, "o", alpha=0.5)

            # Update the figure
            plt.pause(0.01)

    plt.show()

if __name__ == "__main__":
    main()
