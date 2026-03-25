from textual.app import App
from textual.widgets import Button #, Static
#from textual.containers import Horizontal, Vertical
# turn some of these styles on and off to illustrate

class MyLabelApp(App):
        
    def compose(self):   
        
        self.screen.styles.background = "antiquewhite"
        self.screen.styles.border = ("heavy", "silver")
        
        self.btn_1 = Button('Button 1', id = "btn_1")
        self.btn_2 = Button('Button 2', id= "btn_2")
        
        yield self.btn_1        
        yield self.btn_2
        
    def on_mount(self):
        
        self.btn_1.styles.background = 'orange'
        self.btn_1.styles.width = 45
        self.btn_1.styles.height = "2fr"
        
        self.btn_2.styles.border = ('double', 'red')
        self.btn_2.styles.height="1fr"

if __name__ == "__main__":
    MyLabelApp().run()
