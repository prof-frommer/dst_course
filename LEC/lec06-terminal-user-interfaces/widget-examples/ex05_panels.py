from textual.app import App
from textual.widgets import Button, Static
from textual.containers import Horizontal, Vertical

class MyApp(App):

    def compose(self):
        # Create a horizontal layout with two panels
        with Horizontal():
            # Left panel: buttons stacked vertically
            with Vertical(id="left_panel"):
                yield Button("Add 2 + 3", id="btn_add")
                yield Button("Greet", id="btn_greet")
                yield Button("Clear", id="btn_clear")

            # Right panel: output area
            with Vertical(id="right_panel"):
                yield Static("Click a button, output will appear here", id="output") 

if __name__ == "__main__":
    MyApp().run()