from textual import on
from textual.app import App
from textual.screen import ModalScreen
from textual.widgets import Checkbox, Footer, Header, Input


class NewItemModal(ModalScreen):
    def compose(self):
        yield Input()

    @on(Input.Submitted)
    def any_name_stephen_gruppetta(self, event):
        description = event.value
        self.dismiss(description)


class TodoApp(App):
    BINDINGS = [
        # key  action name|description for the footer
        ("n", "new_item", "New item"),
    ]

    def compose(self):
        yield Header()
        yield Checkbox("Give NZ PUG presentation.")
        yield Footer()

    def action_new_item(self):
        self.push_screen(
            NewItemModal(), self.create_description_item
        )  # pushes the screen to the stack

    def create_description_item(self, description):
        checkbox = Checkbox(description)
        self.mount(checkbox)


if __name__ == "__main__":
    TodoApp().run()
