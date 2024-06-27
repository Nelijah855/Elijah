


#Config.set("kivy", "keyboard_layout", 'qwerty')


"""
libraries reqiured 

mysql.connector,plyer, ffpyplayer,mtnmomo

"""
#project class [][][][]
from gui import Inner
#from login import Login
#import client
#import server
#m mtn import Mtn
from network import Client,Server
#from message import Message
#from online_box import Online
#from account import Account
#from security import Loophole,Blockchain,Phisphing,Crsf,Crypto
#project class [][][][]

from kivy.properties import NumericProperty


import kivy
import mysql.connector 
kivy.require('2.0.0')
import time
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
from kivy.uix.videoplayer import VideoPlayer
#from plyer import notification

import os
from kivy.graphics import Rectangle,Color
import sys
import sqlite3
#from kivy.uix.widget import Widget

from kivy.core.audio import SoundLoader


import os
import sys


images=['']

print("import done")



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


#sql=Sqlite("")

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
        print(" #comment section")
    def logout(self):
        self.ids.logout.text='out'
        time.sleep(3)
    def check():
        Inner().check()  
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
        print('searching.....................')
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
        code.border(16,16,16,16)
        a_m.border(16,16,16,16)
        user_id.border(16,16,16,16)
        finish.border(16,16,16,16)
        
        self.add_widget(finish)
        self.add_widget(code)
        self.add_widget(a_m)
        self.add_widget(ugx)
        self.add_widget(user_id)
    """
    video function
    """
    def video(self):
        vid=Video(source='',preview='icon.png',state='play',options={'eos':'loop'},pos_hint={'x':.7,'y':.5})
        self.add_widget(vid)

        
    def pay(self):
        a_m=TextInput(text="code ...",size_hint=(.2,.05),pos_hint={'x':.1,'y':.3},color=(0,1,0,1),background_color=(0,1,0,1))
        #variable to hold the currency
        ugx=TextInput(text="money ...",size_hint=(.2,.05),pos_hint={'x':.1,'y':.4},color=(0,1,0,1),background_color=(0,1,0,1))
        #variable to hold the sellers name 
        user_id=TextInput( text="user_id", size_hint=(.2,.05),pos_hint={'x':.1,'y':.5},color=(0,1,0,1),background_color=(0,1,0,1))
        self.add_widget(a_m)
        self.add_widget(ugx)
        self.add_widget(user_id)
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
        sound=SoundLoader.load('')
        self.add_widget(sound)
        if True:
            sound.play()
    
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
    def buy(self,*args):
        # varaible to hld the passcode for the user 
        code=TextInput(text="shopcode ...",size_hint=(.2,.05),pos_hint={'x':.7,'y':.5},background_color=(0,1,1,1))
        #variable to hold the ammount of money to be bought on 
        a_m=TextInput(text="name...",size_hint=(.2,.05),pos_hint={'x':.7,'y':.4},background_color=(0,1,1,1))
        #variable to hold the currency
        ugx=TextInput(text="money ...",size_hint=(.2,.05),pos_hint={'x':.7,'y':.3},background_color=(0,1,1,1))
        #variable to hold the buyers name 
        user_id=TextInput( text="user_id", size_hint=(.2,.05),pos_hint={'x':.7,'y':.2},background_color=(0,1,1,1))
        finish=Button( text="finish", size_hint=(.2,.05),pos_hint={'x':.7,'y':.1},background_color=(0,1,1,1),on_press=self.clear_w)
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
    def update(self):
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
        vid=Video(source='',preview='icon.png',state='play',options={'eos':'loop'},size_hint=(.2,.05),pos_hint={'x':.3,'top':.2})
        self.add_widget(vid)
        
    


    def sound(self):
        sound=SoundLoader.load('x.mp3')
        
        if True:
            sound.play()

    def send(self):
        return 'sent'
    def prev(self):
        self.display="loading video......."
        label=Label(text='<=',size_hint=(.2,.05),pos_hint={'x':.1,'top':.2})
        self.add_widget(label)
        self.manager.current='ishps'


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
    def nex(self):
        self.index +=1
        self.index %=len(images)
        self.image=images[self.index]
                
        
    def sell(self):
         # varaible to hld the passcode for the user 
        code=TextInput(size_hint=(.2,.05),pos_hint={'x':.6,'y':.2})
        
        l1=Label(text='usercode ',size_hint=(.1,.1),pos_hint={'x':1,'y':.4})
        #variable to hold the ammount of money to be sold
        a_m=TextInput(size_hint=(.2,.05),pos_hint={'x':.6,'y':.3})
        l2=Label(text='name ',size_hint=(.2,.1),pos_hint={'x':1,'y':.3})
        #variable to hold the currency
        ugx=TextInput(size_hint=(.2,.05),pos_hint={'x':.6,'y':.4})
        l3=Label(text='trust ',size_hint=(.2,.1),pos_hint={'x':1,'y':.2})
        #variable to hold the sellers name 
        user_id=TextInput(size_hint=(.2,.05),pos_hint={'x':.6,'y':.5})
        l4=Label(text='number',size_hint=(.2,.1),pos_hint={'x':1,'y':.1})

        but=Button(text='send',size_hint=(.2,.1),pos_hint={'x':.8,'y':.0})

        
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
            self.manager.current='ads'
        
    def pay(self):
        pass
    def shares(self):
        code=TextInput(size_hint=(.2,.05),pos_hint={'x':.6,'y':.2})
        
        l1=Label(text='usercode ',size_hint=(.1,.1),pos_hint={'x':1,'y':.4})
        #variable to hold the ammount of money to be sold
        a_m=TextInput(size_hint=(.2,.05),pos_hint={'x':.6,'y':.3})
        l2=Label(text='name ',size_hint=(.2,.1),pos_hint={'x':1,'y':.3})
        but=Button(text='send',size_hint=(.2,.1),pos_hint={'x':.8,'y':.0})
        self.add_widget(code)
        self.add_widget(l1)
        self.add_widget(a_m)
        self.add_widget(l2)
        self.add_widget(but)
        if but.state=='down':
            self.manager.current='forex'

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
    def buy(self,*args):
        # varaible to hld the passcode for the user 
        code=TextInput(size_hint=(.3,.05),pos_hint={'x':.4,'y':.2})
        
        l1=Label(text='usercode ',size_hint=(.1,.1),pos_hint={'x':.8,'y':.18})
        #variable to hold the ammount of money to be sold
        a_m=TextInput(size_hint=(.3,.05),pos_hint={'x':.4,'y':.3})
        l2=Label(text='name ',size_hint=(.1,.1),pos_hint={'x':.8,'y':.28})
        #variable to hold the currency
        ugx=TextInput(size_hint=(.3,.05),pos_hint={'x':.4,'y':.4})
        l3=Label(text='trust ',size_hint=(.1,.1),pos_hint={'x':.8,'y':.38})
        #variable to hold the sellers name 
        user_id=TextInput(size_hint=(.3,.05),pos_hint={'x':.4,'y':.5})
        l4=Label(text='number',size_hint=(.1,.1),pos_hint={'x':.8,'y':.48})

        but=Button(text='send',size_hint=(.1,.05),pos_hint={'x':.4,'y':.08})

        
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
        self.manager.current='skillo'
    def prev(self):

        self.index +=1
        self.index %=len(images)
        self.image=images[self.index]
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
    def update(self):
        
        self.manager.current='ads'
    

    def cart(self):
        label=Label(text='items',size_hint=(.2,.2),pos_hint={'x':.1,'top':.2})
        self.add_widget(label)
    
    def cafe(self):
        l1=Label(text='ammount',size_hint=(.3,.05),pos_hint={'x':.4,'y':.3})
        #variable to hold the ammount of money to be sold
        a_m=TextInput(size_hint=(.3,.05),pos_hint={'x':.4,'y':.3})
        a_m=Button(text="complete",size_hint=(.3,.05),pos_hint={'x':.4,'y':.3})
        self.add_widget(l1)
        self.add_widget(a_m)
        if a_m.on_press==True:
            self.remove_widget(l1)
            self.remove_widget(a_m)
        return 

    def chat(self):
        
        Client.connect()
        var='connecting..'

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
        image=Image(source='icon.png',size_hint=(.2,.2),pos_hint={'x':.1,'top':.2})
        self.add_widget(image)




