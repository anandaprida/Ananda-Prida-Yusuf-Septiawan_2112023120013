import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
from showMainPage import showMainPage
from courseSchedulePage import courseSchedulePage
from addTaskPage import addTaskPage
from viewTaskPage import viewTaskPage
from datetime import datetime

class taskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Manager")
        self.root.geometry("860x620")
        self.daftar_tugas = []
        self.current_page = None  # Keep track of the current page

        # Show the main page initially
        self.showMainPage()

    def get_indonesian_day_name(self):
        days = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
        return days[datetime.today().weekday()]

    def showMainPage(self):
        self.clear_frame()
        self.current_page = showMainPage(self.root, self)

    def show_course_schedule(self):
        self.clear_frame()
        self.current_page = courseSchedulePage(self.root, self)

    def show_add_task_page(self):
        self.clear_frame()
        self.current_page = addTaskPage(self.root, self)

    def show_view_tasks_page(self):
        self.clear_frame()
        self.current_page = viewTaskPage(self.root, self)

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")

    window = ctk.CTk()
    app = taskManagerApp(window)
    window.mainloop()
