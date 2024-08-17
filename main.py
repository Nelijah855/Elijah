

"""
libraries reqiured 

mysql.connector,plyer,ffpyplayer,mtnmomo,opencv-python,httplib,
matplotlib,numpy,bio,sympy,tradingeconomics,global-chem,pytube,
sklearn,nltk=3.5

"""
from gui import Inner
#from login import Login
#m mtn import Mtn
#from network import Client,Server

#from security import Loophole,Blockchain,Phisphing,Crsf,Crypto

from kivy.properties import NumericProperty
from kivy.uix.bubble import Bubble
bubble=Bubble()




import kivy
import mysql.connector 
kivy.require('2.0.0')
import time
import datetime
import socket
from kivy.properties import ListProperty, StringProperty,ObjectProperty
import random
from kivy.uix.textinput import TextInput
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.floatlayout import FloatLayout
#class for handling input,doubletap accelemoter
from kivy.input import MotionEvent

from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.video import Video
from kivy.uix.image import Image
# the class to be used to animate wigdets e.g to move button from one end to another 
from kivy.animation import Animation

#clock class to replace the while loop that would have been needed to be employed 
from kivy.clock import Clock
#from plyer import notification
#from utils import CFEVideoconf,image_resize
import os
from kivy.graphics import Rectangle,Color
import sys
import sqlite3
#from kivy.uix.widget import Widget

#from kivy.core.audio import SoundLoader


import os
import sys
#import cv2

images=['']



blue=(.05,.04,.4,1)
lightb=(.04,.07,1,1)
black=(0.01,.04,.044,1)
minsk=(.02,.03,.4,1)


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
        
        self.conn = sqlite3.connect('users_0.db')
        self.conn.execute('''DROP TABLE IF EXISTS users; ''')
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


#sql=Sqlite("")

#class to exit the application on exiting 
class Exit():
    def exi(self):
        sys.exit(0)
        return 0
def exi():
    pass
b=exi()


# class  for handling the drawing of the rectangle 
class Recta_(FloatLayout):
    def canvas_inc_x(self):
        but=Button(text="up",on_press=b,background_color= (0,0.5,1,1))
        self.add_widget(but)
        return 


    def canvas_inc_y(self,y):
        but=Button(text="up",on_press=b,background_color= (0,0.5,1,1))
        self.add_widget(but)
        
        pass


    def draw_rectangle(self):
        with self.canvas:
            Color(.23,1,.34)
            Rectangle(source='icon.png',pos=self.pos,size=self.size,background_color= (0,0.5,1,1))





# kv gui template 

kb=Builder.load_file('ishop.kv')


"""


 class for handling shopping and ads 


"""


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

class to generator code for working with the atomics company



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
    search=True

    #image=StringProperty(images[0])
    #index=NumericProperty(0)
    display=''
    ads=ObjectProperty()
    games=ObjectProperty()
    games=ObjectProperty()
    account=ObjectProperty()
    games=ObjectProperty()

    loop=0
    def cli(self):
        #Client.connector()
        Inner().pop()
        
    def serv(self):
        #Server.listener()
        Inner().progress()
    def logout(self):
        self.ids.logout.text='out'
    def check():
        Inner().check()  
    def loop(self):

        for i in range(4):
            self.add_widget(Label(text='micronet',pos_hint=(.2,.1*i),size_hint=(.2,0.08),background_color= (0,0.5,1,1)))

    
    def is_broker(self):
        #varaible to hold goods sold aday
        d_sales=0
        if (d_sales/30)>=50000:
            return True
        else:
            return False
        
        """
        function responsible for arrenging the shops in the app
        """
    def shops(self):
        # this variable is set True with database after the user pays and finds the path of the video in the video table with db 
        paid=True
        #the path from the database 
        path='x.mp4'
        if paid:
            #FUNCTION TO LOAD THE VIDEO OF THE SHOP
            video=Video(source=path,state='play',background_color= (0,0.5,1,1))
            self.add_widget(video)
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
        """
        items=['elijah']
        search_q="shops"
        for s_q in range(100000):
            if items[0]==search_q:
                display=self.item[s_q]
                return True
            else:
                return False
                """
        label=Label(text='micronet',size_hint=(.2,.2),pos_hint={'x':.1,'top':.2})
        search=Label(text='searching...',size_hint=(.2,.1),pos_hint={'x':.6,'top':.5})
        self.add_widget(search)

        if self.search==True:
            search1=Label(text='Found(1000)',size_hint=(.2,.1),pos_hint={'x':.6,'top':.4})
            self.add_widget(search1)
        else:
            pass
    def nex(self):
        self.index +=1
        self.index %=len(images)
        self.image=images[self.index]
        
    def sell(self):
        global code 
        global a_m
        global ugx
        global user_id
        global finish
        """accesing the ishops ids

        """
        self.ids.member.text


        # varaible to hld the passcode for the user 
        code=TextInput(text="code ...",size_hint=(.2,.05),pos_hint={'x':.1,'y':.2},color=(0,1,0,1),background_color=(0,1,0,1))
        #variable to hold the ammount of money to be sold
        a_m=TextInput(text="code ...",size_hint=(.2,.05),pos_hint={'x':.1,'y':.3},color=(0,1,0,1),background_color=(0,1,0,1))
        #variable to hold the currency
        ugx=TextInput(text="money ...",size_hint=(.2,.05),pos_hint={'x':.1,'y':.4},color=(0,1,0,1),background_color=(0,1,0,1))
        #variable to hold the sellers name 
        user_id=TextInput( text="user_id", size_hint=(.2,.05),pos_hint={'x':.1,'y':.5},color=(0,1,0,1),background_color=(0,1,0,1))
        finish=Button( text="finish", size_hint=(.2,.05),pos_hint={'x':.1,'y':.6},color=(0,1,0,1),background_color=(0,1,0,1),on_pres=self.clear_w)
        
        
        self.add_widget(finish)
        self.add_widget(code)
        self.add_widget(a_m)
        self.add_widget(ugx)
        self.add_widget(user_id)
    """
    video function
    """
    def video(self):
        vid=Video(source='x.mp4',preview='icon.png',state='play',options={'eos':'loop'},pos_hint={'x':.3,'y':.0},size_hint=(.4,.3))
        self.add_widget(vid)

        
    def pay(self):
        search=Label(text='usercode ',size_hint=(.2,.1),pos_hint={'x':.3,'top':.3})
        a_m=TextInput(size_hint=(.2,.05),pos_hint={'x':.1,'y':.3},color=(0,1,0,1),background_color=(0,1,0,1))
        #variable to hold the currency
        search1=Label(text='money',size_hint=(.2,.1),pos_hint={'x':.3,'top':.4})
        ugx=TextInput(size_hint=(.2,.05),pos_hint={'x':.1,'y':.4},color=(0,1,0,1),background_color=(0,1,0,1))
        #variable to hold the sellers name
        search2=Label(text='userid',size_hint=(.2,.1),pos_hint={'x':.3,'top':.5},background_color= (0,0.5,1,1)) 
        user_id=TextInput( size_hint=(.2,.05),pos_hint={'x':.1,'y':.5},color=(0,1,0,1),background_color=(0,1,0,1),focus=True,multiline=False)
        self.add_widget(a_m)
        self.add_widget(ugx)
        self.add_widget(user_id)
        self.add_widget(search)
        self.add_widget(search1)
        self.add_widget(search2)
    def clear_w(self):
        self.remove_widget(code)
        self.remove_widget(finish)
        self.remove_widget(a_m)
        self.remove_widget(ugx)
        self.remove_widget(user_id)


        """
        
        audio function
        """
    def audio(self):
        """sound=SoundLoader.load('x.mp3')
        self.add_widget(sound)
        if True:
            sound.play()"""
        pass

    
    def mtn(self):
            #a=Mtn()
            #a.mtnpay()
            #Mtn.mtntrans()
            pass
    def painter(self):
        a=Inner()
        a.draw()
    
    def airtel(self):
        pass
    def entering(self,value):
        self.add_widget(Label(text=value,size_hint=(.2,.05),pos_hint={'x':.7,'y':.2}),background_color=minsk)
    def pressed(self):
        self.add_widget(Label(text="sent order",size_hint=(.3,.05),pos_hint={'x':.3,'y':.2}),background_color=blue)
    def buy(self,*args):
        # varaible to hld the passcode for the user 
        code=TextInput(text="shopcode ...",size_hint=(.2,.05),pos_hint={'x':.7,'y':.5},background_color=(0,1,1,1))
        #variable to hold the ammount of money to be bought on 
        a_m=TextInput(text="name...",size_hint=(.2,.05),pos_hint={'x':.7,'y':.4},background_color=(0,1,1,1))
        #variable to hold the currency
        ugx=TextInput(text="money ...",size_hint=(.2,.05),pos_hint={'x':.7,'y':.3},background_color=(0,1,1,1))
        #variable to hold the buyers name 
        user_id=TextInput( text="user_id", size_hint=(.2,.05),pos_hint={'x':.7,'y':.2},background_color=(0,1,1,1))
        user_id.bind(on_text_validate=self.entering)
        finish=Button( text="finish", size_hint=(.2,.05),pos_hint={'x':.7,'y':.1},background_color=(0,1,1,1),on_press=self.clear_w)
        finish.bind(on_press=self.pressed())
        self.add_widget(code)
        self.add_widget(finish)
        self.add_widget(a_m)
        self.add_widget(ugx)
        self.add_widget(user_id)


    def prev(self):

        self.index +=1
        self.index %=len(images)
        self.image=images[self.index]
    def deliver(self):
        label=Label(text='micronet',size_hint=(.2,.2),pos_hint={'x':.1,'top':.2},background_color= (.2,0.5,1,1))
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
    def update(self):
        self.items.append(self.image)
        return "db updated..."
    

    def cart(self):
        label=Label(text='auto ',size_hint=(.2,.2),pos_hint={'x':.1,'top':.2},background_color= (0,0.5,1,1))
        self.add_widget(label)
        return "cart..."
    
    

    def chat(self):
        
        #Client.connect()
        #var='connecting'
        pass 

        return 
    def rec_(self):
        for i in range(10):
            x=2*10
            y=2*10
            x=x+10
            y=y+10
            with self.canvas:
                Color(.1,1,.2,1)
                Rectangle(source='icon.png',pos=(x,y),size=(100,100),background_color= (0,0.5,1,1))
    def view_shops(self):
        but=Button(text="view shops", on_press=self.rec_, pos=(100,100),size=(100,100),background_color= (0,0.5,1,1))
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