"""
class for handling the   forex bereau 

"""


class Forex(Screen):


    # variable to hold the info the display variables '

   
    
    def loop(self):
        for i in range(100000):
            loop=i+1

            #variable to control the screen
            self.manager.current=''
            
    
    def is_broker(self):
        #varaible to hold goods sold aday
        d_sales=0
        if (d_sales/30)>=50000:
            return True
        else:
            return False

           
    
        
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
            finish=Button(text="paid with airtel...",size_hint=(.2,.1),pos_hint={'x':.5,'y':.2})
            self.add_widget(finish)
            pass 
    def airtel(self):
        finish=Button(text="paid with airtel...",size_hint=(.2,.1),pos_hint={'x':.5,'y':.2})
        self.add_widget(finish)
    def buy(self):
        # varaible to hld the passcode for the user 
        code=TextInput(text="shopcode ...",size_hint=(.2,.1),pos_hint={'x':.1,'y':.2})
        #variable to hold the ammount of money to be bought on 
        a_m=TextInput(text="name...",size_hint=(.2,.1),pos_hint={'x':.3,'y':.2})
        #variable to hold the currency
        ugx=TextInput(text="money ...",size_hint=(.2,.1),pos_hint={'x':.5,'y':.2})
        #variable to hold the buyers name 
        user_id=TextInput( text="user_id", size_hint=(.2,.1),pos_hint={'x':.7,'y':.2})
        finish=Button(text="finish...",size_hint=(.2,.1),pos_hint={'x':.5,'y':.2})
        self.add_widget(finish)
        self.add_widget(code)
        self.add_widget(a_m)
        self.add_widget(ugx)
        self.add_widget(user_id)


    def tools(self):
        cod=Label(text="premium [(4) ->paid only]",size_hint=(.2,.1),pos_hint={'x':.5,'y':1})
        # varaible to hld the passcode for the user 
        code=Button(text="graphs",size_hint=(.2,.1),pos_hint={'x':.1,'y':.2})
        #variable to hold the ammount of money to be bought on 
        a_m=Button(text="lines",size_hint=(.2,.1),pos_hint={'x':.3,'y':.2})
        #variable to hold the currency
        ugx=Button(text="indexers",size_hint=(.2,.1),pos_hint={'x':.5,'y':.2})
        #variable to hold the buyers name 
        user_id=Button( text="Ai", size_hint=(.2,.1),pos_hint={'x':.7,'y':.2})
        finish=Button(text="finish...",size_hint=(.2,.1),pos_hint={'x':.5,'y':.2})
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
    
    def forex(self):
        inr=Inner()
        inr.forex()
        return 
    def exc(self):
        pass
    def rates(self):
        label=Label(text='0.05%',size_hint=(.2,.2),pos_hint={'x':.1,'top':.2})
        self.add_widget(label)
    def futures(self):
        l1=Label(text='currency',size_hint=(.3,.05),pos_hint={'x':.0,'y':.2})
        code=TextInput(size_hint=(.3,.05),pos_hint={'x':.4,'y':.2})
        
        l1=Label(text='ammount',size_hint=(.3,.05),pos_hint={'x':.4,'y':.3})
        #variable to hold the ammount of money to be sold
        a_m=TextInput(size_hint=(.3,.05),pos_hint={'x':.4,'y':.3})

        l2=Label(text='username ',size_hint=(.3,.05),pos_hint={'x':.4,'y':.4})
        #variable to hold the currency
        ugx=TextInput(size_hint=(.3,.05),pos_hint={'x':.4,'y':.4})

        l3=Label(text='phone ',size_hint=(.3,.05),pos_hint={'x':.4,'y':.5})
        #variable to hold the sellers name 
        user_id=TextInput(size_hint=(.3,.05),pos_hint={'x':.4,'y':.5})

        l4=Label(text='pin',size_hint=(.3,.05),pos_hint={'x':.4,'y':.6})
        pin=TextInput(size_hint=(.3,.05),pos_hint={'x':.4,'y':.5})
        
        b=Button(text='finish',size_hint=(.2,.05),pos_hint={'x':.5,'y':.6} )
        clear=Button(text='clear',size_hint=(.2,.05),pos_hint={'x':.5,'y':.6} )
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

        time.sleep(60)
        self.remove_widget(code)
        self.remove_widget(l1)
        self.remove_widget(l2)
        self.remove_widget(l3)
        self.remove_widget(l4)
        self.remove_widget(a_m)
        self.remove_widget(ugx)
        self.remove_widget(user_id)
        self.remove_widget(pin)
        self.remove_widget(b)




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
        self.username=self.ids.username.text
        self.password=self.ids.password.text
         
    def log(self):
        l=Label(text='logined in ',size_hint=(.2,.8),pos_hint={'x':5,'top':.2})
        self.add_widget(l)
        time.sleep(10)
        self.manager.current='ishops'
            

        
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
        code=TextInput(text="code ...",size_hint=(.2,.05),pos_hint={'x':.3,'y':.2})
        #variable to hold the ammount of money to be saved 
        a_m=TextInput(text="code ...",size_hint=(.2,.05),pos_hint={'x':.3,'y':.3})
        #variable to hold the currency
        ugx=TextInput(text="money ...",size_hint=(.2,.05),pos_hint={'x':.3,'y':.4})
        #variable to hold the savers name 
        user_id=TextInput( text="user_id", size_hint=(.2,.05),pos_hint={'x':.3,'y':.5})
        btn=Button(text="credit",pos_hint={'x':.3,'top':.1},size_hint=(.2,.2),color=[0,1,0,1])
        self.add_widget(code)
        self.add_widget(a_m)
        self.add_widget(ugx)
        self.add_widget(user_id)
        self.add_widget(btn)
    # the function to carry out crediting the user 
    def credited(self):
        with open('credit.txt' ,'w') as file:
            file.write("credited with an ammount of 10000000ugx...")
            file.close()
    # where cr stands for credit 
    def cr_track(self):
        pass
    def insurance(self):
        code=TextInput(text="policy ...",size_hint=(.2,.05),pos_hint={'x':.3,'y':.2})
        #variable to hold the ammount of money to be saved 
        a_m=TextInput(text="premium ...",size_hint=(.2,.05),pos_hint={'x':.3,'y':.3})
        #variable to hold the currency
        ugx=TextInput(text="target ...",size_hint=(.2,.05),pos_hint={'x':.3,'y':.4})
        #variable to hold the savers name 
        user_id=TextInput( text="username", size_hint=(.2,.05),pos_hint={'x':.3,'y':.5})
        btn=Button(text="length",pos_hint={'x':.3,'top':.1},size_hint=(.2,.2),color=[0,1,0,1])
        self.add_widget(code)
        self.add_widget(a_m)
        self.add_widget(ugx)
        self.add_widget(user_id)
        self.add_widget(btn)

    def loan(self):
        pass
    
    def eligable(self):
        pass
    def enter(self):
        a=Inner()
        a.forex()


