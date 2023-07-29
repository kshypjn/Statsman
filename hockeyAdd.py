from tkinter import *
from tkinter import Entry

import mysql.connector as my

window = Tk()
window.configure(bg="#121212")
window.title("Hockey")

con = my.connect(host="localhost", user="root", passwd="kashyap07")
myCursor = con.cursor()
curse = con.cursor()

# Label and Entry
HomeTeam = Label(window, text="HomeTeam:", width=14, bg="#3CB371")
iHomeTeam = Entry(window, width=14)
AwayTeam = Label(window, text="AwayTeam:", width=14, bg="#3CB371")
iAwayTeam = Entry(window, width=14)
tName = Label(window, text="Name", width=14, bg="#3CB371")
iName = Entry(window, width=14)
tGoals = Label(window, text="Goals Scored", width=14, bg="#3CB371")
iGoals = Entry(window, width=14)
tCleansheet = Label(window, text="Clean Sheets", width=14, bg="#3CB371")
iCleansheet = Entry(window, width=14)
tTeam = Label(window, text="Team", width=14, bg="#3CB371")
iTeam = Entry(window, width=14)

# grid
HomeTeam.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
iHomeTeam.grid(row=0, column=3, padx=10, pady=10)
AwayTeam.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
iAwayTeam.grid(row=1, column=3, columnspan=2, padx=10, pady=10)
tName.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
iName.grid(row=2, column=3, padx=10, pady=10)
tGoals.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
iGoals.grid(row=3, column=3, padx=10, pady=10)
tCleansheet.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
iCleansheet.grid(row=4, column=3, padx=10, pady=10)
tTeam.grid(row=5, column=0, columnspan=2, padx=10, pady=10)
iTeam.grid(row=5, column=3, padx=10, pady=10)
data = []


def clr():
    match = iHomeTeam.get().upper() + iAwayTeam.get().upper()+"hock"
    print(match)
    n = iName.get().title()
    g = int(iGoals.get())
    cs = int(iCleansheet.get())
    t = iTeam.get().upper()
    iTeam.delete(0, END)
    iName.delete(0, END)
    iCleansheet.delete(0, END)
    iGoals.delete(0, END)

    if con.is_connected():
        myCursor.execute("use statsman")
        go = "CREATE TABLE if not exists HOCKEY (NAME VARCHAR(255),team varchar(250))"
        myCursor.execute(go)
        con.commit()
        qry = "CREATE TABLE if not exists HockStats (Name varchar(20),Goals numeric(4),CleanSheets numeric(4)," \
              "Team varchar(255)) "
        myCursor.execute(qry)
        one = "create table if not exists {}(Name varchar(20),Goals numeric(3),CleanSheets numeric(3) default 0," \
              "Team varchar(255))".format(match)
        myCursor.execute(one)
        con.commit()
        sql = "INSERT INTO {} (Name,Goals,CleanSheets,Team) VALUES (%s,%s,%s,%s)".format(match)
        val = (n, g, cs, t)
        myCursor.execute(sql, val)
        con.commit()
        sell = "SELECT * FROM Hockstats"
        myCursor.execute(sell)
        names = {}
        for x in myCursor:
            names[x[0]] = x[1]

        if n in names:
            sqr = "update hockstats set GOALS = {} where name ='{}'".format(g + names[n], n)
            myCursor.execute(sqr)
            con.commit()
        else:
            sk = "insert into hockstats (Name,Goals,CleanSheets,Team) values (%s,%s,%s,%s)"
            vad = (n, g, cs, t)
            print(sk, vad)
            myCursor.execute(sk, vad)
            con.commit()

        s = "SELECT * FROM Hockey"
        myCursor.execute(s)
        print(list(myCursor))
        if len(list(myCursor)) == 0:
            key = "insert into Hockey (Name,Team) values (%s,%s)"
            inside = (n, t)
            myCursor.execute(key, inside)
            con.commit()
            data.append(n)
        else:
            for player in myCursor:
                print(player)
                if player[0] != n:
                    key = "insert into Hockey (Name,Team) values (%s,%s)"
                    inside = (n, t)
                    myCursor.execute(key, inside)
                    con.commit()
                    data.append(n)
                else:
                    pass

        """drop = "DROP TABLE FOOTY"
        myCursor.execute(drop)
        con.commit()"""
        con.commit()


def close():
    window.destroy()

    print("done")


nxt = Button(window, text='Next', width=14, command=clr)
nxt.grid(row=6, column=3, padx=10, pady=10)
cls = Button(window, text='Close', width=14, command=close)
cls.grid(row=7, column=3, padx=10, pady=10)
window.mainloop()
