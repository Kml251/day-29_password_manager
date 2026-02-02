from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list =[choice(letters) for _ in range(randint(8, 10)) ]+ \
                    [choice(symbols) for _ in range(randint(2, 4))] + \
                    [choice(numbers) for _ in range(randint(2, 4))]
    shuffle(password_list)

    password ="".join(password_list)
    password_entry.insert(0, password)
    print(f"Your password is: {password}")
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    mail = mail_entry.get()
    password = password_entry.get()

    if website == "" or mail == "" or password == "":
        messagebox.showerror("Oopss!", "Please enter all required information")
    else:
        is_ok = messagebox.askyesno(title=website, message=f"These are the details entered: \nEmail: {mail}"
                                                           f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data:
                data.write(f"{website} | {mail} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)
        # else:
        #     messagebox.showerror("Error", "Please enter all required information")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50)

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
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()
mail_entry = Entry(width=35)
mail_entry.grid(column=1, row=2, columnspan=2)
mail_entry.insert(0, "angela@mail.com")
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

# Button
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)
add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)



window.mainloop()