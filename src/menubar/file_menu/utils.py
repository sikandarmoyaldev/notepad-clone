from tkinter import Text, filedialog, messagebox


def new_file(text_area: Text):
    text_area.delete(1.0, "end")

    return None  # Clear the current file path


def open_file(text_area: Text):
    file_path = filedialog.askopenfilename(
        defaultextension=".txt", 
        filetypes=[
            ("Text Documents", "*.txt"), 
            ("All Files", "*.*")
        ]
    )

    if file_path:
        with open(file_path, "r") as file:
            text_area.delete(1.0, "end")
            text_area.insert(1.0, file.read())
        return file_path
    
    return None


def save_file(text_area: Text, file_path: str):
    if file_path:
        # Save the file
        with open(file_path, "w") as file:
            file.write(text_area.get(1.0, "end"))
    else:
        file_path = save_file_as(text_area)

        # if file not saved, press cancel button
        if (isinstance(file_path, tuple)):
            file_path = "Untitled"
        elif (file_path == ""):
            file_path = None
        else:
            # Save a new file
            with open(file_path, "w") as file:
                file.write(text_area.get(1.0, "end"))

    return file_path

    
def save_file_as(text_area: Text):
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt", 
        filetypes=[
            ("Text Documents", "*.txt"), 
            ("All Files", "*.*")
        ]
    )

    if file_path:
        with open(file_path, "w") as file:
            file.write(text_area.get(1.0, "end"))

    return file_path


def page_setup(text_area: Text):
    messagebox.showinfo("Page Setup", "Page setup dialog is not implemented.")


def print_file(text_area: Text):
    messagebox.showinfo("Print", "Print dialog is not implemented.")
