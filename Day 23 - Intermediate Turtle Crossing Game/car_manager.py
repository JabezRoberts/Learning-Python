from turtle import Turtle
import random

# Constants for car appearance and movement
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5  # Initial movement speed for cars
MOVE_INCREMENT = 10         # Speed increase per level (if implemented)

class CarManager:
    """Manages the creation and movement of cars in the game."""
    
    def __init__(self):
        # List to keep track of all car turtle objects on the screen
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        
        
    def create_car(self):
        """Randomly creates a new car with a 1 in 6 chance per call."""
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            # Create a new turtle shaped like a stretched square (rectangle/car shape)
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))  # Random car color
            new_car.shapesize(stretch_wid=1, stretch_len=2)  # Make the car rectangular
            new_car.penup()  # Prevent drawing lines as the car moves
            
            # Position the car at the far right edge (x=300) with a random vertical (y) position
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            
            # Add the new car to the list of all cars
            self.all_cars.append(new_car)
    
    def move_cars(self):
        """Moves all cars on the screen to the left by the starting move distance."""
        for car in self.all_cars:
            car.backward(self.car_speed)  # Move each car leftwards
    
    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT