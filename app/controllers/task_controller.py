from app.module.tasks import Tasks
from app.utils import rand_color
from app.views.task import Task


class TaskController:
    def __init__(self,taskbox):
        self.taskbox = taskbox
        self.value = Tasks()

    def add_task_event(self, event):
        content = event.widget.get("0.0","end-1c").strip()
        if not content:
            return
        self.add_task(content)
        event.widget.delete("0.0","end-1c")

    def add_task(self,content):
        t = Task(self.taskbox, row=len(self.value.tasks), text=content, finish=False)
        self.value.tasks.append(t)



    # 删除一个任务,对其后面的任务更新位置
    def delete_task_event(self, event):
        #if isinstance(event.widget, tk.Label):
        index = event.widget.grid_info()["in"].row
        size = len(self.value.tasks)
        for i in range(index + 1, size):
            self.value.tasks[i].grid(row=i - 1, column=0, padx=10, pady=2, sticky="ew")
            self.value.tasks[i].row = i - 1
        tmp = self.value.tasks.pop(index)
        tmp.destroy()



    #完成一个任务
    def finish_task_event(self,event):
        tsk = event.widget
        finish = tsk.grid_info()["in"].finish
        index = tsk.grid_info()["in"].row
        if not finish:
            self.value.tasks[index].finish = True
            self.finish_task(index)
        else:
            self.value.tasks[index].finish = False
            self.value.tasks[index].configure(fg_color=rand_color())

    def finish_task(self,index):
        self.value.tasks[index].configure(fg_color="#BEBEBE")

    def saving(self) -> list:
        data = [ (i.cget('text'),i.finish) for i in self.value.tasks ]
        return data
    def resume(self,data:list):
        for i in data:
            t = Task(self.taskbox, row=len(self.value.tasks), text=i[0], finish=i[1])
            self.value.tasks.append(t)
