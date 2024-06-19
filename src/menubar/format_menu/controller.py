from tkinter import Tk, Text
from .utils import *
from .dialog import *


class FormatController:
    def __init__(self, root: Tk, text_area: Text):
        self.root = root
        self.text_area = text_area
        self.current_file_path = None
        self.word_wrap_enabled = False
        self.font_dialog = None  # Initialize font dialog attribute

    
    def show_font_dialog(self):
        if not self.font_dialog:
            self.font_dialog = FontDialog(self.root, self.text_area)
        
        self.font_dialog.show()

        # NOTE: Destroy the font dialog
        self.font_dialog = None


    def toggle_word_wrap(self):
        self.word_wrap_enabled = not(self.word_wrap_enabled)
        toggle_word_wrap(self.text_area, self.word_wrap_enabled)