"""
class to handle the savings account

"""


class Savings(Screen):
    def save(self):
        code=TextInput(text="code ...",size_hint=(.2,.05),pos_hint={'x':.2,'y':.2})
        money=TextInput(text="money ...",size_hint=(.2,.05),pos_hint={'x':.2,'y':.3})
        receiver=TextInput( text="reciever_id", size_hint=(.2,.05),pos_hint={'x':.2,'y':.4})
        btn=Button(text="Save ",pos_hint={'x':.2,'top':.1},size_hint=(.2,.05),color=[0,1,0,1])
        #receiver.border(16,16,16,16)
        #money.border(16,16,16,16)
        #btn.border(16,16,16,16)
        #code.border(16,16,16,16)
        btn.bold=True
        btn.font_size=20
        self.add_widget(code)
        self.add_widget(btn)
        self.add_widget(money)
        self.add_widget(receiver)
        if btn.state=='down':
            self.remove_widget(code)
            self.remove_widget(btn)
            self.remove_widget(money)
            self.remove_widget(receiver)
        
    # the function to carry out crediting the user 
    def saved(self):
        with open('saved.txt' ,'w') as file:
            file.write("saved  an ammount of 10000000ugx...")
            file.close()



"""
class for handling the media files 

"""
class Media(Screen):
    
    programs=[]
    hrs=0
    days=0
    green=True 
    def music(self):
        music=Button(text='xmusic',size_hint=(.2,.05),pos_hint={'x':.6,'y':.7} )
        self.add_widget(music)
        if music.on_press==True:
            self.remove_widget(music)
    def editor(self):
        #changing  the font size of the words and alignment 
        
        
        next1=Button(text="cede TV",size_hint=(.2,.05),pos_hint={'x':.5,'y':.8} )
        self.add_widget(next1)

        video=Video(state='play',source='',size_hint=(.6,.4),pos_hint={'x':.4,'y':.2})
        self.add_widget(video)
        next=Button(text="news",size_hint=(.2,.05),pos_hint={'x':.9,'y':.1} )
        self.add_widget(next)
            #self.remove_widget(next1)
            



    
    def news(self):
        # the news anchors platform for the new delivery

        l=Label(text="News daily live",size_hint=(.4,.1),pos_hint={'x':.0,'y':.2})
        next1=Button(text='next',size_hint=(.2,.05),pos_hint={'x':.6,'y':.7} )
        self.add_widget(l)
        self.add_widget(next1)
        #if next1.on_press==True:
        #self.remove_widget(next1)
    """
    
    presenter function 


    """
    def presenter(self):
        l1=Label(text='salary:',size_hint=(.3,.05),pos_hint={'x':.0,'y':.2})
        code=TextInput(size_hint=(.3,.05),pos_hint={'x':.4,'y':.2})
        
        l1=Label(text='ammount:',size_hint=(.3,.05),pos_hint={'x':.4,'y':.3})
        #variable to hold the ammount of money to be sold
        a_m=TextInput(size_hint=(.3,.05),pos_hint={'x':.7,'y':.3})

        l2=Label(text='username: ',size_hint=(.3,.05),pos_hint={'x':.4,'y':.4})
        #variable to hold the currency
        ugx=TextInput(size_hint=(.3,.05),pos_hint={'x':.7,'y':.4})

        l3=Label(text='phone: ',size_hint=(.3,.05),pos_hint={'x':.4,'y':.5})
        #variable to hold the sellers name 
        user_id=TextInput(size_hint=(.3,.05),pos_hint={'x':.7,'y':.5})

        l4=Label(text='pin:',size_hint=(.3,.05),pos_hint={'x':.4,'y':.6})
        pin=TextInput(size_hint=(.3,.05),pos_hint={'x':.7,'y':.5})
        
        b=Button(text='finish',size_hint=(.2,.05),pos_hint={'x':.5,'y':.7} )
        b.bold=True
        #b.border=16,16,16,16
        b.background_color=0,1,1,1
        b.background_down=''
        b.background_down=''

        """
        l1.border(16,16,16,16)
        l2.border(16,16,16,16)
        l3.border(16,16,16,16)
        l4.border(16,16,16,16)
        b.border(16,16,16,16)
        a_m.border(16,16,16,16)

        """
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
        l1=Label(text='name: Timo',size_hint=(.3,.05),pos_hint={'x':.0,'y':.2})
        code=Label(text="age: 20",size_hint=(.3,.05),pos_hint={'x':.4,'y':.2})
        
        l1=Label(text='country:ug',size_hint=(.3,.05),pos_hint={'x':.4,'y':.3})
        #variable to hold the ammount of money to be sold
        a_m=Label(text="profs: media fx",size_hint=(.3,.05),pos_hint={'x':.7,'y':.3})

        l2=Label(text='salary: 900000ugx',size_hint=(.3,.05),pos_hint={'x':.4,'y':.4})
        #variable to hold the currency
        ugx=Label(text="date:......",size_hint=(.3,.05),pos_hint={'x':.7,'y':.4})

        l3=Label(text='phone:+256789498333 ',size_hint=(.3,.05),pos_hint={'x':.4,'y':.5})
        #variable to hold the sellers name 
        user_id=Label(text="show : youth dev",size_hint=(.3,.05),pos_hint={'x':.7,'y':.5})

        l4=Label(text='hobby: movies',size_hint=(.3,.05),pos_hint={'x':.4,'y':.6})
        pin=Label(text="about: xxxx",size_hint=(.3,.05),pos_hint={'x':.7,'y':.5})
        
        b=Button(text='finish',size_hint=(.2,.05),pos_hint={'x':.8,'y':.6} )
        b.bold=True
        b.border=16,16,16,16
        b.background_color=0,1,1,1
        b.background_down=''
        b.background_down=''
        """
        l1.border(16,16,16,16)
        l2.border(16,16,16,16)
        l3.border(16,16,16,16)
        l4.border(16,16,16,16)
        b.border(16,16,16,16)

        
        a_m.border(16,16,16,16)

        """
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
        time.sleep(20)

        self.remove_widget(code)
        self.remove_widget(l1)
        self.remove_widget(l2)
        self.remove_widget(l3)
        self.remove_widget(l4)
        self.remove_widget(a_m)
        self.remove_widget(ugx)
        self.remove_widget(user_id)
        self.remove_widget(pin)
        self.remove_widget(b)

        if b.state=='down':
            self.manager.current='cedes'
    def entertain(self):
        #tools for writing and editing the music 
        pin=Label(text="afro",size_hint=(.3,.05),pos_hint={'x':.4,'y':.5})
        p=Label(text="rnb ",size_hint=(.3,.05),pos_hint={'x':.4,'y':.6})
        b=Button(text='play',size_hint=(.2,.05),pos_hint={'x':.5,'y':.7} )
        exi=Button(text='exit',size_hint=(.2,.05),pos_hint={'x':.5,'y':.7} )
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
        next1=Button(text='fabs',size_hint=(.2,.05),pos_hint={'x':.6,'y':.4} )
        self.add_widget(next1)
        nex=Button(text='fansay',size_hint=(.2,.05),pos_hint={'x':.6,'y':.2} )
        self.add_widget(nex)

        pass
    def movies(self):
        #adding clips to form back the movies like they were 
        pin=Label(text="adventure",size_hint=(.3,.05),pos_hint={'x':.4,'y':.5})
        p=Label(text="horor ",size_hint=(.3,.05),pos_hint={'x':.4,'y':.6})
        b=Button(text='play',size_hint=(.2,.05),pos_hint={'x':.5,'y':.7} )
        next1=Button(text='next',size_hint=(.2,.05),pos_hint={'x':.6,'y':.7} )
        prev=Button(text='play',size_hint=(.2,.05),pos_hint={'x':.7,'y':.7} )
        exi=Button(text='exit',size_hint=(.2,.05),pos_hint={'x':.5,'y':.7} )
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
        
        
        code=Label(text='20,000ugx',size_hint=(.3,.05),pos_hint={'x':.4,'y':.2})
        
        
        l1=Label(text='october',size_hint=(.1,.1),pos_hint={'x':.8,'y':.18})
        self.add_widget(l1)
        #variable to hold the ammount of money to be sold
        a_m=TextInput(size_hint=(.3,.05),pos_hint={'x':.4,'y':.3})

        l2=Label(text='profile',size_hint=(.1,.1),pos_hint={'x':.8,'y':.28})
        #variable to hold the currency
        ugx=Label(text="credit",size_hint=(.3,.05),pos_hint={'x':.4,'y':.4})
        l3=Label(text='  location',size_hint=(.1,.1),pos_hint={'x':.8,'y':.38})
        #variable to hold the sellers name 
        user_id=Label(text="district",size_hint=(.3,.05),pos_hint={'x':.4,'y':.5})
        l4=Label(text='phone',size_hint=(.1,.1),pos_hint={'x':.8,'y':.48})

        but=Button(text='finish',size_hint=(.1,.05),pos_hint={'x':.4,'y':.08})
        b=Button(text='send',size_hint=(.1,.05),pos_hint={'x':.5,'y':.08} )
        
        self.add_widget(code)
        self.add_widget(l2)
        self.add_widget(l3)
        self.add_widget(l4)
        self.add_widget(a_m)
        self.add_widget(ugx)
        self.add_widget(user_id)
        self.add_widget(but)
        self.add_widget(b)
        if b.state=='down':
            self.remove_widget(code)
            self.remove_widget(l1)
            self.remove_widget(l2)
            self.remove_widget(l3)
            self.remove_widget(l4)
            self.remove_widget(a_m)
            self.remove_widget(ugx)
            self.remove_widget(user_id)
            self.remove_widget(but)
            self.remove_widget(b)




    """
    function to sleep for agiven duration
    
    """
    def wait(self,duration):
        time.sleep(duration)
        return 


        """
        
        function to handle account records 
        """
    def records(self):
        
        l4=Label(text='record',size_hint=(1,.1),pos_hint={'x':.8,'y':.48})
        self.add_widget(l4)
    """
    function to analyse the user status
    
    """
            
    def status(self):
        
        l4=Label(text='success',size_hint=(1,.1),pos_hint={'x':.8,'y':.48})
        self.add_widget(l4)
        self.wait(4)
        self.remove_widget(l4)
    


