from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = [ # This list comprehension creates a list of Question objects from the question_data
    Question(q["text"], q["answer"]) for q in question_data
]

# or
# question_bank = [ #
#     for q in question_data:
#         Question(q["text"], q["answer"]) 
# ]

# OR
# question_bank = []
# for question in question_data: # This loop iterates through each question in question_data
#     new_question = Question(question["text"], question["answer"]) # Creates a new Question object
#     question_bank.append(new_question) # Appends the new Question object to the question_bank list

#ORRR CLASS ANSWER
# question_bank = [] # This is an empty list that will hold Question objects
# for question in question_data:
#     question_text = question["text"]
#     question_answer = question["answer"]
#     new_question = Question(question_text, question_answer)
#     question_bank.append(new_question)
print(question_bank)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions(): # This loop continues as long as there are questions left in the quiz 
    quiz.next_question()

print("You've completed the quiz!")
print(f"Your final score was: {quiz.score}/{quiz.question_number}") # Displays the user's final score and the total number of questions answered. can also use len(quiz.question_bank) to get the total number of questions