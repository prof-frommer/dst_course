# based on https://youtu.be/dpJrM2_NOT8?si=qP920m3DTI_Nmz87
from textual.app import App
from textual.widgets import Static

class TCSSApp(App):
    # DEFINE tcss file name and path here
    CSS_PATH = "ex10.tcss"

    def compose(self):
        yield Static("A static widget")
        yield Static("Using an id", id="static_with_id")
        yield Static("First class", classes="static_cls1")
        yield Static("Second class", classes="static_cls1 static_cls2")

if __name__ == "__main__":
    TCSSApp().run()   