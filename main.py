import tkinter as tk
from tkinter import ttk
import pyttsx3

engine = pyttsx3.init()

root = tk.Tk()

root.title("Ghost Computer")

window_width = 600
window_height = 400

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
root.resizable(False, False)
root.attributes('-alpha', 1) #Opaque but can be lowered to be translucent.
root.attributes('-topmost', 1) #Tab in front of all other tabs. Can be lowered to back.
root.iconbitmap('./icons/misc.ico')


welcome = ttk.Label(root, text="Welcome Vex! What would you like today?")
welcome.pack()

engine.say("Welcome Vex! What would you like today?")


if __name__ == '__main__':
    root.mainloop() 
    engine.runAndWait()