import random
import pandas

numbers = [1, 2, 3]
new_list = []
for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)

# Can be written as
"""new_list = [new_item for item in list]"""
numbers = [1, 2, 3]
new_list = [n + 1 for n in numbers]

# It also works with Strings, Tuples, Dictionaries
name = "Angela"
letters_list = [letter for letter in name] # split off your string to individual letters and added them to a brand new list

# Create a range(1,5) and create a list where each number is doubled
doubled_nums = [num * 2 for num in range(1,5)]

# Conditional list comprehension
"""new_list = [new_item for item in list if test]"""
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"] # Now return a list of all the names with less than 5 letters
short_names = [name for name in names if len(name) < 5]

# Convert all names with 6 letters or more to Uppercase
uppercase_names = [name.upper() for name in names if len(name) > 5]




# Dictionary Comprehension
"""
new_dict = {new_key:new_value for item in list}
new_dict = {new_key:new_value for (key,value) in dict.items()}
new_dict = {new_key:new_value for (key,value) in dict.items() if test}
"""
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# Now create a dictionary where you generate a random score for each of them
student_scores = {student:random.randint(1,100) for student in names}


# Now loop through a dictionary and return a new dictionary if some condition is satisfied.
passed_students = {student:score for (student,score) in student_scores.items() if score > 80}


# Using list comprehension with dictionary and pandas dataframe
student_dict = {
    "Student": ["Angela", "James", "John"],
    "Grades": [56,90,76]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    print(value)
student_data_frames = pandas.DataFrame(student_dict)
print(student_data_frames)

# Loop through a data frame
for (key, value) in student_data_frames.items():
    print(key) #gives titles of columns
    print(value) #give data of columns but loops through names of columns then data in each column which makes the data not useful

# to loop through the rows of the data frame instead use iterrows
for (index, row) in student_data_frames.iterrows():
    print(index)
    print(row) # check the output of this --> it prints first row with student and score then second row then third
    print(row.student) # First prints the entire data frame then each of the student in that data frame
    print(row.score) # First prints the entire data frame then each of the scores in that data frame
    
    if row.student == "Angela":
        print(row.score) # Would print Angela and her score


# Dict list comprehension
{new_key:new_value for (key,value) in dict.items()}

# Use instead to loop through a data frame
{new_key:new_value for (index, row) in df.iterrows()}




# 💪 This exercise is HARD 💪 

# Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line. 

# You are going to create a list called result which contains the numbers that are common in both files. 

# e.g. if file1.txt contained: 

# 1 

# 2 

# 3

# and file2.txt contained: 

# 2

# 3

# 4

# result = [2, 3]



# IMPORTANT:  The output should be a list of integers and not strings!

# Try to use List Comprehension instead of a Loop. 

with open("file1.txt") as file1:
  list1 = file1.readlines()
    
with open("file2.txt") as file2:
  list2 = file2.readlines()
    
result = [int(num) for num in list1 if num in list2]
 
print(result)


# You are going to use Dictionary Comprehension to create a dictionary called result that takes each word in the given sentence and calculates the number of letters in each word.   

# Try Googling to find out how to convert a sentence into a list of words.  *

# *Do NOT** Create a dictionary directly.

# Try to use Dictionary Comprehension instead of a Loop. 

# To keep this exercise simple, count any punctuation following a word with no whitespace as part of the word. Note that "Swallow?" therefore has a length of 8.
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word: len(word) for word in sentence.split()}
print(result)



# You are going to use Dictionary Comprehension to create a dictionary called weather_f that takes each temperature in degrees Celsius and converts it into degrees Fahrenheit. 

# To convert temp_c into temp_f use this formula: 

(temp_c * 9/5) + 32 = temp_f



weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
 
weather_f = {day:temp * 9/5 + 32 for (day, temp) in weather_c.items()}
 
print(weather_f)

