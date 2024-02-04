from tkinter import *
import datetime
def date_time():
    time=datetime.datetime.now()
    hr=time.strftime("%I")
    min=time.strftime("%M")
    sec=time.strftime("%S")
    am=time.strftime("%p")
    lab_hr.config(text=hr)
    lab_min.config(text=min)
    lab_sec.config(text=sec)

    lab_hr.after(200,date_time)
clock=Tk()
clock.title('##############DIGITAL CLOCK###############')
clock.config(bg='purple')
lab_hr=Label(clock,text="00",font=("Time new Roman",60,"bold"),bg="black",fg="white")
lab_hr.place(x=50,y=50,height=100,width=100)
lab_min=Label(clock,text="00",font=("Time new Roman",60,"bold"),bg="black",fg="white")

lab_min.place(x=150,y=150,height=100,width=100)
lab_sec=Label(clock,text="00",font=("Time new Roman",60,"bold"),bg="black",fg="white")

lab_sec.place(x=250,y=250,height=100,width=100)
date_time()

clock.mainloop()


