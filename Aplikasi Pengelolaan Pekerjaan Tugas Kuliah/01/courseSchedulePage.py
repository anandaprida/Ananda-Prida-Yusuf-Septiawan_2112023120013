import customtkinter as ctk
from page import Page
from subjectSchedule import subjectSchedule

class courseSchedulePage(Page):
    def __init__(self, parent, task_manager):
        super().__init__(parent, task_manager)
        self.show()

    def show(self):
        self.clear_frame()

        title_label = ctk.CTkLabel(self.frame, text="Jadwal Mata Kuliah", font=("Helvetica", 20, "bold"))
        title_label.grid(row=0, column=0, columnspan=4, pady=20)

        row = 1
        for hari, jadwal in subjectSchedule.items():
            hari_label = ctk.CTkLabel(self.frame, text=hari, font=("Helvetica", 16, "bold"))
            hari_label.grid(row=row, column=0, columnspan=4, sticky="w", pady=10, padx=20)
            row += 1
            for mata_kuliah, dosen, waktu in jadwal:
                ctk.CTkLabel(self.frame, text=mata_kuliah, wraplength=550, justify="left").grid(row=row, column=0, sticky="w", padx=20)
                ctk.CTkLabel(self.frame, text=dosen, wraplength=550, justify="left").grid(row=row, column=1, sticky="w", padx=20)
                ctk.CTkLabel(self.frame, text=waktu, wraplength=550, justify="left").grid(row=row, column=2, sticky="w", padx=20)
                row += 1

        back_button = ctk.CTkButton(self.frame, text="Kembali", command=self.task_manager.showMainPage)
        back_button.grid(row=row, column=0, columnspan=4, pady=20)

        # Centering the frame content
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_rowconfigure(row, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_columnconfigure(1, weight=1)
        self.frame.grid_columnconfigure(2, weight=1)
        self.frame.grid_columnconfigure(3, weight=1)