"""

class for handling and linking the media advertising 

"""
class Ads(Screen):
    display=StringProperty('')
    def exi(self):
        
        Exit().exit()
    def nex(self):
        self.index +=1
        self.index %=len(images)
        self.image=images[self.index]
    
    def prev(self):
        
        self.index +=1
        self.index %=len(images)
        self.image=images[self.index]

        
    def sell(self):
        # varaible to hld the passcode for the user 
        search=Label(text='usercode ',size_hint=(.2,.1),pos_hint={'x':.3,'top':.2},background_color= (0,0.5,1,1))
        code=TextInput(size_hint=(.2,.1),pos_hint={'x':.1,'y':.2})
        #variable to hold the ammount of money to be sold
        search1=Label(text='code ',size_hint=(.2,.1),pos_hint={'x':.3,'top':.3},background_color= (0,0.5,1,1))
        a_m=TextInput(size_hint=(.2,.1),pos_hint={'x':.1,'y':.3})
        #variable to hold the currency
        search2=Label(text='money',size_hint=(.2,.1),pos_hint={'x':.3,'top':.4},background_color= (0,0.5,1,1))
        ugx=TextInput(size_hint=(.2,.1),pos_hint={'x':.3,'y':.4})
        #variable to hold the sellers name 
        search3=Label(text='userid',size_hint=(.2,.1),pos_hint={'x':.3,'top':.5},background_color= (0,0.5,1,1))
        user_id=TextInput(size_hint=(.2,.1),pos_hint={'x':.3,'y':.5})
        
        
        self.add_widget(code)
        self.add_widget(a_m)
        self.add_widget(ugx)
        self.add_widget(user_id)
        self.add_widget(search)
        self.add_widget(search1)
        self.add_widget(search2)
        self.add_widget(search3)

        
    def pay(self):
        
        inr=Inner()
        

        
    def nex(self,*args):
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
    
    def video(self):
        vid=Video(source='x.mp4',preview='icon.png',state='play',options={'eos':'loop'},size_hint=(.5,.2),pos_hint={'x':0,'top':.2})
        self.add_widget(vid)
        
    


    def sound(self):
        #sound=SoundLoader.load('x.mp3')
        self.add_widget(Button(text='Audio',size_hint=(.2,.05),pos_hint={'x':.8,'top':.2},background_color= (0,0.5,1,1)))
        
        if True:
            #sound.play()
            pass

        else:
            pass 


    def send(self):
        return 'sent'
    def prev(self):
        self.display="loading video......."
        label=Button(text='video',size_hint=(.2,.05),pos_hint={'x':.1,'top':.2},background_color= (1,0.5,1,1))
        self.add_widget(label)
    


"""
class for peoples investments


"""





class Invest(Screen):


    # variable to hold the info the display variables '
    var='I G'
    balance=ObjectProperty()
    phone='+2567...'

    email='elaijahn8@gmail.com'
    txt=''

    address=''

    price=''

    image=StringProperty(images[0])
    index=NumericProperty(0)

    display=''

    loop=0

    
    def loop(self):
        for i in range(10):
            self.add_widget(Label(text=i,size_hint=(.1,.1),pos_hint={'x':.2,'top':.1},background_color= (0,0.5,1,1)))
            

    
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
    def nex(self):
        self.index +=1
        self.index %=len(images)
        self.image=images[self.index]
                
        
    def sell(self):
         # varaible to hld the passcode for the user 
        code=TextInput(size_hint=(.2,.05),pos_hint={'x':.6,'y':.2})
        
        l1=Label(text='usercode ',size_hint=(.1,.1),pos_hint={'x':1,'y':.4},background_color= (0,0.5,1,1))
        #variable to hold the ammount of money to be sold
        a_m=TextInput(size_hint=(.2,.05),pos_hint={'x':.6,'y':.3})
        l2=Label(text='name ',size_hint=(.2,.1),pos_hint={'x':1,'y':.3},background_color= (0,0.5,1,1))
        #variable to hold the currency
        ugx=TextInput(size_hint=(.2,.05),pos_hint={'x':.6,'y':.4})
        l3=Label(text='trust ',size_hint=(.2,.1),pos_hint={'x':1,'y':.2},background_color= (0,0.5,1,1))
        #variable to hold the sellers name 
        user_id=TextInput(size_hint=(.2,.05),pos_hint={'x':.6,'y':.6})
        l4=Label(text='number',size_hint=(.2,.1),pos_hint={'x':1,'y':.1},background_color= (0,0.5,1,1))

        but=Button(text='send',size_hint=(.2,.1),pos_hint={'x':.8,'y':.0},background_color= (1,0.5,1,1))

        
        self.add_widget(code)
        self.add_widget(l1)
        self.add_widget(l2)
        self.add_widget(l3)
        self.add_widget(l4)
        self.add_widget(a_m)
        self.add_widget(ugx)
        self.add_widget(user_id)
        self.add_widget(but)
        if but.state=='down':
            pass
        
    def pay(self):
        pass
    def shares(self):
        code=TextInput(size_hint=(.2,.05),pos_hint={'x':.6,'y':.2})
        
        l1=Label(text='usercode ',size_hint=(.1,.1),pos_hint={'x':1,'y':.4},background_color= (0,0.5,1,1))
        #variable to hold the ammount of money to be sold
        a_m=TextInput(size_hint=(.2,.05),pos_hint={'x':.6,'y':.3})
        l2=Label(text='name ',size_hint=(.2,.1),pos_hint={'x':1,'y':.3},background_color= (0,0.5,1,1))
        but=Button(text='send',size_hint=(.2,.1),pos_hint={'x':.8,'y':.0},background_color= (1,0.5,1,1))
        self.add_widget(code)
        self.add_widget(l1)
        self.add_widget(a_m)
        self.add_widget(l2)
        self.add_widget(but)
        if but.state=='down':
            pass

    def account(self):
        #balance=self.ids.account.text
        if True:
            balance=20000
        else:
            balance=0.0
        return balance
    
    def invest(self):
        data=Inner.investment()
        return data

    def mtn(self):
            #a=Mtn()
            #a.mtnpay()
            #Mtn.mtntrans()
            pass 
    def forex(self):
        Inner.forex()

    def pinnacle(self):
        pin=Inner()
        pin.pinnacle()
        return pin
    
    def airtel(self):
        pass

    def buy(self):
        # varaible to hld the passcode for the user 
        code=TextInput(size_hint=(.3,.05),pos_hint={'x':.4,'y':.2},background_color= (0,0.5,1,1))
        
        l1=Label(text='usercode ',size_hint=(.1,.1),pos_hint={'x':.8,'y':.18},background_color= (0,0.5,1,1))
        #variable to hold the ammount of money to be sold
        a_m=TextInput(size_hint=(.3,.05),pos_hint={'x':.4,'y':.3})
        l2=Label(text='name ',size_hint=(.1,.1),pos_hint={'x':.8,'y':.28},background_color= (0,0.5,1,1))
        #variable to hold the currency
        ugx=TextInput(size_hint=(.3,.05),pos_hint={'x':.4,'y':.4})
        l3=Label(text='trust ',size_hint=(.1,.1),pos_hint={'x':.8,'y':.38},background_color= (0,0.5,1,1))
        #variable to hold the sellers name 
        user_id=TextInput(size_hint=(.3,.05),pos_hint={'x':.4,'y':.6})
        l4=Label(text='+phone',size_hint=(.1,.1),pos_hint={'x':.8,'y':.48},background_color= (0,0.5,1,1))

        but=Button(text='send',size_hint=(.1,.05),pos_hint={'x':.4,'y':.08},background_color= (0,0.5,0,1))

        
        self.add_widget(code)
        self.add_widget(l1)
        self.add_widget(l2)
        self.add_widget(l3)
        self.add_widget(l4)
        self.add_widget(a_m)
        self.add_widget(ugx)
        self.add_widget(user_id)
        self.add_widget(but)
        

    def trade(self):
        pass
    def prev(self):

        self.index +=1
        self.index %=len(images)
        self.image=images[self.index]
    def deliver(self):
        label=Label(text='micronet',size_hint=(.2,.2),pos_hint={'x':.1,'top':.2},background_color= (0,0.5,1,1))
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
    def update(self):
        
        pass
    

    def cart(self):
        label=Label(text='items',size_hint=(.2,.2),pos_hint={'x':.1,'top':.2},background_color= (0,0.5,1,1))
        self.add_widget(label)
    def cafepay(self,value):
        label=Label(text='paying['+str(value)+']ugx',size_hint=(.3,.2),pos_hint={'x':.6,'top':.1},background_color= (0,0.5,1,1))
        self.add_widget(label)
    def cafe(self):
        l1=Label(text='money',size_hint=(.2,.05),pos_hint={'x':.4,'top':.4},background_color= (0,0.5,1,1))
        #variable to hold the ammount of money to be sold
        a_in=TextInput(size_hint=(.2,.05),pos_hint={'x':.4,'top':.3},on_text_validate=self.cafepay)
        a_m=Button(text="complete",size_hint=(.2,.05),pos_hint={'x':.4,'top':.2},background_color= (0,0.5,1,1))
        self.add_widget(l1)
        self.add_widget(a_m)
        self.add_widget(a_in)
        
        return 

    def chat(self):
        
        #Client.connect()
        var='connecting..'
        self.add_widget(Label(text=var,size_hint=(.2,.08),pos_hint=(.2,.1),background_color= (0,0.5,1,1)))

        return 
    def rec_(self):
        for i in range(10):
            x=2*10
            y=2*10
            x=x+10
            y=y+10
            with self.canvas:
                Color(.1,1,.2,1)
                Rectangle(source='icon.png',pos=(x,y),size=(100,100),background_color= (0,0.5,0,1))
    def view_shops(self):
        but=Button(text="shopview", on_press=self.rec_, pos=(100,100),size=(100,100),background_color= (0,0.5,1,1))
        self.add_widget(but)
        image=Image(source='icon.png',size_hint=(.2,.2),pos_hint={'x':.1,'top':.2})
        self.add_widget(image)




