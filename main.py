import customtkinter as ct
import tkinter as tk
from time import strftime
from datetime import *
import pyttsx3 as tts
import speech_recognition as sr
import comp_control
import basic_functions
import json
from tkinter import Image, PhotoImage, ttk
from PIL import Image
from customtkinter import *

# Use #242424 as background color to blend in with device if using dark mode
# Use white for light mode

engine = tts.init()

name = "Vex"

#functions down here

show_time = True  # Global variable to keep track of whether to show the time label

entries = []  # Initialize an empty list to store the entries

def update_time():
    global show_time
    if show_time:
        string_time = "The time is currently " + strftime('%I:%M %p')  # Change here to display time in AM/PM format
        time_label.config(text=string_time)
    app.after(1000, update_time)

# Create a function to add a placeholder to an entry
def add_placeholder(entry, placeholder):
    # Set the initial text to the placeholder
    entry.insert(0, placeholder)
    # Set the initial foreground color to grey
    entry.config(fg="grey")
    # Define a function to handle focus events
    def focus(event):
        # If the entry is empty and gets focus, delete the placeholder and set the foreground color to black
        if entry.get() == placeholder:
            entry.delete(0, tk.END)
            entry.config(fg="black")
        # If the entry is not empty and loses focus, do nothing
        elif event.type == "FocusOut":
            pass
        # If the entry is empty and loses focus, restore the placeholder and set the foreground color to grey
        else:
            entry.insert(0, placeholder)
            entry.config(fg="grey")
    # Bind the focus events to the entry
    entry.bind("<FocusIn>", focus)
    entry.bind("<FocusOut>", focus)

def show_tabs():
    print("placeholder")



app = ct.CTk()

app.title("da muhfukin app")

# Window geometrics
window_width = 900
window_height = 600

screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()

center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# Set the position of the window to the center of the screen
app.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

app.attributes('-topmost', 1)
app.attributes('-alpha', 1)

app.iconbitmap('./icons/Skater xbox pfp.ico')

app.resizable(False, False)

ct.set_appearance_mode("system")
appearance_mode = get_appearance_mode()
if appearance_mode == "Dark":
    print("Dark mode")
elif appearance_mode == "Light":
    print("Light mode")

# App content below

home_img = ct.CTkImage(light_image=Image.open("home.png"),
                                  dark_image=Image.open("home.png"),
                                  size=(30, 30))
tasks_img = ct.CTkImage(light_image=Image.open("tasks.png"),
                                  dark_image=Image.open("tasks.png"),
                                  size=(30, 30))
chat_img = ct.CTkImage(light_image=Image.open("chat.png"),
                                  dark_image=Image.open("chat.png"),
                                  size=(30, 30))
data_img = ct.CTkImage(light_image=Image.open("data.png"),
                                  dark_image=Image.open("data.png"),
                                  size=(30, 30))
settings_img = ct.CTkImage(light_image=Image.open("settings.png"),
                                  dark_image=Image.open("settings.png"),
                                  size=(30, 30))

time_label = tk.Label(app, font=('calibri', 40, 'bold'), background='#242424', foreground='white')
time_label.pack(padx=0, pady=0, anchor='center')


def show_home_content():
    global some_label
    some_label = tk.Label(app, text="Wazzap?")
    some_label.pack(padx=0, pady=0, anchor='center')

def hide_home_content():
    some_label.pack_forget()

home_label = ct.CTkLabel(app, font=('calibri', 40, 'bold'), text="Home stuff", bg_color='#242424', fg_color='white')
home_label.pack(padx=0, pady=50, anchor='center')

#Bottom navigation will consist of 5 buttons in this exact order: Home, Tasks, Chat, Data, Settings
home_btn = ct.CTkButton(app, font=('calibri', 40, 'bold'), bg_color='#242424', fg_color='#242424', text_color='white', image=home_img, text="", command=show_home_content())
home_btn.pack(padx=0, pady=0, anchor='n')

tasks_btn = ct.CTkButton(app, font=('calibri', 40, 'bold'), bg_color='#242424', fg_color='#242424', text_color='white', image=tasks_img, text="", command=hide_home_content())
tasks_btn.pack(padx=20, pady=30, anchor='n')

chat_btn = ct.CTkButton(app, font=('calibri', 40, 'bold'), bg_color='#242424', fg_color='#242424', text_color='white', image=chat_img, text="")
chat_btn.pack(padx=30, pady=0, anchor='n')

data_btn = ct.CTkButton(app, font=('calibri', 40, 'bold'), bg_color='#242424', fg_color='#242424', text_color='white', image=data_img, text="")
data_btn.pack(padx=40, pady=0, anchor='n')

settings_btn = ct.CTkButton(app, font=('calibri', 40, 'bold'), bg_color='#242424', fg_color='#242424', image=settings_img, text="")
settings_btn.pack(padx=50, pady=0, anchor='n')

update_time()

if __name__ == '__main__':
    app.mainloop()
    