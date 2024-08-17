

import tradingeconomics as trade

import json
import statistics 
 #plotinng using kivy
from kivy.graphics import Line, Color
from kivy.uix.widget import Widget

from kivy.graphics import Rectangle, Ellipse, Line, Color
# ploting using canvas 
class MyCanvasWidget(Widget):
    def __init__(self, **kwargs):
        super(MyCanvasWidget, self).__init__(**kwargs)
        self.opening=0
        self.closing=0
        self.high=0
        self.low


        # Draw elements on the canvas
        with self.canvas:
            # Set the color to red
            Color(1, 0, 0, 1)  # RGBA

            # Draw a rectangle
            self.rect = Rectangle(pos=(100, 100), size=(20, 50))

            # Set the color to blue
            Color(0, 0, 1, 1)

            # Draw an ellipse (which is a circle if the width and height are equal)
            #self.ellipse = Ellipse(pos=(400, 100), size=(100, 100))

            # Set the color to green
            Color(0, 1, 0, 1)

            # Draw a line
            self.line = Line(points=[600, 100, 700, 200, 800, 100], width=2)


apikey="dd5cdff2ad30444:xqo2nkjkdr1wfzw"
#function to handle login in tradingneconomics 
trade.login(apikey)
country_market=trade.getMarketsByCountry('mexico')
print('market of the country....',country_market)

#print(trade.getNews())


class Formulea():
    def __init__(self,l,w,h):
        v=l*w*h # for the 3d  objects 
        v=l*w # for the 2d  objects 
class Circle:
    pass
        

        
        
        
        
        
        
        
class Conic:
    pass
class Gausian:
    pass
class Vectors:
    def scalor(self):
        pass
    def dotp(self):
        pass
    def line_plane(self):
        pass

class Numerical:
    pass
class Applied_m:
    def flowchart(self):
        initial=0
        
    def bearing(self):
        angle=20
        length=20
    
