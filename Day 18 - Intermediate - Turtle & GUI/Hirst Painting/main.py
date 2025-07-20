###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
# import colorgram

# rgb_colors = []
# colors = colorgram.extract('./hirst.jpg', 30)  # Extract 30 colors from the image
# for color in colors:
#     r = color.rgb.r  # Get the red component
#     g = color.rgb.g  # Get the green component
#     b = color.rgb.b  # Get the blue component
#     new_color = (r, g, b)  # Create a tuple for the RGB color
#     rgb_colors.append(new_color)  # Append the color to the list

# print(rgb_colors)

import turtle as turtle_module
import random

tim = turtle_module.Turtle()
turtle_module.colormode(255)  # Set the color mode to RGB
tim.speed("fastest")  # Set the turtle speed to fastest
tim.penup()  # Lift the pen to avoid drawing lines
tim.hideturtle()  # Hide the turtle cursor for cleaner output

# Generate a list of colors in a tuple 
rgb_colors = [(173, 240, 243), (198, 226, 173), (206, 185, 175), (168, 223, 162), (193, 199, 233),
    (194, 198, 255), (167, 228, 233), (179, 235, 232), (150, 232, 183), (247, 158, 164),
    (150, 212, 229), (197, 208, 202), (236, 200, 234), (248, 222, 175), (174, 203, 196),
    (186, 164, 246), (216, 151, 218), (243, 151, 237), (160, 195, 157), (248, 242, 244),
    (159, 155, 151), (203, 205, 201), (237, 180, 237), (254, 182, 224), (210, 194, 193),
    (249, 250, 216), (150, 194, 238), (183, 150, 252), (223, 151, 186), (219, 255, 243)]

tim.setheading(225)  # Set the initial heading of the turtle
# Each time the turtle moves by 50 so move it 50 x 5 = 250
tim.forward(250)  # Move the turtle forward by 250 units
tim.setheading(0)  # Set the turtle heading to 0 degrees (facing right)
number_of_dots = 100  # Number of dots total to draw


# Function to draw a dot with a random color from the list

for dot_count in range(1, number_of_dots + 1):  # Loop through the range of dots to draw
    tim.dot(20, random.choice(rgb_colors))  # Draw a dot with a random color
    tim.forward(50)  # Move forward by 50 units
    
    if dot_count % 10 == 0:  # Check if we have drawn 10 dots in a row    
        tim.setheading(90)  # Set the turtle heading to 90 degrees (facing up) to start a new row
        tim.forward(50)  # Move forward by 50 units to start the next row
        tim.setheading(180)  # Set the turtle heading to 180 degrees (facing left) to start the next row
        tim.forward(500) # Move back to the left side of the screen at the start of the new row in same column 10 dots by 50 paces = 500
        tim.setheading(0)  # Set the turtle heading to 0 degrees (facing right) to start the next row




screen = turtle_module.Screen()
screen.exitonclick()  # Exit on click