"""
class games for handling the games ,
mision games 
vision games 
football 
double chances 

"""
class Games(Screen):
    
    def slider(self):
         value=self.ids.slider.value
         return value
 

class Tec(Screen):
    
    def capture(self):
        l4=Label(text='capture',size_hint=(1,.1),pos_hint={'x':.8,'y':.48})
        self.add_widget(l4)

    
    def auto(self):
        l4=Label(text='mobile',size_hint=(1,.1),pos_hint={'x':.8,'y':.48})
        l3=Label(text='markets',size_hint=(1,.1),pos_hint={'x':.8,'y':.48})
        l2=Label(text='funlab',size_hint=(1,.1),pos_hint={'x':.8,'y':.48})
        l1=Label(text='social',size_hint=(1,.1),pos_hint={'x':.8,'y':.48})
        self.add_widget(l4)
        self.add_widget(l3)
        self.add_widget(l2)
        self.add_widget(l1)
    def apps(self):
        l4=Label(text='mobile',size_hint=(1,.1),pos_hint={'x':.8,'y':.48})
        l3=Label(text='markets',size_hint=(1,.1),pos_hint={'x':.8,'y':.58})
        l2=Label(text='funlab',size_hint=(1,.1),pos_hint={'x':.8,'y':.68})
        l1=Label(text='social',size_hint=(1,.1),pos_hint={'x':.8,'y':.78})
        self.add_widget(l4)
        self.add_widget(l3)
        self.add_widget(l2)
        self.add_widget(l1)
   
    def prog(self):
        l4=Button(text='java',size_hint=(1,.1),pos_hint={'x':.8,'y':.28})
        l3=Button(text='cpp',size_hint=(1,.1),pos_hint={'x':.8,'y':.38})
        l2=Button(text='python',size_hint=(1,.1),pos_hint={'x':.8,'y':.48})
        l1=Button(text='kotlin',size_hint=(1,.1),pos_hint={'x':.8,'y':.58})
        l0=Button(text='swift',size_hint=(1,.1),pos_hint={'x':.8,'y':.68})
        l=Button(text='kotlin',size_hint=(1,.1),pos_hint={'x':.8,'y':.78})
        l6=Button(text='Remove',size_hint=(1,.1),pos_hint={'x':.8,'y':.78})
        
        self.add_widget(l4)
        self.add_widget(l3)
        self.add_widget(l2)
        self.add_widget(l1)
        self.add_widget(l0)
        self.add_widget(l)
        self.add_widget(l6)
        if l6.state=='down':
            self.remove_widget(l4)
            self.remove_widget(l3)
            self.remove_widget(l2)
            self.remove_widget(l1)
            self.remove_widget(l0)
            self.remove_widget(l)
            self.remove_widget(l6)
    def sci(self):
        l4=Label(text='food ',size_hint=(1,.1),pos_hint={'x':.8,'y':.28})
        l3=Label(text='ai',size_hint=(1,.1),pos_hint={'x':.8,'y':.38})
        l2=Label(text='edge',size_hint=(1,.1),pos_hint={'x':.8,'y':.48})
        l1=Label(text='social',size_hint=(1,.1),pos_hint={'x':.8,'y':.58})
        self.add_widget(l4)
        self.add_widget(l3)
        self.add_widget(l2)
        self.add_widget(l1)


