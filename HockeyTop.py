
from tkinter import *
import mysql.connector as my
import matplotlib.pyplot as p
window = Tk()
window.configure(bg="#121212")
window.title("SportZilla")
con = my.connect(host="localhost", user="root", passwd="kashyap07")
myCursor = con.cursor()

def HGoalsGraph():
    if con.is_connected():
        print("MySql DataBase is connected Successfully.")
        myCursor.execute("use statsman")
        qry = "SELECT NAME,goals,TEAM FROM hockstats order by goals desc limit 8"
        myCursor.execute(qry)
        goals = {}
        for x in myCursor:
            goals[x[0]] = x[1]

        # sns.barplot(x='player', y='runs', data=runs)
        p.title('Goals Scored')
        p.bar(goals.keys(), goals.values(), align='center', width=0.5, color=['#93C4D7'])
        p.xlabel('Player')
        p.ylabel('Goals')
        p.show()


def HCSgraph():
    if con.is_connected():
        print("MySql DataBase is connected Successfully.")
        myCursor.execute("use statsman")
        qry = "SELECT NAME,cleansheets,TEAM FROM hockstats order by cleansheets desc limit 7"
        myCursor.execute(qry)
        w = {}
        for x in myCursor:
            w[x[0]] = x[1]

        # sns.barplot(x='player', y='runs', data=runs)
        p.title('Cleansheets')
        p.bar(w.keys(), w.values(), align='center', width=0.5, color=['blue'])
        p.xlabel('Player')
        p.ylabel('Cleansheets',labelpad=int())
        p.show()


def HmostGs():
    window.destroy()
    tv = Tk()
    tv.configure(bg="#121212")
    tv.title("SportZilla")
    """sb = Scrollbar(tv)
    sb.grid(column,side=RIGHT, fill=Y)"""
    Header = Label(tv, text="MOST GOALS")
    Header.grid(row=0, column=0, columnspan=3)

    if con.is_connected():
        print("MySql DataBase is connected Successfully.")
        myCursor.execute("use statsman")
        qry = "SELECT NAME,GOALS,TEAM FROM hockstats order by GOALS desc"
        myCursor.execute(qry)

        t1 = "   NAME\t"
        t2 = "   GOALS\t"
        t3 = "   TEAM"
        head = Label(tv, width=14, fg='orange', text=t1)
        head.grid(row=1, column=0)
        head2 = Label(tv, width=14, fg='orange', text=t2)
        head2.grid(row=1, column=1)
        head3 = Label(tv, width=14, fg='orange', text=t3)
        head3.grid(row=1, column=2)
        i = 2
        for player in myCursor:
            for j in range(len(player)):
                w = Label(tv, width=14, text=player[j], fg='pink')
                w.grid(row=i, column=j)
            i = i + 1


    g = Button(tv, text="graph",command=HGoalsGraph)
    g.grid()

    tv.mainloop()

def HmostCS():
    window.destroy()
    tv = Tk()
    tv.configure(bg="#121212")
    tv.title("SportZilla")
    Header = Label(tv, text="MOST CleanSheets")
    Header.grid(row=0, column=0, columnspan=3)

    if con.is_connected():
        print("MySql DataBase is connected Successfully.")
        myCursor.execute("use statsman")
        qry = "SELECT NAME,Cleansheets,TEAM FROM hockstats order by cleansheets desc"
        myCursor.execute(qry)

        t1 = "   NAME\t"
        t2 = "   CleanSheets\t"
        t3 = "   TEAM"
        head = Label(tv, width=14, fg='orange', text=t1)
        head.grid(row=1, column=0)
        head2 = Label(tv, width=14, fg='orange', text=t2)
        head2.grid(row=1, column=1)
        head3 = Label(tv, width=14, fg='orange', text=t3)
        head3.grid(row=1, column=2)
        i = 2
        for player in myCursor:
            for j in range(len(player)):
                w = Label(tv, width=14, text=player[j], fg='pink')
                w.grid(row=i, column=j)
            i = i + 1
    g = Button(tv, text="graph", command=HCSgraph)
    g.grid()

    tv.mainloop()



bat = Button(window, command=HmostGs, text='Goals')
bat.grid()
bowl = Button(window, command=HmostCS, text='Cleansheets')
bowl.grid()

window.mainloop()
