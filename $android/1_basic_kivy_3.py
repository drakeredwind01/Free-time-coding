from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        label1 = Label(text='Hello World!', size_hint=(0.3, 0.2), pos_hint={'center_x':0.2, 'center_y':0.3})
        label2 = Label(text='button 2', size_hint=(0.5, 0.7), pos_hint={'center_x':0.3, 'center_y':0.1})
        button = Button(text='Press Me')
        layout.add_widget(label1)
        layout.add_widget(label2)
        layout.add_widget(button)
        return layout  # Return the layout

if __name__=='__main__':
    MyApp().run()
