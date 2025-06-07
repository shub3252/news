import customtkinter as ctk
from PIL import ImageTk, Image
import dashboard
import dashboard2

class MainApp:
    def __init__(self, user):
        # Initialize main root window
        self.root = ctk.CTk()
        self.root.attributes('-fullscreen', False)
        self.root.geometry("1366x768")
        self.root.title("Home Page")
        self.user = user
        print(f"User ID: {self.user}")

        # Load and set background image on the left
        self.load_side_image()

        # Welcome message
        self.welcome_label = ctk.CTkLabel(master=self.root, text="Welcome to the Info fusion", font=("Arial", 24, "bold"))
        self.welcome_label.place(x=880, y=50)

        # Display news info text in multiple lines
        news_info_text = [
            "Info fusion provides the best news from all over the world.",
            "Real-time updates on important events.",
            "Provide real-feel temperature considering wind chill, humidity, etc."
        ]
        
        y_position = 120  # Starting y position for the first line
        for line in news_info_text:
            label = ctk.CTkLabel(master=self.root, text=line, font=("Arial", 20))
            label.place(x=780, y=y_position)
            y_position += 40  # Increment y position for each line

        # Add buttons for News and Weather, similar to Login/Register style
        self.news_button = ctk.CTkButton(master=self.root, width=400, height=50, text="News", command=self.open_news_page, corner_radius=6)
        self.news_button.place(x=850, y=340)

        self.news_info = ctk.CTkLabel(master=self.root, text="Explore global news:", font=("Arial", 20, "bold"))
        self.news_info.place(x=850, y=310)

        self.weather_button = ctk.CTkButton(master=self.root, width=400, height=50, text="Weather Details", command=self.open_weather_page, corner_radius=6)
        self.weather_button.place(x=850, y=540)

        self.weather_info = ctk.CTkLabel(master=self.root, text="Check detailed weather information:", font=("Arial", 20, "bold"))
        self.weather_info.place(x=850, y=510)

        # Start the main loop
        self.root.mainloop()

    def load_side_image(self):
        # Load the side image (logo or aesthetic image)
        try:
            side_img = Image.open("img/Untitled (2).png").resize((700, 1000))
            self.side_image = ImageTk.PhotoImage(side_img)
            self.side_image_label = ctk.CTkLabel(master=self.root, image=self.side_image)
            self.side_image_label.pack(side="left", padx=0, pady=0)
        except FileNotFoundError:
            print("Background image not found. Please check the path.")

    def open_news_page(self):
        self.root.destroy()
        dashboard.Dashboard2(self.user)

    def open_weather_page(self):
        self.root.destroy()
        dashboard2.Dashboard2(self.user)

# Run the application
if __name__ == "__main__":
    app = MainApp("1")





# import customtkinter as ctk
# import dashboard
# # Define the main application class
# class MainApp(ctk.CTk):

#     def __init__(self):
#         super().__init__()

#         # Main window configuration
#         self.title("Professional UI")
#         self.geometry("800x500")  # Large window size
        
#         # Set appearance and scaling
#         ctk.set_appearance_mode("System")  # Modes: "System" (default), "Dark", "Light"
#         ctk.set_default_color_theme("blue")  # Themes: "blue" (default), "green", "dark-blue"

#         # Frame to contain the buttons
#         button_frame = ctk.CTkFrame(self, fg_color="transparent")
#         button_frame.pack(pady=100)

#         # Button to open News page (with loading screen)
#         news_button = ctk.CTkButton(button_frame, text="News", width=200, height=50, command=self.show_loading_screen)
#         news_button.grid(row=0, column=0, padx=20)

#         # Button to open Weather Details page directly
#         weather_button = ctk.CTkButton(button_frame, text="Weather Details", width=200, height=50, command=self.open_weather_page)
#         weather_button.grid(row=0, column=1, padx=20)

#     # Function to show the loading screen and close home screen
#     def show_loading_screen(self):
#         # Destroy the main application window (home screen)
#         self.destroy()

