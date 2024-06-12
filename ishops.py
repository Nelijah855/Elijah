
"""
libraries reqiured 

mysql.connector,plyer, ffpyplayer,

"""



import kivy
import mysql.connector 
kivy.require('2.0.0')
import time

import socket
from kivy.properties import ListProperty, StringProperty
import random
from kivy.uix.textinput import TextInput
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.videoplayer import VideoPlayer
from plyer import notification
import os
from kivy.graphics import Rectangle,Color
import sys
import sqlite3
from kivy.uix.widget import Widget


import os


"""
#from mtnmomo.collection import Collection


class Mtn():


   
    client = Collection({
        "COLLECTION_USER_ID": os.environ.get("053c6dea-dd68-xxxx-xxxx-c830dac9f401'}"),
        "COLLECTION_API_SECRET": os.environ.get('b0431db58a9b41faa8f5860230xxxxxx'),
        "COLLECTION_PRIMARY_KEY": os.environ.get("COLLECTION_PRIMARY_KEY"),
    })

    
    

    
    def mtnpay(self):
        self.client.requestToPay(
    mobile="0778056923", amount="600", external_id="123456789", payee_note="dd", payer_message="dd", currency="EUR")

"""


#class to handle the database
        
        
class Mysql():


    sql="SELECT * FROM "
    def __init__(self,host,user,password,database):
        self.host=host
        self.user=user
        self.database=database
        self.password=password

        #mysql obj_
        self.conn=mysql.connector.connect(host=host,user=user,password=password,database=database)
        self.cursor=self.conn.cursor()
        

    def insert(self):
        self.conn.execute(self.sql)
    def update(self):
        self.conn.execute(self.sql)
    def remove(self):
        self.conn.execute(self.sql)
    def get_data(self):
        self.conn.execute(self.sql)
    def create(self):
        self.conn.execute(self.sql)





#class for sqlite db_


class Sqlite():
    def __init__(self,sql):
        
        self.conn = sqlite3.connect('userrs_device.db')
        self.conn.execute('''DROP TABLE IF EXISTS ig_users; ''')
        self.sql='''CREATE TABLE foci
         (ID INT PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         AGE            INT     NOT NULL,
         ADDRESS        CHAR(50),
         SALARY         REAL);'''
    def insert(self):
        self.conn.execute(self.sql)
    def update(self):
        self.conn.execute(self.sql)
    def remove(self):
        self.conn.execute(self.sql)
    def get_data(self):
        self.conn.execute(self.sql)
    def create(self):
        self.conn.execute(self.sql)


sql=Sqlite("")

#class to exit the application on exiting 
class Exit():
    def exit(self):
        sys.exit(0)
        return 0

# class  for handling the drawing of the rectangle 
class Recta_(FloatLayout):
    def canvas_inc_x(self):
        but=Button(text="up",on_press='')
        self.add_widget(but)
        return 


    def canvas_inc_y(self,y):
        but=Button(text="up",on_press='')
        self.add_widget(but)
        
        pass


    def draw_rectangle(self):
        with self.canvas:
            Color(.23,1,.34)
            Rectangle(source='',pos=self.pos,size=self.size)



"""
class responsible for the client side connection

"""
class Client():
    
    def connector(self,host):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            

            sock.connect((host,3000))
            data=sock.recv(1000)
            message="paria company"
            sock.sendall(str.encode(message))
        
            

        except:
            sys.exit(0)

            
    

"""
class responsible for the server  side connection

"""
class Server():
    s_host=""
    port=""
    
    def listener(self,host):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((host, 3000))
        sock.listen(5)
        
        while True:
            new_soc,addr=sock.accept()
            new_soc.sendall('thanks for connecting to the ic company....'.encode('utf-8'))
            data=new_soc.recv(1024)



# kv gui template 

kb=Builder.load_file('ishop.kv')


"""


 class for handling shopping and ads 


"""

class Ads(FloatLayout):

    display=''
    items=[]
    def play(self):

         for i in self.items:
            VideoPlayer(source=i,play="True",size_hint=(.5,.4),allow_stretch=True)





    def next(self):
        self.items=[]
        for s_q in range(100000):
            if self.items[s_q]=="search_q":
                display=self.item[s_q]
                return True
            else:
                return False

    
    def prev(self):
        
        for s_q in range(100000):
            if self.item[s_q]=="search_q":
                display=self.item[s_q]
                return True
            else:
                return False


            
    def all(self):
        for i in range(1000):
            self.item[i]
            time.sleep(20000)

