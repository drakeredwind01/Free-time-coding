from textual.app import App
from textual.screen import ModalScreen
from textual.widgets import Input, Label





class MyApp(App):
    CSS_PATH = "myapp.tcss"

    def compose(self):
        """Responsible for putting widgets on the screen."""
        yield Label("Hello, world!", id="first-label")
        yield Label("How are you doing, NZ?")
        yield Input()


if __name__ == "__main__":
    MyApp().run()

"""
Label, Input {
    background: white;
    color: black;
}
"""