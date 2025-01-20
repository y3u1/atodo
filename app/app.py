import json

import customtkinter as ctk
from app.views.task_textbox import TaskTextBox
from app.views.taskbox import TaskBox
from app.views.time_label import TimeLabel


class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Atodo")
        self.geometry("400x400")

        self.widgets = []
        self.last_row=-1
        self.grid_rowconfigure(0,weight=1)
        self.grid_columnconfigure(0,weight=1)

        """ 初始化组件 """
        # 定义字体
        self.font = ctk.CTkFont(family="微软雅黑")

        # 任务容器
        self.taskbox = TaskBox(self,width=300,height=400)
        self.taskbox.grid(row=self.rowgener(),column=0,padx=5, pady=2, sticky="nsew")
        self.widgets.append(self.taskbox)

        # 用于显示时间
        self.timelabel = TimeLabel(self)
        self.timelabel.grid(row=self.rowgener(), column=0, padx=8, pady=1, sticky="new")
        self.widgets.append(self.timelabel)

        # 用于添加任务
        self.task_textbox = TaskTextBox(self,width=400,height=20)
        self.task_textbox.grid(row=self.rowgener(),column=0,padx=8,pady=(1,10),sticky="new")
        self.widgets.append(self.task_textbox)

        """读取数据"""
        self.resume_data()


    def rowgener(self):
        self.last_row = self.last_row + 1
        return self.last_row


    def resume_data(self):
        try:
            with open('data.json', 'r') as f:
                data = json.load(f)
                for widget in self.widgets:
                    if hasattr(widget, 'controller') and hasattr(widget.controller, 'resume'):
                        k = type(widget).__name__
                        if k in data:
                            widget.controller.resume(data[k])
        except:
            pass

    def save_data(self):
        data = {}
        for widget in self.widgets:
            if hasattr(widget, 'controller') and hasattr(widget.controller, 'value'):
                k = type(widget).__name__
                d = widget.controller.saving()
                data[k] = d
        with open('data.json', 'w') as f:
            json.dump(data, f)

    def destroy(self):
        # 销毁之前
        self.save_data()
        super().destroy()
