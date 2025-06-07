import mysql.connector 
# import database

#pip install mysql-connector 

try:
    db= mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    db='news'
    )
    print("Connected")
except Exception as e:
    print("Error----",e)

cursor= db.cursor()


def registerUser(data):
    try:
        print(data)
        cursor.execute('Insert into user (name, mail, password, number) values(%s,%s,%s,%s)',data)
        db.commit()
        return True
    except Exception as e:
        print("Error is ",e)
        return False
    
def loginUser(data):
    try:
        cursor.execute('Select * from user where mail=%s and password=%s ',data)
        return cursor.fetchone()
    except Exception as e:
        print("Error is ",e)
        return False
        
def allUser():
    try:
        cursor.execute('select * from user')
        return cursor.fetchall()
    except Exception as e:
        print("Error is----",e)
        return False
    
def admin(data):
    try:
        cursor.execute('select * from  admin  where admin_email=%s and password=%s',data)
        return cursor.fetchone()
    except Exception as e:
        print("Error is----",e)
        return False   


def newsSave(data):
    try:
        cursor.execute('insert into news (user_id,news_img,title,content,author_name,date) values(%s,%s,%s,%s,%s,%s)', data)
        db.commit()
        return True
    except Exception as e:
        print("Error is",e)
        return False
    
    
def getSavedNews(id):
    try:
        cursor.execute('select * from news where user_id=%s',id)
        return cursor.fetchall()
    except Exception as e:
        print("Error is ",e)
        return False 

def getUser(data):
    try:
        cursor.execute('Select * from user where id=%s ',(data,))
        return cursor.fetchone()
    except Exception as e:
        print("Error is ",e)
        return False
#--make database
     