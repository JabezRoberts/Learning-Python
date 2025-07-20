# PART 1
# import turtle
# import another_module

# print(another_module.another_variable)

# timmy = turtle.Turtle()


# PART 2
# from turtle import Turtle, Screen
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle") # changes arrow to turtle shape
# timmy.color("DarkOliveGreen") # changes turtle color to green
# timmy.forward(100) # moves turtle forward by 100 units


# my_screen = Screen() # creates a screen for the turtle to draw on
# print(my_screen.canvheight) # a screen will show up but will imediately close
# my_screen.exitonclick() # this line keeps the screen open until clicked, we see the turtle in the form of an arrow


# PART 3
# Installing packages from pypi.org --> pip install prettytable
from prettytable import PrettyTable
table = PrettyTable()
print(table)
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"]) # Adds a column with the name "Pokemon Name" and three rows with the names of the Pokémon
table.add_column("Type", ["Electric", "Water", "Fire"]) # Adds another column with the name "Type" and three rows with the types of the Pokémon
print(table.align)  # Prints the alignment of the columns
table.align = "l"  # Center align the columns
print(table)
print(table.align)  # Prints the alignment of the columns again to confirm the change