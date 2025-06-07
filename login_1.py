import tkinter as tk
import customtkinter
import database as database
from PIL import ImageTk, Image
from tkinter import messagebox
import dashboard
import page1
class Entry:
    def __init__(self):
                
        customtkinter.set_appearance_mode("System")  
        # customtkinter.set_default_color_theme("green") 

        self.app = customtkinter.CTk()  
        self.app.attributes('-fullscreen',False)
        # app.geometry("600x440")
        self.app.title('Login')


        self.img1=ImageTk.PhotoImage(Image.open("img/mathew-macquarrie-u6OnpbMuZAs-unsplash.jpg").resize((1370,800)))
        self.l1=customtkinter.CTkLabel(master=self.app,image=self.img1)
        self.l1.pack()

        self.frame=customtkinter.CTkFrame(master=self.l1, width=720, height=460, corner_radius=15,fg_color="#272926")
        self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.side_image = Image.open('img/left_img_login_page-removebg-preview.png').resize((400,400))
        photo = ImageTk.PhotoImage(self.side_image)
        self.side_image_label = tk.Label(self.frame, image=photo, bg="#272926")
        self.side_image_label.image = photo
        self.side_image_label.place(x=10, y=50)

        l2=customtkinter.CTkLabel(master=self.frame, text="Log into your Account",font=('Century Gothic',20))
        l2.place(x=450, y=45)

        self.entry_mail=customtkinter.CTkEntry(master=self.frame, width=220, placeholder_text='Email')
        self.entry_mail.place(x=450, y=110)

        self.entry_pwd=customtkinter.CTkEntry(master=self.frame, width=220, placeholder_text='Password', show="*")
        self.entry_pwd.place(x=450, y=165)

        l3=customtkinter.CTkLabel(master=self.frame, text="Forget password?",font=('Century Gothic',12))
        l3.place(x=455,y=195)

        #Create custom button
        self.button1 = customtkinter.CTkButton(master=self.frame, width=220, text="Login", command=self.check_credentials, corner_radius=6)
        self.button1.place(x=450, y=240)

        self.img2=ImageTk.PhotoImage(Image.open("img/image8-2.webp").resize((20,20),))
        self.img3=ImageTk.PhotoImage(Image.open("img/3D_Square_with_Facebook_Logo.jpg").resize((20,20),))
        self.button2= customtkinter.CTkButton(master=self.frame, image=self.img2, text="Google", width=100, height=20, compound="left", fg_color='white', text_color='black', hover_color='#AFAFAF')
        self.button2.place(x=450, y=290)

        self.button3= customtkinter.CTkButton(master=self.frame, image=self.img3, text="Facebook", width=100, height=20, compound="left", fg_color='white', text_color='black', hover_color='#AFAFAF')
        self.button3.place(x=580, y=290)


        self.app.mainloop()
     
    def check_credentials(self):
        email = self.entry_mail.get()
        password = self.entry_pwd.get()

        if email == "" or password == "":
            messagebox.showerror("Error", "Please fill all the fields")
        else:
            result = database.loginUser((email, password))
            if result:
                messagebox.showinfo("Success", "Login Successful")
                self.app.destroy()
                print(result[0])
                page1.MainApp(result[0])
                
            else:
                messagebox.showerror("Error", "Invalid Email or Password")


if __name__=="__main__":

    entry = Entry()
    