"""
class for handling the   forex bereau 

"""


class Forex(Screen):


    # variable to hold the info the display variables '

   
    
    def loop(self):
        for i in range(10):
            loop=i+1

            #variable to control the screen
    def forec(self):
        import market 
        mark=True
        if mark:
            
            for i in market.country_market:

                self.add_widget(Label(text=i,size_hint=(.3,.4),pos_hint={'x':0,'y':.1},background_color=(.2,.2,.3,1)))
    def is_broker(self):
        #varaible to hold goods sold aday
        d_sales=0
        if (d_sales/30)>=50000:
            return True
        else:
            return False

    def wallet(self):
        self.add_widget(Button(text='100usd',size_hint=(.2,.05),pos_hint={'x':.7,'y':1},background_color=(.2,.2,.3,1)))
    
        
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
    def nex(self):
        self.index +=1
        self.index %=len(images)
        self.image=images[self.index]
                
        
    
    def mtn(self):
            #a=Mtn()
            #a.mtnpay()
            #Mtn.mtntrans()
            finish=Button(text="mtn pay ",size_hint=(.2,.1),pos_hint={'x':.5,'y':.2},background_color= (0,1,1,1))
            self.add_widget(finish)
            pass 
    def airtel(self):
        finish=Button(text="airtel pay",size_hint=(.2,.1),pos_hint={'x':.5,'y':.2},background_color= (1,0.5,1,1))
        self.add_widget(finish)
    def buy(self):
        # varaible to hld the passcode for the user 
        code=Label(text="shop",size_hint=(.2,.1),pos_hint={'x':.1,'y':.2},background_color= (0,0.5,1,1))
        codet=TextInput(size_hint=(.2,.1),pos_hint={'x':.4,'y':.2})
        #variable to hold the ammount of money to be bought on 
        name=Label(text="name",size_hint=(.2,.1),pos_hint={'x':.1,'y':.3},background_color= (0,0.5,1,1))
        namet=TextInput(size_hint=(.2,.1),pos_hint={'x':.4,'y':.3})
        #variable to hold the currency
        money=Label(text="money",size_hint=(.2,.1),pos_hint={'x':.1,'y':.4},background_color= (0,0.5,1,1))
        moneyt=TextInput(size_hint=(.2,.1),pos_hint={'x':.4,'y':.4})
        #variable to hold the buyers name 
        userid=Label(text="userid",size_hint=(.2,.1),pos_hint={'x':.1,'y':.5},background_color= (0,0.5,1,1))
        useridt=TextInput(size_hint=(.2,.1),pos_hint={'x':.4,'y':.2})
        finish=Button(text="finish...",size_hint=(.2,.1),pos_hint={'x':.3,'y':.5},background_color= (0,0.5,1,1))
        self.add_widget(finish)
        self.add_widget(codet)
        self.add_widget(namet)
        self.add_widget(moneyt)
        self.add_widget(useridt)
        self.add_widget(code)
        self.add_widget(name)
        self.add_widget(money)
        self.add_widget(userid)


    def tools(self):
        cod=Label(text="premium services",size_hint=(.2,.1),pos_hint={'x':.5,'y':1},background_color= (0,0.5,1,1))
        # varaible to hld the passcode for the user 
        code=Button(text="graphs",size_hint=(.2,.1),pos_hint={'x':.1,'y':.2},background_color= (0,0.5,1,1))
        #variable to hold the ammount of money to be bought on 
        a_m=Button(text="lines",size_hint=(.2,.1),pos_hint={'x':.3,'y':.2},background_color= (0,0.5,1,1))
        #variable to hold the currency
        ugx=Button(text="indexers",size_hint=(.2,.1),pos_hint={'x':.5,'y':.2},background_color= (0,0.5,1,1))
        #variable to hold the buyers name 
        user_id=Button( text="Ai", size_hint=(.2,.1),pos_hint={'x':.7,'y':.2},background_color= (0,0.5,1,1))
        finish=Button(text="finish...",size_hint=(.2,.1),pos_hint={'x':.5,'y':.2},background_color= (0,0.5,1,1))
        self.add_widget(finish)
        self.add_widget(code)
        self.add_widget(cod)
        self.add_widget(a_m)
        self.add_widget(ugx)
        self.add_widget(user_id)


    def prev(self):

        self.index +=1
        self.index %=len(images)
        self.image=images[self.index]
    def deliver(self):
        label=Label(text='micronet',size_hint=(.2,.2),pos_hint={'x':.1,'top':.2})
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
    def update(self):
        self.items.append(self.image)
        return "db updated..."
    

    def cart(self):
        label=Label(text='cedar tecs',size_hint=(.2,.2),pos_hint={'x':.1,'top':.2},background_color= (0,0.5,1,1))
        self.add_widget(label)
        return "cart..."
    
    def forex(self):
        inr=Inner()
        inr.forex()
        return 
    def exc(self):
        pass
    def rates(self):
        label=Label(text='0.05%',size_hint=(.2,.2),pos_hint={'x':.1,'top':.2},background_color= (0,0.5,1,1))
        self.add_widget(label)
    def futures(self):
        l1=Label(text='currency',size_hint=(.3,.05),pos_hint={'x':.0,'y':.2})
        code=TextInput(size_hint=(.3,.05),pos_hint={'x':.4,'y':.2})
        
        l1=Label(text='ammount',size_hint=(.3,.05),pos_hint={'x':.4,'y':.3},background_color= (0,0.5,1,1))
        #variable to hold the ammount of money to be sold
        a_m=TextInput(size_hint=(.3,.05),pos_hint={'x':.4,'y':.3})

        l2=Label(text='username ',size_hint=(.3,.05),pos_hint={'x':.4,'y':.4},background_color= (0,0.5,1,1))
        #variable to hold the currency
        ugx=TextInput(size_hint=(.3,.05),pos_hint={'x':.4,'y':.4})

        l3=Label(text='phone ',size_hint=(.3,.05),pos_hint={'x':.4,'y':.5},background_color= (0,0.5,1,1))
        #variable to hold the sellers name 
        user_id=TextInput(size_hint=(.3,.05),pos_hint={'x':.4,'y':.5})

        l4=Label(text='pin',size_hint=(.3,.05),pos_hint={'x':.4,'y':.6},background_color= (0,0.5,1,1))
        pin=TextInput(size_hint=(.3,.05),pos_hint={'x':.4,'y':.5})
        
        
        b=Button(text='finish',size_hint=(.2,.05),pos_hint={'x':.5,'y':.6} ,background_color= (1,0,0,1))
        clear=Button(text='clear',size_hint=(.2,.05),pos_hint={'x':.5,'y':.6} ,background_color= (1,0,0,1))
        
        self.add_widget(code)
        self.add_widget(l1)
        self.add_widget(l2)
        self.add_widget(l3)
        self.add_widget(l4)
        self.add_widget(a_m)
        self.add_widget(ugx)
        self.add_widget(user_id)
        self.add_widget(pin)
        self.add_widget(b)

        



    def chat(self):
        
        #Client.connect()
        label=Label(text='sms..',size_hint=(.2,.08),pos_hint={'x':.2,'top':.2},background_color= (0,0.5,1,1))
        self.add_widget(label)

        return 
    def rec_(self):
        for i in range(10):
            x=2*10
            y=2*10
            x=x+10
            y=y+10
            with self.canvas:
                Color(.1,1,.2,1)
                Rectangle(source='icon.png',pos=(x,y),size=(100,100),background_color= (0,0.5,1,1))
    def view_shops(self):
        but=Button(text="view shops", on_press=self.rec_, pos=(100,100),size=(100,100),background_color= (0,0.5,1,1))
        self.add_widget(but)

class Settings():
    COLOR=(0,0,0,1)
    X=0
    Y=0
    POS={'x':X,'top':Y}


"""

login screen
"""

class Login(Screen):
    username=ObjectProperty()
    password=ObjectProperty()
    
    def register(self):
        

        if self.ids.username.on_text==True and self.ids.password.on_text==True:
            username=self.ids.username.text
            password=self.ids.password.text
            if username=='' and password=='':
                label=Label(text='values missing!!',size_hint=(.2,.08),pos_hint={'x':.2,'top':.2},background_color= (1,0,0,1))
                self.add_widget(label)
            elif username!=None and password!=None:
                label=Label(text='validating!!',size_hint=(.2,.08),pos_hint={'x':.2,'top':.2},background_color= (1,0.5,1,1))
                self.add_widget(label)
            else:
                label=Label(text='user registerd',size_hint=(.2,.08),pos_hint={'x':.2,'top':.2},background_color= (0,0.5,1,1))
                self.add_widget(label)
                self.log()




         
    def log(self):
        l=Label(text='logined in ',size_hint=(.2,.8),pos_hint={'x':5,'top':.2},background_color= (0,0.5,1,1))
        self.add_widget(l)
        
            

        
    def start(self):
        self.register()
        