#         # Create a loading window
#         self.loading_window = ctk.CTkToplevel()
#         self.loading_window.title("Loading")
#         self.loading_window.geometry("400x200")
#         loading_label = ctk.CTkLabel(self.loading_window, text="Loading, please wait...", font=("Arial", 16))
#         loading_label.pack(pady=50)
        
#         # Schedule the loading window to close after 10 seconds
#         self.loading_window.after(10000, self.close_loading_screen)

#         # After a delay, close the loading screen and open the News page
#         self.loading_window.after(2000, lambda: self.open_news_page())

#     # Function to close the loading screen manually
#     def close_loading_screen(self):
#         if self.loading_window.winfo_exists():  # Check if loading window still exists
#             self.loading_window.destroy()

#     # Function to open the News page and close the loading window
#     def open_news_page(self):
        
        
#         # Create the News page window
#         dashboard.Dashboard2("1")

#     # Function to open the Weather Details page directly
#     def open_weather_page(self):
#         weather_window = ctk.CTkToplevel(self)
#         weather_window.title("Weather Details")
#         weather_window.geometry("600x400")
#         weather_label = ctk.CTkLabel(weather_window, text="Welcome to the Weather Details Page", font=("Arial", 18))
#         weather_label.pack(pady=20)

# # Run the application if this file is the main program
# if __name__ == "__main__":
#     app = MainApp()
#     app.mainloop()


# import customtkinter as ctk
# import dashboard
# import dashboard2
# from PIL import ImageTk, Image

# class MainApp:
#     def __init__(self, user):
#         # Initialize main root window
#         self.root = ctk.CTk()
#         self.user = user
#         print(f"User ID: {self.user}")
        
#         # Configure main window
#         self.root.title("Home Page")
#         self.root.geometry("1350x750")  # Large window size

#         # Set appearance and color theme
#         ctk.set_appearance_mode("System")  # "System" (default), "Dark", "Light"
#         ctk.set_default_color_theme("blue")  # Themes: "blue", "green", "dark-blue"

#         # Set background image
#         bg_image = Image.open("img/bg1.jpg")
#         bg_image = bg_image.resize((1350, 750))
#         self.bg_image = ImageTk.PhotoImage(bg_image)

#         # Create label for background image
#         bg_label = ctk.CTkLabel(self.root, image=self.bg_image, text="")
#         bg_label.place(x=0, y=0, relwidth=1, relheight=1)

#         # Set transparent frame for buttons
#         button_frame = ctk.CTkFrame(self.root, fg_color="transparent")
#         button_frame.pack(pady=200)  # Centered with ample spacing

#         # Add title label with a multi-line message
#         title_text = (
#             "Welcome to the Dashboard\n"
#             "Info fusion provides the best news from all over the world.\n"
#             "Real-time updates on important events.\n"
#             "Provide real-feel temperature considering wind chill, humidity, etc."
#         )
        
#         title_label = ctk.CTkLabel(button_frame, text=title_text, font=("Helvetica", 24, "bold"), justify="center")
#         title_label.grid(row=0, columnspan=2, pady=20)  # Large title centered over buttons

#         # Add buttons with custom styles
#         self.create_button(button_frame, "News", self.open_news_page, row=1, col=0)
#         self.create_button(button_frame, "Weather Details", self.open_weather_page, row=1, col=1)
        
#         # Start the main loop
#         self.root.mainloop()

#     def create_button(self, frame, text, command, row, col):
#         """
#         Helper function to create styled buttons.
#         """
#         button = ctk.CTkButton(
#             frame,
#             text=text,
#             width=220,
#             height=50,
#             command=command,
#             font=("Helvetica", 16),
#             corner_radius=10,  # Rounded button corners
#             hover=True,
#             hover_color="#2980b9",  # Hover effect color
#         )
#         button.grid(row=row, column=col, padx=30, pady=10)  # Adequate padding for button separation
    
#     def open_news_page(self):
#         self.root.destroy()
#         dashboard.Dashboard2(self.user)

#     def open_weather_page(self):
#         self.root.destroy()
#         dashboard2.Dashboard2(self.user)

# # Run the application
# if __name__ == "__main__":
#     app = MainApp("1")