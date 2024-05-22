from customtkinter import *

class Page:
    def __init__(self, parent, task_manager):
        self.parent = parent
        self.task_manager = task_manager
        self.frame = CTkFrame(parent)
        self.frame.pack(fill="both", expand=True)

    def clear_frame(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
