from tkinter import *

import mysql.connector as my

window = Tk()
window.configure(bg="#121212")
window.title("Bowling")

con = my.connect(host="localhost", user="root", passwd="kashyap07")
myCursor = con.cursor()

# Label and Entry
MatchName = Label(window, text="TeamsPlaying:", width=14, bg="#B63A3A")
iMatchName = Entry(window, width=14)
tName = Label(window, text="Name", width=14, bg="#B63A3A")
iName = Entry(window, width=14)
tOvers = Label(window, text="Overs", width=14, bg="#B63A3A")
iOvers = Entry(window, width=14)
tRuns = Label(window, text="Runs", width=14, bg="#B63A3A")
iRuns = Entry(window, width=14)
tTeam = Label(window, text="Team", width=14, bg="#B63A3A")
iTeam = Entry(window, width=14)
tWick = Label(window, text="Wickets", width=14, bg="#B63A3A")
iWick = Entry(window, width=14)
# grid
MatchName.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
iMatchName.grid(row=0, column=3, padx=10, pady=10)
tName.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
iName.grid(row=1, column=3, padx=10, pady=10)
tOvers.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
iOvers.grid(row=2, column=3, padx=10, pady=10)
tRuns.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
iRuns.grid(row=3, column=3, padx=10, pady=10)
tTeam.grid(row=5, column=0, columnspan=2, padx=10, pady=10)
iTeam.grid(row=5, column=3, padx=10, pady=10)
tWick.grid(row=4, column=0, padx=10, pady=10)
iWick.grid(row=4, column=3, padx=10, pady=10)


def clr():
    match = iMatchName.get().upper() + "bowl"
    n = iName.get().title()
    r = int(iRuns.get())
    o = float(iOvers.get())
    t = iTeam.get().upper()
    w = int(iWick.get())

    iTeam.delete(0, END)
    iName.delete(0, END)
    iOvers.delete(0, END)
    iRuns.delete(0, END)
    iWick.delete(0, END)
    econ = (r / o)
    data = []
    if con.is_connected():
        print("MySql DataBase is connected Successfully.")
        myCursor.execute("use statsman")
        qry = "CREATE TABLE if not exists Bowlstats (Name varchar(20),Wickets numeric(4),Team varchar(255))"
        myCursor.execute(qry)
        myCursor.execute(
            "create table if not exists {}(Name varchar(20),Overs numeric(3,1),Runs numeric(2),Wickets numeric(2),"
            "Economy numeric(5,2),Team varchar(255))".format(match))
        creation = "CREATE TABLE if not exists CRIC (NAME VARCHAR(255),TEAM VARCHAR(255))"
        myCursor.execute(creation)
        con.commit()
        sql2 = "INSERT INTO {} (Name,Overs,Runs,Wickets,Economy,Team) VALUES (%s,%s, %s,%s,%s,%s)".format(match)
        val = (n, o, r, w, econ, t)
        myCursor.execute(sql2, val)

        con.commit()
        sell = "SELECT NAME,WICKETS,TEAM FROM bowlstats"
        myCursor.execute(sell)
        names = {}
        for x in myCursor:
            names[x[0]] = x[1]

        if n in names:
            sqr = "update bowlstats set wickets = {} where name ='{}'".format(w + names[n], n)
            myCursor.execute(sqr)
            con.commit()
        else:
            sk = "insert into bowlstats (Name,Wickets,Team) values (%s,%s,%s)"
            vad = (n, w, t)
            myCursor.execute(sk, vad)
            con.commit()

        s = "SELECT * FROM CRIC"
        myCursor.execute(s)
        if len(list(myCursor)) == 0:
            key = "insert into cric (Name,Team) values (%s,%s)"
            inside = (n, t)
            myCursor.execute(key, inside)
            con.commit()
            data.append(n)
        else:
            for player in myCursor:
                print(player)
                if player[0] != n:
                    key = "insert into cric (Name,Team) values (%s,%s)"
                    inside = (n, t)
                    myCursor.execute(key, inside)
                    con.commit()
                    data.append(n)
                else:
                    pass

        con.commit()


def close():
    window.destroy()

    print("done")


nxt = Button(window, text='Next', width=14, command=clr, highlightbackground='black')
nxt.grid(row=6, column=3, padx=10, pady=10)


def bacc():
    window.destroy()
    import cricket


back = Button(window, text="Back", command=bacc, width=14, highlightbackground='black')
back.grid(row=7, column=0, padx=10, pady=10)
cls = Button(window, text='Close', width=14, command=close, highlightbackground='black')
cls.grid(row=7, column=3, padx=10, pady=10)

window.mainloop()