#checking the password  
    def password(self):
        if Login.is_password():
            return True
        else:
            False

#checking the name
    def name(self):
        if Login.is_name():
            return True
        else:
            return False
    
    def both(self):
        if self.name() and self.password():
            return True
        else:
            False 

"""
class to handle the credit section

"""
class Credit(Screen):
    def credit(self):
        # varaible to hld the passcode for the user 
        label=Label(text='usercode',size_hint=(.2,.05),pos_hint={'x':.3,'y':.2},background_color= (0,0.5,1,1))
        code=TextInput(size_hint=(.2,.05),pos_hint={'x':.1,'y':.2})
        #variable to hold the ammount of money to be saved 
        label1=Label(text='passcode',size_hint=(.2,.05),pos_hint={'x':.3,'y':.3},background_color= (0,0.5,1,1))
        a_m=TextInput(size_hint=(.2,.05),pos_hint={'x':.1,'y':.3})
        #variable to hold the currency
        label2=Label(text='money',size_hint=(.2,.05),pos_hint={'x':.3,'y':.4},background_color= (0,0.5,1,1))
        ugx=TextInput(size_hint=(.2,.05),pos_hint={'x':.1,'y':.4})
        #variable to hold the savers name 
        label3=Label(text='usercode',size_hint=(.2,.05),pos_hint={'x':.3,'y':.5},background_color= (0,0.5,1,1))

        user_id=TextInput( size_hint=(.2,.05),pos_hint={'x':.1,'y':.5})
        btn=Button(text="loan",pos_hint={'x':.3,'top':.1},size_hint=(.2,.2),color=(0,1,0,1),background_color= (0,0.5,1,1))
        self.add_widget(code)
        self.add_widget(a_m)
        self.add_widget(ugx)
        self.add_widget(user_id)
        self.add_widget(btn)
        self.add_widget(label)
        self.add_widget(label1)
        self.add_widget(label2)
        self.add_widget(label3)
        
        
    # the function to carry out crediting the user 
    def credited(self):
        with open('credit.txt' ,'w') as file:
            file.write("credited with an ammount of 10000000ugx...")
            file.close()
    # where cr stands for credit 
    def cr_track(self):
        pass
    def clear(self):
        self.clear_widgets()
    def insurance(self):
        search=Label(text='policy',size_hint=(.2,.1),pos_hint={'x':.4,'top':.25},background_color=(0,0,1,1))
        code=TextInput(size_hint=(.2,.05),pos_hint={'x':.3,'y':.2})
        #variable to hold the ammount of money to be saved 
        search1=Label(text='premium',size_hint=(.2,.1),pos_hint={'x':.4,'top':.4},background_color=(0,0,1,1))
        a_m=TextInput(size_hint=(.2,.05),pos_hint={'x':.3,'y':.3})
        #variable to hold the currency
        
        ugx=TextInput(size_hint=(.2,.05),pos_hint={'x':.3,'y':.4})
        #variable to hold the savers name 
        search3=Label(text='usename',size_hint=(.2,.1),pos_hint={'x':.4,'top':.5},background_color=(0,0,1,1))
        user_id=TextInput(size_hint=(.2,.05),pos_hint={'x':.3,'y':.5},color=(0,1,0,1))
        search2=Label(text='money',size_hint=(.2,.1),pos_hint={'x':.3,'top':.6},background_color=(0,0,1,1))
        btn=Button(text="insure",pos_hint={'x':.3,'top':.1},size_hint=(.2,.08),color=(0,1,0,1),background_color=(0,0,1,1))
        self.add_widget(code)
        self.add_widget(a_m)
        self.add_widget(ugx)
        self.add_widget(user_id)
        self.add_widget(btn)
        self.add_widget(search)
        self.add_widget(search1)
        self.add_widget(search2)
        self.add_widget(search3)
        btn_c=Button(text="clear",pos_hint={'x':.6,'top':.1},size_hint=(.2,.08),color=(0,1,0,1),background_color=(0,0,1,1),on_press=self.clear)
        self.add_widget(btn_c)
    def loan(self):
        maturity=30
        issue_d=0
        tim=time.asctime()
        #this record the time the loan is taken  and uses current time to calculate the time taken with loan 
        #if time is greater than 30 days then the fine is inserted 
        
        return 
    
    def eligable(self):
        pass
    def enter(self):
        a=Inner()
        a.forex()


"""
class to handle the savings account

--mobilizing savings 
--goods and services 
--transportation
--education 
--devolepment
--equity financing 
--joint savings 
--tecnology advancements
--transformation

"""


class Savings(Screen):
    def save(self):
        label=Label(text='usecode',size_hint=(.2,.1),pos_hint={'x':.4,'top':.2},background_color= (0,0.5,1,1))
        code=TextInput(size_hint=(.2,.05),pos_hint={'x':.2,'y':.2})
        label1=Label(text="money",size_hint=(.2,.1),pos_hint={'x':.4,'top':.3},background_color= (0,0.5,1,1))
        money=TextInput(size_hint=(.2,.05),pos_hint={'x':.2,'y':.3})
        label2=Label(text='userid',size_hint=(.2,.1),pos_hint={'x':.4,'top':.4},background_color= (0,0.5,1,1))
        receiver=TextInput( size_hint=(.2,.05),pos_hint={'x':.2,'y':.4})
        btn=Button(text="Save ",pos_hint={'x':.2,'top':.1},size_hint=(.2,.05),color=[0,1,0,1],background_color= (0,0.5,1,1))
        
        self.add_widget(code)
        self.add_widget(btn)
        self.add_widget(money)
        self.add_widget(receiver)
        self.add_widget(label)
        self.add_widget(label1)
        self.add_widget(label2)
        if btn.state=='down':
            pass
        
    # the function to carry out crediting the user 
    def saved(self):
        with open('saved.txt' ,'w') as file:
            file.write("saved  an ammount of 10000000ugx...")
            file.close()



