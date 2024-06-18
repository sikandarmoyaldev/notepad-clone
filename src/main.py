from tkinter import Tk, Text, Frame


class MainWindow:
    def __init__(self, root: Tk):
        # Initialized Main Window
        self.root = root
        self.root.title("Untitled - Notepad")
        self.root.geometry("800x600")

        # Create Widgets
        self._create_widgets()


    def _create_widgets(self):
        # Create text area
        self.text_area = Text(self.root, undo=True, wrap="none")
        self.text_area.pack(side="left", expand=True, fill="both")


if __name__ == "__main__":
    root = Tk()
    app = MainWindow(root)
    root.mainloop()
    