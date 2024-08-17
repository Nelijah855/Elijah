
from kivy.animation import Animation
from kivy.uix.button import Button
b=Button(text="micronet",pos={'x':.1,'y':.2},size=(.2,.2))
a=Animation(x=.2,size=(.2,.2),t='micro')
a.start(b)
