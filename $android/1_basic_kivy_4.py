from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
'''absolute (not as good for different screens)'''
class MyApp(App):
    def build(self):
        layout = FloatLayout()
        button = Button(text='Press Me', size=(50, 50), size_hint=(0.3, 0.2), pos=(500, 100))
        layout.add_widget(button)
        return layout  # Return the layout

if __name__=='__main__':
    MyApp().run()
