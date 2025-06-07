from tkinter import *
from PIL import ImageTk, Image
from datetime import datetime
import time
import requests
import pytz
import uuid
from io import BytesIO
from tkinter import ttk
import database
from tkinter import messagebox
import weather
import page1

class Dashboard2:
    def __init__(self, user):
        self.window = Tk()
        self.window.title("System Management Dashboard")
        self.window.geometry("1366x768")
        self.window.resizable(0, 0)
        self.window.state('zoomed')
        self.window.config(background='#eff5f6')
        self.user= user
        icon = PhotoImage(file='dashboard_img/pic-icon.png')
        self.window.iconphoto(True, icon)

        self.user= user
        print(self.user)
        self.res=database.getUser(self.user)
        print(self.res)

        self.header = Frame(self.window, bg='#009df4')
        self.header.place(x=300, y=0, width=1070, height=60)

        self.logout_text = Button(self.header, text="Logout", bg='#32cf8e', font=("", 13, "bold"), bd=0, fg='white',
                                  cursor='hand2', activebackground='#32cf8e')
        self.logout_text.place(x=950, y=15)

        self.sidebar = Frame(self.window, bg='#ffffff')
        self.sidebar.place(x=0, y=0, width=300, height=750)

        self.heading = Label(self.window, text='Dashboard', font=("", 15, "bold"), fg='#0064d3', bg='#eff5f6')
        self.heading.place(x=325, y=70)

        self.bodyFrame1 = Frame(self.window, bg='#ffffff')
        self.bodyFrame1.place(x=328, y=110, width=1040, height=550)

        # self.bodyFrame2 = Frame(self.window, bg='#009aa5')
        # self.bodyFrame2.place(x=328, y=680, width=310, height=120)

        # self.bodyFrame3 = Frame(self.window, bg='#e21f26')
        # self.bodyFrame3.place(x=680, y=680, width=310, height=120)

        # self.bodyFrame4 = Frame(self.window, bg='#ffcb1f')
        # self.bodyFrame4.place(x=1030, y=680, width=310, height=120)

        self.logoImage = ImageTk.PhotoImage(file='dashboard_img/hyy.png')
        self.logo = Label(self.sidebar, image=self.logoImage, bg='#ffffff')
        self.logo.place(x=70, y=80)

       
        self.logoImage = ImageTk.PhotoImage(file='dashboard_img/hyy.png')
        self.logo = Label(self.sidebar, image=self.logoImage, bg='#ffffff')
        self.logo.place(x=70, y=80)

        self.brandName = Label(self.sidebar, text=self.res[1], bg='#ffffff', font=("", 15, "bold"))
        self.brandName.place(x=80, y=200)

        # self.dashboardImage = ImageTk.PhotoImage(file='dashboard_img/dashboard-icon.png')
        # self.dashboard = Label(self.sidebar, image=self.dashboardImage, bg='#ffffff')
        # self.dashboard.place(x=35, y=289)

        # self.dashboard_text = Button(self.sidebar, text="Dashboard", bg='#80ed9d', font=("", 13, "bold"), bd=0,
        #                              cursor='hand2', activebackground='#ffffff', command=lambda: self.display_news())
        # self.dashboard_text.place(x=80, y=287)

        # self.manageImage = ImageTk.PhotoImage(file='dashboard_img/manage-icon.png')
        # self.manage = Label(self.sidebar, image=self.manageImage, bg='#ffffff')
        # self.manage.place(x=35, y=340)

        # self.manage_text = Button(self.sidebar, text="View Saved News", bg='#80ed9d', font=("", 13, "bold"), bd=0,
        #                           cursor='hand2', activebackground='#ffffff', command=lambda :self.display_saved_news())
        # self.manage_text.place(x=80, y=345)

        self.page1=Button(self.sidebar, text="Home Page", bg='#80ed9d', font=("", 13, "bold"), bd=0,
                                  cursor='hand2', activebackground='#ffffff', command=lambda :self.display_page1())
        self.page1.place(x=80, y=340)


        self.settingsImage = ImageTk.PhotoImage(file='dashboard_img/settings-icon.png')
        self.settings = Label(self.sidebar, image=self.settingsImage, bg='#ffffff')
        self.settings.place(x=35, y=402)

        self.settings_text = Button(self.sidebar, text="Weather Details    ", bg='#80ed9d', font=("", 13, "bold"), bd=0,
                                    cursor='hand2', activebackground='#ffffff', command=self.viewWeather)
        self.settings_text.place(x=80, y=402)

        self.ExitImage = ImageTk.PhotoImage(file='dashboard_img/exit-icon.png')
        self.Exit = Label(self.sidebar, image=self.ExitImage, bg='#ffffff')
        self.Exit.place(x=25, y=452)

        self.Exit_text = Button(self.sidebar, text="Exit", bg='#80ed9d', font=("", 13, "bold"), bd=0,
                                cursor='hand2', activebackground='#ffffff', command=self.exit)
        self.Exit_text.place(x=85, y=462)

        self.clock_image = ImageTk.PhotoImage(file="dashboard_img/time.png")
        self.date_time_image = Label(self.sidebar, image=self.clock_image, bg="white")
        self.date_time_image.place(x=88, y=20)

        self.date_time = Label(self.window)
        self.date_time.place(x=115, y=15)
        self.show_time()
        self.viewWeather()
        # self.setup_news_frame()
        # self.display_news()
        # self.seeCurrentTemp()
        self.window.mainloop()
    
    def display_page1(self):
        self.window.destroy()
        page1.MainApp(self.res[0])
    def exit(self):
        self.window.destroy()
        
    def show_time(self):
        self.time = time.strftime("%H:%M:%S")
        self.date = time.strftime('%Y/%m/%d')
        set_text = f"  {self.time} \n {self.date}"
        self.date_time.configure(text=set_text, font=("", 13, "bold"), bd=0, bg="white", fg="black")
        self.date_time.after(100, self.show_time)

    # def getNews(self, category='all'):
    #     headers = {
    #         'authority': 'inshorts.com',
    #         'accept': '*/*',
    #         'accept-language': 'en-GB,en;q=0.5',
    #         'content-type': 'application/json',
    #         'referer': 'https://inshorts.com/en/read',
    #         'sec-ch-ua': '"Not/A)Brand";v="99", "Brave";v="115", "Chromium";v="115"',
    #         'sec-ch-ua-mobile': '?0',
    #         'sec-ch-ua-platform': '"macOS"',
    #         'sec-fetch-dest': 'empty',
    #         'sec-fetch-mode': 'cors',
    #         'sec-fetch-site': 'same-origin',
    #         'sec-gpc': '1',
    #         'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    #     }

    #     params = (
    #         ('category', 'top_stories'),
    #         ('max_limit', '1000'),
    #         ('include_card_data', 'true')
    #     )

    #     if category == 'all':
    #         response = requests.get(
    #             'https://inshorts.com/api/en/news?category=all_news&max_limit=1000&include_card_data=true')
    #     else:
    #         response = requests.get(
    #             f'https://inshorts.com/api/en/search/trending_topics/{category}', headers=headers, params=params)
        
    #     try:
    #         news_data = response.json()['data']['news_list']
    #     except Exception as e:
    #         print(response.text)
    #         news_data = None

    #     newsDictionary = {
    #         'success': True,
    #         'category': category,
    #         'data': []
    #     }

    #     if not news_data:
    #         newsDictionary['success'] = response.json()['error']
    #         newsDictionary['error'] = 'Invalid Category'
    #         return newsDictionary

    #     for entry in news_data:
    #         try:
    #             news = entry['news_obj']
    #             author = news['author_name']
    #             title = news['title']
    #             imageUrl = news['image_url']
    #             url = news['shortened_url']
    #             content = news['content']
    #             timestamp = news['created_at'] / 1000
    #             dt_utc = datetime.utcfromtimestamp(timestamp)
    #             tz_utc = pytz.timezone('UTC')
    #             dt_utc = tz_utc.localize(dt_utc)
    #             tz_ist = pytz.timezone('Asia/Kolkata')
    #             dt_ist = dt_utc.astimezone(tz_ist)
    #             date = dt_ist.strftime('%A, %d %B, %Y')
    #             time = dt_ist.strftime('%I:%M %p').lower()
    #             readMoreUrl = news['source_url']

    #             newsObject = {
    #                 'id': uuid.uuid4().hex,
    #                 'title': title,
    #                 'imageUrl': imageUrl,
    #                 'url': url,
    #                 'content': content,
    #                 'author': author,
    #                 'date': date,
    #                 'time': time,
    #                 'readMoreUrl': readMoreUrl
    #             }
    #             newsDictionary['data'].append(newsObject)
    #         except Exception as e:
    #             print(f"Error processing news entry: {entry}")
    #             print(e)
    #     return newsDictionary

    def seeCurrentTemp(self):
        API_KEY = '6ee01bd686ddb245a7b5e0f7bd6547b0'  # Replace with your OpenWeatherMap API key
        city = 'Jalandhar'  # Replace with your desired city

        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
        response = requests.get(url)
        data = response.json()
        print("------***************",data)
        current_temperature = data['main']['temp']
        wind= data['wind']['speed']
        
        temperature_label = Label(self.bodyFrame2, text=f'{city} \n  {current_temperature}° C', font=('Arial', 18, 'bold'), bg='#009aa5' ,fg='#ffffff')
        temperature_label.pack(pady=30)
        
        humidity_label = Label(self.bodyFrame3, text=f"Min - {data['main']['temp_min']}°C\nMax - {data['main']['temp_max']}°C", font=('Arial', 18, 'bold'), bg='#e21f26' ,fg='#ffffff')
        humidity_label.pack(pady=30)
        
        temperature_label = Label(self.bodyFrame4, text=f'{city} Wind Speed \n  {wind}', font=('Arial', 15, 'bold'), bg='#ffcb1f' ,fg='#ffffff')
        temperature_label.pack(pady=30)
        
        
    # def setup_news_frame(self):
    #     self.canvas = Canvas(self.bodyFrame1, bg='#ffffff')
    #     self.scrollbar = Scrollbar(self.bodyFrame1, orient=VERTICAL, command=self.canvas.yview)
    #     self.scrollable_frame = Frame(self.canvas, bg='#ffffff')

    #     self.scrollable_frame.bind(
    #         "<Configure>",
    #         lambda e: self.canvas.configure(
    #             scrollregion=self.canvas.bbox("all")
    #         )
    #     )

    #     self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
    #     self.canvas.configure(yscrollcommand=self.scrollbar.set)

    #     self.canvas.pack(side=LEFT, fill=BOTH, expand=True)
    #     self.scrollbar.pack(side=RIGHT, fill=Y)

    # def display_news(self):
    #     news_data = self.getNews('all')['data']
    #     print(news_data)
        
    #     for idx, news in enumerate(news_data[:50]):  # Limit to first 50 news items for display
    #         try:
    #             # Fetch image
    #             image_response = requests.get(news['imageUrl'])
    #             image_data = Image.open(BytesIO(image_response.content))
    #             image_data.thumbnail((150, 150))
    #             img = ImageTk.PhotoImage(image_data)

    #             # Create frame for each news item
    #             frame = Frame(self.scrollable_frame, background='#ffffff')
    #             frame.grid(row=idx, column=0, pady=10, sticky='w')

    #             # Display image
    #             img_label = Label(frame, image=img,  background='#ffffff', width=160, height=160)
    #             img_label.image = img
    #             img_label.grid(row=0, column=0, rowspan=2)

    #             # Display title
    #             title_label = ttk.Label(frame, text=news['title'], background='#ffffff', font=('Arial', 16, 'bold'), wraplength=500, justify="left")
    #             title_label.grid(row=0, column=1, padx=5, pady=2, sticky='w')
    #             # title_label.grid(row=0, column=1, padx=0, pady=20)
    #             # Display content
    #             content_label = ttk.Label(frame, text=f"{news['content'][:70]}......", background='#ffffff', font=('Arial', 12), wraplength=500, justify="left")
    #             content_label.grid(row=1, column=1, padx=5, pady=5, sticky='w')
    #             # content_label.grid(row=1, column=1, padx=0, pady=20)

    #             # Display author and date
    #             info_label = ttk.Label(frame, text=f"By {news['author']} on {news['date']} at {news['time']}", background='#ffffff', font=('Arial', 10, 'italic'))
    #             info_label.grid(row=2, column=1, padx=5, pady=2, sticky='w')
    #             # info_label.grid(row=2, column=1, padx=5, pady=5, sticky='w')

    #             # Add "View" button
    #             view_button = Button(frame, text="View More", command=lambda news=news: self.view_news(news), background='#009df4', fg='white', font=('Arial', 12, 'bold'))
    #             view_button.grid(row=0, column=2, padx=10)
                
    #         except Exception as e:
    #             print(f"Error displaying news: {news}")
    #             print(e)

    # def view_news(self, news):
    #     # Create a new window
    #     new_window = Toplevel(self.window)
    #     new_window.title(news['title'])
    #     new_window.geometry("800x700")
    #     new_window.config(background='#ffffff')

    #     # Fetch and display the image
    #     image_response = requests.get(news['imageUrl'])
    #     image_data = Image.open(BytesIO(image_response.content))
    #     image_data = image_data.resize((300, 300),)
    #     img = ImageTk.PhotoImage(image_data)

    #     img_label = Label(new_window, image=img, background='#ffffff')
    #     img_label.image = img
    #     img_label.pack(pady=10)

    #     # Display title
    #     title_label = Label(new_window, text=news['title'], background='#ffffff', font=('Arial', 18, 'bold'), wraplength=700, justify="left")
    #     title_label.pack(pady=10)

    #     # Display content
    #     content_label = Label(new_window, text=news['content'], background='#ffffff', font=('Arial', 14), wraplength=700, justify="left")
    #     content_label.pack(pady=10)

    #     # Display author and date
    #     info_label = Label(new_window, text=f"By {news['author']} on {news['date']} at {news['time']}", background='#ffffff', font=('Arial', 12, 'italic'))
    #     info_label.pack(pady=10)
        
    #     # save_news= Button()
    #     save_button = Button(new_window, text="Save News", command=lambda news=news: self.saveNews(news), background='#009df4', fg='white', font=('Arial', 12, 'bold'))
    #     save_button.pack(pady=10)

        
        
    # def saveNews(self,news):
    #     user_id= self.user[0]
    #     # user_id= self.userid
    #     news_img= news['imageUrl']
    #     title= news['title']
    #     content= news['content']
    #     author_name= news['author']
    #     news_date= news['date']
        
    #     news_data=(user_id, news_img,title, content, author_name, news_date)
    #     print(news_data)
    #     res= database.newsSave(news_data)
    #     if res:
    #         messagebox.showinfo("Saved","Saved Successfully")
    #     else:
    #         messagebox.showerror("Error","Not Saved")
    
    def display_saved_news(self):
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        saved_news_data = database.getSavedNews((self.user[0],))
        for idx, news in enumerate(saved_news_data):
            try:
                image_response = requests.get(news[2])
                image_data = Image.open(BytesIO(image_response.content))
                image_data.thumbnail((150, 150))
                img = ImageTk.PhotoImage(image_data)

                frame = Frame(self.scrollable_frame, background='#ffffff')
                frame.grid(row=idx, column=0, pady=10, sticky='w')

                img_label = Label(frame, image=img, background='#ffffff', width=160, height=160)
                img_label.image = img
                img_label.grid(row=0, column=0, rowspan=2)

                title_label = ttk.Label(frame, text=news[3], background='#ffffff', font=('Arial', 16, 'bold'), wraplength=500, justify="left")
                title_label.grid(row=0, column=1, padx=5, pady=2, sticky='w')

                content_label = ttk.Label(frame, text=news[4], background='#ffffff', font=('Arial', 12), wraplength=500, justify="left")
                content_label.grid(row=1, column=1, padx=5, pady=5, sticky='w')

                info_label = ttk.Label(frame, text=f"By {news[5]} on {news[6]}", background='#ffffff', font=('Arial', 10, 'italic'))
                info_label.grid(row=2, column=1, padx=5, pady=2, sticky='w')

            except Exception as e:
                print(f"Error displaying saved news: {news}")
                print(e)
                
    def viewWeather(self):
        # self.scrollable_frame.destroy()
        # loginObj =search(self.bodyFrame1)
        # loginObj.search_frame(['jal', '', '', ''])
        search=weather.search(self.bodyFrame1)
        search.search_frame(['jal', '', '', ''])





if __name__ == '__main__':
    Dashboard2("1")
    # search(self.bodyFrame1)


