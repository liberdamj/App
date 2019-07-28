import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

#Grid Layout Class
class MyGrid(Widget):
    name = ObjectProperty(None) #Initialized as None to start
    lastName = ObjectProperty(None)
    email = ObjectProperty(None)

    def btn(self):
        print("Name:", self.name.text, "Last Name:", self.lastName.text, "email:", self.email.text)
        self.name.text = ""
        self.lastName.text = ""
        self.email.text = ""

#Building Class
class MyApp(App):
    def build(self):
        return MyGrid()

#Runs MyApp Method
if __name__ == "__main__":
    MyApp().run()
