from tkinter import Tk, Text, Menu
from .controller import FileMenuController


class FileMenu:
    def __init__(self, root: Tk, text_area: Text, parent_menu: Menu):
        self.root = root
        self.text_area = text_area
        self.parent_menu = parent_menu
        self.file_menu_controller = FileMenuController(self.root, self.text_area)

        # Setup File Menu
        self.file_menu = Menu(self.parent_menu, tearoff=0)
        self.parent_menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", accelerator="Ctrl+N", command=self.file_menu_controller.new_file)
        self.file_menu.add_command(label="Open...", accelerator="Ctrl+O", command=self.file_menu_controller.open_file)
        self.file_menu.add_command(label="Save", accelerator="Ctrl+S", command=self.file_menu_controller.save_file)
        self.file_menu.add_command(label="Save As...", command=self.file_menu_controller.save_file_as)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Page Setup...", command=self.file_menu_controller.page_setup)
        self.file_menu.add_command(label="Print...", accelerator="Ctrl+P", command=self.file_menu_controller.print_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.root.quit)

        # Bind shortcuts
        self.root.bind_all("<Control-n>", lambda event: self.file_menu_controller.new_file())
        self.root.bind_all("<Control-o>", lambda event: self.file_menu_controller.open_file())
        self.root.bind_all("<Control-s>", lambda event: self.file_menu_controller.save_file())
        self.root.bind_all("<Control-p>", lambda event: self.file_menu_controller.print_file())
