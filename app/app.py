import customtkinter as ctk
from app.views.taskbox import TaskBox
from app.views.task_textbox import TaskTextBox
from app.views.time_label import TimeLabel


class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Atodo")
        self.geometry("400x400")
        self.last_row=-1
        self.grid_rowconfigure(0,weight=1)
        self.grid_columnconfigure(0,weight=1)
        # 定义字体
        self.font = ctk.CTkFont(family="微软雅黑")

        # 任务容器
        self.taskbox = TaskBox(self,width=300,height=400)
        self.taskbox.grid(row=self.rowgener(),column=0,padx=5, pady=2, sticky="nsew")
        # 用于显示时间
        self.timelabel = TimeLabel(self)
        self.timelabel.grid(row=self.rowgener(), column=0, padx=8, pady=1, sticky="new")
        # 用于添加任务
        self.task_textbox = TaskTextBox(self,width=400,height=20)
        self.task_textbox.grid(row=self.rowgener(),column=0,padx=8,pady=(1,10),sticky="new")

    def rowgener(self):
        self.last_row = self.last_row + 1
        return self.last_row