"""
class for handling mtn and airtel sending in and removal of money
"""
class A_M_api():
    def airtel(self):
        pass
    def mtn(self):
        pass
    def paypal(self):
        pass
    def ipay(self):
        pass
    def gpay(self):
        pass

"""

class to generator code for working with the ics company



class to handle how shops are displayed in the interface 

"""
class Ishop(Screen):


    # variable to hold the info the display variables '
    var='I G'

    phone='+2567...'

    email='elaijahn8@gmail.com'
    txt=''

    address=''

    price=''

    image=''

    display=''

    loop=0

    
    def loop(self):
        for i in range(100000):
            loop=i

    
    def is_broker(self):
        #varaible to hold goods sold aday
        d_sales=0
        if (d_sales/30)>=50000:
            return True
        else:
            return False

    def is_commision(self):

        #varaible to hold goods sold aday
        d_sales=0
        if (d_sales/30)>=10:
            return True
        else:
            return False
        
    def retail(self):
        #price of the item
        price=0
        #max_profit
        max_p=3000
        #min_profit
        min_p=500
        #selling price of the item

        s_p=price
    def wholesale(self):

        #price of the item
        price=0
        #max_profit
        max_p=300000
        #min_profit
        min_p=50000
        #selling price of the item
        tax=.1*min_p
        return True

        
    def search(self):
        items=['elijah']
        search_q="shops"
        for s_q in range(100000):
            if items[0]==search_q:
                display=self.item[s_q]
                return True
            else:
                return False
    def next(self):
        items=[]
        for i in len(items):
            if i==0:
                i=0+1
                break
            elif i==len(items):
                display="indexfail check prev button  plz!!!!"
                break
            elif i==None:
                display="no item!!!!"
            else:
                i=i+1
                break
                
        
    def sell(self):
        # varaible to hld the passcode for the user 
        code=TextInput(text="code ...",size_hint=(.2,.1),pos_hint={'x':.1,'y':.2})
        #variable to hold the ammount of money to be sold
        a_m=TextInput(text="code ...",size_hint=(.2,.1),pos_hint={'x':.3,'y':.2})
        #variable to hold the currency
        ugx=TextInput(text="money ...",size_hint=(.2,.1),pos_hint={'x':.5,'y':.2})
        #variable to hold the sellers name 
        user_id=TextInput( text="user_id", size_hint=(.2,.1),pos_hint={'x':.7,'y':.2})
        
        self.add_widget(code)
        self.add_widget(a_m)
        self.add_widget(ugx)
        self.add_widget(user_id)
        
    def pay(self):
        pass
    
    def mtn(self):
            #a=Mtn()
            #a.mtnpay()
            #Mtn.mtntrans()
            pass
    
    def airtel(self):
        pass
    def buy(self,*args):
        # varaible to hld the passcode for the user 
        code=TextInput(text="shopcode ...",size_hint=(.2,.1),pos_hint={'x':.1,'y':.2})
        #variable to hold the ammount of money to be bought on 
        a_m=TextInput(text="name...",size_hint=(.2,.1),pos_hint={'x':.3,'y':.2})
        #variable to hold the currency
        ugx=TextInput(text="money ...",size_hint=(.2,.1),pos_hint={'x':.5,'y':.2})
        #variable to hold the buyers name 
        user_id=TextInput( text="user_id", size_hint=(.2,.1),pos_hint={'x':.7,'y':.2})
        
        self.add_widget(code)
        self.add_widget(a_m)
        self.add_widget(ugx)
        self.add_widget(user_id)


    def prev(self):

        items=[]
        for i in range(len(items)):
            if i==len(items):
                i=i-1
                break
            elif i==0:
                display="fail index!!!!, check next button"
            elif i==None:
                display="no item!!!!"
            else:
                i=i-1
        pass
    def deliver(self):
        label=Label(text='i watch',size_hint=(.2,.2),pos_hint={'x':.1,'top':.2})
        self.add_widget(label)
        for pieces in range(10):    
            if pieces>=5:
                charge=200000
                break
            else:
                charge=200000
                break
        
        # the fucntion shud pause for 30 seconds waiting for the label to be gracefully executed 


    # function to add things in the db
    def upate(self):
        self.items.append(self.image)
        return "db updated..."
    

    def cart(self):
        label=Label(text='i watch',size_hint=(.2,.2),pos_hint={'x':.1,'top':.2})
        self.add_widget(label)
        return "cart..."
    
    

    def chat(self):
        
        Client.connect()
        var='sending ...sms..'

        return 
    def rec_(self):
        for i in range(10):
            x=2*10
            y=2*10
            x=x+10
            y=y+10
            with self.canvas:
                Color(.1,1,.2,1)
                Rectangle(source='',pos=(x,y),size=(100,100))
    def view_shops(self):
        but=Button(text="view shops", on_press=self.rec_, pos=(100,100),size=(100,100))
        self.add_widget(but)