"""
class for handling the media files 
--news 
--entertainment
--talks
--hangouts 
--share
--comment section
--youth devolelpment
--science and tecnology talks

"""
class Media(Screen):
    
    programs=[]
    hrs=0
    days=0
    green=True 
    def music(self):
        music=Button(text='Djmusic',size_hint=(.2,.05),pos_hint={'x':.6,'y':.7} ,background_color= (0,0.5,1,1))
        self.add_widget(music)
        if music.on_press==True:
            self.remove_widget(music)
    def editor(self):
        #changing  the font size of the words and alignment 
        
        
        next1=Button(text="micronetTV",size_hint=(.2,.05),pos_hint={'x':.5,'y':.8} ,background_color= (0,0.5,1,1))
        self.add_widget(next1)

        video=Video(state='play',source='x.mp4',size_hint=(.6,.4),pos_hint={'x':.4,'y':.2},background_color= (0,0.5,1,1))
        self.add_widget(video)
        nex=Button(text="news",size_hint=(.2,.05),pos_hint={'x':.9,'y':.1} ,background_color= (0,0.5,1,1))
        self.add_widget(nex)
            #self.remove_widget(next1)
            



    
    def news(self):
        # the news anchors platform for the new delivery

        l=Label(text="News live",size_hint=(.4,.1),pos_hint={'x':.0,'y':.2},background_color= (0,0.5,1,1))
        next1=Button(text='next',size_hint=(.2,.05),pos_hint={'x':.6,'y':.7},background_color= (0,0.5,1,1) )
        self.add_widget(l)
        self.add_widget(next1)
        #if next1.on_press==True:
        #self.remove_widget(next1)
    """
    
    presenter function 


    """
    def presenter(self):
        l1=Label(text='salary:',size_hint=(.3,.05),pos_hint={'x':.0,'y':.1},background_color= (0,0.5,1,1))
        code=TextInput(size_hint=(.3,.05),pos_hint={'x':.7,'y':.2})
        
        l1=Label(text='ammount:',size_hint=(.3,.05),pos_hint={'x':.4,'y':.2},background_color= (0,0.5,1,1))
        #variable to hold the ammount of money to be sold
        a_m=TextInput(size_hint=(.3,.05),pos_hint={'x':.7,'y':.3})

        l2=Label(text='username: ',size_hint=(.3,.05),pos_hint={'x':.4,'y':.3},background_color= (0,0.5,1,1))
        #variable to hold the currency
        ugx=TextInput(size_hint=(.3,.05),pos_hint={'x':.7,'y':.4})

        l3=Label(text='phone: ',size_hint=(.3,.05),pos_hint={'x':.4,'y':.4},background_color= (0,0.5,1,1))
        #variable to hold the sellers name 
        user_id=TextInput(size_hint=(.3,.05),pos_hint={'x':.7,'y':.5})

        l4=Label(text='pin:',size_hint=(.3,.05),pos_hint={'x':.4,'y':.5},background_color= (0,0.5,1,1))
        pin=TextInput(size_hint=(.3,.05),pos_hint={'x':.7,'y':.5})
        
        b=Button(text='finish',size_hint=(.2,.05),pos_hint={'x':.6,'y':.6} ,background_color=(1,0,0,1))
        b.bold=True
        
        b.background_color=0,1,1,1
        b.background_down=''
        b.background_down=''

        
        self.add_widget(code)
        self.add_widget(l1)
        self.add_widget(l2)
        self.add_widget(l3)
        self.add_widget(l4)
        self.add_widget(a_m)
        self.add_widget(ugx)
        self.add_widget(user_id)
        self.add_widget(pin)
        self.add_widget(b)
        # the news anchors platform for the new delivery
        
    
        
        """
    function show
    
    
    """
    def show(self):
        l1=Label(text='name: Timo',size_hint=(.3,.05),pos_hint={'x':.0,'y':.2},background_color= (0,0.5,1,1))
        code=Label(text="age: 20",size_hint=(.3,.05),pos_hint={'x':.4,'y':.2},background_color= (0,0.5,1,1))
        
        l1=Label(text='country:ug',size_hint=(.3,.05),pos_hint={'x':.4,'y':.3},background_color= (0,0.5,1,1))
        #variable to hold the ammount of money to be sold
        a_m=Label(text="profs: media fx",size_hint=(.3,.05),pos_hint={'x':.7,'y':.3},background_color= (0,0.5,1,1))

        l2=Label(text='salary: 900000ugx',size_hint=(.3,.05),pos_hint={'x':.4,'y':.4},background_color= (0,0.5,1,1))
        #variable to hold the currency
        ugx=Label(text="date:......",size_hint=(.3,.05),pos_hint={'x':.7,'y':.4},background_color= (0,0.5,1,1))

        l3=Label(text='phone:+256754562905 ',size_hint=(.3,.05),pos_hint={'x':.4,'y':.5},background_color= (0,0.5,1,1))
        #variable to hold the sellers name 
        user_id=Label(text="show : youth dev",size_hint=(.3,.05),pos_hint={'x':.7,'y':.5},background_color= (0,0.5,1,1))

        l4=Label(text='hobby: movies',size_hint=(.3,.05),pos_hint={'x':.4,'y':.6},background_color= (0,0.5,1,1))
        pin=Label(text="about: cedes inc",size_hint=(.3,.05),pos_hint={'x':.7,'y':.5},background_color= (0,0.5,1,1))
        
        b=Button(text='finish',size_hint=(.2,.05),pos_hint={'x':.8,'y':.6} ,background_color= (1,0,0,1))
        b.bold=True
        b.border=16,16,16,16
        b.background_color=0,1,1,1
        b.background_down=''
        b.background_down=''
        
        self.add_widget(code)
        self.add_widget(l1)
        self.add_widget(l2)
        self.add_widget(l3)
        self.add_widget(l4)
        self.add_widget(a_m)
        self.add_widget(ugx)
        self.add_widget(user_id)
        self.add_widget(pin)
        self.add_widget(b)
        

        
    def entertain(self):
        #tools for writing and editing the music 
        pin=Label(text="afro",size_hint=(.3,.05),pos_hint={'x':.4,'y':.5},background_color= (0,0.5,1,1))
        p=Label(text="rnb ",size_hint=(.3,.05),pos_hint={'x':.4,'y':.6},background_color= (0,0.5,1,1))
        b=Button(text='play',size_hint=(.2,.05),pos_hint={'x':.5,'y':.7},background_color= (0,0.5,1,1) )
        exi=Button(text='exit',size_hint=(.2,.05),pos_hint={'x':.5,'y':.7},background_color= (0,0.5,1,1) )
        self.add_widget(pin)
        self.add_widget(p)
        self.add_widget(b)
        
        
    def art_of_life(self):
        #overview of the general life 
        next1=Button(text='fabs',size_hint=(.2,.05),pos_hint={'x':.6,'y':.4} ,background_color= (0,0.5,1,1))
        self.add_widget(next1)
        nex=Button(text='race',size_hint=(.2,.05),pos_hint={'x':.6,'y':.2},background_color= (0,0.5,1,1) )
        self.add_widget(nex)
        time=Button(text='Time:{}'.format(time.asctime()),size_hint=(.2,.05),pos_hint={'x':.2,'y':.1} )
        self.add_widget(time)
        pass
    def movies(self):
        #adding clips to form back the movies like they were 
        pin=Label(text="adventure",size_hint=(.3,.05),pos_hint={'x':.4,'y':.5},background_color= (0,0.5,1,1))
        p=Label(text="horor ",size_hint=(.3,.05),pos_hint={'x':.4,'y':.6},background_color= (0,0.5,1,1))
        b=Button(text='play',size_hint=(.2,.05),pos_hint={'x':.5,'y':.7} ,background_color= (0,0.5,1,1))
        next1=Button(text='next',size_hint=(.2,.05),pos_hint={'x':.6,'y':.7} ,background_color= (0,0.5,1,1))
        prev=Button(text='play',size_hint=(.2,.05),pos_hint={'x':.7,'y':.7} ,background_color= (0,0.5,1,1))
        exi=Button(text='exit',size_hint=(.2,.05),pos_hint={'x':.5,'y':.7} ,background_color= (0,0.5,1,1))
        self.add_widget(pin)
        self.add_widget(p)
        self.add_widget(next1)
        self.add_widget(prev)
        self.add_widget(b)
        Inner().pop()

    def best_ranking(): 
        # employing quick alorithms tobe able to extract insight from the bigdata models ie recurent and reinforcement ann
        pass
    def exi(self):
        sys.exit()

    """
account holders 
# 
# 
# 
# 
# 
# """


class Account(Screen):
    account=ObjectProperty()
    
    def holder(self):
        
        
        code=Label(text='20,000ugx',size_hint=(.3,.05),pos_hint={'x':.4,'y':.2},background_color=(.5,0.5,1,1))
        
        
        l1=Label(text='october',size_hint=(.1,.1),pos_hint={'x':.8,'y':.18})
        self.add_widget(l1)
        #variable to hold the ammount of money to be sold
        a_m=TextInput(size_hint=(.3,.05),pos_hint={'x':.4,'y':.3})
        

        l2=Label(text='profile',size_hint=(.1,.1),pos_hint={'x':.8,'y':.28},background_color= (.5,0.5,1,1))
        #variable to hold the currency
        ugx=Label(text="credit",size_hint=(.3,.05),pos_hint={'x':.4,'y':.4},background_color= (.5,0.5,1,1))
        l3=Label(text='  location',size_hint=(.1,.1),pos_hint={'x':.8,'y':.38},background_color= (.5,0.5,1,1))
        #variable to hold the sellers name 
        user_id=Label(text="district",size_hint=(.3,.05),pos_hint={'x':.4,'y':.5},background_color= (.5,0.5,1,1))
        l4=Label(text='phone',size_hint=(.1,.1),pos_hint={'x':.8,'y':.48},background_color= (.5,0.5,1,1))

        but=Button(text='finish',size_hint=(.1,.05),pos_hint={'x':.4,'top':.08},background_color= (.5,0.5,1,1))
        b=Button(text='send',size_hint=(.1,.05),pos_hint={'x':.5,'top':.08} ,background_color= (.5,0.5,1,1))
        time=Button(text='Time:',size_hint=(.2,.05),pos_hint={'x':.2,'top':.08},background_color= (.5,0.5,1,1) )
        self.add_widget(time)
        self.add_widget(code)
        self.add_widget(l2)
        self.add_widget(l3)
        self.add_widget(l4)
        self.add_widget(a_m)
        self.add_widget(ugx)
        self.add_widget(user_id)
        self.add_widget(but)
        self.add_widget(b)
        



    """
    waiting ...
    
    """
    def wait(self):
        self.add_widget(Label(text='waiting..',size_hint=(.1,.1),pos_hint={'x':.8,'y':.48},background_color= (0,0.5,1,1)))
        return 


        """
        
        function to handle account records 
        """
    def records(self):
        
        l4=Label(text='record',size_hint=(1,.1),pos_hint={'x':.8,'y':.48},background_color= (0,0.5,1,1))
        self.add_widget(l4)
    """
    function to analyse the user status
    
    """
            
    def status(self):
        
        l4=Label(text='success',size_hint=(1,.1),pos_hint={'x':.8,'y':.48},background_color= (.5,0.5,1,1))
        self.add_widget(l4)
        time=Button(text='Time:{}'.format(time.asctime()),size_hint=(.2,.05),pos_hint={'x':.2,'y':.1},background_color= (.5,0.5,1,1) )
        self.add_widget(time)
    
    
    


"""
class games for handling the games ,
mision games 
vision games 
football 
double chances 

"""
class Games(Screen):
    
    def slider(self):
        return
    # this functions handles the english premier league 
    def epl(self):
        pass
    # this function handles all football leagues 
    def fb(self):
        x=True
        #x is true if allowed/subscribed and defualts to True for the first 20 days
        if x:
            import bet
            # the place for loading football games 
            bet.games
            bet.ball
            bet.epl
            bet.bundesliga
            bet.serie_a
            bet.laliga
        else:
            print("bet not import !!!")

