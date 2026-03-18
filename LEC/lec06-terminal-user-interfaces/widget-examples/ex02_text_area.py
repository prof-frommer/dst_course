# -*- coding: utf-8 -*-
"""
Created on Fri Jul 11 12:29:15 2025
@author: IFrommer
test2.py - just display hello world
"""

from textual.app import App  # ComposeResult (a type hint)
from textual.widgets import TextArea

class MyTextBoxApp(App):

    def compose(self):   # -> ComposeResult:
        yield TextArea( 'Hello World!',
                       id = 'main_text_area',
                       show_line_numbers = True)

if __name__ == "__main__":
    MyTextBoxApp().run()