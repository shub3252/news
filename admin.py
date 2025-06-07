import tkinter as tk
import customtkinter
from PIL import ImageTk, Image
from tkinter import messagebox

class LoginFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master, width=320, height=380, corner_radius=15)
        self.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.create_widgets()

    def create_widgets(self):
        l2 = customtkinter.CTkLabel(master=self, text="Register your Account", font=('Century Gothic', 20))
        l2.place(x=50, y=5)

        self.entry0 = customtkinter.CTkEntry(master=self, width=220, placeholder_text='Admin email')
        self.entry0.place(x=50, y=55)

        self.entry1 = customtkinter.CTkEntry(master=self, width=220, placeholder_text='Password', show="*")
        self.entry1.place(x=50, y=110)

        l3 = customtkinter.CTkLabel(master=self, text="Forget password?", font=('Century Gothic', 12))
        l3.place(x=155, y=120)

        self.button1 = customtkinter.CTkButton(master=self, width=220, text="Login", command=self.validate, corner_radius=6)
        self.button1.place(x=50, y=290)

        self.img2 = ImageTk.PhotoImage(Image.open("img/image8-2.webp").resize((20, 20)))
        self.button2 = customtkinter.CTkButton(master=self, image=self.img2, text="Google", width=100, height=20, compound="left", fg_color='white', text_color='black', hover_color='#AFAFAF')
        self.button2.place(x=50, y=340)

        self.img3 = ImageTk.PhotoImage(Image.open("img/mathew-macquarrie-u6OnpbMuZAs-unsplash.jpg").resize((20, 20)))
        self.button3 = customtkinter.CTkButton(master=self, image=self.img3, text="Facebook", width=100, height=20, compound="left", fg_color='white', text_color='black', hover_color='#AFAFAF')
        self.button3.place(x=170, y=340)

    def validate(self):
        # Add validation logic here
        pass

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")

app = customtkinter.CTk()
app.attributes('-fullscreen', True)
app.title('Register')

img1 = ImageTk.PhotoImage(Image.open("img/preview.jpg").resize((1370, 800)))
l1 = customtkinter.CTkLabel(master=app, image=img1)
l1.pack()

login_frame = LoginFrame(app)

app.mainloop()