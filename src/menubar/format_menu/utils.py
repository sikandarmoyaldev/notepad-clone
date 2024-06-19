from tkinter import Text


def toggle_word_wrap(text_area: Text, enabled: bool):
    if enabled:
        text_area.config(wrap="word")
    else:
        text_area.config(wrap="none")