class Tec(Screen):
    def exi(self):
        sys.exit()
    
    def capture(self):
        pass
        """
        l4=Label(text='shoot',size_hint=(1,.1),pos_hint={'x':.8,'top':.48})
        self.add_widget(l4)
        # code for writing the mage from either the camera or file and further editing
        cap=cv2.VideoCapture('x.mp4')
        fps=int(cap.get(cv2.CAP_PROP_FPS))
        width=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        x=cap.isOpened()
        
        p,v=cap.read()
    
        c=cv2.imwrite('elijah.jpg',v)



        a=1
        T=True
        while T:
            cv2.imshow('elijah',v)
            a+=1
            if a>20:
                T=False
        #cv2.addText(v,'elijah',(20,300),'')
        cv2.waitKey(20)
        """

    
    def auto(self):
        l4=Label(text='volkswag',size_hint=(.2,.1),pos_hint={'x':.2,'top':.48},background_color= (.2,0.5,1,1))
        l3=Label(text='mercedes',size_hint=(.2,.1),pos_hint={'x':.2,'top':.58},background_color= (.5,0.2,1,1))
        l2=Label(text='Bmw',size_hint=(.2,.1),pos_hint={'x':.2,'top':.68},background_color= (.5,0.5,0,1))
        l1=Label(text='porsche',size_hint=(.2,.1),pos_hint={'x':.2,'top':.78},background_color= (.5,0.5,1,1))
        but=Button(text='end',size_hint=(.2,.1),pos_hint={'x':.2,'top':.38},background_color= (.5,0.5,1,1))
        self.add_widget(l4)
        self.add_widget(l3)
        self.add_widget(l2)
        self.add_widget(l1)
        self.add_widget(but)
    def apps(self):
        l4=Label(text='web3',size_hint=(.2,.1),pos_hint={'x':.2,'top':.48},background_color= (.5,0.5,1,1))
        l3=Label(text='android',size_hint=(.2,.1),pos_hint={'x':.2,'top':.58},background_color=(.2,0,1,1))
        l2=Label(text='ios',size_hint=(.2,.1),pos_hint={'x':.2,'top':.68},background_color= (0,.4,1,1))
        l1=Label(text='window',size_hint=(.2,.1),pos_hint={'x':.2,'top':.78},background_color= (0.7,0,1,1))
        but=Button(text='end',size_hint=(.2,.1),pos_hint={'x':.2,'top':.38})
        other=Button(text='other',size_hint=(.2,.05),pos_hint={'x':.2,'y':.1},background_color= (0,.1,1,1) )
        # calling the auto function for cars 
        other.on_touch_up(self.auto)
        self.add_widget(time)
        self.add_widget(l4)
        self.add_widget(l3)
        self.add_widget(l2)
        self.add_widget(l1)
        self.add_widget(but)
   
    def prog(self):
        l4=Button(text='java',size_hint=(.2,.1),pos_hint={'x':.2,'top':.28},background_color= (0,0,1,1))
        l3=Button(text='cpp',size_hint=(.2,.1),pos_hint={'x':.2,'top':.38},background_color= (0,0,1,1))
        l2=Button(text='python',size_hint=(.2,.1),pos_hint={'x':.2,'top':.48},background_color= (0,.5,1,1))
        l1=Button(text='kotlin',size_hint=(.2,.1),pos_hint={'x':.2,'top':.58},background_color= (.2,0,1,1))
        l0=Button(text='swift',size_hint=(.2,.1),pos_hint={'x':.2,'top':.68},background_color= (.4,0,1,1))
        l=Button(text='kotlin',size_hint=(.2,.1),pos_hint={'x':.2,'top':.78},background_color= (0,0,1,1))
        l6=Button(text='exit',size_hint=(.2,.1),pos_hint={'x':.2,'top':.88},background_color= (.1,0,1,1))
        time=Button(text='Time:',size_hint=(.2,.05),pos_hint={'x':.2,'y':.1},background_color= (0,.4,1,1) )
        self.add_widget(time)
        self.add_widget(l4)
        self.add_widget(l3)
        self.add_widget(l2)
        self.add_widget(l1)
        self.add_widget(l0)
        self.add_widget(l)
        self.add_widget(l6)
        
    def sci(self):
        time=Button(text='Time:',size_hint=(.2,.05),pos_hint={'x':.2,'y':.1},background_color=(1,0,0,1))
        self.add_widget(time)
        l4=Button(text='food ',size_hint=(.2,.1),pos_hint={'x':.2,'top':.28},background_color= (0,0,1,1))
        l3=Button(text='ai',size_hint=(.2,.1),pos_hint={'x':.2,'top':.38},background_color= (0,0,1,1))
        l2=Button(text='edge',size_hint=(.2,.1),pos_hint={'x':.2,'top':.48},background_color= (0,0,1,1))
        l1=Button(text='social',size_hint=(.2,.1),pos_hint={'x':.2,'top':.58},background_color= (0,0,1,1))
        l6=Button(text='exit',size_hint=(.2,.1),pos_hint={'x':.2,'top':.18},background_color= (0,0,1,1))
        self.add_widget(l4)
        self.add_widget(l3)
        self.add_widget(l2)
        self.add_widget(l1)
        self.add_widget(l6)


class Skillo(Screen):

    def talent_show(self):
        self.add_widget(Label(text='accessible to premium users !!!',size_hint=(.4,.1),pos_hint={'x':.1,'top':.1},background_color= (0,0.5,1,1)))
    def editor(self):
        #changing  the font size of the words and alignment 
        
        
        next1=Button(text="talent TV",size_hint=(.2,.05),pos_hint={'x':.6,'y':.5} ,on_press=self.talent_show,background_color= (0,0.5,1,1))
        self.add_widget(next1)
        next2=Button(text="hide",size_hint=(.2,.05),pos_hint={'x':.6,'y':.4} ,background_color= (0,0.5,1,1))
        self.add_widget(next2)
        time=Button(text='Time',size_hint=(.2,.05),pos_hint={'x':.2,'y':.1} ,background_color= (0,0.5,1,1))
        self.add_widget(time)
        if next1.state=='down':
            pass
            


    
    def news(self):
        # the news anchors platform for the new delivery

        l=Label(text="News live",size_hint=(.4,.1),pos_hint={'x':.2,'y':.7},background_color= (0,0.5,1,1))
        next1=Button(text='next',size_hint=(.2,.05),pos_hint={'x':.2,'y':.6} ,background_color= (0,0.5,1,1))
        next2=Button(text='end',size_hint=(.2,.05),pos_hint={'x':.2,'y':.5} ,background_color= (0,0.5,1,1))
        premium=Button(text='premium ',size_hint=(.2,.05),pos_hint={'x':.8,'y':.1} ,background_color= (0,0.5,1,1))
        time=Button(text='Time:',size_hint=(.2,.05),pos_hint={'x':.2,'y':.1} ,background_color= (0,0.5,1,1))
        self.add_widget(time)
        self.add_widget(premium)
        
        self.add_widget(l)
        self.add_widget(next1)
        if next2.state=='down':
            pass

    """
    
    presenter function 


    """
    def presenter(self):
        l1=Label(text='currency',size_hint=(.3,.05),pos_hint={'x':.0,'y':.2},background_color= (0,0.5,1,1))
        code=TextInput(size_hint=(.3,.05),pos_hint={'x':.4,'y':.2})
        
        l1=Label(text='ammount',size_hint=(.3,.05),pos_hint={'x':.4,'y':.3},background_color= (0,0.5,1,1))
        #variable to hold the ammount of money to be sold
        a_m=TextInput(size_hint=(.3,.05),pos_hint={'x':.4,'y':.3})

        l2=Label(text='username ',size_hint=(.3,.05),pos_hint={'x':.4,'y':.4},background_color= (0,0.5,1,1))
        #variable to hold the currency
        ugx=TextInput(size_hint=(.3,.05),pos_hint={'x':.4,'y':.4})

        l3=Label(text='phone ',size_hint=(.3,.05),pos_hint={'x':.4,'y':.5},background_color= (0,0.5,1,1))
        #variable to hold the sellers name 
        user_id=TextInput(size_hint=(.3,.05),pos_hint={'x':.4,'y':.5})

        l4=Label(text='pin',size_hint=(.3,.05),pos_hint={'x':.4,'y':.6},background_color= (0,0.5,1,1))
        pin=TextInput(size_hint=(.3,.05),pos_hint={'x':.4,'y':.5})
        
        b=Button(text='finish',size_hint=(.2,.05),pos_hint={'x':.4,'y':.6} ,background_color= (0,0.5,1,1))
        

        self.add_widget(code)
        self.add_widget(l1)
        self.add_widget(l2)
        self.add_widget(l3)
        self.add_widget(l4)
        self.add_widget(a_m)
        self.add_widget(ugx)
        self.add_widget(user_id)
        self.add_widget(pin)
        self.add_widget(b)
        
        
        """
    function show
    
    
    """
    def show(self):
        l1=Label(text='name: Timo',size_hint=(.3,.05),pos_hint={'x':.0,'y':.2},background_color= (0,0.5,1,1))
        code=Label(text="age: 20",size_hint=(.3,.05),pos_hint={'x':.4,'y':.2})
        
        l1=Label(text='country:ug',size_hint=(.3,.05),pos_hint={'x':.4,'y':.3},background_color= (0,0.5,1,1))
        #variable to hold the ammount of money to be sold
        a_m=Label(text="profs: media fx",size_hint=(.3,.05),pos_hint={'x':.7,'y':.3},background_color= (0,0.5,1,1))

        l2=Label(text='salary: 900000ugx',size_hint=(.3,.05),pos_hint={'x':.4,'y':.4},background_color= (0,0.5,1,1))
        #variable to hold the currency
        ugx=Label(text="date:......",size_hint=(.3,.05),pos_hint={'x':.7,'y':.4},background_color= (0,0.5,1,1))

        l3=Label(text='phone:+256754562905',size_hint=(.3,.05),pos_hint={'x':.4,'y':.5},background_color= (0,0.5,1,1))
        #variable to hold the sellers name 
        user_id=Label(text="show : youth dev",size_hint=(.3,.05),pos_hint={'x':.7,'y':.5},background_color= (0,0.5,1,1))

        l4=Label(text='hobby: movies',size_hint=(.3,.05),pos_hint={'x':.4,'y':.6},background_color= (0,0.5,1,1))
        pin=Label(text="about: cedar ",size_hint=(.3,.05),pos_hint={'x':.7,'y':.45},background_color= (0,0.5,1,1))
        
        b=Button(text='finish',size_hint=(.2,.05),pos_hint={'x':.8,'y':.6},background_color= (.4,0.5,1,1) )
        
        self.add_widget(code)
        self.add_widget(l1)
        self.add_widget(l2)
        self.add_widget(l3)
        self.add_widget(l4)
        self.add_widget(a_m)
        self.add_widget(ugx)
        self.add_widget(user_id)
        self.add_widget(pin)
        self.add_widget(b)
        
    def mcm(self):
        pass
    def entertain(self):
        #tools for writing and editing the music 
        pin=Label(text="afro",size_hint=(.3,.05),pos_hint={'x':.4,'y':.5},background_color= (0,0.5,1,1))
        p=Label(text="rnb ",size_hint=(.3,.05),pos_hint={'x':.4,'y':.6},background_color= (0,0.5,1,1))
        b=Button(text='play',size_hint=(.2,.05),pos_hint={'x':.5,'y':.7},on_press=self.talent_show,background_color= (0,0.5,1,1) )
        exi=Button(text='exit',size_hint=(.2,.05),pos_hint={'x':.5,'y':.7},background_color= (.4,0.5,1,1) )
        self.add_widget(pin)
        self.add_widget(p)
        self.add_widget(b)
        
        
        
    def art_of_life(self):
        # overview of the general life 
        next1=Button(text='fabs',size_hint=(.2,.05),pos_hint={'x':.6,'y':.4} ,background_color= (0,0.5,1,1))
        self.add_widget(next1)
        nex=Button(text='fansay',size_hint=(.2,.05),pos_hint={'x':.6,'y':.2} ,background_color= (0,0.5,1,1))
        self.add_widget(nex)

        pass
    def movies(self):
        #adding clips to form back the movies like they were 
        pin=Button(text="adventure",size_hint=(.3,.05),pos_hint={'x':.7,'y':.7},background_color= (0,0.5,1,1))
        p=Button(text="horor ",size_hint=(.3,.05),pos_hint={'x':.7,'y':.6},background_color= (0,0.5,1,1))
        b=Button(text='scifi',size_hint=(.2,.05),pos_hint={'x':.7,'y':.5} ,background_color= (0,0.5,1,1))
        next1=Button(text='next',size_hint=(.2,.05),pos_hint={'x':.7,'y':.4} ,background_color= (0,0.5,1,1))
        prev=Button(text='play',size_hint=(.2,.05),pos_hint={'x':.7,'y':.3},on_press=self.talent_show ,background_color= (0,0.5,1,1))
        exi=Button(text='exit',size_hint=(.2,.05),pos_hint={'x':.7,'y':.2},background_color= (1,0.5,1,1) )
        self.add_widget(pin)
        self.add_widget(p)
        self.add_widget(next1)
        self.add_widget(prev)
        self.add_widget(b)

        if prev.state=='down':
            
            self.add_widget(Label(text="horor ",size_hint=(.3,.05),pos_hint={'x':.2,'y':.6}))
            self.remove_widget(Label(text="horor ",size_hint=(.3,.05),pos_hint={'x':.2,'y':.6}))
        if exi.state=='down':
            pass
        
    def best_ranking():
        # employing quick alorithms tobe able to extract insight from the bigdata models ie recurent and reinforcement ann
        pass




