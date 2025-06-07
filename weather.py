from tkinter import*
from PIL import ImageTk, Image
from tkinter import messagebox
import PIL
import requests
from time import strftime
from datetime import datetime
from win10toast import ToastNotifier
from time import sleep
# import addCity
import time

dates = datetime.now()
# import home


class search:
    
  
    API_KEY = "6ee01bd686ddb245a7b5e0f7bd6547b0"

    def __init__(self, window):    
        self.root = window
        
        
        # self.root.title('Weather Application')
        # self.root.geometry("1070x650")
        # self.root.configure(bg="#99ccff")
# 
        #to make window in center
        # self.fullwidth=self.root.winfo_screenwidth()
        # self.fullheight=self.root.winfo_screenheight()
        # self.width=int((self.fullwidth-1370)/2)
        # self.height=int((self.fullheight-750)/2)
        # s="1370x750+" +str(self.width)+ "+" +str(self.height)
        # self.root.resizable(height=False,width=False)
        
    def search_frame(self, res):
        self.loginResponse = res
        self.login = Frame(self.root)
        # self.login.pack()
        self.data = res
        print(self.data)

        self.frame1=Frame(self.root,bg='#99ccff',width=1370,height=750) #ccccff
        self.frame1.place(x=0,y=0)
        
        #title

        # self.title=Label(self.root,text='City Weather',font=('arial',42,'underline','bold'),bg="#91CEFF")
        # self.title.place(x=435,y=40)
        self.heading=Label(self.frame1,text='Weather Forecast',fg='grey',bg='#99ccff',font=('Lato',23,'bold'))
        self.heading.place(x=60,y=15)

        # HEADING ---- time
        self.timeHeading=Label(self.frame1,fg='grey',bg='#99ccff',font=('Lato',23,'bold'))
        self.timeHeading.place(x=690,y=15)
        

        self.time()
        # HEADING ---- SIGN IN 
        self.heading=Label(self.frame1,text=dates.strftime("%b %d %Y %a"),fg='grey',bg='#99ccff',font=('Lato',10,'bold'))
        self.heading.place(x=690,y=50)

          #buttons

        # self.button=Button(self.root,text='search',width=8,height=2,bg='black',fg="white", command = self.searchWeather)
        # self.button.place(x=730,y=152)
        self.img6 = Image.open('img/logo.png').resize((50,50))
        self.imgtk6 = ImageTk.PhotoImage(self.img6)
        self.imgLbl6 = Label(self.frame1,image=self.imgtk6,bg='#99ccff')
        self.imgLbl6.place(x=8,y=10)
           
        self.img1 = Image.open('images/icon.png').resize((100,100))
        self.imgtk1 = ImageTk.PhotoImage(self.img1)
        self.imgLbl1 = Label(self.frame1,image=self.imgtk1,width=150,height=150,bg='#99ccff')
        self.imgLbl1.place(x=400,y=-30)
        
        # IMAGE SEARCH BOX
        self.img2 = Image.open('img/search2.png').resize((250,30))
        self.imgtk2 = ImageTk.PhotoImage(self.img2)
        self.imgLbl2 = Label(self.frame1,image=self.imgtk2,bg='#99ccff')
        self.imgLbl2.place(x=350,y=80)
        
        # ICON IN SEARCH BOX
        self.img3 = Image.open('images/icon.png').resize((20,20))
        self.imgtk3 = ImageTk.PhotoImage(self.img3)
        self.imgLbl3 = Label(self.frame1,image=self.imgtk3,width=20,height=20,bg='#203243')
        self.imgLbl3.place(x=360,y=85)
        # text typing
        self.textfield = Entry(self.frame1,justify='center',width=15,bg='#203243',border=0,fg='white',font=('Microsoft YaHei UI Light',15,'bold'))
        self.textfield.place(x=390,y=83)

        self.textfield.insert(0, res[-4])
        
        #img_btn
        self.img10 = Image.open('img/Layer 6.png').resize((20,20))
        self.click_btn9 =ImageTk.PhotoImage(self.img10)
        self.img_label = Label(image=self.click_btn9)
        self.button = Button(self.frame1,image=self.click_btn9,width=30,bg='#203243',pady=2,borderwidth=0,command=self.searchWeather)
        self.button.place(x=565,y=85)

        # self.addBtn = Button(self.frame1, text = 'Add City', bg = 'black', fg = 'white', command = self.addCities)
        # self.addBtn.place(x = 890, y = 150)
       
        #entryes
        # self.entry=Entry(self.root,width=14,font=('arial',20),bd=2)
        
        # self.entry.place(x=440,y=150,width=265,height=44)
         
      
      #center
      
        # to get the width and height of your computer screen
        # self.fullwidth = self.root.winfo_screenwidth()
        # self.fullheight = self.root.winfo_screenheight()
        # self.width = int((self.fullwidth-1280)/2)
        # self.height=int((self.fullheight-750)/2)

        # s = "1280x750+" +str(self.width)+ "+" +str(self.height)
    

        # so screen cant be resized
        # self.root.resizable(height=False,width=False)
        self.noti = ToastNotifier() 
        
        
        #logo

        self.root.mainloop()

    # def addCities(self):
    #    self.root.destroy()
    #    obj = addCity.addcityadd()
    #    obj.city(self.data)
    
    def time(self):
        string = strftime('%H:%M:%S %p')
        self.timeHeading.config(text=string)
        self.timeHeading.after(1000, self.time)

    def back(self):        
        self.root.destroy()
        # Obj1 =home.AdminNav()
        # Obj1.navframe(self.loginResponse)
      


    def searchWeather(self):
      if self.textfield.get() == '':
        messagebox.showinfo('Alert', 'Please enter city name first.')
      
      else:

        #for widget in self.mainframe.winfo_children():
         # widget.destroy()

        self.cityName = self.textfield.get()
        #self.entry.delete(0, 'end')
        self.api_address = "https://api.openweathermap.org/data/2.5/forecast?q=" + self.cityName + "&appid=" + self.API_KEY

        print(self.api_address)

        try:
          res = requests.get(self.api_address)
          a = res.json()

          dates = []
          for i in a['list']:
              dates.append(i['dt_txt'][:10])

          dates = list(set(dates))
          dates.sort()
          print(dates)

          finalData = dict()
          firstDate = []
          secondDate = []
          thirdDate = []
          fourthDate = []
          fifthDate = []
          
          for i in dates:
            for j in a['list']:
              if j['dt_txt'][:10] == i:
                if dates.index(i) == 0:
                  firstDate.append(j)
                elif dates.index(i) == 1:
                  secondDate.append(j)
                elif dates.index(i) == 2:
                  thirdDate.append(j)
                elif dates.index(i) == 3:
                  fourthDate.append(j)
                elif dates.index(i) == 4:
                  fifthDate.append(j)

        
          

          self.a=Label(self.root,text='Daily',bg="#91CEFF",font=('arial',28,'underline','bold'))
          self.a.place(x=20,y=900)

          self.b=Label(self.root,text=datetime.strptime(dates[0], '%Y-%m-%d').strftime('%a'),bg="#91CEFF",font=('arial',12,'bold'))
          self.b.place(x=100,y=140)
          self.C=Label(self.root,text=self.farenToCel(firstDate[0]['main']['temp']) ,bg="#91CEFF",font=('arial',20,'bold'))
          self.C.place(x=100,y=180)
          self.D=Label(self.root,text=firstDate[0]['weather'][0]['main'],bg="#91CEFF",font=('arial',12,'bold'))
          self.D.place(x=100,y=220)

          self.b=Label(self.root,text=datetime.strptime(dates[1], '%Y-%m-%d').strftime('%a'),bg="#91CEFF",font=('arial',12,'bold'))
          self.b.place(x=300,y=140)
          self.C=Label(self.root,text=self.farenToCel(secondDate[0]['main']['temp']) ,bg="#91CEFF",font=('arial',20,'bold'))
          self.C.place(x=300,y=180)
          self.D=Label(self.root,text=secondDate[0]['weather'][0]['main'],bg="#91CEFF",font=('arial',12,'bold'))
          self.D.place(x=300,y=220)


          self.b=Label(self.root,text=datetime.strptime(dates[2], '%Y-%m-%d').strftime('%a'),bg="#91CEFF",font=('arial',12,'bold'))
          self.b.place(x=500,y=140)
          self.C=Label(self.root,text=self.farenToCel(thirdDate[0]['main']['temp']),bg="#91CEFF",font=('arial',20,'bold'))
          self.C.place(x=500,y=180)
          self.D=Label(self.root,text=thirdDate[0]['weather'][0]['main'],bg="#91CEFF",font=('arial',12,'bold'))
          self.D.place(x=500,y=220)

          self.b=Label(self.root,text=datetime.strptime(dates[3], '%Y-%m-%d').strftime('%a'),bg="#91CEFF",font=('arial',12,'bold'))
          self.b.place(x=700,y=140)
          self.C=Label(self.root,text=self.farenToCel(fourthDate[0]['main']['temp']),bg="#91CEFF",font=('arial',20,'bold'))
          self.C.place(x=700,y=180)
          self.D=Label(self.root,text=fourthDate[0]['weather'][0]['main'],bg="#91CEFF",font=('arial',12,'bold'))
          self.D.place(x=700,y=220) 

          self.b=Label(self.root,text=datetime.strptime(dates[4], '%Y-%m-%d').strftime('%a'),bg="#91CEFF",font=('arial',12,'bold'))
          self.b.place(x=900,y=140)
          self.C=Label(self.root,text=self.farenToCel(fifthDate[0]['main']['temp']),bg="#91CEFF",font=('arial',20,'bold'))
          self.C.place(x=900,y=180)
          self.D=Label(self.root,text=fifthDate[0]['weather'][0]['main'],bg="#91CEFF",font=('arial',12,'bold'))
          self.D.place(x=900,y=220)

          #buttons
          self.click=Button(self.root,bg='black',text='view',fg="white",font=('arial',10,'bold') ,command = lambda: self.getHourly(firstDate))
          self.click.place(x=100,y=260,width=50,height=30)
          self.click=Button(self.root,text='view',bg="black",fg="white",font=('arial',10,'bold'), command = lambda: self.getHourly(secondDate))
          self.click.place(x=300,y=260,width=50,height=30)
          self.click=Button(self.root,text='view',bg="black",fg="white",font=('arial',10,'bold'), command = lambda: self.getHourly(thirdDate))
          self.click.place(x=500,y=260,width=50,height=30)
          self.click=Button(self.root,text='view',bg="black",fg="white",font=('arial',10,'bold'), command = lambda: self.getHourly(fourthDate))
          self.click.place(x=700,y=260,width=50,height=30)
          self.click=Button(self.root,text='view',bg="black",fg="white",font=('arial',10,'bold'), command = lambda: self.getHourly(fifthDate))
          self.click.place(x=900,y=260,width=50,height=30)

          
          if firstDate[0]['weather'][0]['main'] == 'Clear':
            self.noti.show_toast('Clear','Today is clear. So don\'t forget to go outside and play.',duration=20, threaded=True)
          elif firstDate[0]['weather'][0]['main'] == 'Thunderstorm':
            self.noti.show_toast('Thunderstorm','There is thunderstorm today. \n When thunder roars, go indoors',duration=20, threaded=True)
          elif firstDate[0]['weather'][0]['main'] == 'Drizzle':
            self.noti.show_toast('Drizzle','You should drive considerably slower than you normally would.',duration=20, threaded=True)
          elif firstDate[0]['weather'][0]['main'] == 'Rain':
            self.noti.show_toast('Rain','Try to wear good quality footwear and avoid street food.',duration=20, threaded=True)
          elif firstDate[0]['weather'][0]['main'] == 'Snow':
            self.noti.show_toast('Snow','Wear layers of light & warm clothing, a wind-resistant coat, a hat, gloves.',duration=20, threaded=True)
          elif firstDate[0]['weather'][0]['main'] == 'Clouds':
            print('clouds is the weather')
            self.noti.show_toast('Clouds','There might be rain so try to carry umbrella outdoors.',duration=20, threaded=True)
            # sleep(40)
          elif firstDate[0]['weather'][0]['main'] == 'Atmosphere':
            self.noti.show_toast('Atmosphere','Avoid outdoor activities especially outdoor sports.',duration=20, threaded=True)

        
          

          # self.getHourl(firstDate)
          
        except:
          messagebox.showinfo('Alert', 'Something went wrong.')

    def getHourly(self, dateIndex):
          # self.image3 = Image.open("image/x.png")
          # self.bgImage3 = ImageTk.PhotoImage(self.image3)
          # self.bgLabel3 = Label(self.root, image=self.bgImage3)
          # self.bgLabel3.place(x = -9, y = 500, width = "2200", height = "50")
        
        
        
          self.a=Label(self.root,text='Hourly',bg="#91CEFF",font=('arial',22,'underline','bold'))
          self.a.place(x=20,y=320)

          self.b = Label(self.root, text = datetime.strptime(dateIndex[0]['dt_txt'][:10], '%Y-%m-%d').strftime('%a'), bg="#91CEFF",font=('arial',10,'underline','bold'))
          self.b.place(x = 20, y = 370)

          self.b=Label(self.root,text=self.getAmPm(dateIndex[0]['dt_txt'][11:]),bg="#91CEFF",font=('arial',12,'bold'))
          self.b.place(x=260,y=380)
          self.C=Label(self.root,text=self.farenToCel(dateIndex[0]['main']['temp']),bg="#91CEFF",font=('arial',19,'bold'))
          self.C.place(x=260,y=420)
          self.D=Label(self.root,text=dateIndex[0]['weather'][0]['main'],bg="#91CEFF",font=('arial',12,'bold'))
          self.D.place(x=260,y=470)

          self.b=Label(self.root,text=self.getAmPm(dateIndex[1]['dt_txt'][11:]),bg="#91CEFF",font=('arial',12,'bold'))
          self.b.place(x=460,y=380)
          self.C=Label(self.root,text=self.farenToCel(dateIndex[1]['main'
          ]['temp']),bg="#91CEFF",font=('arial',19,'bold'))
          self.C.place(x=460,y=420)
          self.D=Label(self.root,text=dateIndex[1]['weather'][0]['main'],bg="#91CEFF",font=('arial',12,'bold'))
          self.D.place(x=480,y=470)

          
          self.b=Label(self.root,text=self.getAmPm(dateIndex[2]['dt_txt'][11:]),bg="#91CEFF",font=('arial',12,'bold'))
          self.b.place(x=660,y=380)
          self.C=Label(self.root,text=self.farenToCel(dateIndex[2]['main']['temp']),bg="#91CEFF",font=('arial',19,'bold'))
          self.C.place(x=660,y=420)
          self.D=Label(self.root,text=dateIndex[2]['weather'][0]['main'],bg="#91CEFF",font=('arial',12,'bold'))
          self.D.place(x=660,y=470)

          
          self.b=Label(self.root,text=self.getAmPm(dateIndex[3]['dt_txt'][11:]),bg="#91CEFF",font=('arial',12,'bold'))
          self.b.place(x=860,y=380)
          self.C=Label(self.root,text=self.farenToCel(dateIndex[3]['main']['temp']),bg="#91CEFF",font=('arial',19,'bold'))
          self.C.place(x=860,y=420)
          self.D=Label(self.root,text=dateIndex[3]['weather'][0]['main'],bg="#91CEFF",font=('arial',12,'bold'))
          self.D.place(x=860,y=470)

          
          self.b=Label(self.root,text=self.getAmPm(dateIndex[4]['dt_txt'][11:]),bg="#91CEFF",font=('arial',12,'bold'))
          self.b.place(x=1040,y=380)
          self.C=Label(self.root,text=self.farenToCel(dateIndex[4]['main']['temp']),bg="#91CEFF",font=('arial',19,'bold'))
          self.C.place(x=1040,y=420)
          self.D=Label(self.root,text=dateIndex[4]['weather'][0]['main'],bg="#91CEFF",font=('arial',12,'bold'))
          self.D.place(x=1040,y=470)

          
    def farenToCel(self, temp):
      a = int(temp) - 273
      return f'{a}°C'
    
    def getAmPm(self, times):
       t_obj = datetime.strptime( times, '%H:%M:%S')
       return t_obj.strftime('%I:%M %p')



if __name__ == "__main__":
    loginObj = search()
    loginObj.search_frame(['jal', '', '', ''])
