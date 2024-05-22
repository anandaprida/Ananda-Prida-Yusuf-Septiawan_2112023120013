from page import Page
from datetime import datetime
import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk

class addTaskPage(Page):
    def __init__(self, parent, task_manager):
        super().__init__(parent, task_manager)
        self.show()

    def show(self):
        self.clear_frame()

        ctk.CTkLabel(self.frame, text="Tambah Tugas Baru", font=("Helvetica", 18)).pack(pady=10)
        ctk.CTkLabel(self.frame, text="Nama Tugas:").pack(pady=5)
        self.nama_tugas_entry = ctk.CTkEntry(self.frame)
        self.nama_tugas_entry.pack(pady=5)

        ctk.CTkLabel(self.frame, text="Mata Kuliah:").pack(pady=5)
        self.mata_kuliah_entry = ctk.CTkEntry(self.frame)
        self.mata_kuliah_entry.pack(pady=5)

        ctk.CTkLabel(self.frame, text="Deskripsi Tugas:").pack(pady=5)
        self.deskripsi_tugas_entry = ctk.CTkEntry(self.frame)
        self.deskripsi_tugas_entry.pack(pady=5)

        ctk.CTkLabel(self.frame, text="Deadline Tugas:").pack(pady=5)
        self.create_date_picker()

        ctk.CTkLabel(self.frame, text="Tingkat Prioritas:").pack(pady=5)
        self.priority_value = ctk.StringVar()
        ctk.CTkRadioButton(self.frame, text="Tinggi", variable=self.priority_value, value="Tinggi").pack()
        ctk.CTkRadioButton(self.frame, text="Sedang", variable=self.priority_value, value="Sedang").pack()
        ctk.CTkRadioButton(self.frame, text="Rendah", variable=self.priority_value, value="Rendah").pack()

        ctk.CTkButton(self.frame, text="Simpan", command=self.save_task).pack(pady=10)
        ctk.CTkButton(self.frame, text="Kembali", command=self.task_manager.showMainPage).pack(pady=10)

    def create_date_picker(self):
        self.date_frame = ctk.CTkFrame(self.frame)
        self.date_frame.pack(pady=5)

        days = list(map(str, range(1, 32)))
        months = list(map(str, range(1, 13)))
        years = list(map(str, range(datetime.now().year, datetime.now().year + 5)))

        self.day_combobox = ctk.CTkComboBox(self.date_frame, values=days)
        self.day_combobox.set(str(datetime.now().day))
        self.day_combobox.pack(side='left', padx=5)

        self.month_combobox = ctk.CTkComboBox(self.date_frame, values=months)
        self.month_combobox.set(str(datetime.now().month))
        self.month_combobox.pack(side='left', padx=5)

        self.year_combobox = ctk.CTkComboBox(self.date_frame, values=years)
        self.year_combobox.set(str(datetime.now().year))
        self.year_combobox.pack(side='left', padx=5)

    def get_selected_date(self):
        day = self.day_combobox.get()
        month = self.month_combobox.get()
        year = self.year_combobox.get()
        return f"{int(day):02d}/{int(month):02d}/{int(year)}"

    def save_task(self):
        nama_tugas = self.nama_tugas_entry.get().strip()
        mata_kuliah = self.mata_kuliah_entry.get().strip()
        deskripsi_tugas = self.deskripsi_tugas_entry.get().strip()
        deadline_tugas = self.get_selected_date()
        priority_value = self.priority_value.get()

        if not (nama_tugas and mata_kuliah and deskripsi_tugas and deadline_tugas and priority_value):
            messagebox.showerror("Error", "Semua input harus diisi")
            return

        tugas = {
            'nama': nama_tugas,
            'mata_kuliah': mata_kuliah,
            'deskripsi': deskripsi_tugas,
            'deadline': deadline_tugas,
            'prioritas': priority_value
        }
        self.task_manager.daftar_tugas.append(tugas)
        self.task_manager.showMainPage()
