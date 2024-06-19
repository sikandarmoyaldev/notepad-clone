from tkinter import Text


def cut(text_area: Text):
    text_area.event_generate("<<Cut>>")


def copy(text_area: Text):
    text_area.event_generate("<<Copy>>")


def paste(text_area: Text):
    text_area.event_generate("<<Paste>>")


def undo(text_area: Text):
    text_area.event_generate("<<Undo>>")


def delete(text_area):
    text_area.delete("sel.first", "sel.last")


def find(text_area: Text):
    # TODO: Implement your find logic here
    pass


def find_next(text_area: Text):
    # TODO: Implement your find next logic here
    pass


def replace(text_area: Text):
    # TODO: Implement your replace logic here
    pass


def go_to(text_area: Text):
    # TODO: Implement your go to logic here
    pass


def select_all(text_area: Text):
    text_area.tag_add("sel", "1.0", "end")


def time_date(text_area: Text):
    # TODO: Implement your time/date insertion logic here
    pass
