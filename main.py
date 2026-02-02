from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # Use list comprehension instead of looping for
    password_list =[choice(letters) for _ in range(randint(8, 10)) ]+ \
                    [choice(symbols) for _ in range(randint(2, 4))] + \
                    [choice(numbers) for _ in range(randint(2, 4))]
    shuffle(password_list)

    # Get the password as a value
    password ="".join(password_list)
    # Add the generated password to password field
    password_entry.insert(0, password)
    # print(f"Your password is: {password}")
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    mail = mail_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": mail,
            "password": password
        }
    }

    # Check if all required field filled
    if website == "" or mail == "" or password == "":
        messagebox.showerror("Oops!", "Please enter all required information")
    else:
        with open("data.json", "r") as data_file:
            # Read the old data
            data = json.load(data_file)
            # Update old data
            data.update(new_data)

        with open("data.json", "w") as data_file:
            # Save updated data
            json.dump(data, data_file, indent=4)

            website_entry.delete(0, END)
            password_entry.delete(0, END)
        # else:
        #     messagebox.showerror("Error", "Please enter all required information")

# ---------------------------- UI SETUP ------------------------------- #

# Create a window with Tkinter module
window = Tk()
window.title("Password Generator")
window.config(padx=40, pady=40)

# Use the image as a graphic
canvas = Canvas(width=200, height=200)
key_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=key_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
mail_label = Label(text="Email/Username:")
mail_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entry
website_entry = Entry(width=21)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()
mail_entry = Entry(width=40)
mail_entry.grid(column=1, row=2, columnspan=2)
# Shown a text on the entry field.
mail_entry.insert(0, "user@mail.com")
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

# Button
search_button = Button(text="Search")
search_button.grid(column=2, row=1, columnspan=2)
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)
add_button = Button(text="Add", width=41, command=save_password)
add_button.grid(column=1, row=4, columnspan=3)

window.mainloop()