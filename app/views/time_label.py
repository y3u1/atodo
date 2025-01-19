import customtkinter as ctk
from tkinter import StringVar
from app.controllers.time_controller import TimeController

class TimeLabel(ctk.CTkLabel):
    def __init__(self,master):
        self.var = StringVar()
        super().__init__(master,textvariable=self.var,font=master.font)
        self.time_controller = TimeController(self)





