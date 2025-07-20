from tkinter import *
import time
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_pomodoro():
    window.after_cancel(timer) # Stops window.after from running or in this case stops our timer
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0



# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_pomodoro():
    global reps
    reps += 1
    # print(count)
    work_sec = WORK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    
    if reps % 8 == 0:
        countdown(long_break_sec)
        timer_label.config(text="Break Time", fg=RED)
    elif reps % 2 == 0:
        countdown(short_break_sec)
        timer_label.config(text="Break Time!", fg=PINK)
    else:
        countdown(work_sec)
        timer_label.config(text="Work Time!", fg=GREEN)

        
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def countdown(count):
    count_min = math.floor(count / 60)
    
    # Use Dynamic Typing to change the text from 5:0 to 5:00
    # Dynamic Typing is when you can change a variable's data type by changing the type of data it holds
    # Eg. a = 5 means a is an int but if you now write a = "hello" it means a is now a string. Congratulations! You just dynamic typed
    
    count_seconds = count % 60
    if count_seconds < 10 :
        count_seconds == f"0{count_seconds}" # Dynamic typing
    
    # change the timer on the window
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_pomodoro()
        mark = ""
        for _ in range(math.floor(reps/2)): #math.floor to avoid float division
            mark += "✔"
        check_marks.config(text=mark)
    



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Clock")
window.config(padx=100, pady=50, bg=YELLOW)

# Put an image in the program --> tomato as the background
# Tkinter Canvas Widget
canvas = Canvas(width=210, height=240, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="C:/Users/Zeilhan Co/Desktop/Study/100 Days of Code Python/Code/Day 28 - Pomodoro GUI and Dynamic Typing/Pomodoro Start/tomato.png")
canvas.create_image(102, 110, image=tomato_img) # To center our image set the image at half the width and height, requires a photoimage
timer_text = canvas.create_text(102,130, text="00:00", fill="white", font=(FONT_NAME, 42, "bold"))
canvas.grid(column=1, row=1)

timer_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 50), highlightthickness=0, bg=YELLOW)
timer_label.grid(column=1, row=0)

start_button = Button(text="Start", command=start_pomodoro)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_pomodoro)
reset_button.grid(column=2, row=2)


# #Checkbutton
# def checkbutton_used():
#     #Prints 1 if On button checked, otherwise 0.
#     print(checked_state.get())
# #variable to hold on to checked state, 0 is off, 1 is on.
# checked_state = IntVar()
# checkbutton = Checkbutton(text="✔", variable=checked_state, command=checkbutton_used)
# checked_state.get()
# checkbutton.grid(column=1, row=2)

# OR
check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=2)










window.mainloop()