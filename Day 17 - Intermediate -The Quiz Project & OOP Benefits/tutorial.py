# PART 1 # Demonstrating the use of the User class with attributes        
# class User:
#     pass
# user_1 = User()
# user_1.id = "001"
# user_1.username = "john_doe"

# print(user_1.id)  # Output: 001
# print(user_1.username)  # Output: john_doe

# user_2 = User()
# user_2.id = "002"
# user_2.username = "jane_doe"


# PART 2 # Using a constructor to initialize attributes in the User class
class User:
    
    def __init__(self, user_id, username): # Constructor to initialize user attributes
        """Initializes a User object with an ID and username."""
        self.id = user_id
        self.username = username
        self.followers = 0 # Initializing followers to 0. We don't need to add it as an argument as it will always start at 0. Think Instagram followers of new accounts
        self.following = 0 # Another default attribute
    
    # Now we define a method that allows our followers to increase
    def follow(self, user): # A method, unlike a function, always needs to have a self parameter. Here we also pass in the user we've decided to follow
        user.followers += 1 # The user that we follow has their followers count increase by 1
        self.following += 1 # Our following count goes up by 1. The 'self' keyword allows us to reffer to the object that will be created by a class inside the class itself

user_1 = User("001", "john_doe") # Creating an instance of User with attributes, must create with user_id and username
user_2 = User("002", "jane_doe") # Creating another instance of User
print(user_1.id)  # Output: 001
print(user_1.username)  # Output: john_doe
print(user_2.id)  # Output: 002
print(user_2.username)  # Output: jane_doe

# In OOP Attributes are things the object has, or variables, while methods are what it does, think functions

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)

print(user_2.followers)
print(user_2.following)


# # PART 3 
# class Car:
#     def enter_race_mode():
#         self.seats = 2
