from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from time import sleep

class MyLayout(BoxLayout):
    def __init__(self):
        super().__init__()
        self.button = Button(text='press me')
        self.button.bind(on_press=self.new_label)

        self.add_widget(self.button)

    def new_label(self, button):
        self.label = Label(text='my new label')
        self.add_widget(self.label)
        sleep(1)
        # self.remove_wedget(button)

class MyApp(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    MyApp().run()