class Mode():
    image=''
    display=''
    width=0
    height=0
    def screen_c(self):
        r=range(128)
        g=range(128)
        b=range(128)

    def screen_o(self):
        potr=1
        land=0
    def screen_w_h(self):
        self.width
        self.height



class Ads(Screen):
    display=StringProperty('')
    def exit(self):
        Exit().exit()
        
    def sell(self):
        # varaible to hld the passcode for the user 
        code=TextInput(text="code ...",size_hint=(.2,.1),pos_hint={'x':.1,'y':.2})
        #variable to hold the ammount of money to be sold
        a_m=TextInput(text="code ...",size_hint=(.2,.1),pos_hint={'x':.3,'y':.2})
        #variable to hold the currency
        ugx=TextInput(text="money ...",size_hint=(.2,.1),pos_hint={'x':.5,'y':.2})
        #variable to hold the sellers name 
        user_id=TextInput( text="user_id", size_hint=(.2,.1),pos_hint={'x':.7,'y':.2})
        
        self.add_widget(code)
        self.add_widget(a_m)
        self.add_widget(ugx)
        self.add_widget(user_id)
        
    def pay(self):
        pass
    def mtn(self):
        pass
    def airtel(self):
        pass
    
    def next(self,*args):
        # varaible to hld the passcode for the user 
        code=TextInput(text="shopcode ...",size_hint=(.2,.1),pos_hint={'x':.1,'y':.2})
        #variable to hold the ammount of money to be bought on 
        a_m=TextInput(text="name...",size_hint=(.2,.1),pos_hint={'x':.3,'y':.2})
        #variable to hold the currency
        ugx=TextInput(text="money ...",size_hint=(.2,.1),pos_hint={'x':.5,'y':.2})
        #variable to hold the buyers name 
        user_id=TextInput( text="user_id", size_hint=(.2,.1),pos_hint={'x':.7,'y':.2})
        
        self.add_widget(code)
        self.add_widget(a_m)
        self.add_widget(ugx)
        self.add_widget(user_id)


    def load(self):

        items=[]
        self.display="loading audio......."
        label=Label(text=self.display,size_hint=(.2,.2),pos_hint={'x':.3,'top':.2})
        self.add_widget(label)
        for i in range(len(items)):
            if i==len(items):
                i=i-1
                break
            elif i==0:
                display="fail index!!!!, check next button"
            elif i==None:
                display="no item!!!!"
            else:
                i=i-1
        pass
    def prev(self):
        self.display="loading video......."
        label=Label(text=self.display,size_hint=(.2,.2),pos_hint={'x':.1,'top':.2})
        self.add_widget(label)
        for pieces in range(10):    
            if pieces>=5:
                charge=200000
                break
            else:
                charge=200000
                break



"""
class for peoples investments


"""





