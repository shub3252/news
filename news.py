# import requests
# import pytz
# import uuid
# import datetime
# import tkinter as tk
# from tkinter import ttk
# from PIL import Image, ImageTk
# from io import BytesIO
# from tkinter import PhotoImage

# def getNews(category='all'):
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
#             dt_utc = datetime.datetime.utcfromtimestamp(timestamp)
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

# def fetch_and_display_news():
#     news_data = getNews('all')['data']
#     print(news_data)
    
#     #deign
#     for idx, news in enumerate(news_data[:20]):  # Display first 20 news items
#         try:
#             # Fetch image
#             image_response = requests.get(news['imageUrl'])
#             image_data = Image.open(BytesIO(image_response.content))
#             image_data.thumbnail((150, 150))
#             img = ImageTk.PhotoImage(image_data)

#             # Create frame for each news item
#             frame = ttk.Frame(inner_frame, padding="5")
#             frame.grid(row=idx, column=0, pady=10, sticky='w')

#             # Display image
#             img_label = ttk.Label(frame, image=img)
#             img_label.image = img
#             img_label.grid(row=0, column=0, rowspan=2)

#             # Display title
#             title_label = ttk.Label(frame, text=news['title'], font=('Arial', 14, 'bold'), wraplength=800, justify="left")
#             title_label.grid(row=0, column=1, padx=10)

#             # Display content
#             content_label = ttk.Label(frame, text=news['content'], font=('Arial', 12), wraplength=800, justify="left")
#             content_label.grid(row=1, column=1, padx=10)

#             # Display author and date
#             info_label = ttk.Label(frame, text=f"By {news['author']} on {news['date']} at {news['time']}", font=('Arial', 10, 'italic'))
#             info_label.grid(row=2, column=1, padx=6, pady=5, sticky='w')
            

#         except Exception as e:
#             print(f"Error displaying news: {news}")
#             print(e)

# # Create the main Tkinter window
# root = tk.Tk()
# root.title("News Channel")
# root.geometry("1100x600")

# # Create a Canvas widget
# canvas = tk.Canvas(root)
# canvas.pack(side=tk.LEFT, fill='both', expand=True)

# # Add a vertical scrollbar to the Canvas
# vsb = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
# vsb.pack(side=tk.RIGHT, fill='y')

# # Add a horizontal scrollbar to the Canvas
# hsb = ttk.Scrollbar(root, orient="horizontal", command=canvas.xview)
# hsb.pack(side=tk.BOTTOM, fill='x')

# # Configure the canvas to work with the scrollbars
# canvas.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

# # Create a frame inside the canvas
# inner_frame = ttk.Frame(canvas)
# canvas.create_window((0, 0), window=inner_frame, anchor='nw')

# # Update the canvas scroll region when the size of the inner frame changes
# def on_frame_configure(event):
#     canvas.configure(scrollregion=canvas.bbox('all'))

# inner_frame.bind("<Configure>", on_frame_configure)

# # Fetch and display news
# fetch_and_display_news()

# # Run the Tkinter event loop
# root.mainloop()




import requests
import pytz
import uuid
import datetime
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from io import BytesIO
import json
import os

