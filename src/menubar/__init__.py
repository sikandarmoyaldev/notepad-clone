from tkinter import Tk, Text, Menu


class MenuBar:
    def __init__(self, root: Tk, text_area: Text):
        self.root = root
        self.text_area = text_area
        self.menu = Menu(self.root)

    
    