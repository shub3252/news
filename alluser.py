

from tkinter import *
from tkinter import messagebox
import database
from tkinter import ttk
import update
class Home:
    # def __init__(self):
    def __init__(self,name):
        self.screen= Tk()
        self.screen.title("All user")
        self.width= self.screen.winfo_screenwidth()
        self.height= self.screen.winfo_screenheight()
        self.screen.geometry('800x400')
        
        
        data= database.allUser()
        print(data)
        
        
        self.table= ttk.Treeview(self.screen,columns=['a','b','c','d','e','f','g'], show='headings')
        
        
        self.table.heading('#1',text='Id')
        self.table.heading('#2',text='Name')
        self.table.heading('#3',text='Email')
        self.table.heading('#4',text='Password')
        self.table.heading('#5',text='Number')
        self.table.heading('#6',text='Edit')
        self.table.heading('#7',text='Delete')
        
        self.table.column('#1',width=100)
        self.table.column('#2',width=100)
        self.table.column('#3',width=100)
        self.table.column('#4',width=100)
        self.table.column('#5',width=100)
        self.table.column('#6',width=100)
        self.table.column('#7',width=100)
        
        for i in data:
            print(i)
            self.table.insert('',len(data),text=i[0],values=[i[0],i[1],i[2],i[3],i[4],'Edit','Delete'])
            
        self.table.bind('<Double-Button-1>',self.actions)
        self.table.pack()
        self.screen.mainloop()
        
    def actions(self,n):
        
        tt= self.table.focus()
        col= self.table.identify_column(n.x)
        print("Column is",col)
        
        self.rowid= (self.table.item(tt).get('text'),)
        print(self.rowid)
        if col=="#6":
            messagebox.askyesno("Delete ","Do you want to delete this item ?")
            res= database.deleteuser(self.rowid)
            if res :
                messagebox.showinfo("Delete","Deleted Successfully")
                self.screen.destroy()
                Home("User")
            
        if col=="#5":
            m= messagebox.askyesno("Delete ","Do you want to Edit this item ?")
            if m :
                self.screen.destroy()
                update.Home(self.rowid)
                
                
            
            
        
if __name__=="__main__":
    obj= Home("user")