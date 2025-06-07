from tkinter import *
from tkinter import messagebox
import database
import alluser
import welcome
class Home:
    # def __init__(self):
    def __init__(self,id):
        self.screen= Tk()
        self.screen.title("Update User")
        self.width= self.screen.winfo_screenwidth()
        self.height= self.screen.winfo_screenheight()
        self.screen.geometry(f'{self.width}x{self.height}')
        
        self.id=id
        
        self.data= database.allUser((self.id))
        print("Data is ",self.data)
        
        self.label1= Label(self.screen,text=f"welcome {self.id}", font=('sans-serif',25,'bold'))
        self.label1.pack(pady=100)
        
        self.frame= Frame(self.screen,height=400, width=600,background="#474439")
        self.frame.pack()
        
        self.name= Label(self.frame,text="Name", font=('roboto',22,'bold'),bg="#474439", fg='white')
        self.name.place(x=30,y=40)
        
        self.name_entry= Entry(self.frame,font=('roboto',22,'bold'))
        self.name_entry.place(x=200,y=40)
        self.name_entry.insert(0,self.data[1])
        
        self.mail= Label(self.frame,text="Email", font=('roboto',22,'bold'),bg="#474439", fg='white')
        self.mail.place(x=30,y=100)
        
        self.mail_entry= Entry(self.frame,font=('roboto',22,'bold'))
        self.mail_entry.place(x=200,y=100)
        self.mail_entry.insert(0,self.data[2])
        
        self.pwd= Label(self.frame,text="Password", font=('roboto',22,'bold'),bg="#474439", fg='white')
        self.pwd.place(x=30,y=160)
        
        self.password_entry= Entry(self.frame,font=('roboto',22,'bold'), show="*")
        self.password_entry.place(x=200,y=160)
        self.password_entry.insert(0,self.data[3])

        self.numb= Label(self.frame,text="Email", font=('roboto',22,'bold'),bg="#474439", fg='white')
        self.numb.place(x=30,y=100)
        
        self.numb_entry= Entry(self.frame,font=('roboto',22,'bold'))
        self.numb_entry.place(x=200,y=100)
        self.numb_entry.insert(0,self.data[4])
       
        self.btn= Button(self.frame, text="Submit",font=('Arial',20,'normal'), command=self.action)
        self.btn.place(x=250, y=250)
        
        self.screen.mainloop()
        
    def action(self):
        # data= (self.name_entry.get(),self.mail_entry.get(),self.password_entry.get())
        # print(data)
        
        if self.name_entry.get()=="" or self.mail_entry.get()=="" or self.password_entry.get()=="":
            messagebox.showwarning("Warning","Required")

        else:
            data= (self.name_entry.get(),self.mail_entry.get(),self.password_entry.get(), self.id[0])
            response= database.allUser(data)
            if response:
                messagebox.showinfo("Success","User Updated")
                self.screen.destroy()
                
                alluser.Home("User")
                

            else:
                messagebox.showerror("Error","Not Registered")
            
        
if __name__=="__main__":
    obj= Home("User")