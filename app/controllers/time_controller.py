import time

class TimeController:
    def __init__(self,timelabel):
        self.timelabel = timelabel
        self.update_time()

    def update_time(self):
        self.timelabel.var.set(time.strftime("%H:%M:%S",time.localtime()))
        self.timelabel.master.after(1000,self.update_time)



