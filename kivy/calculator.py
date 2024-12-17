from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen


class ScrButton(Button):
	def __init__(self, screen, direction='right', goal='main', **kwargs):
		super().__init__(**kwargs)
		self.screen = screen
		self.direction = direction
		self.goal = goal
	def on_press(self):
		global var1,var2
		var1 = self.lbl.text
		var2 = self.lbl.text
		self.screen.manager.current = self.goal
		return eval(var1,'text')

class FirstScr(Screen):
	def __init__(self, name='first'):
		super().__init__(name=name)
		vl = BoxLayout(orientation='vertical')
		lbl = TextInput(multiline=False)
		
		h1 = BoxLayout()
		h2 = BoxLayout()
		h3 = BoxLayout()
		h4 = BoxLayout()
		h5 = BoxLayout()
		btn1 = Button(text="1")
		btn2 = Button(text="2")
		btn3 = Button(text="3")
		btn4 = Button(text="4")
		btn5 = Button(text="5")
		btn6 = Button(text="6")
		btn7 = Button(text="7")
		btn8 = Button(text="8")
		btn9 = Button(text="9")
		btn0 = Button(text="0")
		btnAC = Button(text="AC")
		btnplusminus = Button(text="+/-")
		btnprocent = Button(text="%")
		btnplus = Button(text="+")
		btnminus = Button(text="-")
		btndivide = Button(text="/")
		btnmultiply = Button(text="*")
		btncomma = Button(text=",")
		btnHereWeGO = Button(text="=")

		h1.add_widget(btnAC)
		h1.add_widget(btnplusminus)
		h1.add_widget(btnprocent)
		h1.add_widget(btndivide)
		
		h2.add_widget(btn7)
		h2.add_widget(btn8)
		h2.add_widget(btn9)
		h2.add_widget(btnmultiply)
		
		h3.add_widget(btn4)
		h3.add_widget(btn5)
		h3.add_widget(btn6)
		h3.add_widget(btnminus)

		h4.add_widget(btn1)
		h4.add_widget(btn2)
		h4.add_widget(btn3)
		h4.add_widget(btnplus)

		h5.add_widget(btn0)
		h5.add_widget(btncomma)
		h5.add_widget(btnHereWeGO)
		#================
		vl.add_widget(lbl)
		vl.add_widget(h1)
		vl.add_widget(h2)
		vl.add_widget(h3)
		vl.add_widget(h4)
		vl.add_widget(h5)
		#================#
		self.add_widget(vl)

class MyApp(App):
	def build(self):
		sm = ScreenManager()
		sm.add_widget(FirstScr())
		return sm

app = MyApp()
app.run()