class Invest(Screen):


    # variable to hold the info the display variables '
    var='I G'

    phone='+2567...'

    email='elaijahn8@gmail.com'
    txt=''

    address=''

    price=''

    image=''

    display=''

    loop=0

    
    def loop(self):
        for i in range(100000):
            loop=i

    
    def is_broker(self):
        #varaible to hold goods sold aday
        d_sales=0
        if (d_sales/30)>=50000:
            return True
        else:
            return False

    def is_commision(self):

        #varaible to hold goods sold aday
        d_sales=0
        if (d_sales/30)>=10:
            return True
        else:
            return False
        
    def retail(self):
        #price of the item
        price=0
        #max_profit
        max_p=3000
        #min_profit
        min_p=500
        #selling price of the item

        s_p=price
    def wholesale(self):

        #price of the item
        price=0
        #max_profit
        max_p=300000
        #min_profit
        min_p=50000
        #selling price of the item
        tax=.1*min_p
        return True

        
    def search(self):
        items=['elijah']
        search_q="shops"
        for s_q in range(100000):
            if items[0]==search_q:
                display=self.item[s_q]
                return True
            else:
                return False
    def next(self):
        items=[]
        for i in len(items):
            if i==0:
                i=0+1
                break
            elif i==len(items):
                display="indexfail check prev button  plz!!!!"
                break
            elif i==None:
                display="no item!!!!"
            else:
                i=i+1
                break
                
        
    def sell(self):
        # varaible to hld the passcode for the user 
        code=TextInput(text="code ...",size_hint=(.2,.1),pos_hint={'x':.1,'y':.2})
        #variable to hold the ammount of money to be sold
        a_m=TextInput(text="code ...",size_hint=(.2,.1),pos_hint={'x':.3,'y':.2})
        #variable to hold the currency
        ugx=TextInput(text="money ...",size_hint=(.2,.1),pos_hint={'x':.5,'y':.2})
        #variable to hold the sellers name 
        user_id=TextInput( text="user_id", size_hint=(.2,.1),pos_hint={'x':.7,'y':.2})
        
        self.add_widget(code)
        self.add_widget(a_m)
        self.add_widget(ugx)
        self.add_widget(user_id)
        
    def pay(self):
        pass
    
    def mtn(self):
            #a=Mtn()
            #a.mtnpay()
            #Mtn.mtntrans()
            pass 
    
    def airtel(self):
        pass
    def buy(self,*args):
        # varaible to hld the passcode for the user 
        code=TextInput(text="shopcode ...",size_hint=(.2,.1),pos_hint={'x':.1,'y':.2})
        #variable to hold the ammount of money to be bought on 
        a_m=TextInput(text="name...",size_hint=(.2,.1),pos_hint={'x':.3,'y':.2})
        #variable to hold the currency
        ugx=TextInput(text="money ...",size_hint=(.2,.1),pos_hint={'x':.5,'y':.2})
        #variable to hold the buyers name 
        user_id=TextInput( text="user_id", size_hint=(.2,.1),pos_hint={'x':.7,'y':.2})
        
        self.add_widget(code)
        self.add_widget(a_m)
        self.add_widget(ugx)
        self.add_widget(user_id)


    def prev(self):

        items=[]
        for i in range(len(items)):
            if i==len(items):
                i=i-1
                break
            elif i==0:
                display="fail index!!!!, check next button"
            elif i==None:
                display="no item!!!!"
            else:
                i=i-1
        pass
    def deliver(self):
        label=Label(text='i watch',size_hint=(.2,.2),pos_hint={'x':.1,'top':.2})
        self.add_widget(label)
        for pieces in range(10):    
            if pieces>=5:
                charge=200000
                break
            else:
                charge=200000
                break
        
        # the fucntion shud pause for 30 seconds waiting for the label to be gracefully executed 


    # function to add things in the db
    def upate(self):
        self.items.append(self.image)
        return "db updated..."
    

    def cart(self):
        label=Label(text='i watch',size_hint=(.2,.2),pos_hint={'x':.1,'top':.2})
        self.add_widget(label)
        return "cart..."
    
    

    def chat(self):
        
        Client.connect()
        var='sending ...sms..'

        return 
    def rec_(self):
        for i in range(10):
            x=2*10
            y=2*10
            x=x+10
            y=y+10
            with self.canvas:
                Color(.1,1,.2,1)
                Rectangle(source='',pos=(x,y),size=(100,100))
    def view_shops(self):
        but=Button(text="view shops", on_press=self.rec_, pos=(100,100),size=(100,100))
        self.add_widget(but)





"""
paris forex

"""


