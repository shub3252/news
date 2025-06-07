import tkinter as tk
import customtkinter
from PIL import ImageTk, Image
from tkinter import messagebox

class WelcomeScreen:
    def __init__(self):
        self.window = customtkinter.CTk()
        self.window.attributes('-fullscreen', False)
        self.window.title('Login')
        # self.window.wm_attributes("-alpha", 0.5)
        self.load_image()
        self.create_widgets()

        self.window.mainloop()

    def load_image(self):
        img1 = ImageTk.PhotoImage(Image.open("img/pexels-gdtography-277628-911738.jpg").resize((1370, 800)))
        self.image_label = customtkinter.CTkLabel(master=self.window, image=img1)
        self.image_label.pack()

    def create_widgets(self):
        self.frame = customtkinter.CTkFrame(self.window, width=1370, height=50, fg_color="white" ,bg_color="black")
        self.frame.place(x=0, y=0)
        

        self.title_label = customtkinter.CTkLabel(master=self.frame, text="INFO FUSION", text_color="black" ,font=('Century Gothic', 20))
        self.title_label.place(x=5, y=5)

        self.button1 = customtkinter.CTkButton(master=self.frame, text="Admin Login", width=100, height=50, compound="left", fg_color='white', text_color='black', hover_color='#AFAFAF')
        self.button1.place(x=1000, y=0)

        self.button2 = customtkinter.CTkButton(master=self.frame, text="Sign Up", width=100, height=50, compound="left", fg_color='white', text_color='black', hover_color='#AFAFAF')
        self.button2.place(x=1130, y=0)

        self.button3 = customtkinter.CTkButton(master=self.frame, text="Login", width=100, height=50, compound="left", fg_color='white', text_color='black', hover_color='#AFAFAF')
        self.button3.place(x=1250, y=0)

        self.frame2 =customtkinter.CTkFrame(self.window, width=500, height=500, bg_color="#FFFFFF",fg_color="transparent")
        self.frame2.place(x=50,y=100)
        
        self.side_image = Image.open('img/Untitled (2).png').resize((500,500))
        photo = ImageTk.PhotoImage(self.side_image)
        self.side_image_label = tk.Label(self.frame2, image=photo, bg="white",foreground="white")
        self.side_image_label.image = photo
        self.side_image_label.place(x=10, y=10)


        self.frame3=customtkinter.CTkFrame(self.window, width=450 ,height=550 ,bg_color="#FFFFFF",fg_color="transparent")
        self.frame3.place(x=700,y=100)

       
    



if __name__ == "__main__":
    WelcomeScreen()





















































# import tkinter as tk
# import customtkinter
# import database as database
# from PIL import ImageTk, Image
# from tkinter import messagebox
# import regis_1



# class wel:
#     def __init__(self, master):
#         # customtkinter.set_windowearance_mode("System")  
#         # customtkinter.set_default_color_theme("green") 

#         window = customtkinter.CTk()  
#         window.attributes('-fullscreen',False)
#         # window.geometry("600x440")
#         window.title('Login')



#         img1=ImageTk.PhotoImage(Image.open("D:/Games/py(o7)/project/img/mathew-macquarrie-u6OnpbMuZAs-unsplash.jpg").resize((1370,800)))
#         l1=customtkinter.CTkLabel(master=window,image=img1)
#         l1.pack()

#         self.frame=customtkinter.CTkFrame(window, width=1370, height=50,fg_color="white")
#         self.frame.place(x=0,y=0)
#         l2=customtkinter.CTkLabel(master=self.frame, text="INFO FUSION",font=('Century Gothic',20))
#         l2.place(x=5, y=5)
#         self.button1= customtkinter.CTkButton(master=self.frame,  text="Admin Login", width=100, height=50, compound="left", fg_color='white', text_color='black', hover_color='#AFAFAF')
#         self.button1.place(x=1000, y=0)

#         self.button2= customtkinter.CTkButton(master=self.frame,  text="Sign Up", width=100, height=50, compound="left", fg_color='white', text_color='black'   ,hover_color='#AFAFAF')
#         self.button2.place(x=1130, y=0)

#         self.button3= customtkinter.CTkButton(master=self.frame,  text="Login", width=100, height=50, compound="left", fg_color='white', text_color='black', hover_color='#AFAFAF')
#         self.button3.place(x=1250, y=0)



#         window.mainloop()

#     # def reg(self):
#     #     self.window.destroy()
#     #     window = ()
#     #     regis_1.Entry(window)
#     #     print("hi")
#     #  entry=wel("User")
# entry = wel()




















