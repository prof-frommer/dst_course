# -*- coding: utf-8 -*-
"""
Created on Fri Jul 11 12:29:15 2025
@author: IFrommer
ex01_label.py - just display hello world
"""

from textual.app import App
from textual.widgets import Label

class MyLabelApp(App):

    def compose(self):
        yield Label('Hello World!')

    def on_key(self, event):
        if event.key == 'q':
            self.exit()

if __name__ == "__main__":
    MyLabelApp().run()