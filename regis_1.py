import tkinter as tk
import customtkinter 
import database as database
from PIL import ImageTk, Image
from tkinter import messagebox
import login_1
import re  

customtkinter.set_appearance_mode("System")  
customtkinter.set_default_color_theme("green") 

app = customtkinter.CTk()  
app.attributes('-fullscreen', False)
app.title('Register')

def button_function():
    app.destroy()
    w = customtkinter.CTk()  
    w.geometry("1280x720")
    w.title('Welcome')
    l1=customtkinter.CTkLabel(master=w, text="Home Page", font=('Century Gothic', 60))
    l1.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    w.mainloop()

img1 = ImageTk.PhotoImage(Image.open("img/preview.jpg").resize((1370, 800)))
l1 = customtkinter.CTkLabel(master=app, image=img1)
l1.pack()

class Entry:
    def __init__(self, master):
        self.frame = customtkinter.CTkFrame(master=master, width=320, height=380, corner_radius=15)
        self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        l2 = customtkinter.CTkLabel(master=self.frame, text="Register your Account", font=('Century Gothic', 20))
        l2.place(x=50, y=5)

        self.entry0 = customtkinter.CTkEntry(master=self.frame, width=220, placeholder_text='Name')
        self.entry0.place(x=50, y=55)

        self.entry1 = customtkinter.CTkEntry(master=self.frame, width=220, placeholder_text='Email')
        self.entry1.place(x=50, y=110)

        self.entry2 = customtkinter.CTkEntry(master=self.frame, width=220, placeholder_text='Password', show="*")
        self.entry2.place(x=50, y=165)

        l3 = customtkinter.CTkLabel(master=self.frame, text="Forget password?", font=('Century Gothic', 12))
        l3.place(x=155, y=194)

        self.entry3 = customtkinter.CTkEntry(master=self.frame, width=220, placeholder_text='Number')
        self.entry3.place(x=50, y=225)

        # Create custom button
        self.button1 = customtkinter.CTkButton(master=self.frame, width=220, text="Login", command=self.validate, corner_radius=6)
        self.button1.place(x=50, y=290)

        self.img2 = ImageTk.PhotoImage(Image.open("img/image8-2.webp").resize((20, 20)))
        self.img3 = ImageTk.PhotoImage(Image.open("img/mathew-macquarrie-u6OnpbMuZAs-unsplash.jpg").resize((20, 20)))
        self.button2 = customtkinter.CTkButton(master=self.frame, image=self.img2, text="Google", width=100, height=20, compound="left", fg_color='white', text_color='black', hover_color='#AFAFAF') 
        self.button2.place(x=50, y=340)

        self.button3 = customtkinter.CTkButton(master=self.frame, image=self.img3, text="Facebook", width=100, height=20, compound="left", fg_color='white', text_color='black', hover_color='#AFAFAF')
        self.button3.place(x=170, y=340)

    def validate(self):
        password = self.entry2.get()
        phone_number = self.entry3.get()

        # Check if any fields are empty
        if self.entry0.get() == "" or self.entry1.get() == "" or password == "" or phone_number == "":
            messagebox.showerror("Error", "Please fill all the fields")
        
        # Password validation regex (minimum 8 characters, one uppercase, one lowercase, one digit, one special char)
        elif not re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$', password):
            messagebox.showerror("Error", "Password must be at least 8 characters long, with uppercase, lowercase, digit, and special character")
        
        # Phone number validation regex (10 digits only)
        elif not re.match(r'^\d{10}$', phone_number):
            messagebox.showerror("Error", "Phone number must be 10 digits")

        else:
            data = (self.entry0.get(), self.entry1.get(), password, phone_number)
            response = database.registerUser(data)
            if response:
                messagebox.showinfo("Success", "User Registered")
                app.destroy()
                login_1.Entry()
            else:
                messagebox.showerror("Error", "Not Registered")

entry = Entry(app)
app.mainloop()
