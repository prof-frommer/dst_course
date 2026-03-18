from unittest import result
from textual.app import App
from textual.widgets import Static, Select

MENU_ITEMS = ["apple", "banana", "cherry"]

class MyApp(App):

    def compose(self):
        yield Select([(item, item) for item in MENU_ITEMS],
            prompt="Choose your item:",
            id="select_menu",
            )
        yield Static("", id="output")

    def on_select_changed(self, event):
        result = f"You selected: {event.value}"
        output_widget = self.query_one("#output", Static)
        output_widget.update(result)

if __name__ == "__main__":
    MyApp().run()