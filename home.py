import tkinter as tk
import customtkinter
from PIL import ImageTk, Image
from tkinter import messagebox
import regis_1

class WelcomeScreen:
    def __init__(self):
        # Create main window
        self.window = customtkinter.CTk()
        self.window.attributes('-fullscreen', False)
        self.window.geometry("1366x768")
        self.window.title('HOME')

        # Load images and set up layout
        self.load_image()

         # Welcome message
        self.welcome_label = customtkinter.CTkLabel(master=self.window, text="Welcome to the Application", font=("Arial", 24, "bold"))
        self.welcome_label.place(x=880, y=50)

        # Breaking down the news info label into multiple lines with the same padding
        news_info_text = [
            "Info fusion provides the best news from all over the world.",
            "Real-time updates on important events.",
            "Provide real-feel temperature considering wind chill, humidity, etc."
        ]

        # Start placing them one below the other
        y_position = 120  # Starting y position for the first line
        for line in news_info_text:
            label = customtkinter.CTkLabel(master=self.window, text=line, font=("Arial", 20))
            label.place(x=780, y=y_position)  # Same x position, different y positions
            y_position += 40  # Move y position down by 40 units for the next line

        # Add Login, Register, and Edit buttons at the top right corner
        self.login_button = customtkinter.CTkButton(master=self.window, width=400, height=50, text="Login", command=self.login_action, corner_radius=6)
        self.login_button.place(x=850, y=540)

        self.login_info = customtkinter.CTkLabel(master=self.window, text="If you are already registered then login:", font=("Arial", 20, "bold"))
        self.login_info.place(x=850, y=510)

        self.register_button = customtkinter.CTkButton(master=self.window, width=400, height=50, text="Register", command=self.register_action)
        self.register_button.place(x=850, y=340)

        self.register_info = customtkinter.CTkLabel(master=self.window, text="If you are a new visitor, first register:", font=("Arial", 20, "bold"))
        self.register_info.place(x=850, y=310)

        # self.edit_button = customtkinter.CTkButton(master=self.window, text="Edit", command=self.edit_action)
        # self.edit_button.place(relx=0.70 + button_padding * 2, rely=0.05)  # Adjusted with padding for the third button

        # self.create_widgets()

        # Start the main loop
        self.window.mainloop()

    def load_image(self):
        # Left side image (could be a logo or anything for aesthetics)
        self.side_img = ImageTk.PhotoImage(Image.open('D:/Games/py(o7)/newsproject/img/side_leftimg.jpg').resize((700, 1000)))
        self.side_image_label = customtkinter.CTkLabel(master=self.window, image=self.side_img)
        self.side_image_label.pack(side="left", padx=0, pady=0)

    def login_action(self):
        messagebox.showinfo("Login", "Login button clicked!")

    def register_action(self):
        messagebox.showinfo("Register", "Register button clicked!")
        WelcomeScreen.welcome.destroy()
        regis_1.Entry()


    def edit_action(self):
        messagebox.showinfo("Edit", "Edit button clicked!")

    # def create_widgets(self):
        # # Welcome message
        # self.welcome_label = customtkinter.CTkLabel(master=self.window, text="Welcome to the Application", font=("Arial", 24, "bold"))
        # self.welcome_label.place(x=880, y=50)

        # # Breaking down the news info label into multiple lines with the same padding
        # news_info_text = [
        #     "Info fusion provides the best news from all over the world.",
        #     "Real-time updates on important events.",
        #     "Provide real-feel temperature considering wind chill, humidity, etc."
        # ]

        # # Start placing them one below the other
        # y_position = 120  # Starting y position for the first line
        # for line in news_info_text:
        #     label = customtkinter.CTkLabel(master=self.window, text=line, font=("Arial", 20))
        #     label.place(x=780, y=y_position)  # Same x position, different y positions
        #     y_position += 40  # Move y position down by 40 units for the next line

        # # Add Login, Register, and Edit buttons at the top right corner
        # self.login_button = customtkinter.CTkButton(master=self.window, width=400, height=50, text="Login", command=self.login_action, corner_radius=6)
        # self.login_button.place(x=850, y=540)

        # self.login_info = customtkinter.CTkLabel(master=self.window, text="If you are already registered then login:", font=("Arial", 20, "bold"))
        # self.login_info.place(x=850, y=510)

        # self.register_button = customtkinter.CTkButton(master=self.window, width=400, height=50, text="Register", command=self.register_action)
        # self.register_button.place(x=850, y=340)

        # self.register_info = customtkinter.CTkLabel(master=self.window, text="If you are a new visitor, first register:", font=("Arial", 20, "bold"))
        # self.register_info.place(x=850, y=310)

        # # self.edit_button = customtkinter.CTkButton(master=self.window, text="Edit", command=self.edit_action)
        # # self.edit_button.place(relx=0.70 + button_padding * 2, rely=0.05)  # Adjusted with padding for the third button

# Run the application
if __name__ == "__main__":
    app = WelcomeScreen()
