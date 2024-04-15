from tkinter import *
from datetime import datetime

temp = 0
after_id = ''


def tick():
    global temp, after_id
    after_id = root.after(1000, tick)
    f_temp = datetime.fromtimestamp(temp).strftime('%M:%S')
    label1.configure(text=str(f_temp))
    temp += 1

def start_tick():
    btnStart.pack_forget()
    btnStop.pack()
    tick()

def stop_tick():
    btnStop.pack_forget()
    btnCont.pack()
    btnReplay.pack()
    root.after_cancel(after_id)

def continue_tick():
    btnCont.pack_forget()
    btnReplay.pack_forget()
    btnStop.pack()
    tick()

def replay_tick():
    global temp
    temp = 0
    label1.configure(text='00:00')
    btnReplay.pack_forget()
    btnStart.pack()

root = Tk()
root.title('Секундомер')
root.resizable(width=False, height=False)
root.geometry('350x150')

label1 = Label(root, width=10, font=('Silkscreen [Rus by Mr.Enot]', 30), text='00:00')
label1.pack()

btnStart = Button(root, text='Старт', font=('Silkscreen [Rus by Mr.Enot]', 20), width=15, command=start_tick)
btnStop = Button(root, text='Стоп', font=('Silkscreen [Rus by Mr.Enot]', 20), width=15, command=stop_tick)
btnCont = Button(root, text='Продолжить', font=('Silkscreen [Rus by Mr.Enot]', 20), width=15, command=continue_tick)
btnReplay = Button(root, text='Сброс', font=('Silkscreen [Rus by Mr.Enot]', 20), width=15, command=replay_tick)

btnStart.pack()
                                            
root.mainloop()
