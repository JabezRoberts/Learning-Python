import pandas

name_data = pandas.read_csv("C:/Users/Zeilhan Co/Desktop/Study/100 Days of Code Python/Code/Day 26 - Intermediate List Comprehension & NATO Alphabet/NATO Alphabet Project/NATO-alphabet-start/nato_phonetic_alphabet.csv")
print(name_data.to_dict())
print("lol")
#TODO 1. Create a dictionary in this format:
phonetic_dictionary = {row.letter:row.code for (index, row) in name_data.iterrows()}
print(phonetic_dictionary)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
# TODO 3. Catch the keyError when a user enters a character that is not in the dictionary. Provide feedback to the user when an illegal word was entered. Continue prompting the user to enter another word until they enter a valid word

def generate_phonetic():    
    user_input = input("Enter a word: ").upper()
    try:
        output = [phonetic_dictionary[letter] for letter in user_input]
    except KeyError:
        print("The user did not enter letters in the alphabet.")
        generate_phonetic()
    else:
        print(output)

generate_phonetic()