from turtle import Turtle, Screen, colormode
import random


colormode(255)  # Enable RGB color mode (0-255)

wartortle = Turtle()
wartortle.shape("turtle")  # Set the shape to turtle
wartortle.color("DodgerBlue4")  # Set the color to blue
# wartortle.forward(100)  # Move the turtle forward by 100 units
# wartortle.left(90)  # Turn the turtle right by 90 degrees

# draw a square
for i in range(4):
    wartortle.forward(100)  # Move the turtle forward by 100 units
    wartortle.left(90)  # Turn the turtle right by 90 degrees

# draw a dashed line
for _ in range(15):
    wartortle.forward(10)  # Move the turtle forward by 10 units
    wartortle.penup()  # Lift the pen to not draw
    wartortle.forward(10)  # Move the turtle forward by another 10 units
    wartortle.pendown()  # Put the pen down to draw again



# draw many shapes in one with each shape having a different color outline
colors = ["DodgerBlue4", "DarkOrange1", "DarkOliveGreen3", "DarkOrchid1", "DarkSeaGreen3", "DarkSalmon", "DarkTurquoise", "DarkViolet", "DeepPink", "DeepSkyBlue", "DimGray", "DodgerBlue3", "FireBrick1", "ForestGreen", "Gold2", "Goldenrod1", "GreenYellow", "HotPink1", "IndianRed1", "LightPink1", "LightSalmon1", "LightSkyBlue1", "LightSteelBlue1", "MediumOrchid1", "MediumPurple1", "MediumSeaGreen", "MediumSpringGreen", "MediumTurquoise"]

def draw_shape(sides):
    angle = 360 / sides  # Calculate the angle for the shape
    for _ in range(sides):
        wartortle.forward(100)  # Move the turtle forward by 100 units
        wartortle.right(angle)  # Turn the turtle by the calculated angle

for shape_side_n in range(3, 11):  # Draw shapes from triangle (3 sides) to decagon (10 sides)
    wartortle.color(random.choice(colors))  # Choose a random color from the list
    draw_shape(shape_side_n)

# Random Walk with turtle
# Speed up the turtle
wartortle.speed("fastest")  # Set the turtle speed to fastest
# Increase the size of the turtle line
pen_size = wartortle.pensize(15)  # Set the pen size to 15
pen_directions = [0, 90, 180, 270]  # Define possible directions
for _ in range(10):  # Draw 500 random lines
    size = 15  # Set the pen size
    wartortle.color(random.choice(colors))
    wartortle.setheading(random.choice(pen_directions))  # Set a random direction
    wartortle.forward(30)  # Move the turtle forward by 30 units
    wartortle.pensize(size) # Increase the pen size by 1
    size += 1  # Increment the pen size

# Generate a random color for the turtle - PYTHON TUPLES
# wartortle.colormode(255)  # Set the color mode to RGB
# r = random.randint(0, 255)  # Random red value
# g = random.randint(0, 255)  # Random green value
# b = random.randint(0, 255)  # Random blue value
# wartortle.pencolor((r, g, b))  # Set the turtle color

def random_color():
    """ Generate a random color tuple for the turtle."""
    r = random.randint(0, 255)  # Random red value
    g = random.randint(0, 255)  # Random green value
    b = random.randint(0, 255)  # Random blue value
    color = (r, g, b)  # Create a tuple for the random color
    return color

size = 15  # Set the pen size
for _ in range(500):  # Draw 500 random lines
    wartortle.color(random_color())  # Set a random color using our previous function
    wartortle.setheading(random.choice(pen_directions))  # Set a random direction
    wartortle.forward(30)  # Move the turtle forward by 30 units
    wartortle.pensize(size) # Increase the pen size by 1
    size += 1  # Increment the pen size


# Draw a spirograph
# wartortle.circle(100)  # Draw a circle with radius 100
def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):  # Draw 36 circles
        wartortle.color(random_color())  # Set a random color
        wartortle.circle(100)  # Draw a circle with radius 100
        wartortle.setheading(wartortle.heading() + size_of_gap) # Rotate the turtle by the gap size
        
draw_spirograph(5)  # Call the function to draw a spirograph with a gap of 5 degrees




screen = Screen() # Set up the screen
screen.exitonclick() # Wait for a click to exit