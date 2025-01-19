import customtkinter as ctk

class TaskTextBox(ctk.CTkTextbox):
    def __init__(self,master,width=300,height=400):
        super().__init__(master,width=width,height=height,activate_scrollbars=False)
        self.bind("<Return>",master.taskbox.task_controller.add_task)