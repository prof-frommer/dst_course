# -*- coding: utf-8 -*-
"""
Created on Fri Jul 11 12:29:15 2025  @author: IFrommer
"""

from textual.app import App
from textual.widgets import Select

MENU_ITEMS = ['Hello','World!','DST']

class MyApp(App):

    def compose(self):
        yield Select( [(item, item) for item in MENU_ITEMS], 
                       prompt = 'Choose your item:',
                       id = 'select_menu',
                       )

if __name__ == "__main__":
    MyApp().run()