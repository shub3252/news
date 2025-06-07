 with your image path
        bg_image = bg_image.resize((600, 400))  # Resize to fit the window
        self.bg_image = ImageTk.PhotoImage(bg_image)
        
        # Create a label for the background image
        bg_label = ctk.CTkLabel(self.root, image=self.bg_image, text="")
        bg_label.place(x=0, y=0, relwidth=1, relheight=1) 