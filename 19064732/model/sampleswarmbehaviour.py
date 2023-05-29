# Import necessary libraries
import random
import math

# Define parameters
num_robots = 1  # Number of robots
num_iterations = 10  # Number of iterations
max_speed = 5  # Maximum speed of the robots
max_turn_angle = 30  # Maximum turning angle of the robots
target_x = 50  # X coordinate of the target location
target_y = 50  # Y coordinate of the target location
swarm_strength = 0.1  # Strength of the swarm behavior

# Define class for robots
class Robot:
    def __init__(self, x, y, speed, direction):
        self.x = x
        self.y = y
        self.speed = speed
        self.direction = direction

    def update(self, swarm_direction):
        # Randomly adjust direction and speed
        self.direction += random.uniform(-max_turn_angle, max_turn_angle) + swarm_direction
        self.speed += random.uniform(-1, 1)
        self.speed = max(0, min(self.speed, max_speed))

        # Update position based on speed and direction
        self.x += self.speed * math.cos(math.radians(self.direction))
        self.y += self.speed * math.sin(math.radians(self.direction))

# Initialize robots
robots = []
for i in range(num_robots):
    robots.append(Robot(random.uniform(0, 100), random.uniform(0, 100), random.uniform(0, max_speed), random.uniform(0, 360)))

# Run simulation
for i in range(num_iterations):
    # Calculate swarm direction
    swarm_direction_x = 0
    swarm_direction_y = 0
    for robot in robots:
        swarm_direction_x += target_x - robot.x
        swarm_direction_y += target_y - robot.y
    swarm_direction = math.atan2(swarm_direction_y, swarm_direction_x)
    swarm_direction += random.uniform(-swarm_strength, swarm_strength)

    # Update each robot
    for robot in robots:
        robot.update(swarm_direction)

    # Print robot positions
    for robot in robots:
        print(f"Robot {i}: ({robot.x}, {robot.y})")