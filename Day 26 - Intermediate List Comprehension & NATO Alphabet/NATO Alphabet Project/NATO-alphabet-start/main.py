import pandas

# student_dict = {
#     "student": ["Angela", "James", "Lily"], 
#     "score": [56, 76, 98]
# }

# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

# import pandas
# student_data_frame = pandas.DataFrame(student_dict)

# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# # Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

name_data = pandas.read_csv("C:/Users/Zeilhan Co/Desktop/Study/100 Days of Code Python/Code/Day 26 - Intermediate List Comprehension & NATO Alphabet/NATO Alphabet Project/NATO-alphabet-start/nato_phonetic_alphabet.csv")
print(name_data.to_dict())
print("lol")
#TODO 1. Create a dictionary in this format:
phonetic_dictionary = {row.letter:row.code for (index, row) in name_data.iterrows()}
print(phonetic_dictionary)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter a word: ").upper()
output = [phonetic_dictionary[letter] for letter in user_input]
print(output)