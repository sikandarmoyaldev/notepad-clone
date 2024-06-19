from tkinter import Tk, Text, Menu
from .controller import EditMenuController


class EditMenu:
    def __init__(self, root: Tk, text_area: Text, parent_menu: Menu):
        self.root = root
        self.text_area = text_area
        self.parent_menu = parent_menu
        self.edit_menu_controller = EditMenuController(self.text_area)

        # Setup Edit Menu
        self.edit_menu = Menu(self.parent_menu, tearoff=0)
        self.parent_menu.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Undo", accelerator="Ctrl+Z", command=self.edit_menu_controller.undo)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Cut", accelerator="Ctrl+X", command=self.edit_menu_controller.cut)
        self.edit_menu.add_command(label="Copy", accelerator="Ctrl+C", command=self.edit_menu_controller.copy)
        self.edit_menu.add_command(label="Paste", accelerator="Ctrl+V", command=self.edit_menu_controller.paste)
        self.edit_menu.add_command(label="Delete", command=self.edit_menu_controller.delete)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Find...", accelerator="Ctrl+F", command=self.edit_menu_controller.find)
        self.edit_menu.add_command(label="Find Next", accelerator="F3", command=self.edit_menu_controller.find_next)
        self.edit_menu.add_command(label="Replace...", accelerator="Ctrl+H", command=self.edit_menu_controller.replace)
        self.edit_menu.add_command(label="Go To...", accelerator="Ctrl+G", command=self.edit_menu_controller.go_to)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Select All", accelerator="Ctrl+A", command=self.edit_menu_controller.select_all)
        self.edit_menu.add_command(label="Time/Date", accelerator="F5", command=self.edit_menu_controller.time_date)

        # Bind shortcuts
        self.root.bind_all("<Control-z>", lambda _event: self.edit_menu_controller.undo())
        self.root.bind_all("<Control-x>", lambda _event: self.edit_menu_controller.cut())
        self.root.bind_all("<Control-c>", lambda _event: self.edit_menu_controller.copy())
        self.root.bind_all("<Control-v>", lambda _event: self.edit_menu_controller.paste())
        self.root.bind_all("<Control-f>", lambda _event: self.edit_menu_controller.find())
        self.root.bind_all("<F3>", lambda _event: self.edit_menu_controller.find_next())
        self.root.bind_all("<Control-h>", lambda _event: self.edit_menu_controller.replace())
        self.root.bind_all("<Control-g>", lambda _event: self.edit_menu_controller.go_to())
        self.root.bind_all("<Control-a>", lambda _event: self.edit_menu_controller.select_all())
        self.root.bind_all("<F5>", lambda _event: self.edit_menu_controller.time_date())
        
