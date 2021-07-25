from tkinter import *

FONT_NAME = "Arial"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    # get entered values from tkinter entries
    add_website_entry = website_entry.get()
    add_username_entry = username_entry.get()
    add_password_entry = password_entry.get()
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
password_generate_button = Button(text="Generate Password")
password_generate_button.grid(row=3, column=2)

# recorde Add button
add_button = Button(text="Add Password", width=36, command=add_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
