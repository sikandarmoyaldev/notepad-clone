import os
from tkinter import Tk, Text
from .utils import *


class FileMenuController:
    def __init__(self, root: Tk, text_area: Text):
        self.root = root
        self.text_area = text_area
        self.current_file_path = None


    def new_file(self):
        self.current_file_path = new_file(self.text_area)
        self.root.title("Untitled - Notepad")


    def open_file(self):
        self.current_file_path = open_file(self.text_area)
        self.root.title(f"{os.path.basename(str(self.current_file_path))} - Notepad")


    def save_file(self):
        self.current_file_path = save_file(self.text_area, self.current_file_path)
        self.root.title(f"{os.path.basename(str(self.current_file_path))} - Notepad")


    def save_file_as(self):
        self.current_file_path = save_file_as(self.text_area)
        self.root.title(f"{os.path.basename(str(self.current_file_path))} - Notepad")


    def page_setup(self):
        page_setup(self.text_area)


    def print_file(self):
        print_file(self.text_area)