class Forex(Screen):


    # variable to hold the info the display variables '
    var='I G'

    phone='+2567...'

    email='elaijahn8@gmail.com'
    txt=''

    address=''

    price=''

    image=''

    display=''

    loop=0

    
    def loop(self):
        for i in range(100000):
            loop=i

    
    def is_broker(self):
        #varaible to hold goods sold aday
        d_sales=0
        if (d_sales/30)>=50000:
            return True
        else:
            return False

    def is_commision(self):

        #varaible to hold goods sold aday
        d_sales=0
        if (d_sales/30)>=10:
            return True
        else:
            return False
        
    def retail(self):
        #price of the item
        price=0
        #max_profit
        max_p=3000
        #min_profit
        min_p=500
        #selling price of the item

        s_p=price
    def wholesale(self):

        #price of the item
        price=0
        #max_profit
        max_p=300000
        #min_profit
        min_p=50000
        #selling price of the item
        tax=.1*min_p
        return True

        
    def search(self):
        items=['elijah']
        search_q="shops"
        for s_q in range(100000):
            if items[0]==search_q:
                display=self.item[s_q]
                return True
            else:
                return False
    def next(self):
        items=[]
        for i in len(items):
            if i==0:
                i=0+1
                break
            elif i==len(items):
                display="indexfail check prev button  plz!!!!"
                break
            elif i==None:
                display="no item!!!!"
            else:
                i=i+1
                break
                
        
    def sell(self):
        # varaible to hld the passcode for the user 
        code=TextInput(text="code ...",size_hint=(.2,.1),pos_hint={'x':.1,'y':.2})
        #variable to hold the ammount of money to be sold
        a_m=TextInput(text="code ...",size_hint=(.2,.1),pos_hint={'x':.3,'y':.2})
        #variable to hold the currency
        ugx=TextInput(text="money ...",size_hint=(.2,.1),pos_hint={'x':.5,'y':.2})
        #variable to hold the sellers name 
        user_id=TextInput( text="user_id", size_hint=(.2,.1),pos_hint={'x':.7,'y':.2})
        
        self.add_widget(code)
        self.add_widget(a_m)
        self.add_widget(ugx)
        self.add_widget(user_id)
        
    def pay(self):
        pass
    
    def mtn(self):
            #a=Mtn()
            #a.mtnpay()
            #Mtn.mtntrans()
            pass 
    def airtel(self):
        pass
    def buy(self,*args):
        # varaible to hld the passcode for the user 
        code=TextInput(text="shopcode ...",size_hint=(.2,.1),pos_hint={'x':.1,'y':.2})
        #variable to hold the ammount of money to be bought on 
        a_m=TextInput(text="name...",size_hint=(.2,.1),pos_hint={'x':.3,'y':.2})
        #variable to hold the currency
        ugx=TextInput(text="money ...",size_hint=(.2,.1),pos_hint={'x':.5,'y':.2})
        #variable to hold the buyers name 
        user_id=TextInput( text="user_id", size_hint=(.2,.1),pos_hint={'x':.7,'y':.2})
        
        self.add_widget(code)
        self.add_widget(a_m)
        self.add_widget(ugx)
        self.add_widget(user_id)


    def prev(self):

        items=[]
        for i in range(len(items)):
            if i==len(items):
                i=i-1
                break
            elif i==0:
                display="fail index!!!!, check next button"
            elif i==None:
                display="no item!!!!"
            else:
                i=i-1
        pass
    def deliver(self):
        label=Label(text='i watch',size_hint=(.2,.2),pos_hint={'x':.1,'top':.2})
        self.add_widget(label)
        for pieces in range(10):    
            if pieces>=5:
                charge=200000
                break
            else:
                charge=200000
                break
        
        # the fucntion shud pause for 30 seconds waiting for the label to be gracefully executed 


    # function to add things in the db
    def upate(self):
        self.items.append(self.image)
        return "db updated..."
    

    def cart(self):
        label=Label(text='i watch',size_hint=(.2,.2),pos_hint={'x':.1,'top':.2})
        self.add_widget(label)
        return "cart..."
    
    

    def chat(self):
        
        Client.connect()
        var='sending ...sms..'

        return 
    def rec_(self):
        for i in range(10):
            x=2*10
            y=2*10
            x=x+10
            y=y+10
            with self.canvas:
                Color(.1,1,.2,1)
                Rectangle(source='',pos=(x,y),size=(100,100))
    def view_shops(self):
        but=Button(text="view shops", on_press=self.rec_, pos=(100,100),size=(100,100))
        self.add_widget(but)

class Settings():
    pass


sm=ScreenManager()
sm.add_widget(Ishop(name="ishops"))
sm.add_widget(Ads(name="ads"))
sm.add_widget(Invest(name="invest"))

sm.add_widget(Forex(name="forex"))





class MainApp(App):


    def build(self):
        self.title='iphone shop'
        return sm
    
    def playing(self):
        notification.notify(title='iphone shop', message='playing ..')
        return Ads()

if __name__=='__main__':
    e=MainApp()
    e.run()