from tkinter import*
from tkinter import messagebox
win=Tk()
win.geometry("400x300")
win.title("python")
def clear():
    ent_fname.delete(0,END)
    ent_lname.delete(0,END) 
    ent_score.delete(0,END)
def exit():
    a=messagebox.askquestion("exit","are you sure to exit ")
    if a=="yes": 
        win.destroy()
def insert():
   score=int(ent_score.get())
   if score>=1000:
        a=insert=score*0.1
        p=score-a
   else:
        return("no score")
        messagebox.showinfo("insert",f" youe score is {p}")
    




print('*********************')
lbl_fname=Label(win,text="fname",font="calibri 14"fg = 'red')
lbl_fname.place(x=20,y=20)
ent_fname=Entry(win,font="calibri11")
ent_fname.place(x=70,y=20)
lbl_lname=Label(win,text="lname",font="calibri 11")
lbl_lname.place(x=20,y=50)
ent_lname=Entry(win,font="calibri11")
ent_lname.place(x=70,y=50)
lbl_score=Label(win,text="score",font="calibri 11")
lbl_score.place(x=20,y=80)
ent_score=Entry(win,font="calibri11")
ent_score.place(x=70,y=80)
btn_insert=Button(win,text="insert",font="calibri11",width= 10,command=insert)
btn_insert.pack(side=BOTTOM)
btn_clear=Button(win,text="clear",font="calibri 11",width= 10,command=clear)
btn_clear.pack(side=BOTTOM)
btn_exit=Button(win,text="exit",font="calibri11",width= 10,command=exit)
btn_exit.pack(side=BOTTOM)






win.mainloop()