class Cedar(Screen):

    def admin(self):
        l=Label(text="Ceo",size_hint=(.2,.2),pos_hint={'x':.8,'y':.58},background_color= (0,0.5,1,1))
        self.add_widget(l)
        return 
    def news(self):
        l=Label(text="live news",size_hint=(.2,.1),pos_hint={'x':.1,'y':.58},background_color= (0,0.5,1,1))
        self.add_widget(l)

    def admin(self):
        #changing  the font size of the words and alignment 
        
        while self.green:
            next1=Button(text="Ceo",size_hint=(.2,.05),pos_hint={'x':.5,'y':.8},background_color= (0,0.5,1,1))
            self.add_widget(next1)

            video=Video(state="play",source='',size_hint=(.6,.4),pos_hint={'x':.4,'y':.2},background_color=(0,.5,0,1))
            self.add_widget(video)
            nex=Button(text="company",size_hint=(.2,.05),pos_hint={'x':.9,'y':.1} ,background_color= (1,0.5,1,1))
            self.add_widget(nex)
            self.add_widget(video)
            #self.remove_widget(next1)
            


    
    def manager(self):
        # the news anchors platform for the new delivery

        l=Label(text="manager",size_hint=(.4,.1),pos_hint={'x':.0,'y':.2},background_color= (0,0.5,1,1))
        next1=Button(text='next',size_hint=(.2,.05),pos_hint={'x':.6,'y':.7},background_color= (0,0.5,1,1) )
        self.add_widget(l)
        self.add_widget(next1)
        if next1.state=='down':
            self.remove_widget(next1)
            self.add_widget(l)
    """
    
    presenter function 


    """
    def financier(self):
        l1=Label(text='currency',size_hint=(.3,.05),pos_hint={'x':.0,'y':.2},background_color= (0,0.5,1,1))
        code=TextInput(size_hint=(.3,.05),pos_hint={'x':.4,'y':.2})
        
        l1=Label(text='ammount',size_hint=(.3,.05),pos_hint={'x':.4,'y':.3},background_color= (0,0.5,1,1))
        #variable to hold the ammount of money to be sold
        a_m=TextInput(size_hint=(.3,.05),pos_hint={'x':.4,'y':.3})

        l2=Label(text='username ',size_hint=(.3,.05),pos_hint={'x':.4,'y':.4},background_color= (0,0.5,1,1))
        #variable to hold the currency
        ugx=TextInput(size_hint=(.3,.05),pos_hint={'x':.4,'y':.4})

        l3=Label(text='phone ',size_hint=(.3,.05),pos_hint={'x':.4,'y':.5},background_color= (0,0.5,1,1))
        #variable to hold the sellers name 
        user_id=TextInput(size_hint=(.3,.05),pos_hint={'x':.4,'y':.5})

        l4=Label(text='pin',size_hint=(.3,.05),pos_hint={'x':.4,'y':.6},background_color= (0,0.5,1,1))
        pin=TextInput(size_hint=(.3,.05),pos_hint={'x':.4,'y':.5})
        
        b=Button(text='finish',size_hint=(.2,.05),pos_hint={'x':.5,'y':.6} ,background_color= (1,0.5,1,1))
        
    
        self.add_widget(code)
        self.add_widget(l1)
        self.add_widget(l2)
        self.add_widget(l3)
        self.add_widget(l4)
        self.add_widget(a_m)
        self.add_widget(ugx)
        self.add_widget(user_id)
        self.add_widget(pin)
        self.add_widget(b)
        # the news anchors platform for the new delivery
        pass
    
        
        """
    function show
    
    
    """
    def show(self):
        l1=Label(text='name: Timo',size_hint=(.3,.05),pos_hint={'x':.0,'y':.2},background_color= (0,0.5,1,1))
        code=Label(text="age: 20",size_hint=(.3,.05),pos_hint={'x':.4,'y':.2},background_color= (0,0.5,1,1))
        
        l1=Label(text='country:ug',size_hint=(.3,.05),pos_hint={'x':.4,'y':.3},background_color= (0,0.5,1,1))
        #variable to hold the ammount of money to be sold
        a_m=Label(text="profs: media fx",size_hint=(.3,.05),pos_hint={'x':.7,'y':.3},background_color= (0,0.5,1,1))

        l2=Label(text='salary: 900000ugx',size_hint=(.3,.05),pos_hint={'x':.4,'y':.4},background_color= (0,0.5,1,1))
        #variable to hold the currency
        ugx=Label(text="date:.07/2024",size_hint=(.3,.05),pos_hint={'x':.7,'y':.4},background_color= (0,0.5,1,1))

        l3=Label(text='phone:+256754562905 ',size_hint=(.3,.05),pos_hint={'x':.4,'y':.5},background_color= (0,0.5,1,1))
        #variable to hold the sellers name 
        user_id=Label(text="show : youth dev",size_hint=(.3,.05),pos_hint={'x':.7,'y':.5},background_color= (0,0.5,1,1))

        l4=Label(text='hobby: movies',size_hint=(.3,.05),pos_hint={'x':.4,'y':.6},background_color= (0,0.5,1,1))
        pin=Label(text="about: xxxx",size_hint=(.3,.05),pos_hint={'x':.7,'y':.5},background_color= (0,0.5,1,1))
        b=Button(text='finish',size_hint=(.2,.05),pos_hint={'x':.8,'y':.6} ,background_color= (0,0.5,1,1))
        
        self.add_widget(code)
        self.add_widget(l1)
        self.add_widget(l2)
        self.add_widget(l3)
        self.add_widget(l4)
        self.add_widget(a_m)
        self.add_widget(ugx)
        self.add_widget(user_id)
        self.add_widget(pin)
        self.add_widget(b)



    def tronics(self):
        code=TextInput(size_hint=(.3,.05),pos_hint={'x':.4,'y':.2})
        
        l1=Label(text='photons',size_hint=(.1,.1),pos_hint={'x':.8,'y':.18},background_color= (0,0.5,1,1))
        #variable to hold the ammount of money to be sold
        a_m=TextInput(size_hint=(.3,.05),pos_hint={'x':.4,'y':.3})
        l2=Label(text='trans',size_hint=(.1,.1),pos_hint={'x':.8,'y':.28},background_color= (0,0.5,1,1))
        #variable to hold the currency
        ugx=TextInput(size_hint=(.3,.05),pos_hint={'x':.4,'y':.4})
        l3=Label(text='dio ',size_hint=(.1,.1),pos_hint={'x':.8,'y':.38},background_color= (0,0.5,1,1))
        #variable to hold the sellers name 
        user_id=TextInput(size_hint=(.3,.05),pos_hint={'x':.4,'y':.5})
        l4=Label(text='serials',size_hint=(.1,.1),pos_hint={'x':.8,'y':.48},background_color= (0,0.5,1,1))

        but=Button(text='send',size_hint=(.1,.05),pos_hint={'x':.4,'y':.08},background_color= (0,0.5,1,1))

        
        self.add_widget(code)
        self.add_widget(l1)
        self.add_widget(l2)
        self.add_widget(l3)
        self.add_widget(l4)
        self.add_widget(a_m)
        self.add_widget(ugx)
        self.add_widget(user_id)
        self.add_widget(but)

    def reality(self):
        code=TextInput(size_hint=(.3,.05),pos_hint={'x':.4,'y':.2})
        text=code._get_text()
        print(text,'inside cedar class in reality function')
        l1=Label(text='VR',size_hint=(.1,.1),pos_hint={'x':.8,'y':.18},background_color= (0,0.5,1,1))
        #variable to hold the ammount of money to be sold
        a_m=TextInput(size_hint=(.3,.05),pos_hint={'x':.4,'y':.3})
        l2=Label(text='AR',size_hint=(.1,.1),pos_hint={'x':.8,'y':.28},background_color= (0,0.5,1,1))
        #variable to hold the currency
        ugx=TextInput(size_hint=(.3,.05),pos_hint={'x':.4,'y':.4})
        l3=Label(text='Euler ',size_hint=(.1,.1),pos_hint={'x':.8,'y':.38},background_color= (0,0.5,1,1))
        #variable to hold the sellers name 
        user_id=TextInput(size_hint=(.3,.05),pos_hint={'x':.4,'y':.5})
        l4=Label(text='serial',size_hint=(.1,.1),pos_hint={'x':.8,'y':.48},background_color= (0,0.5,1,1))

        but=Button(text='send',size_hint=(.1,.05),pos_hint={'x':.4,'y':.08},background_color= (0,0.5,1,1))

        
        self.add_widget(code)
        self.add_widget(l1)
        self.add_widget(l2)
        self.add_widget(l3)
        self.add_widget(l4)
        self.add_widget(a_m)
        self.add_widget(ugx)
        self.add_widget(user_id)
        self.add_widget(but)
    def cyber(self):
        code=TextInput(size_hint=(.3,.05),pos_hint={'x':.4,'y':.2})
        
        l1=Label(text='crsf',size_hint=(.2,.1),pos_hint={'x':.8,'y':.18},background_color= (0,0.5,1,1))
        #variable to hold the ammount of money to be sold
        a_m=TextInput(size_hint=(.3,.05),pos_hint={'x':.4,'y':.3})
        l2=Label(text='bforce',size_hint=(.2,.1),pos_hint={'x':.8,'y':.28},background_color= (0,0.5,1,1))
        #variable to hold the currency
        ugx=TextInput(size_hint=(.3,.05),pos_hint={'x':.4,'y':.4})
        l3=Label(text='phish ',size_hint=(.2,.1),pos_hint={'x':.8,'y':.38},background_color= (0,0.5,1,1))
        #variable to hold the sellers name 
        user_id=TextInput(size_hint=(.3,.05),pos_hint={'x':.4,'y':.5})
        l4=Label(text='crack',size_hint=(.2,.1),pos_hint={'x':.8,'y':.48},background_color= (0,0.5,1,1))

        but=Button(text='send',size_hint=(.2,.05),pos_hint={'x':.4,'y':.08},background_color= (0,0.5,1,1))

        
        self.add_widget(code)
        self.add_widget(l1)
        self.add_widget(l2)
        self.add_widget(l3)
        self.add_widget(l4)
        self.add_widget(a_m)
        self.add_widget(ugx)
        self.add_widget(user_id)
        self.add_widget(but)
    def ai(self):
        code=TextInput(size_hint=(.3,.05),pos_hint={'x':.4,'y':.2})
        
        l1=Label(text='model',size_hint=(.2,.1),pos_hint={'x':.8,'y':.18},background_color= (0,0.5,1,1))
        #variable to hold the ammount of money to be sold
        a_m=TextInput(size_hint=(.3,.05),pos_hint={'x':.4,'y':.3})
        l2=Label(text='data',size_hint=(.2,.1),pos_hint={'x':.8,'y':.28},background_color= (0,0.5,1,1))
        #variable to hold the currency
        ugx=TextInput(size_hint=(.3,.05),pos_hint={'x':.4,'y':.4})
        l3=Label(text='duo ',size_hint=(.2,.1),pos_hint={'x':.8,'y':.38},background_color= (0,0.5,1,1))
        #variable to hold the sellers name 
        user_id=TextInput(size_hint=(.3,.05),pos_hint={'x':.4,'y':.5})
        l4=Label(text='serial',size_hint=(.2,.1),pos_hint={'x':.8,'y':.48},background_color= (0,0.5,1,1))

        but=Button(text='send',size_hint=(.1,.05),pos_hint={'x':.4,'y':.08},background_color= (0,0.5,1,1))

        
        self.add_widget(code)
        self.add_widget(l1)
        self.add_widget(l2)
        self.add_widget(l3)
        self.add_widget(l4)
        self.add_widget(a_m)
        self.add_widget(ugx)
        self.add_widget(user_id)
        self.add_widget(but)
    def cloud(self):
        pass

    def blockchain(self):
        code=TextInput(size_hint=(.3,.05),pos_hint={'x':.4,'y':.2})
        
        l1=Label(text='ledger',size_hint=(.2,.1),pos_hint={'x':.8,'y':.18},background_color= (0,0.5,1,1))
        #variable to hold the ammount of money to be sold
        a_m=TextInput(size_hint=(.3,.05),pos_hint={'x':.4,'y':.3})
        l2=Label(text='node',size_hint=(.2,.1),pos_hint={'x':.8,'y':.28},background_color= (0,0.5,1,1))
        #variable to hold the currency
        ugx=TextInput(size_hint=(.3,.05),pos_hint={'x':.4,'y':.4})
        l3=Label(text='duo ',size_hint=(.2,.1),pos_hint={'x':.8,'y':.38},background_color= (0,0.5,1,1))
        #variable to hold the sellers name 
        user_id=TextInput(size_hint=(.3,.05),pos_hint={'x':.4,'y':.5})
        l4=Label(text='serial',size_hint=(.2,.1),pos_hint={'x':.8,'y':.48},background_color= (0,0.5,1,1))

        but=Button(text='send',size_hint=(.2,.05),pos_hint={'x':.4,'y':.08},background_color= (0,0.5,1,1))

        
        self.add_widget(code)
        self.add_widget(l1)
        self.add_widget(l2)
        self.add_widget(l3)
        self.add_widget(l4)
        self.add_widget(a_m)
        self.add_widget(ugx)
        self.add_widget(user_id)
        self.add_widget(but)

    class c:
        a=10
        def m(self):
            self.m


    def entertain(self):
        #tools for writing and editing the music 
        pin=Label(text="afro",size_hint=(.3,.05),pos_hint={'x':.4,'y':.5},background_color= (0,0.5,1,1))
        p=Label(text="rnb ",size_hint=(.3,.05),pos_hint={'x':.4,'y':.6},background_color= (0,0.5,1,1))
        b=Button(text='play',size_hint=(.2,.05),pos_hint={'x':.5,'y':.7},background_color= (0,0.5,1,1) )
        exi=Button(text='exit',size_hint=(.2,.05),pos_hint={'x':.5,'y':.7},background_color= (0,0.5,1,1) )
        self.add_widget(pin)
        self.add_widget(p)
        self.add_widget(b)
        
        if exi.state=='down':
            self.remove_widget(pin)
            self.remove_widget(p)
            self.remove_widget(b)
            self.remove_widget(exi)

    
    def art_of_life(self):
        # overview of the general life 
        next1=Button(text='fabs',size_hint=(.2,.05),pos_hint={'x':.6,'y':.4} ,background_color= (0,0.5,1,1))
        self.add_widget(next1)
        nex=Button(text='fansay',size_hint=(.2,.05),pos_hint={'x':.6,'y':.2} ,background_color= (0,0.5,1,1))
        self.add_widget(nex)

        pass
    def movies(self):
        print("watching movies ")
        #adding clips to form back the movies like they were 
        pin=Label(text="adventure",size_hint=(.3,.05),pos_hint={'x':.4,'y':.5},background_color= (0,0.5,1,1))
        p=Label(text="horor ",size_hint=(.3,.05),pos_hint={'x':.4,'y':.6},background_color= (0,0.5,1,1))
        b=Button(text='play',size_hint=(.2,.05),pos_hint={'x':.5,'y':.7} ,background_color= (0,0.5,1,1))
        next1=Button(text='next',size_hint=(.2,.05),pos_hint={'x':.6,'y':.7},background_color= (0,0.5,1,1) )
        prev=Button(text='start',size_hint=(.2,.05),pos_hint={'x':.7,'y':.7},background_color= (0,0.5,1,1) )
        exi=Button(text='exit',size_hint=(.2,.05),pos_hint={'x':.5,'y':.7},background_color= (0,0.5,1,1) )
        self.add_widget(pin)
        self.add_widget(p)
        self.add_widget(next1)
        self.add_widget(prev)
        self.add_widget(b)

        if exi.state=='down':
            self.remove_widget(pin)
            self.remove_widget(p)
            self.remove_widget(b)
            self.remove_widget(next1)
            self.remove_widget(prev)
            self.remove_widget(exi)
        
    def best_ranking():
        # employing quick alorithms tobe able to extract insight from the bigdata models ie recurent and reinforcement ann
        pass


    def jobs():
        pass
    def xit():
        sys.exit()

"""
the screenmanager class instatation object 

"""
# screenmanager variable
sm=ScreenManager()
print("screen manager")

sm.add_widget(Ishop(name="ishops"))
sm.add_widget(Ads(name="ads"))
sm.add_widget(Invest(name="invest"))
sm.add_widget(Account(name="account"))
sm.add_widget(Forex(name="forex"))
sm.add_widget(Media(name="imedia"))
sm.add_widget(Savings(name="savings"))
sm.add_widget(Credit(name="credit"))
sm.add_widget(Login(name="login"))
sm.add_widget(Games(name="games"))
sm.add_widget(Tec(name="tec"))
sm.add_widget(Skillo(name="skillo"))
#sm.add_widget(Cedar(name="cedar"))



"""
the application main loop

"""

class MainApp(App):


    def build(self):
        self.title='micronet '
        self.icon='icon.png'
        self.presplash='presplash.png'
    
        return sm

    
"""

checking if the name is equal to main
"""
if __name__=='__main__':
    e=MainApp()
    
    e.run()