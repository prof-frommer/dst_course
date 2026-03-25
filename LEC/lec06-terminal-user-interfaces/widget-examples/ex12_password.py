from textual.app import App
from textual.widgets import Input, Label, Static

class PwdApp(App):
    def compose(self):
        yield Label("Type your password:")
        yield Input(password=True, id="input")
        yield Static("status...", id="output")

    def on_input_changed(self, event):
        msg = self.query_one("#input", Input).value
        output = self.query_one("#output", Static)
        output.update('user typed something')

    def on_input_submitted(self, event):
        msg = self.query_one("#input", Input).value
        output = self.query_one("#output", Static)
        # output.update(msg)
        self.exit(msg)

if __name__ == "__main__":
    PwdApp().run()