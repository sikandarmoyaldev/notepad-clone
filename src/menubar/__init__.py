from tkinter import Tk, Text, Menu
from .file_menu import FileMenu


class MenuBar:
    def __init__(self, root: Tk, text_area: Text):
        self.root = root
        self.text_area = text_area
        self.menu = Menu(self.root)

        # Add Submenus
        self.file_menu = FileMenu(self.root, self.text_area, self.menu)
