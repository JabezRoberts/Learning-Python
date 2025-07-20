import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Guessing Game")

# How to set turtles shape to a new shape and load an image as a new shape
image = "C:/Users/Zeilhan Co/Desktop/Study/100 Days of Code Python/Code/Day 25 - Intermediate - Working with CSV Data and Pandas/US States Game/blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

# Now we need a function that takes the guess we enter and add it to a specific x,y coordinate to match it to the state's location on the map
# def get_mouse_click_coor(x,y):
#     print(x,y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop() # use this to keep the screen open even after click
guessed_states = []


while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?")

    # Now we know the x,y coordinate for the state the user has guessed and we have a way of getting the user's guess. now we need to match the guess with the location of the state using 
    # x,y coordinates

    # Now use the user's answer to find the corresponding state (convert to lower for both of course) to find if the state exists then grab the row, get the x,y coord, for where to write to the screen/map. Be sure to keep track of their score in the heading of the text input screen

    # Step 1 - Convert guess to title case
    title_case_answer = answer_state.title()

    #2. Check if the guess is among the 50 states. If they guessed right we need to create a turtle to write the name at that state's x,y coord
    data = pandas.read_csv("C:/Users/Zeilhan Co/Desktop/Study/100 Days of Code Python/Code/Day 25 - Intermediate - Working with CSV Data and Pandas/US States Game/50_states.csv")
    print(data)

    # Now we are going to save all the data from the state column to a list to get all the states in one list... obvi
    all_states = data.state.to_list()
    
    if title_case_answer == "Exit":
        missing_state = [state for state in all_states if state not in guessed_states]
        # missing_states = []
        # for state in all_states:
        #     if state not in guesses_states:
        #         missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)          
        new_data.to_csv("States To Learn.csv")
        break

    if title_case_answer in all_states:
        guessed_states.append(title_case_answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        # Now we need to get the x,y coord for the state and use it as the goto coordinates for the turtle to write the name
        state_data = data[data.state == title_case_answer] # returns the entire row with the state, x, and y coord
        t.goto(state_data.x, state_data.y) # Because this is a row we can tap into the data using the column headings in a dot notation
        # the above will return an error because state_data.x returns a Pandas Series from our Data Frame. Consider it a column from our data frame. Use the line below instead to
        # extract the integer value of the coordinates
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(title_case_answer) # or t.write(state_data.state.item()) --> look up Pandas item()
        
        # Now we need to change the title of the window from "Guess the US State" to the number of states guessed out of 50
        # do this by changing the title to a f string then using the len(guessed_states) to say how many of 50 states were guess.
        # previous was: answer_state = screen.textinput(title="Guess the US State", prompt="What's another state's name?")
        # currently: answer_state = screen.textinput(title=f"{len(guesses_states)}/50 States Correct", prompt="What's another state's name?")
        
        # Now finally, we end the game by saving to a CSV all the states not guessed, making it more educational, and a way to end the game when they enter 'exit'
        # Used if title_case_answer == "Exit":
        #break
        #then commented out screen.exitonclick()
        
        # Now to make the game more educational get the csv with states to learn





# screen.exitonclick() # When you click on the map the window will close so we will use turtle.mainloop()