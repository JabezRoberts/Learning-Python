class Question: # This class represents a single question in the quiz.
    """A class to represent a question in the quiz."""
    def __init__(self, text, answer): # Constructor to initialize question attributes
        """Initializes a Question object with text and answer."""
        self.text = text 
        self.answer = answer
    
    def __str__(self): # This method returns a string representation of the question object
        """Returns the question text."""
        return self.text

    def check_answer(self, user_answer): # Method to check if the user's answer is correct
        """Checks if the provided answer matches the question's answer."""
        return user_answer.lower() == self.answer.lower()