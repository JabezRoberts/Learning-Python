class QuizBrain:
    
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list # next initialize QuizBrain in main.py and set the question list variable will be the question bank. QuizBrain(question_bank)
        self.score = 0 # This variable will keep track of the user's score throughout the quiz.
        
    def still_has_questions(self):
        """Check if there are more questions left in the question_list."""
        """Returns True if there are more questions, otherwise False."""
        return self.question_number < len(self.question_list)
    
    def next_question(self):
        """Retrieve the item at the current question_number from the question_list. Use the input function to show the user the Question text and ask the user for an answer."""
        current_question = self.question_list[self.question_number] # go into question list in main.py to get the question at the current question number
        # Remember each of the questions are question objects with both a text and answer attribute
        self.question_number += 1 # Increment the question number by 1 to move to the next question
        # The input function will prompt the user to answer the question
        user_answer = input(f"Q.{self.question_number}: {current_question} (True/False)") # prompts the user to input True or False to the current question while also showign the question number and text.
        self.check_answer(user_answer, current_question.answer) # Calls the check_answer method to compare the user's answer with the correct answer of the current question.
        # The check_answer method will compare the user's answer with the correct answer and update the score
    
    def check_answer(self, user_answer, correct_answer):
        """Check if the user's answer is correct."""
        """Compares the user's answer with the correct answer and updates the score."""
        if user_answer.lower() == correct_answer.lower(): # Compares the user's answer with the correct answer, ignoring case
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}.") # Displays the user's current score and the total number of questions answered so far.
        print("\n") # Prints a new line for better readability