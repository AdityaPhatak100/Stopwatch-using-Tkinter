from tkinter import *

class Stopwatch:
    def start(self):
        self.seconds = self.minutes = self.hours = 0
        self.label = label
        self.lap_frame = lap_frame
        start_button.config(state='disabled')
        lap_button.config(state='active')
        stop_button.config(state='active')
        self.update_bool = True
        self.count = 1
        self.update()

    def update(self):
        if self.update_bool:
            self.label.config(text = '%.2d:%.2d:%.2ds' % (self.hours, self.minutes, self.seconds))
            self.seconds+=1

            if self.seconds<60:
                self.label.after(995,self.update)

            elif self.seconds >=60 and self.minutes < 60:
                self.seconds = 0
                self.minutes+=1
                self.label.after(995,self.update)

            if self.minutes >= 60:
                self.minutes = 0
                self.hours+=1

    def stop(self):
        self.update_bool = False 
        reset_button.config(state='active')
        stop_button.config(state='disabled')
        lap_button.config(state='disabled')

    
    def reset(self):
        self.count = 1
        self.seconds = self.minutes = self.hours = 0
        start_button.config(state='active')
        lap_button.config(state='disabled')
        reset_button.config(state='disabled')
        stop_button.config(state='disabled')
        self.label.config(text = '%.2d:%.2d:%.2ds' % (self.hours, self.minutes, self.seconds))
        # clearing previous entries in the lap frame 
        for widget in self.lap_frame.winfo_children():
            widget.destroy()
        self.lap_frame.pack_forget()

    def lap(self):
        self.lap_frame.pack(side='left')
        if self.seconds-1>=0: # number of laps can be changed.
            lap_label = Label(lap_frame,text='%d. %.2d:%.2d:%.2ds' % (self.count,self.hours, self.minutes, self.seconds-1),font='12',)
            lap_label.pack()
            self.count+=1
            if self.count>10:
                lap_button.config(state='disabled')
        else:
            pass


s=Stopwatch()


root = Tk()

label = Label(root,text='00:00:00s',font= 'Arial 74 bold',foreground='white',background='black',width=8)
button_frame = Frame(root)
lap_frame = Frame(root)
start_button = Button(button_frame,text='Start',width=16,height=1,relief='raised',bd=3 ,command=s.start)
stop_button = Button(button_frame,text='Stop',width=16,height=1,relief='raised',bd=3 ,state='disabled',command=s.stop)
reset_button = Button(button_frame,text='Reset',width=16,height=1,relief='raised',bd=3 ,state='disabled',command=s.reset)
lap_button = Button(button_frame,text='Lap',width=16,height=1,relief='raised',bd=3 ,state='disabled',command=s.lap)

label.pack()
start_button.grid(row=1,column=1)
stop_button.grid(row=1,column=2)
reset_button.grid(row=1,column=3)
lap_button.grid(row=1,column=4)
button_frame.pack()

root.mainloop()