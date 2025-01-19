import customtkinter as ctk
from app.utils import rand_color

class Task(ctk.CTkLabel):
    def __init__(self,master:ctk.CTk,row:int,text:str,finish:bool):
        super().__init__(master,text=text)
        self.finish = finish
        self.row = row

        self.configure(corner_radius=6)
        self.configure(fg_color=rand_color())
        self.configure(text_color="black")

        self.grid(row=row, column=0, padx=10, pady=2, sticky="ew")
        self.bind("<Double-Button-3>",master.task_controller.delete_task)
        self.bind("<Button-1>", master.task_controller.finish_task)

