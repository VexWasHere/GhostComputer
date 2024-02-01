import customtkinter as ct
import tkinter as tk
from time import strftime
from datetime import *
import pyttsx3 as tts
import speech_recognition as sr


# Use #242424 as background color to blend in with device if using dark mode
# Use white for light mode

engine = tts.init()

name = "Vex"

#functions down here

def update_time():
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


app = ct.CTk()

app.title("My App")

# Window geometrics
window_width = 600
window_height = 200

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

# App content below

welcome_label = tk.Label(app, font=('calibri', 40, 'bold'), background='#242424', foreground='white', text=f"Welcome, {name}!")
welcome_label.pack(padx=0, pady=0, anchor='center')

time_label = tk.Label(app, font=('calibri', 40, 'bold'), background='#242424', foreground='white')
time_label.pack(padx=1.0, pady=1.0, anchor='center')

entry = ct.CTkEntry(app, placeholder_text="What do you want cuh?")
entry.pack(ipadx=200, ipady=5, padx=1, pady=5, anchor="center")



update_time()

if __name__ == '__main__':
    app.mainloop()