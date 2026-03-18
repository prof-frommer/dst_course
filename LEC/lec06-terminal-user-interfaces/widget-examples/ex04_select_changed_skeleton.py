from textual.app import App
from textual.widgets import # YOUR CODE HERE

MENU_ITEMS = ["apple", "banana", "cherry"]

class MyApp(App):

    def compose(self):
        yield Select([(item, item) for item in MENU_ITEMS],
            prompt="Choose your item:",
            id="select_menu",
            )
        yield # YOUR CODE HERE

    def on_select_changed(self, # YOUR CODE HERE ):
        result = f"You selected: {# YOUR CODE HERE}"
        output_widget = self.query_one( # YOUR CODE HERE
        # YOUR CODE HERE
        
if __name__ == "__main__":
    MyApp().run()