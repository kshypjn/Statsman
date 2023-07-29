from tkinter import *

tv = Tk()
tv.configure(bg="#121212")
tv.title("SportZilla")
tv.geometry("420x420")

def ScoreCard():
    tv.destroy()
    import cricketscorecard
def EnterStats():
    tv.destroy()
    import bat
    import bowl
def Topper():
    tv.destroy()
    import cricTop

tv.grid_rowconfigure(1,weight=1)
tv.grid_columnconfigure(1,weight=1)
heading = "Cricket".upper()
head = Label(tv, text=heading, font=('Fira Sans', 18), fg="White", bg="#B63A3A")
head.grid(row=0, column=1, columnspan=4, sticky="nesw")
head.grid_rowconfigure(2, weight=1)
head.grid_columnconfigure(2, weight=1)

add = Button(tv,text="Add Data",width=30,command=EnterStats, highlightbackground='black')
add.place(x=60,y=60)
score = Button(tv,text="View Scorecard",width=30,command=ScoreCard, highlightbackground='black')
score.place(x=60,y=120)
stat = Button(tv,text="View Stats",width=30,command=Topper, highlightbackground='black')
stat.place(x=60,y=180)

def bacc():
    tv.destroy()
    import landing

back = Button(tv, text="Back", command=bacc, width=20, highlightbackground='black')
back.place(x=100,y=240)
tv.mainloop()
