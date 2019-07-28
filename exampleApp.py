import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget

#Grid Layout Class
class MyGrid(Widget):
    pass

#Building Class
class MyApp(App):
    def build(self):
        return MyGrid()

#Runs MyApp Method
if __name__ == "__main__":
    MyApp().run()
