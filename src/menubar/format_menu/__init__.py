from tkinter import Tk, Text, Menu
from .controller import FormatController


class FormatMenu:
    def __init__(self, root: Tk, text_area: Text, parent_menu: Menu):
        self.root = root
        self.text_area = text_area
        self.parent_menu = parent_menu
        self.format_controller = FormatController(self.root, self.text_area)

        # Setup Format Menu
        self.format_menu = Menu(self.parent_menu, tearoff=0)
        self.parent_menu.add_cascade(label="Format", menu=self.format_menu)
        self.format_menu.add_checkbutton(label="Word Wrap", command=self.format_controller.toggle_word_wrap)
        self.format_menu.add_command(label="Font...", command=self.format_controller.show_font_dialog)