def getNews(category='all'):
    # Check if news data is already saved in a JSON file
    filename = f"news_data_{category}.json"
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            newsDictionary = json.load(file)
        return newsDictionary
    
    # If no saved data, make the API call
    headers = {
        'authority': 'inshorts.com',
        'accept': '*/*',
        'accept-language': 'en-GB,en;q=0.5',
        'content-type': 'application/json',
        'referer': 'https://inshorts.com/en/read',
        'sec-ch-ua': '"Not/A)Brand";v="99", "Brave";v="115", "Chromium";v="115"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sec-gpc': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    }

    params = (
        ('category', 'top_stories'),
        ('max_limit', '1000'),
        ('include_card_data', 'true')
    )

    if category == 'all':
        response = requests.get(
            'https://inshorts.com/api/en/news?category=all_news&max_limit=1000&include_card_data=true')
    else:
        response = requests.get(
            f'https://inshorts.com/api/en/search/trending_topics/{category}', headers=headers, params=params)
    
    try:
        news_data = response.json()['data']['news_list']
    except Exception as e:
        print(response.text)
        news_data = None

    newsDictionary = {
        'success': True,
        'category': category,
        'data': []
    }

    if not news_data:
        newsDictionary['success'] = response.json()['error']
        newsDictionary['error'] = 'Invalid Category'
        return newsDictionary

    for entry in news_data:
        try:
            news = entry['news_obj']
            author = news['author_name']
            title = news['title']
            imageUrl = news['image_url']
            url = news['shortened_url']
            content = news['content']
            timestamp = news['created_at'] / 1000
            dt_utc = datetime.datetime.utcfromtimestamp(timestamp)
            tz_utc = pytz.timezone('UTC')
            dt_utc = tz_utc.localize(dt_utc)
            tz_ist = pytz.timezone('Asia/Kolkata')
            dt_ist = dt_utc.astimezone(tz_ist)
            date = dt_ist.strftime('%A, %d %B, %Y')
            time = dt_ist.strftime('%I:%M %p').lower()
            readMoreUrl = news['source_url']

            newsObject = {
                'id': uuid.uuid4().hex,
                'title': title,
                'imageUrl': imageUrl,
                'url': url,
                'content': content,
                'author': author,
                'date': date,
                'time': time,
                'readMoreUrl': readMoreUrl
            }
            newsDictionary['data'].append(newsObject)
        except Exception as e:
            print(f"Error processing news entry: {entry}")
            print(e)
    
    # Save the fetched news data to a JSON file
    with open(filename, 'w') as file:
        json.dump(newsDictionary, file)
    
    return newsDictionary

def fetch_and_display_news():
    news_data = getNews('all')['data']
    print(news_data)
    
    # Design for displaying news items
    for idx, news in enumerate(news_data[:20]):  # Display first 20 news items
        try:
            # Fetch image
            image_response = requests.get(news['imageUrl'])
            image_data = Image.open(BytesIO(image_response.content))
            image_data.thumbnail((150, 150))
            img = ImageTk.PhotoImage(image_data)

            # Create frame for each news item
            frame = ttk.Frame(inner_frame, padding="5")
            frame.grid(row=idx, column=0, pady=10, sticky='w')

            # Display image
            img_label = ttk.Label(frame, image=img)
            img_label.image = img
            img_label.grid(row=0, column=0, rowspan=2)

            # Display title
            title_label = ttk.Label(frame, text=news['title'], font=('Arial', 14, 'bold'), wraplength=800, justify="left")
            title_label.grid(row=0, column=1, padx=10)

            # Display content
            content_label = ttk.Label(frame, text=news['content'], font=('Arial', 12), wraplength=800, justify="left")
            content_label.grid(row=1, column=1, padx=10)

            # Display author and date
            info_label = ttk.Label(frame, text=f"By {news['author']} on {news['date']} at {news['time']}", font=('Arial', 10, 'italic'))
            info_label.grid(row=2, column=1, padx=6, pady=5, sticky='w')
            

        except Exception as e:
            print(f"Error displaying news: {news}")
            print(e)

# Create the main Tkinter window
root = tk.Tk()
root.title("News Channel")
root.geometry("1100x600")

# Create a Canvas widget
canvas = tk.Canvas(root)
canvas.pack(side=tk.LEFT, fill='both', expand=True)

# Add a vertical scrollbar to the Canvas
vsb = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
vsb.pack(side=tk.RIGHT, fill='y')

# Add a horizontal scrollbar to the Canvas
hsb = ttk.Scrollbar(root, orient="horizontal", command=canvas.xview)
hsb.pack(side=tk.BOTTOM, fill='x')

# Configure the canvas to work with the scrollbars
canvas.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

# Create a frame inside the canvas
inner_frame = ttk.Frame(canvas)
canvas.create_window((0, 0), window=inner_frame, anchor='nw')

# Update the canvas scroll region when the size of the inner frame changes
def on_frame_configure(event):
    canvas.configure(scrollregion=canvas.bbox('all'))

inner_frame.bind("<Configure>", on_frame_configure)

# Fetch and display news
fetch_and_display_news()

# Run the Tkinter event loop
root.mainloop()
