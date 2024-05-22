from page import Page
import customtkinter as ctk
from tkinter import ttk
from datetime import datetime

class viewTaskPage(Page):
    def __init__(self, parent, task_manager):
        super().__init__(parent, task_manager)
        self.show()

    def show(self):
        self.clear_frame()

        ctk.CTkLabel(self.frame, text="Daftar Tugas:", font=("Helvetica", 18)).pack(pady=10)

        self.filter_category = ttk.Combobox(self.frame, values=["Prioritas", "Deadline", "Mata Kuliah"])
        self.filter_category.pack(pady=5)
        self.filter_category.bind("<<ComboboxSelected>>", self.update_filter_choices)

        self.filter_choice_combobox = ttk.Combobox(self.frame, state="readonly")
        self.filter_choice_combobox.pack(pady=5)

        self.update_filter_choices(None)  # Panggil fungsi pertama kali untuk mengisi nilai pada filter_choice_combobox

        ctk.CTkButton(self.frame, text="Terapkan Filter", command=self.apply_filter).pack(pady=5)

        self.tasks_frame = ctk.CTkFrame(self.frame)
        self.tasks_frame.pack(pady=5)

        self.display_all_tasks()

        ctk.CTkButton(self.frame, text="Kembali ke Halaman Utama", command=self.task_manager.showMainPage).pack(pady=10)

    def update_filter_choices(self, event):
        filter_option = self.filter_category.get()
        if filter_option == "Prioritas":
            values = ["Tinggi", "Sedang", "Rendah"]
        elif filter_option == "Deadline":
            values = ["Terdekat", "Terjauh"]
        else:
            values = list(set(tugas['mata_kuliah'] for tugas in self.task_manager.daftar_tugas))
        self.filter_choice_combobox.configure(values=values)
        self.filter_choice_combobox.set("")  # Set nilai kombobox menjadi kosong

    def apply_filter(self):
        filter_option = self.filter_category.get()
        filter_choice = self.filter_choice_combobox.get()

        for widget in self.tasks_frame.winfo_children():
            widget.destroy()

        if filter_option == "Prioritas":
            filtered_tasks = [tugas for tugas in self.task_manager.daftar_tugas if tugas['prioritas'] == filter_choice]
        elif filter_option == "Deadline":
            reverse = filter_choice == "Terjauh"
            filtered_tasks = sorted(self.task_manager.daftar_tugas, key=lambda tugas: datetime.strptime(tugas['deadline'], "%d/%m/%Y"), reverse=reverse)
        else:
            filtered_tasks = [tugas for tugas in self.task_manager.daftar_tugas if tugas['mata_kuliah'] == filter_choice]

        self.display_tasks(filtered_tasks)

    def display_all_tasks(self):
        self.display_tasks(self.task_manager.daftar_tugas)

    def display_tasks(self, tasks):
        for tugas in tasks:
            ctk.CTkLabel(self.tasks_frame, text=f"Nama Tugas: {tugas['nama']}, Mata Kuliah: {tugas['mata_kuliah']}, Deadline: {tugas['deadline']}, Prioritas: {tugas['prioritas']}").pack()
