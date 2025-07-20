from tkinter import * # import all classes and constants from tkinter
from tkinter import messagebox # message box is not a class but a module of code
from random import shuffle, choice, randint
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    #Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))
    password_letters = [choice(letters) for _ in range(randint(10, 12))]


    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)
    password_symbols = [choice(symbols) for _ in range(randint(5, 7))]


    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)
    password_numbers = [choice(numbers) for _ in range(randint(5, 7))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    # password = ""
    # for char in password_list:
    #   password += char
    password = "".join(password_list)

    # print(f"Your password is: {password}")
    password_input.insert(0, password)
    
    # How to copy a string to the clipboard automatically. So after you click generate password the password will automatically get saved to the clipboard so you can paste it in the website --> pyperclip
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
# Save the website, email, and password entered to a file data.txt
def add_password():
    website_entries = website_input.get()
    email_entries = email_input.get()
    password_entries = password_input.get()
    
    # Have a dialog box popup that prevents the user from proceeding when either the website name, email, or password field is empty
    
    if len(website_entries) == 0 or len(email_entries) == 0 or len(password_entries) == 0:
        messagebox.showinfo(title="You have an error!", message="Your website, username/email, or password field is empty. Please enter a username/email, website, or password and try again.")
    else:
        
        # Create a message back to have users check their input and confirm the accuracy before saving it. If they select ok then we proceed but if they cancel nothing happens
        
        is_ok = messagebox.askokcancel(title=website_entries, message=f"These are the details entered: \n Email: {email_entries} \nPassword: {password_entries} \nWebsite: {website_entries}\n\n Do you want to proceed with these entries?")
        
        if is_ok:
            with open("passwords.txt", "a") as passwords_file: # if the file doesn't exist it will create it --> append mode
                passwords_file.write(f"{website_entries} | {email_entries} | {password_entries}\n")
                # now to delete our entered data after we have written to the file
                website_entries.delete(0, END)
                email_entries.delete(0, END)
                password_entries.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Put an image in the program --> MyPass lock as the background
# Tkinter Canvas Widget
canvas = Canvas(width=200, height=200)
mypass_img = PhotoImage(file="C:/Users/Zeilhan Co/Desktop/Study/100 Days of Code Python/Code/Day 29 - Password Manager GUI App/Start/logo.png")
canvas.create_image(100,100, image=mypass_img)
canvas.grid(column=1, row=0)


# Add the website entry field
website_input = Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2)

# When the program starts the cursor will already be in the website entry window by default
website_input.focus()

# Add the website entry label
website_label = Label(text="Website:")
website_label.grid(column=0,row=1)

# Add the Email/Username entry field
email_input = Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2)

# Add a starting or prepopulated value to the email entry field
email_input.insert(0, "info@jabezroberts.com")
# use email_input.insert(END) if you want to insert this text after the text you entered in the field


# Add the website entry label
email_label = Label(text="Email/Username:")
email_label.grid(column=0,row=2)

# Add the Password Entry field then add the Generate Password button
password_input = Entry(width=21)
password_input.grid(column=1, row=3)

# Add the website entry label
password_label = Label(text="Password:")
password_label.grid(column=0,row=3)

# Generate Password Button
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3)


# Add the 'Add' button
add_password_button = Button(text="Add Password", width=36, command=add_password)
add_password_button.grid(column=1, row=4, columnspan=2)





window.mainloop()