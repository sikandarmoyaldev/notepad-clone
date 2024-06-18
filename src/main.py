from tkinter import Tk, Text, Frame, Scrollbar


class MainWindow:
    def __init__(self, root: Tk):
        # Initialized Main Window
        self.root = root
        self.root.title("Untitled - Notepad")
        self.root.geometry("800x600")

        # Create Widgets
        self._create_widgets()


    def _create_widgets(self):
        # Create a frame for the text area and scrollbar
        self.text_frame = Frame(self.root)
        self.text_frame.pack(expand=True, fill="both")

        # Create text area
        self.text_area = Text(self.text_frame, undo=True, wrap="none")
        self.text_area.pack(side="left", expand=True, fill="both")

        # Add vertical scrollbar
        self.scrollbar_y = Scrollbar(self.text_frame, command=self.text_area.yview)
        self.scrollbar_y.pack(side="right", fill="y")
        self.text_area.config(yscrollcommand=self.scrollbar_y.set)


if __name__ == "__main__":
    root = Tk()
    app = MainWindow(root)
    root.mainloop()
    