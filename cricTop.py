from tkinter import *
import matplotlib.pyplot as p

import mysql.connector as my
scale = Tk()
scale.configure(bg="#121212")
scale.title("SportZilla")
con = my.connect(host="localhost", user="root", passwd="kashyap07")
myCursor = con.cursor()


def batting():
    if con.is_connected():
        print("MySql DataBase is connected Successfully.")
        myCursor.execute("use statsman")
        qry = "SELECT NAME,RUNS,TEAM FROM BATSTATS order by runs desc limit 8"
        myCursor.execute(qry)
        runs = {}
        for x in myCursor:
            runs[x[0]] = x[1]

        # sns.barplot(x='player', y='runs', data=runs)
        p.title('Runs Scored')
        p.bar(runs.keys(), runs.values(), align='center', width=0.5, color=['#93C4D7'])
        p.xlabel('Player')
        p.ylabel('Runs')
        p.show()


def Bowling():
    if con.is_connected():
        print("MySql DataBase is connected Successfully.")
        myCursor.execute("use statsman")
        qry = "SELECT NAME,WICKETS,TEAM FROM BOWLSTATS order by wickets desc limit 7"
        myCursor.execute(qry)
        w = {}
        for x in myCursor:
            w[x[0]] = x[1]

        # sns.barplot(x='player', y='runs', data=runs)
        p.title('Wickets Taken')
        p.bar(w.keys(), w.values(), align='center', width=0.5, color=['blue'])
        p.xlabel('Player')
        p.ylabel('Wickets',labelpad=int())
        p.show()


def teamBat():
    if con.is_connected():
        print("MySql DataBase is connected Successfully.")
        myCursor.execute("use statsman")
        qry = "SELECT NAME,runs,TEAM FROM BATSTATS order by runs desc"
        myCursor.execute(qry)
        data = {}
        for x in myCursor:
            data[x[2]] = 0
        qry = "SELECT NAME,runs,TEAM FROM BATSTATS order by runs desc"
        myCursor.execute(qry)
        for y in myCursor:
            print(y)
            data[y[2]] += y[1]
        print(data)
        p.title('Runs Per Team')
        p.bar(data.keys(), data.values(), align='center', width=0.5, color=['purple'])
        p.xlabel('Team')
        p.ylabel('Runs')
        p.show()
        con.commit()


def teamBowl():
    if con.is_connected():
        print("MySql DataBase is connected Successfully.")
        myCursor.execute("use statsman")
        qry = "SELECT NAME,wickets,TEAM FROM BowlSTATS order by wickets desc"
        myCursor.execute(qry)
        data = {}
        for x in myCursor:
            data[x[2]] = 0
        qry = "SELECT NAME,wickets,TEAM FROM Bowlstats order by wickets desc"
        myCursor.execute(qry)
        for y in myCursor:
            print(y)
            data[y[2]] += y[1]
        print(data)
        p.title('Wickets Per Team')
        p.bar(data.keys(), data.values(), align='center', width=0.4, color=['pink'])
        p.xlabel('Team')
        p.ylabel('Wickets')
        p.show()
        con.commit()




def mostRuns():
    scale.destroy()
    tv = Tk()
    tv.configure(bg="#121212")
    tv.title("SportZilla")
    """sb = Scrollbar(tv)
    sb.grid(column,side=RIGHT, fill=Y)"""
    Header = Label(tv, text="MOST RUNS")
    Header.grid(row=0, column=0, columnspan=3)

    if con.is_connected():
        print("MySql DataBase is connected Successfully.")
        myCursor.execute("use statsman")
        qry = "SELECT NAME,RUNS,TEAM FROM BATSTATS order by runs desc"
        myCursor.execute(qry)

        t1 = "   NAME\t"
        t2 = "   RUNS\t"
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

    g = Button(tv, text="graph", command=batting)
    g.grid()


    tv.mainloop()

def mostWickets():
    scale.destroy()
    tv = Tk()
    tv.configure(bg="#121212")
    tv.title("SportZilla")
    Header = Label(tv, text="MOST WICKETS")
    Header.grid(row=0, column=0, columnspan=3)

    if con.is_connected():
        print("MySql DataBase is connected Successfully.")
        myCursor.execute("use statsman")
        qry = "SELECT NAME,WICKETS,TEAM FROM BowlSTATS order by wickets desc"
        myCursor.execute(qry)

        t1 = "   NAME\t"
        t2 = "   WICKETS\t"
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
    #Bowling()
    g = Button(tv, text="graph", command=Bowling)
    g.grid()


    tv.mainloop()




bat = Button(scale, command=mostRuns, text='Battting Individual')
bat.grid()
bowl = Button(scale, command=mostWickets, text='Bowling Individual')
bowl.grid()
teamBat = Button(scale, command=teamBat, text='Batting Team')
teamBat.grid()
teamBowl = Button(scale, command=teamBowl, text='Bowling Team')
teamBowl.grid()

def bacc():
    scale.destroy()
    import cricket


back = Button(scale, text="Back", command=bacc, width=14)
back.grid(row=4, column=0, padx=10, pady=10, columnspan=3)
scale.mainloop()
