from textual.app import App
from textual.widgets import Button, Static
from textual.containers import Horizontal, Vertical

# --- "application logic" (non-Textual code) ---
def add(a, b):
    return a + b

def greet():
    return "Hello from Python logic!"


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
                

    def on_button_pressed(self, event):
        button_id = event.button.id
        output = self.query_one("#output", Static)

        if button_id == "btn_add":
            result = add(2, 3)
        elif button_id == "btn_greet":
            result = greet()
        elif button_id == "btn_clear":
            result = ""
            output.update("")
        
        output.update(f"Result: {result}")

if __name__ == "__main__":
    MyApp().run()