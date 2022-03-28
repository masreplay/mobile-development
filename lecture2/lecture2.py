from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label


class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='Cell 1'))
        self.add_widget(Label(text='Cell 2'))
        self.add_widget(Label(text='Cell 3'))


class MyApp(App):
    def build(self):
        return MyGrid()


def main():
    MyApp().run()


main()
