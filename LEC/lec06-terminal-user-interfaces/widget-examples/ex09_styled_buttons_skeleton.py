from textual.app import App
from textual.widgets import Button #, Static
#from textual.containers import Horizontal, Vertical
# turn some of these styles on and off to illustrate

class MyLabelApp(App):
        
    def compose(self):   
        
        self.screen.styles.background = "antiquewhite"
        self.screen.styles.border = ("heavy", "silver")
        
        # WE WILL CHANGE THIS TO STORE WIDGETS IN INSTANCE VARIABLES
        yield Button('Button 1', id = "btn_1")
        yield Button('Button 2', id= "btn_2")
            
    
    def on_mount(self):
        # WE WILL ADD STYLE PROPERTIES TO THE WIDGET INSTANCES HERE
        pass

if __name__ == "__main__":
    MyLabelApp().run()
