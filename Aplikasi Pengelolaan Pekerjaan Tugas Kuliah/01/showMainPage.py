from page import Page
import customtkinter as ctk
from datetime import datetime, timedelta
from subjectSchedule import subjectSchedule

class showMainPage(Page):
    def __init__(self, parent, task_manager):
        super().__init__(parent, task_manager)
        self.show()

    def show(self):
        self.clear_frame()
        
        self.labelWelcome = ctk.CTkLabel(self.frame, text="", font=("Helvetica", 24))
        self.labelWelcome.pack(pady=10)
        update_welcome_label(self.labelWelcome)  # Panggil function untuk memperbarui label

        hari_ini = self.task_manager.get_indonesian_day_name()
        if hari_ini in subjectSchedule:
            ctk.CTkLabel(self.frame, text="Jadwal Mata Kuliah Hari Ini:", font=("Helvetica", 20)).pack(pady=20)

            for mata_kuliah, dosen, waktu in subjectSchedule[hari_ini]:
                waktu_mulai, waktu_selesai = waktu.split("-")
                
                waktu_mulai = datetime.strptime(waktu_mulai.strip(), "%H:%M").time()
                waktu_selesai = datetime.strptime(waktu_selesai.strip(), "%H:%M").time()
                
                waktu_sekarang = datetime.now().time()
                color = "#4158D0" if waktu_mulai <= waktu_sekarang <= waktu_selesai else "black"
                ctk.CTkLabel(self.frame, text=f"{mata_kuliah} ({dosen}, {waktu})", text_color=color, font=("Helvetica", 16)).pack(pady=6)
        else:
            ctk.CTkLabel(self.frame, text="Tidak ada mata kuliah hari ini", font=("Helvetica", 16)).pack(pady=5)

        today = datetime.now().date()
        tasks_due_soon = [tugas for tugas in self.task_manager.daftar_tugas if (datetime.strptime(tugas['deadline'], "%d/%m/%Y").date() - today) <= timedelta(days=2)]
        if tasks_due_soon:
            ctk.CTkLabel(self.frame, text="Tugas dengan deadline kurang dari 2 hari:", font=("Helvetica", 20)).pack(pady=10)
        for tugas in tasks_due_soon:
            ctk.CTkLabel(self.frame, text=f"Nama Tugas: {tugas['nama']}, Mata Kuliah: {tugas['mata_kuliah']}, Deadline: {tugas['deadline']}, Prioritas: {tugas['prioritas']}").pack()

        ctk.CTkButton(self.frame, text="Lihat Jadwal Mata Kuliah", command=self.task_manager.show_course_schedule).pack(pady=5)
        ctk.CTkButton(self.frame, text="Tambah Tugas Baru", command=self.task_manager.show_add_task_page).pack(pady=5)
        ctk.CTkButton(self.frame, text="Lihat Daftar Tugas", command=self.task_manager.show_view_tasks_page).pack(pady=5)
        ctk.CTkButton(self.frame, text="Keluar", command=self.parent.quit).pack(pady=5)

        # Centering the frame content
        self.frame.pack(expand=True)
        self.frame.pack_propagate(False)

def update_welcome_label(label):
    currentHour = datetime.now().hour
    if currentHour < 12:
        greeting = "Selamat Pagi!"
    elif 12 <= currentHour < 18:
        greeting = "Selamat Siang!"
    else:
        greeting = "Selamat Malam!"
    
    label.configure(text=greeting)
