# based on https://youtu.be/dpJrM2_NOT8?si=qP920m3DTI_Nmz87
from textual.app import App
from textual.widgets import Static

class TCSSApp(App):
    CSS_PATH = # DEFINE tcss file name / path here using built-in CSS_PATH name

    def compose(self):
        yield Static("A static widget")
        yield Static("Using an id", id="static_with_id")
        yield Static("First class", classes=" # FILL IN 
        yield Static("Second class", classes="# FILL IN 

if __name__ == "__main__":
    TCSSApp().run()   