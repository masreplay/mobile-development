from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class MyGrid(AnchorLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.add_widget(Label(text='Name'))
        self.name = TextInput(multiline=False)
        self.add_widget(self.name)

        self.add_widget(Label(text='Age'))
        self.age = TextInput(multiline=False)
        self.add_widget(self.age)

        self.add_widget(Button(text='Submit'))


class MyApp(App):
    def build(self):
        return MyGrid()


def main():
    MyApp().run()


main()
