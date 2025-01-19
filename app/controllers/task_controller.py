from app.views.task import Task
from app.utils import rand_color

class TaskController:
    def __init__(self,taskbox):
        self.taskbox = taskbox

    def add_task(self, event):
        content = event.widget.get("0.0","end-1c").strip()
        if not content:
            return
        event.widget.delete("0.0","end-1c")
        t = Task(self.taskbox, row=len(self.taskbox.tasks), text=content, finish=False)
        self.taskbox.tasks.append(t)


    # 删除一个任务,对其后面的任务更新位置
    def delete_task(self, event):
        #if isinstance(event.widget, tk.Label):
        index = event.widget.grid_info()["in"].row
        size = len(self.taskbox.tasks)
        for i in range(index + 1, size):
            self.taskbox.tasks[i].grid(row=i - 1, column=0, padx=10, pady=2, sticky="ew")
            self.taskbox.tasks[i].row = i - 1
        tmp = self.taskbox.tasks.pop(index)
        tmp.destroy()

    #完成一个任务
    def finish_task(self,event):
        tsk = event.widget
        finish = tsk.grid_info()["in"].finish
        index = tsk.grid_info()["in"].row
        if not finish:
            self.taskbox.tasks[index].finish = True
            self.taskbox.tasks[index].configure(fg_color="#BEBEBE")
        else:
            self.taskbox.tasks[index].finish = False
            self.taskbox.tasks[index].configure(fg_color=rand_color())
