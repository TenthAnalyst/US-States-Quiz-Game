# LIBRARIES
import turtle # to display the game screen.
import pandas as pd # to work with the state coordinate data in "50_states.csv"

# SETTING UP DISPLAY
screen = turtle.Screen() # creating the Screen object
screen.title("U.S. States Game") # title

image = "blank_states_img.gif" # the map image
screen.addshape(image) # adding the shape to the library
turtle.shape(image) # setting the current shape to be the map image

# STATE DATA
df = pd.read_csv("50_states.csv") # dataframe with the states, and their x/y pixel coordinates on the screen

states_all = df.state.to_list() # getting list of all states
states_guessed = [] # initializing list of states user has guessed so far

while len(states_guessed) < len(states_all): # Keep looping while there are still states left. 

    # Ask the user to name a state, and convert it to title case.
    # Title contains a counter of number of states guessed.
    answer_state = screen.textinput(title=f"{len(states_guessed)}/{len(states_all)} States Guessed", prompt="Name a state: \n'Exit' to end quiz.").title()

    # Exit Code to Break
    if answer_state == "Exit" or answer_state == "E": # Capital 'E' because the input will be title cased
        break

    # Check if the answer given is in the list of states.
    if answer_state in states_all:

        # UPDATE THE STATES GUESSED LIST
        states_guessed.append(answer_state)

        # WRITING THE STATE NAME
        pen = turtle.Turtle() # if so, create a pen to write the name of the state.
        pen.hideturtle() # hide the pen.
        pen.penup()  # lift the pen
        
        # Get x- and y-coordinates for given state
        x = df.loc[df['state'] == answer_state, 'x'].values[0]
        y = df.loc[df['state'] == answer_state, 'y'].values[0]
        
        pen.goto(x, y)  # move pen to given coordinates
        pen.write(answer_state, align="center", font=("Arial", 12, "normal")) # write the state name

screen.exitonclick()

# SEND UNGUESSED STATES TO A CSV
states_remaining = [state for state in states_all if state not in states_guessed] # create the list
df = pd.DataFrame(states_remaining, columns=['State']) # convert it to a dataframe
df.to_csv('states_remaining.csv', index=False) # write to csv file