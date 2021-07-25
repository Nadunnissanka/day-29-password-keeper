from tkinter import *
# you have to import messagebox module separately
from tkinter import messagebox
import random
import pyperclip

FONT_NAME = "Arial"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    # required list
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    # select randomize elements from above list
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)
    # generate password by shuffle
    password_letters = [random.choice(letters) for char in range(nr_letters)]
    password_symbols = [random.choice(symbols) for char in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for char in range(nr_numbers)]
    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(END, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    # get entered values from tkinter entries
    add_website_entry = website_entry.get()
    add_username_entry = username_entry.get()
    add_password_entry = password_entry.get()
    if len(add_website_entry) == 0 or len(add_password_entry) == 0:
        messagebox.showinfo(title="Oops", message="Please fill all required fields!")
    else:
        # message box tkinter
        # Important -> messagebox.askokcancel will return a boolean based on the input
        ready_to_save = messagebox.askokcancel(title=add_website_entry,
                                               message=f"These are the details entered: \n Email : {add_username_entry}\n Password : {add_password_entry}\n\n Is above information okay to Save?")
        if ready_to_save:
            # writing the password into password_store.txt file
            with open("password_store.txt", mode="a") as password_file:
                password_file.write(f"{add_website_entry} | {add_username_entry} | {add_password_entry}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("My Pass v0.1 Build 0.1")
window.config(padx=20, pady=20)

# image canvas
canvas = Canvas(width=200, height=200)
my_pass_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=my_pass_image)
canvas.grid(row=0, column=1)

# website label section
website_label = Label(text="Website :", font=(FONT_NAME, 12, "normal"))
website_label.grid(row=1, column=0)
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

# Email/Username section
username_label = Label(text="Username/Email :", font=(FONT_NAME, 12, "normal"))
username_label.grid(row=2, column=0)
username_entry = Entry(width=35)
username_entry.grid(row=2, column=1, columnspan=2)
username_entry.insert(END, "nadunnissanka@icloud.com")

# password
password_label = Label(text="Password :", font=(FONT_NAME, 12, "normal"))
password_label.grid(row=3, column=0)
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)
password_generate_button = Button(text="Generate Password", command=generate_password)
password_generate_button.grid(row=3, column=2)

# recorde Add button
add_button = Button(text="Add Password", width=36, command=add_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
