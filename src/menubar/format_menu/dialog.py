from tkinter import Tk, ttk, Toplevel, StringVar, IntVar, Text


class FontDialog:
    def __init__(self, root: Tk, text_area: Text):
        self.root = root
        self.text_area = text_area
        self.dialog = Toplevel(self.root)
        self.dialog.title("Font")

        # Font Configurations
        self.FONT_SIZE_OPTIONS = [8, 10, 12, 14, 16, 18, 20]
        self.FONT_STYLE_OPTIONS = ["normal", "bold", "italic"]
        self.FONT_FAMILY_OPTIONS = ["Arial", "Times New Roman", "Courier New"]
        
        # Create Widget
        self._create_widgets()
        

    def _create_widgets(self):
        # Font Family
        font_family_label = ttk.Label(self.dialog, text="Font:")
        font_family_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.font_family_var = StringVar()
        self.font_family_combobox = ttk.Combobox(
            self.dialog, textvariable=self.font_family_var,
            values=self.FONT_FAMILY_OPTIONS
        )
        self.font_family_combobox.grid(row=0, column=1, padx=10, pady=10, sticky="we")
        self.font_family_combobox.current(0)

        # Font Size
        font_size_label = ttk.Label(self.dialog, text="Font Size:")
        font_size_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.font_size_var = IntVar()
        self.font_size_combobox = ttk.Combobox(
            self.dialog, textvariable=self.font_size_var,
            values=self.FONT_SIZE_OPTIONS
        )
        self.font_size_combobox.grid(row=1, column=1, padx=10, pady=10, sticky="we")
        self.font_size_combobox.current(1)

        # Font Style
        font_style_label = ttk.Label(self.dialog, text="Font Style:")
        font_style_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        self.font_style_var = StringVar()
        self.font_style_combobox = ttk.Combobox(
            self.dialog, textvariable=self.font_style_var,
            values=self.FONT_STYLE_OPTIONS
        )
        self.font_style_combobox.grid(row=2, column=1, padx=10, pady=10, sticky="we")
        self.font_style_combobox.current(0)

        # OK & Cancel Button
        button_frame = ttk.Frame(self.dialog)
        button_frame.grid(row=3, columnspan=2, padx=10, pady=10)

        ok_button = ttk.Button(button_frame, text="OK", command=self.apply_font)
        ok_button.pack(side="left", padx=5)

        cancel_button = ttk.Button(button_frame, text="Cancel", command=self.dialog.destroy)
        cancel_button.pack(side="right", padx=5)


    def apply_font(self):
        font_family = self.font_family_var.get()
        font_size = self.font_size_var.get()
        font_style = self.font_style_var.get()

        # Apply Changes
        self.text_area.config(font=(font_family, font_size, font_style))


    def show(self):
        self.dialog.transient(self.root)
        self.dialog.grab_set()
        self.root.wait_window(self.dialog)
