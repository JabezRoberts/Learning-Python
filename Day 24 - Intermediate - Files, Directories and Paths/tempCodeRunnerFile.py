file = open("my_file.txt") # to open a file
# contents = file.read() # to read the contents of the file. saved to content as string
# print(contents)
# file.close()

# with open("my_file.txt") as file: # No need to remember to close the file with this method
#     contents = file.read() # to read the contents of the file
#     print(contents)


# # Writing to a file - deletes previous content
# with open("my_file.txt", mode="w") as file: # default is read mode but now we set it to write mode
#     file.write("New text.")



# # Writing to a file - keeps previous content
# with open("my_file.txt", mode="a") as file: # a is append mode
#     file.write("\nNew text.")

# # If you try to open a file in write mode and the file doesn't exist then this will create the file for you
# with open("new_file.txt", mode="w") as file:
#     file.write("New file, new text bebeh!")


# # Using an absolute path to access a file on the desktop
# with open("/Users/Zeilhan Co/Desktop/my_file.txt") as file:
#     contents = file.read()
#     print(contents)