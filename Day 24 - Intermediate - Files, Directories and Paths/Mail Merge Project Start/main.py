#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# The readlines() method returns a list containing each line in the file as a list item.
# f = open("demofile.txt", "r")
# print(f.readlines())

# # Replace the word "bananas":

# txt = "I like bananas"
# x = txt.replace("bananas", "apples")
# print(x)


# # Remove spaces at the beginning and at the end of the string:

# txt = "     banana     "
# x = txt.strip()
# print("of all fruits", x, "is my favorite")

PLACEHOLDER = "[name]"

with open("/Users/Zeilhan Co/Desktop/Study/100 Days of Code Python/Code/Day 24 - Intermediate - Files, Directories and Paths/Mail Merge Project Start/Input/Names/invited_names.txt", mode="r") as names_file:
    names = names_file.readlines()

with open("/Users/Zeilhan Co/Desktop/Study/100 Days of Code Python/Code/Day 24 - Intermediate - Files, Directories and Paths/Mail Merge Project Start/Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"C:/Users/Zeilhan Co/Desktop/Study/100 Days of Code Python/Code/Day 24 - Intermediate - Files, Directories and Paths/Mail Merge Project Start/Output/ReadyToSend/letter_for_{stripped_name}.docx", mode="w") as completed_letter:
            completed_letter.write(new_letter)