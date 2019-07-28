import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

#Grid Layout Class
class MyGrid(GridLayout):
    def __init__(self, **kwargs):

        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1

        self.inside = GridLayout()
        self.inside.cols = 2

        self.inside.add_widget(Label(text="First Name: "))
        self.name = TextInput(multiline=False)
        self.inside.add_widget(self.name)

        self.inside.add_widget(Label(text="Last Name: "))
        self.lastName = TextInput(multiline=False)
        self.inside.add_widget(self.lastName)

        self.inside.add_widget(Label(text="E-mail: "))
        self.email = TextInput(multiline=False)
        self.inside.add_widget(self.email)

        self.add_widget(self.inside)

        self.submit = Button(text="Submit", font_size=36)
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)

    #Button Function to do _ when Button submit is pressed.
    def pressed(self, instance):
        name = self.name.text
        lastName = self.lastName.text
        email = self.email.text
        print("Name: ", name, " Last Name: ", lastName, " E-mail: ", email)
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
