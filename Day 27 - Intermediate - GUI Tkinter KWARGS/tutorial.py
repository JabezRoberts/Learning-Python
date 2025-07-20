"""
import tkinter

window = tkinter.Tk() #Create TK Inter window. Now we need a way to keep the window on the screen. Can use a while loop --> window.mainloop()
window.title("My First GUI Program") # Change title of the window
window.minsize(width=500, height=300) # Set the minimum size of the window and the size the window will start up as

# Create components to put inside the window
my_label = tkinter.Label(text="I'm a label", font=("Arial", 24, "bold")) # Create a label. Then we have to specify how that label will be laid out on the screen before it will show up
my_label.pack() # Automatically add the label to the screen and center it on the screen
# my_label.pack(side="left") # Positions the content to the left of the screen. Also use "bottom" and "right". expand=True has it in the middle trying to take up the entire height and width of the screensize

my_label["text"] = "My Text" # One way to update the label text
my_label.config(text="New Text") # Another way to update the text

# Adding Buttons
button = tkinter.BU
"""




#Use the above when you're only using a few classes but if you're going to use a lot like we do below use this way
 ## Another way to initialize - then remove all the tkinter. to replace with just the class name
from tkinter import *

window = Tk() #Create TK Inter window. Now we need a way to keep the window on the screen. Can use a while loop --> window.mainloop()
window.title("My First GUI Program") # Change title of the window
window.minsize(width=500, height=300) # Set the minimum size of the window and the size the window will start up as
window.config(padx=20,pady=20) # add padding to window


# Create components to put inside the window
my_label = Label(text="I'm a label", font=("Arial", 24, "bold")) # Create a label. Then we have to specify how that label will be laid out on the screen before it will show up
my_label.pack() # Automatically add the label to the screen and center it on the screen
# my_label.pack(side="left") # Positions the content to the left of the screen. Also use "bottom" and "right". expand=True has it in the middle trying to take up the entire height and width of the screensize

my_label["text"] = "My Text" # One way to update the label text
my_label.config(text="New Text") # Another way to update the text
my_label.config(padx=20,pady=20) # Add padding to label

# Adding Buttons
button = Button(text="Click Me")
button.pack() # Every item to be placed on the screen needs the pack

# Add functions to our button
def button_clicked():
    print("I got clicked")

button = Button(text="Clickable Button", command=button_clicked)
button.pack()

# Show 'Button Got Clicked' on my_label when button gets clicked
def button_clicked():
    print("I got clicked")
    my_label.config(text="Button Got Clicked")

button = Button(text="Click To Change Text", command=button_clicked)
button.pack()

# ENTRY COMPONENT
input = Entry(width=10) #creates an input field to window
input.pack()
input.get() # Returns the input as a string
# Now to display the input as the text
def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)
button = Button(text="Click To Change Text With Input", command=button_clicked)
button.pack()


# LAYOUT PACKAGES - PACK, PLACE, GRID
# PACK packs widgets next to each other top to bottom. Change by adding side param. 

# PLACE - All about precise positioning using a x and y value
my_label.place(x=0,y=0)

# GRID - It imagines your entire program is a grid dividable into any number of rows and columns
my_label.grid(column=0,row=0) # Grid is relative to other widgets meaning if we did column=5,row=5 here it would still place the element in the top left corner
# because no element is in position column=4,row=4 etc
# Grid and pacl can't be used in the same program



new_button = Button(text="New Button")
new_button.grid(column=2,row=0)













window.mainloop() # always at the end of the program

