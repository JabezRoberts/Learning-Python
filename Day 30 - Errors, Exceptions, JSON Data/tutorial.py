# FileNotFound
# with open("a_file.txt") as file:
#   file.read()


# KeyError
# a_dictionary = {"key":"value"}
# value = a_dictionary["non_existent_key"]


# IndexError
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]


# TypeError
# text = "abc"
# print(text + 5)

## Catch Exceptions
# try: something that might cause an exception

# except: Do this if there was an exception

# else: Do this if there were no exceptions

# finally: Do this no matter what happens



# this normally causes a FileNotFound error but we will try it
# try:
#     file = open("a_file.txt")
# except: # if an exception like a TypeError or FileNotFound error happens above we will do this next line
#     print("There was an error")
# # we got "There was an error" printed to the console

# The code below is saying (try) if you get an error trying to open the file then (except) create it
# try:
#     file = open("a_file.txt") # will produce a FileNotFoundError
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["sjhfjf"]) # will produce a KeyError
# except FileNotFoundError: # if an exception like for FileNotFound error happens above we will do this next line
#     file = open("a_file_.txt", mode="w")
#     file.write("Write something\n")
# except KeyError as error_message: # as error_message makes us get hold of the error message that would appear to tell us which Key was the problem
#     print(f"The key {error_message}  does not exist")
# else: # if there were no exceptions
#     content = file.read()
#     print(content)
# finally: #runs no matter what
#     file.close()
#     print("File was closed")
#     # raise KeyError
#     raise TypeError("This is a custom error message I made up")


## Raising our own exceptions
# raise: allows us to raise our own exceptions
height = float(input("Height: "))
weight = int(input("Weight: "))

# what if they entered someone was 100m tall? That's an error clearly, right?
if height > 3:
    raise ValueError("Human height not not be over 3 meters.")

bmi = weight/height ** 2
print(bmi)

