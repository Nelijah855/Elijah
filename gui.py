

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.checkbox import CheckBox
from kivy.uix.switch import Switch
from kivy.uix.progressbar import ProgressBar
from kivy.uix.popup import Popup

import time

class Inner(FloatLayout):

    
    
    

    def pop(self):
        # create content and add to the popup
        content = Button(text='seen!')
        popup = Popup(content=content, auto_dismiss=False)
        
        
# bind the on_press event of the button to the dismiss function
        content.bind(on_press=popup.dismiss)

# open the popup
        popup.open()
        

    def check(self):
        
        checkbox = CheckBox()
        checkbox.bind(active=self.on_checkbox_active)
        self.add_widget(checkbox)
    def callback(self):
        label=Label(text='switched', size_hint=(.2, .2),pos_hint={'x':.5,'top':.1})
    def on_checkbox_active(self, value):
            if value:
                self.check()
            else:
                self.switch()


    def switch(self):
        switch=Switch(active=True)
        switch.bind(active=self.callback)
        self.add_widget(switch)
    def progress(self):
        pro=ProgressBar(max=100)
        pro.value=20
        self.add_widget(pro)
        
    def dropdown(self):
    # create a dropdown with 10 buttons
        dropdown = DropDown()
        self.add_widget(dropdown)
        pa=['mtn','airtel','paypal','visa']
        for index in range(4):
    # When adding widgets, we need to specify the height manually
    # (disabling the size_hint_y) so the dropdown can calculate
    # the area it needs.

            btn = Button(text='%s' % pa[index], size_hint_y=None, height=44)

    # for each button, attach a callback that will call the select() method
    # on the dropdown. We'll pass the text of the button as the data of the
    # selection.
            btn.bind(on_release=lambda btn: dropdown.select(btn.text))

    # then add the button inside the dropdown
            dropdown.add_widget(btn)

# create a big main button
        mainbutton = Button(text='pay', size_hint=(.2, .2),pos_hint={'x':.1,'top':.1})

# show the dropdown menu when the main button is released
# note: all the bind() calls pass the instance of the caller (here, the
# mainbutton instance) as the first argument of the callback (here,
# dropdown.open.).
        mainbutton.bind(on_release=dropdown.open)
        self.add_widget(mainbutton)

# one last thing, listen for the selection in the dropdown list and
# assign the data to the button text.
        dropdown.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))
    """

    function to sleep for agiven duration
    
    """
    
    """
    function to draw on the texture 
    
    """
    def draw(self):
        with self.canvas:
            self.Color(0,1,1,1)
            self.Rectangle(pos=self.pos,size=self.size)
            
    """
    function to use the widget properties 
    """
    def widget_prop(self):
        b=Button(text='send',size_hint=(.1,.05),pos_hint={'x':.5,'y':.08} )
        b.bold=True
        b.border=16,16,16,16
        b.background_color=0,1,1,1
        b.background_down=''
        b.background_down=''
    """
    forex bearue fucntion ---> [ishops.py](forex) 
    where the above shows the direction of objects
    
    
    """
    def forex(self):
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
        


    def b(self):
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
    def clear(self):
        self.clear_widgets()
    def remove(self):
        #self.remove_widget()
        pass


    def c(self):
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


    def d(self):
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

    def e(self):
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


        """
        function for investments which links to invest function in the [invest class]
         
           inside [ishops.py] file
        """
    def investment(self):
        ammount=TextInput(size_hint=(.3,.05),pos_hint={'x':.4,'y':.2})
        
        username=Label(text='usercode ',size_hint=(.1,.1),pos_hint={'x':.8,'y':.18})
        #variable to hold the ammount of money to be sold
        time=TextInput(size_hint=(.3,.05),pos_hint={'x':.4,'y':.3})
        handler=Label(text='name ',size_hint=(.1,.1),pos_hint={'x':.8,'y':.28})
        #variable to hold the currency
        intrest=TextInput(size_hint=(.3,.05),pos_hint={'x':.4,'y':.4})
        
        self.add_widget(ammount)
        self.add_widget(username)
        self.add_widget(time)
        self.add_widget(intrest)
        
        self.add_widget(handler)
        but=Button(text='send',size_hint=(.1,.05),pos_hint={'x':.4,'y':.08} ,on_press=self.show )

        self.add_widget(but)
        
        
        return ammount,username,time,handler,intrest
    
    
    def show(self):
        l=Label(text=' [share] [invest] in cede.inc ',size_hint=(.2,.1),pos_hint={'x':.8,'y':.3})
        self.add_widget(l)
        time.sleep(3)
        self.remove_widget(l)
    def pinnacle(self):
        l=Label(text=' invest in cede.inc with [pinnacle] ',size_hint=(.2,.1),pos_hint={'x':.8,'y':.3})
        self.add_widget(l)
     
        self.remove_widget(l)