from tkinter import *

tv = Tk()
tv.configure(bg="#121212")
tv.title("SportZilla")
tv.geometry("420x420")


def EnterStats():
    tv.destroy()
    import hockeyAdd


def scoring():
    tv.destroy()
    import hockeyScore


def stats():
    tv.destroy()
    import HockeyTop


tv.grid_rowconfigure(1, weight=1)
tv.grid_columnconfigure(1, weight=1)
heading = "HOCKEY"
head = Label(tv, text=heading, font=('Fira Sans', 18), fg="White", bg="#3CB371")
head.grid(row=0, column=1, columnspan=4, sticky="nesw")
head.grid_rowconfigure(2, weight=1)
head.grid_columnconfigure(2, weight=1)

add = Button(tv, text="Add Data", width=30,command=EnterStats, highlightbackground='black')
add.place(x=60, y=60)
score = Button(tv, text="View Scorecard", width=30,command=scoring, highlightbackground='black')
score.place(x=60, y=120)
stat = Button(tv, text="View Stats", width=30,command=stats, highlightbackground='black')
stat.place(x=60, y=180)

def bacc():
    tv.destroy()
    import landing


back = Button(tv, text="Back", command=bacc, width=20, highlightbackground='black')
back.place(x=100,y=240)
tv.mainloop()
