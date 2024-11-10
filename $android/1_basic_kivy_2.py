from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class MyApp(App):
    def build(self):
        layout = BoxLayout()
        label1 = Label(text='Hello World!')
        label2 = Label(text='button 2')
        layout.add_widget(label1)
        layout.add_widget(label2)
        return layout  # Return the layout

if __name__=='__main__':
    MyApp().run()
