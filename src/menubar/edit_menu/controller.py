from tkinter import Text
from .utils import *


class EditMenuController:
    def __init__(self, text_area: Text):
        self.text_area = text_area


    def cut(self):
        cut(self.text_area)


    def copy(self):
        copy(self.text_area)


    def paste(self):
        paste(self.text_area)


    def undo(self):
        undo(self.text_area)


    def delete(self):
        delete(self.text_area)


    def find(self):
        find(self.text_area)


    def find_next(self):
        find_next(self.text_area)


    def replace(self):
        replace(self.text_area)


    def go_to(self):
        go_to(self.text_area)


    def select_all(self):
        select_all(self.text_area)


    def time_date(self):
        time_date(self.text_area)
        