class Skillo(Screen):
    def editor(self):
        #changing  the font size of the words and alignment 
        
        
        next1=Button(text="cede TV",size_hint=(.2,.05),pos_hint={'x':.6,'y':.5} )
        self.add_widget(next1)
        next2=Button(text="hide",size_hint=(.2,.05),pos_hint={'x':.6,'y':.4} )
        self.add_widget(next2)
        if next1.state=='down':

            self.remove_widget(next2)
            self.remove_widget(next1)
            


    
    def news(self):
        # the news anchors platform for the new delivery

        l=Label(text="News daily live",size_hint=(.4,.1),pos_hint={'x':.2,'y':.7})
        next1=Button(text='next',size_hint=(.2,.05),pos_hint={'x':.2,'y':.6} )
        next2=Button(text='clear',size_hint=(.2,.05),pos_hint={'x':.2,'y':.5} )
        self.add_widget(l)
        self.add_widget(next1)
        if next2.state=='down':
            self.remove_widget(next1)
            self.remove_widget(l)
            self.remove_widget(next2)

    """
    
    presenter function 


    """
    def presenter(self):
        l1=Label(text='currency',size_hint=(.3,.05),pos_hint={'x':.0,'y':.2})
        code=TextInput(size_hint=(.3,.05),pos_hint={'x':.4,'y':.2})
        
        l1=Label(text='ammount',size_hint=(.3,.05),pos_hint={'x':.4,'y':.3})
        #variable to hold the ammount of money to be sold
        a_m=TextInput(size_hint=(.3,.05),pos_hint={'x':.4,'y':.3})

        l2=Label(text='username ',size_hint=(.3,.05),pos_hint={'x':.4,'y':.4})
        #variable to hold the currency
        ugx=TextInput(size_hint=(.3,.05),pos_hint={'x':.4,'y':.4})

        l3=Label(text='phone ',size_hint=(.3,.05),pos_hint={'x':.4,'y':.5})
        #variable to hold the sellers name 
        user_id=TextInput(size_hint=(.3,.05),pos_hint={'x':.4,'y':.5})

        l4=Label(text='pin',size_hint=(.3,.05),pos_hint={'x':.4,'y':.6})
        pin=TextInput(size_hint=(.3,.05),pos_hint={'x':.4,'y':.5})
        
        b=Button(text='finish',size_hint=(.2,.05),pos_hint={'x':.4,'y':.6} )
        b.bold=True
        b.border=16,16,16,16
        b.background_color=0,1,1,1
        b.background_down=''
        b.background_down=''

        """
        l1.border(16,16,16,16)
        l2.border(16,16,16,16)
        l3.border(16,16,16,16)
        l4.border(16,16,16,16)
        b.border(16,16,16,16)
        a_m.border(16,16,16,16)

        """
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
        if b.state=='down':
            self.remove_widget(code)
            self.remove_widget(l1)
            self.remove_widget(l2)
            self.remove_widget(l3)
            self.remove_widget(l4)
            self.remove_widget(a_m)
            self.remove_widget(ugx)
            self.remove_widget(user_id)
            self.remove_widget(pin)
            self.remove_widget(b)
    
        
        """
    function show
    
    
    """
    def show(self):
        l1=Label(text='name: Timo',size_hint=(.3,.05),pos_hint={'x':.0,'y':.2})
        code=Label(text="age: 20",size_hint=(.3,.05),pos_hint={'x':.4,'y':.2})
        
        l1=Label(text='country:ug',size_hint=(.3,.05),pos_hint={'x':.4,'y':.3})
        #variable to hold the ammount of money to be sold
        a_m=Label(text="profs: media fx",size_hint=(.3,.05),pos_hint={'x':.7,'y':.3})

        l2=Label(text='salary: 900000ugx',size_hint=(.3,.05),pos_hint={'x':.4,'y':.4})
        #variable to hold the currency
        ugx=Label(text="date:......",size_hint=(.3,.05),pos_hint={'x':.7,'y':.4})

        l3=Label(text='phone:+256789498333 ',size_hint=(.3,.05),pos_hint={'x':.4,'y':.5})
        #variable to hold the sellers name 
        user_id=Label(text="show : youth dev",size_hint=(.3,.05),pos_hint={'x':.7,'y':.5})

        l4=Label(text='hobby: movies',size_hint=(.3,.05),pos_hint={'x':.4,'y':.6})
        pin=Label(text="about: xxxx",size_hint=(.3,.05),pos_hint={'x':.7,'y':.45})
        
        b=Button(text='finish',size_hint=(.2,.05),pos_hint={'x':.8,'y':.6} )
        b.bold=True
        b.border=16,16,16,16
        b.background_color=0,1,1,1
        b.background_down=''
        b.background_down=''
        """
        l1.border(16,16,16,16)
        l2.border(16,16,16,16)
        l3.border(16,16,16,16)
        l4.border(16,16,16,16)
        b.border(16,16,16,16)

        
        a_m.border(16,16,16,16)

        """
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
        if b.state=='down':
            self.remove_widget(code)
            self.remove_widget(l1)
            self.remove_widget(l2)
            self.remove_widget(l3)
            self.remove_widget(l4)
            self.remove_widget(a_m)
            self.remove_widget(ugx)
            self.remove_widget(user_id)
            self.remove_widget(pin)
            self.remove_widget(b)

        
    def entertain(self):
        #tools for writing and editing the music 
        pin=Label(text="afro",size_hint=(.3,.05),pos_hint={'x':.4,'y':.5})
        p=Label(text="rnb ",size_hint=(.3,.05),pos_hint={'x':.4,'y':.6})
        b=Button(text='play',size_hint=(.2,.05),pos_hint={'x':.5,'y':.7} )
        exi=Button(text='exit',size_hint=(.2,.05),pos_hint={'x':.5,'y':.7} )
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
        next1=Button(text='fabs',size_hint=(.2,.05),pos_hint={'x':.6,'y':.4} )
        self.add_widget(next1)
        nex=Button(text='fansay',size_hint=(.2,.05),pos_hint={'x':.6,'y':.2} )
        self.add_widget(nex)

        pass
    def movies(self):
        #adding clips to form back the movies like they were 
        pin=Button(text="adventure",size_hint=(.3,.05),pos_hint={'x':.7,'y':.7})
        p=Button(text="horor ",size_hint=(.3,.05),pos_hint={'x':.7,'y':.6})
        b=Button(text='scifi',size_hint=(.2,.05),pos_hint={'x':.7,'y':.5} )
        next1=Button(text='next',size_hint=(.2,.05),pos_hint={'x':.7,'y':.4} )
        prev=Button(text='play',size_hint=(.2,.05),pos_hint={'x':.7,'y':.3} )
        exi=Button(text='exit',size_hint=(.2,.05),pos_hint={'x':.7,'y':.2} )
        self.add_widget(pin)
        self.add_widget(p)
        self.add_widget(next1)
        self.add_widget(prev)
        self.add_widget(b)

        if prev.state=='down':
            
            self.add_widget(Label(text="horor ",size_hint=(.3,.05),pos_hint={'x':.2,'y':.6}))
            self.remove_widget(Label(text="horor ",size_hint=(.3,.05),pos_hint={'x':.2,'y':.6}))
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




