from tkinter import *

import mysql.connector as my

window = Tk()
window.configure(bg="#121212")
window.title("Batting")

con = my.connect(host="localhost", user="root", passwd="kashyap07")
myCursor = con.cursor()
curse = con.cursor()

MatchName = Label(window, text="TeamsPlaying:", width=14, bg="#B63A3A")
iMatchName = Entry(window, width=14)
tName = Label(window, text="Name", width=14, bg="#B63A3A")
iName = Entry(window, width=14)
tRuns = Label(window, text="Runs Scored", width=14, bg="#B63A3A")
iRuns = Entry(window, width=14)
tBalls = Label(window, text="Balls Played", width=14, bg="#B63A3A")
iBalls = Entry(window, width=14)
tTeam = Label(window, text="Team", width=14, bg="#B63A3A")
iTeam = Entry(window, width=14)
tExtra = Label(window, text="Extras", width=14, bg="#B63A3A")
iExtra = Entry(window, width=14)
MatchName.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
iMatchName.grid(row=0, column=3, padx=10, pady=10)
tName.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
iName.grid(row=1, column=3, padx=10, pady=10)
tRuns.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
iRuns.grid(row=2, column=3, padx=10, pady=10)
tBalls.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
iBalls.grid(row=3, column=3, padx=10, pady=10)
tTeam.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
iTeam.grid(row=4, column=3, padx=10, pady=10)
tExtra.grid(row=5, column=0, padx=10, pady=10)
iExtra.grid(row=5, column=3, padx=10, pady=10)

data = []

def clr():
    match = iMatchName.get().upper() + "bat"
    n = iName.get().title()
    r = int(iRuns.get())
    b = int(iBalls.get())
    t = iTeam.get().upper()
    e = iExtra.get()
    data.append([n, r])
    iTeam.delete(0, END)
    iName.delete(0, END)
    iBalls.delete(0, END)
    iRuns.delete(0, END)
    iExtra.delete(0, END)
    try:
        stRate = float(100 * (r / b))
    except ZeroDivisionError:
        r = 0
        b = 0
        stRate = 0.0

    if con.is_connected():
        myCursor.execute("use statsman")
        qry = "CREATE TABLE if not exists Batstats (Name varchar(20),Runs numeric(4),Team varchar(255))"
        myCursor.execute(qry)
        one = "create table if not exists {}(Name varchar(20),Runs numeric(3),BallsPlayed numeric(3),StrikeRate " \
              "numeric(5,2),Team varchar(255),Extras decimal NOT NULL default 0)".format(match)
        myCursor.execute(one)

        con.commit()
        sql = "INSERT INTO {} (Name,Runs,BallsPlayed,StrikeRate,Team,Extras) VALUES (%s, %s,%s,%s,%s,%s)".format(match)
        val = (n, r, b, stRate, t, e)
        myCursor.execute(sql, val)
        con.commit()
        sell = "SELECT NAME,RUNS,TEAM FROM batstats"
        myCursor.execute(sell)
        names = {}
        for x in myCursor:
            names[x[0]] = x[1]

        if n in names:

            sqr = "update batstats set runs = {} where name ='{}'".format(r + names[n], n)

            myCursor.execute(sqr)
            con.commit()
        else:
            sk = "insert into batstats (Name,Runs,Team) values (%s,%s,%s)"
            vad = (n, r, t)
            myCursor.execute(sk, vad)
            con.commit()
        creation = "CREATE TABLE if not exists CRIC (Name varchar(20),Team varchar(255))"
        myCursor.execute(creation)
        reading = "SELECT NAME FROM CRIC"
        myCursor.execute(reading)
        for playa in myCursor:
            if len(list(myCursor)) == 0:
                key = "insert into cric (Name,Team) values (%s,%s)"
                inside = (n, t)
                myCursor.execute(key, inside)
                con.commit()
                data.append(n)
            elif n in list(myCursor):
                pass
            else:
                key = "insert into cric (Name,Team) values (%s,%s)"
                inside = (n, t)
                myCursor.execute(key, inside)
        con.commit()

def close():
    window.destroy()
    print("done")
def bacc():
    window.destroy()
    import cricket

nxt = Button(window, text='Next', width=14, command=clr, highlightbackground='black')
nxt.grid(row=6, column=3, padx=10, pady=10)
back = Button(window, text="Back", command=bacc, width=14, highlightbackground='black')
back.grid(row=7, column=0, padx=10, pady=10)
cls = Button(window, text='Close', width=14, command=close, highlightbackground='#c92a2a')
cls.grid(row=7, column=3)

window.mainloop()
