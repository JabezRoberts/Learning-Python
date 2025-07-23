from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface: 
    
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        
        self.score = Label(text="Score: 0", fg='white', bg=THEME_COLOR)
        self.score.grid(column=1, row=0)
        
        
        self.canvas = Canvas(width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text(
            150,
            125,
            width= 280,
            text="Some Question goes here",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        
        
        right_img = PhotoImage(file="C:/Users/Zeilhan Co/Desktop/Study/100 Days of Code Python/Code/Day 34 - Intermediate API Practice GUI Quiz App/Quizzler Start/images/true.png")
        self.right_button = Button(image=right_img, highlightthickness=0, command=self.right_selection)
        self.right_button.grid(column=0, row=2)
        
        wrong_img = PhotoImage(file="C:/Users/Zeilhan Co/Desktop/Study/100 Days of Code Python/Code/Day 34 - Intermediate API Practice GUI Quiz App/Quizzler Start/images/false.png")
        self.wrong_button = Button(image=wrong_img, highlightthickness=0, command=self.wrong_selection)
        self.wrong_button.grid(column=1, row=2)
        
        # remember that self. turns this into a property that can be accessed anywhere in the class
        # self. was not used on the images because they weren't going to be used anywhere else except to setup the button
        
        self.get_next_question()
        
        self.window.mainloop()
    
    # now we need to call next_question from quiz_brain.py and put it on the canvas
    def get_next_question(self):
        self.canvas.config(bg='white')
        self.canvas.itemconfig(self.question_text, fill="black")
        if self.quiz.still_has_questions():    
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")
        
    
    
    def right_selection(self):
        self.give_feedback(self.quiz.check_answer("True"))   
    
    def wrong_selection(self):
        self.give_feedback(self.quiz.check_answer("False"))      
        
        
    def give_feedback(self, is_right):
        # depending on if the user gets it right we need to change the background to green and red if they got it wrong then turn it back to the default after 1 second has passed
        if is_right:
            self.canvas.config(bg='green')
            self.canvas.itemconfig(self.question_text, fill="white")
        else:
            self.canvas.config(bg='red')
            self.canvas.itemconfig(self.question_text, fill="black")
        self.window.after(1000, self.get_next_question)