class Cedes(Screen):

    def admin(self):
        l=Label(text="Ceo",size_hint=(.2,.2),pos_hint={'x':.8,'y':.58})
        l.add_widget(l)
        return 
    def news(self):
        l=Label(text="news today",size_hint=(.2,.2),pos_hint={'x':.1,'y':.58})
        l.add_widget(l)

    def admin(self):
        #changing  the font size of the words and alignment 
        
        while self.green:
            next1=Button(text="Ceo",size_hint=(.2,.05),pos_hint={'x':.5,'y':.8} )
            self.add_widget(next1)

            video=Video(state="play",source='',size_hint=(.6,.4),pos_hint={'x':.4,'y':.2},background_color=(0,0,0,1))
            self.add_widget(video)
            nex=Button(text="company",size_hint=(.2,.05),pos_hint={'x':.9,'y':.1} )
            self.add_widget(nex)
            self.add_widget(video)
            #self.remove_widget(next1)
            


    
    def manager(self):
        # the news anchors platform for the new delivery

        l=Label(text="manager",size_hint=(.4,.1),pos_hint={'x':.0,'y':.2})
        next1=Button(text='next',size_hint=(.2,.05),pos_hint={'x':.6,'y':.7} )
        self.add_widget(l)
        self.add_widget(next1)
        if next1.state=='down':
            self.remove_widget(next1)
            self.add_widget(l)
    """
    
    presenter function 


    """
    def financier(self):
        l1=Label(text='currency',size_hint=(.3,.05),pos_hint={'x':.0,'y':.2})
        code=TextInput(size_hint=(.3,.05),pos_hint={'x':.4,'y':.2})
        
        l1=Label(text='ammount',size_hint=(.3,.05),pos_hint={'x':.4,'y':.3})
        #variable to hold the ammount of money to be sold
        a_m=TextInput(size_hint=(.3,.05),pos_hint={'x':.4,'y':.3})

        l2=Label(text='username ',size_hint=(.3,.05),pos_hint={'x':.4,'y':.4})
        #variable to hold the currency
        ugx=TextInput(size_hint=(.3,.05),pos_hint={'x':.4,'y':.4})

        l3=Label(text='phone ',size_hint=(.3,.05),pos_hint={'x':.4,'y':.5})
        #variable to hold the sellers name 
        user_id=TextInput(size_hint=(.3,.05),pos_hint={'x':.4,'y':.5})

        l4=Label(text='pin',size_hint=(.3,.05),pos_hint={'x':.4,'y':.6})
        pin=TextInput(size_hint=(.3,.05),pos_hint={'x':.4,'y':.5})
        
        b=Button(text='finish',size_hint=(.2,.05),pos_hint={'x':.5,'y':.6} )
        b.bold=True
        b.border=16,16,16,16
        b.background_color=0,1,1,1
        b.background_down=''
        b.background_down=''

        """
        l1.border(16,16,16,16)
        l2.border(16,16,16,16)
        l3.border(16,16,16,16)
        l4.border(16,16,16,16)
        b.border(16,16,16,16)
        a_m.border(16,16,16,16)

        """
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
        l1=Label(text='name: Timo',size_hint=(.3,.05),pos_hint={'x':.0,'y':.2})
        code=Label(text="age: 20",size_hint=(.3,.05),pos_hint={'x':.4,'y':.2})
        
        l1=Label(text='country:ug',size_hint=(.3,.05),pos_hint={'x':.4,'y':.3})
        #variable to hold the ammount of money to be sold
        a_m=Label(text="profs: media fx",size_hint=(.3,.05),pos_hint={'x':.7,'y':.3})

        l2=Label(text='salary: 900000ugx',size_hint=(.3,.05),pos_hint={'x':.4,'y':.4})
        #variable to hold the currency
        ugx=Label(text="date:......",size_hint=(.3,.05),pos_hint={'x':.7,'y':.4})

        l3=Label(text='phone:+256789498333 ',size_hint=(.3,.05),pos_hint={'x':.4,'y':.5})
        #variable to hold the sellers name 
        user_id=Label(text="show : youth dev",size_hint=(.3,.05),pos_hint={'x':.7,'y':.5})

        l4=Label(text='hobby: movies',size_hint=(.3,.05),pos_hint={'x':.4,'y':.6})
        pin=Label(text="about: xxxx",size_hint=(.3,.05),pos_hint={'x':.7,'y':.5})
        
        b=Button(text='finish',size_hint=(.2,.05),pos_hint={'x':.8,'y':.6} )
        b.bold=True
        b.border=16,16,16,16
        b.background_color=0,1,1,1
        b.background_down=''
        b.background_down=''
        """
        l1.border(16,16,16,16)
        l2.border(16,16,16,16)
        l3.border(16,16,16,16)
        l4.border(16,16,16,16)
        b.border(16,16,16,16)

        
        a_m.border(16,16,16,16)

        """
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
    

        if b.state=='down':
            self.remove_widget(code)
            self.remove_widget(l1)
            self.remove_widget(l2)
            self.remove_widget(l3)
            self.remove_widget(l4)
            self.remove_widget(a_m)
            self.remove_widget(ugx)
            self.remove_widget(user_id)
            self.remove_widget(pin)
            self.remove_widget(b)
    def entertain(self):
        #tools for writing and editing the music 
        pin=Label(text="afro",size_hint=(.3,.05),pos_hint={'x':.4,'y':.5})
        p=Label(text="rnb ",size_hint=(.3,.05),pos_hint={'x':.4,'y':.6})
        b=Button(text='play',size_hint=(.2,.05),pos_hint={'x':.5,'y':.7} )
        exi=Button(text='exit',size_hint=(.2,.05),pos_hint={'x':.5,'y':.7} )
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
        next1=Button(text='fabs',size_hint=(.2,.05),pos_hint={'x':.6,'y':.4} )
        self.add_widget(next1)
        nex=Button(text='fansay',size_hint=(.2,.05),pos_hint={'x':.6,'y':.2} )
        self.add_widget(nex)

        pass
    def movies(self):
        print("watching movies ")
        #adding clips to form back the movies like they were 
        pin=Label(text="adventure",size_hint=(.3,.05),pos_hint={'x':.4,'y':.5})
        p=Label(text="horor ",size_hint=(.3,.05),pos_hint={'x':.4,'y':.6})
        b=Button(text='play',size_hint=(.2,.05),pos_hint={'x':.5,'y':.7} )
        next1=Button(text='next',size_hint=(.2,.05),pos_hint={'x':.6,'y':.7} )
        prev=Button(text='play',size_hint=(.2,.05),pos_hint={'x':.7,'y':.7} )
        exi=Button(text='exit',size_hint=(.2,.05),pos_hint={'x':.5,'y':.7} )
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
#sm.add_widget(Cedes(name="cedes"))



"""
the application main loop

"""

class MainApp(App):


    def build(self):
        self.title='@Cedes'
    
        return sm
    
    
"""

checking if the name is equal to main
"""
if __name__=='__main__':
    e=MainApp()
    e.run()