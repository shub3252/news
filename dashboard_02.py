from tkinter import *
from PIL import Image, ImageTk

class Dashboard:
    def __init__(self, window):
        self.window = window
        self.window.title('System Management Dashboard')
        self.window.geometry('1366x768')
        self.window.state('zoomed')
        self.window.config(background="#eff5f6")

        # Window Icon
        icon =Image.open("D:/Games/py(o7)/project/img/btn1.png")
        self.window.iconphoto(True, icon)

        self.header = Frame(self.window, bg='#009df4',width=1070, height=60)
        self.header.place(x=300, y=0)

        self.logout_text = Button(self.window, text='Logout', bg='#32cf8e', font=("", 13, "bold"), bd=0, fg='white', cursor='hand2', activebackground="#32cf8e")
        self.logout_text.place(x=950, y=15)

def win():
    window = Tk()
    Dashboard(window)
    window.mainloop()

if __name__ == '__main__':
    win()




































# from tkinter import*
# from PIL import Image, ImageTk


# class dashboard:
#     def __init__(self, window):
#      self.window = window

#      self.window.title('System Management Dashboard')

#      self.window.geometry('1366x768')

#      self.window.state('zoomed')

#      self.window.config(background="#eff5f6')

#       #window Icon
#      icon PhotoImage(file='images\\pic-icon.png')
#      self.window.iconphoto (True, icon)
#      self.header Frame(self.window, bg=#009df4')

#      self.header.place(x=300, y=0, width=1070, height=60)
#      self.logout_text= Button(self.window, text='Logout', bg='#32cf8e', font=("", 13, "bold"), bd=0, fg='white', cursor='hand2", activebackground="#32cf8e'))


#      self.header Frame(self.window, bg="#009df4')
#      self.header.place( x = 500 y = 0 width I = 1070 height=60)

#      self.logout text = Button(self.window, text='Logout", bg='#32cf8e", font=("", 13, "bold"), bd = 0 , fg='white', cursor='hand', activebackground="#32cf8e')
#      self.logout_text.place( x=950,y=15)


#      def win()
#      window=Tk
#      dashboard(window)
#      window.mainloop()
#      if__name__='__main__':
#      win()