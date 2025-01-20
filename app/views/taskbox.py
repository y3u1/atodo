import customtkinter as ctk

from app.controllers.task_controller import TaskController


class TaskBox(ctk.CTkScrollableFrame):
    def __init__(self,master,width=400,height=400):
        super().__init__(master,width=width,height=height,label_font=master.font)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0,weight=1)

        self.configure(scrollbar_fg_color="transparent")
        self.configure(corner_radius=6)
        self.configure(fg_color="transparent")

        self.controller = TaskController(self)

