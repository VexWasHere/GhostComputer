import customtkinter as ct
import tkinter as tk
from time import strftime
from datetime import datetime
import pyttsx3 as tts
import speech_recognition as sr
import unfinished.comp_control as comp_control
import unfinished.basic_functions as basic_functions
import json
from PIL import Image

class Application:
    def __init__(self):
        self.app = ct.CTk()
        self.app.title("da muhfukin app")
        self.window_width = 900
        self.window_height = 600
        self.center_x = int(self.app.winfo_screenwidth() / 2 - self.window_width / 2)
        self.center_y = int(self.app.winfo_screenheight() / 2 - self.window_height / 2)
        self.app.geometry(f'{self.window_width}x{self.window_height}+{self.center_x}+{self.center_y}')
        self.app.attributes('-topmost', 1)
        self.app.attributes('-alpha', 1)
        self.app.iconbitmap('./icons/Skater xbox pfp.ico')
        self.app.resizable(False, False)
        ct.set_appearance_mode("system")
        self.appearance_mode = ct.get_appearance_mode()
        if self.appearance_mode == "Dark":
            print("Dark mode")
        elif self.appearance_mode == "Light":
            print("Light mode")

        self.time_label = tk.Label(self.app, font=('calibri', 40, 'bold'), background='#242424', foreground='white')
        self.time_label.pack(padx=0, pady=0, anchor='center')

        self.home_img = ct.CTkImage(light_image=Image.open("home.png"), dark_image=Image.open("home.png"), size=(30, 30))
        self.tasks_img = ct.CTkImage(light_image=Image.open("tasks.png"), dark_image=Image.open("tasks.png"), size=(30, 30))
        self.chat_img = ct.CTkImage(light_image=Image.open("chat.png"), dark_image=Image.open("chat.png"), size=(30, 30))
        self.data_img = ct.CTkImage(light_image=Image.open("data.png"), dark_image=Image.open("data.png"), size=(30, 30))
        self.settings_img = ct.CTkImage(light_image=Image.open("settings.png"), dark_image=Image.open("settings.png"), size=(30, 30))

        self.home_btn = ct.CTkButton(self.app, font=('calibri', 40, 'bold'), bg_color='#242424', fg_color='#242424', text_color='white', image=self.home_img, text="", command=self.show_home_content)
        self.home_btn.pack(padx=0, pady=0, anchor='n')

        self.tasks_btn = ct.CTkButton(self.app, font=('calibri', 40, 'bold'), bg_color='#242424', fg_color='#242424', text_color='white', image=self.tasks_img, text="", command=self.show_tasks_content)
        self.tasks_btn.pack(padx=20, pady=30, anchor='n')

        self.chat_btn = ct.CTkButton(self.app, font=('calibri', 40, 'bold'), bg_color='#242424', fg_color='#242424', text_color='white', image=self.chat_img, text="", command=self.show_chat_content)
        self.chat_btn.pack(padx=30, pady=0, anchor='n')

        self.data_btn = ct.CTkButton(self.app, font=('calibri', 40, 'bold'), bg_color='#242424', fg_color='#242424', text_color='white', image=self.data_img, text="", command=self.show_data_content)
        self.data_btn.pack(padx=40, pady=0, anchor='n')

        self.settings_btn = ct.CTkButton(self.app, font=('calibri', 40, 'bold'), bg_color='#242424', fg_color='#242424', image=self.settings_img, text="", command=self.show_settings_content)
        self.settings_btn.pack(padx=50, pady=0, anchor='n')

        self.show_home_content()
        self.update_time()

    def show_home_content(self):
        global home_label
        self.home_label = tk.Label(self.app, text="Home")
        self.home_label.pack(padx=0, pady=0, anchor='center', side=tk.TOP)
        self.tasks_label.pack_forget()
        self.chat_label.pack_forget()
        self.data_label.pack_forget()
        self.settings_label.pack_forget()

    def show_tasks_content(self):
        try:
            global tasks_label
            self.tasks_label = ct.CTkLabel(self.app, text="Tasks")
            self.tasks_label.pack(padx=0, pady=0, anchor='center', side=tk.TOP)
            self.home_label.pack_forget()
            self.chat_label.pack_forget()
            self.data_label.pack_forget()
            self.settings_label.pack_forget()
        except Exception as e:
            print(f"Error: {e}")

    def show_chat_content(self):
        try:
            global chat_label
            self.chat_label = ct.CTkLabel(self.app, text="Chat")
            self.chat_label.pack(padx=0, pady=0, anchor='center', side=tk.TOP)
            self.home_label.pack_forget()
            self.tasks_label.pack_forget()
            self.data_label.pack_forget()
            self.settings_label.pack_forget()
        except Exception as e:
            print(f"Error: {e}")

    def show_data_content(self):
        try:
            global data_label
            self.data_label = ct.CTkLabel(self.app, text="Data")
            self.data_label.pack(padx=0, pady=0, anchor='center', side=tk.TOP)
            self.home_label.pack_forget()
            self.tasks_label.pack_forget()
            self.chat_label.pack_forget()
            self.settings_label.pack_forget()
        except Exception as e:
            print(f"Error: {e}")

    def show_settings_content(self):
        try:
            global settings_label
            self.settings_label = ct.CTkLabel(self.app, text="Settings")
            self.settings_label.pack(padx=0, pady=0, anchor='center', side=tk.TOP)
            self.home_label.pack_forget()
            self.tasks_label.pack_forget()
            self.chat_label.pack_forget()
            self.data_label.pack_forget()
        except Exception as e:
            print(f"Error: {e}")

    def update_time(self):
        string_time = "The time is currently " + strftime('%I:%M %p')
        self.time_label.config(text=string_time)
        self.app.after(1000, self.update_time)

if __name__ == '__main__':
    app = Application()
    app.app.mainloop()