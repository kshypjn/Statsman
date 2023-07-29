from tkinter import *
import mysql.connector as mcon

con = mcon.connect(host="localhost", user="root", passwd="kashyap07")
myCursor = con.cursor()

tv = Tk()
tv.configure(bg="#121212")
tv.title("SportZilla")

def scoreBat():
    match = iMatchName.get()
    tName = teamEntry.get().upper()
    wTeam = bowlTeamEntry.get().upper()
    submit.destroy()
    teamEntry.destroy()
    teamName.destroy()
    bowlTeam.destroy()
    bowlTeamEntry.destroy()
    MatchName.destroy()
    iMatchName.destroy()
    if con.is_connected():
        print("MySql DataBase is connected Successfully.")
        myCursor.execute("use statsman")
        q = "select Name,Runs,BallsPlayed,StrikeRate,Extras from {} where Team='{}'".format(match + "bat", tName)

        myCursor.execute(q)

        i = 1
        t1 = "   NAME\t"
        t2 = "   RUNS\t"
        t4 = "  BALLS PLAYED\t"
        t3 = "   STRIKE RATE"
        head = Label(tv, width=14, fg='yellow', text=t1, bg="#B63A3A")
        head.grid(row=0, column=0)
        head2 = Label(tv, width=14, fg='yellow', text=t2, bg="#B63A3A")
        head2.grid(row=0, column=1)
        head4 = Label(tv, width=14, fg='yellow', text=t4, bg="#B63A3A")
        head4.grid(row=0, column=2)
        head3 = Label(tv, width=14, fg='yellow', text=t3, bg="#B63A3A")
        head3.grid(row=0, column=3)
        runs, sc, c, ext = 0, ' ', -2, 0

        for player in myCursor:
            runs += int(player[1])

            ext += int(player[4])
            c += 1
            for j in range(len(player) - 1):
                w = Label(tv, width=14, text=player[j], fg='pink')
                w.grid(row=i, column=j)


            i = i + 1
        sc = f"Total: {runs + ext}/{c}"
        e = f"Extras:{ext}"
        tscore = Label(tv, text=sc, width=42, bg="#B63A3A")
        extras = Label(tv, text=e, width=42, bg="#B63A3A")
        extras.grid(row=i + 1, column=0, columnspan=4)
        tscore.grid(row=i + 2, column=0, columnspan=4)

        q2 = "select Name,Overs,Runs,Wickets,Economy from {} where Team='{}'".format(match + "bowl", wTeam)
        myCursor.execute(q2)
        tt1 = "   NAME\t"
        tt2 = "   OVERS\t"
        tt4 = "  RUNS\t"
        tt3 = "   WICKETS\t"
        tt5 = "  ECONOMY"
        Whead1 = Label(tv, width=14, fg='yellow', text=tt1)
        Whead1.grid(row=i + 4, column=0)
        Whead2 = Label(tv, width=14, fg='yellow', text=tt2)
        Whead2.grid(row=i + 4, column=1)
        Whead4 = Label(tv, width=14, fg='yellow', text=tt4)
        Whead4.grid(row=i + 4, column=2)
        Whead3 = Label(tv, width=14, fg='yellow', text=tt3)
        Whead3.grid(row=i + 4, column=3)
        Whead5 = Label(tv, width=14, fg='yellow', text=tt5)
        Whead5.grid(row=i + 4, column=4)
        k = i
        for sport in myCursor:
            print(sport)
            for r in range(len(sport)):
                w = Label(tv, width=14, text=sport[r], fg='pink')
                w.grid(row=k + 5, column=r)

            k += 1


MatchName = Label(tv, text="TeamsPlaying:", width=14)
iMatchName = Entry(tv, width=14)
teamName = Label(tv, text="BattingTeam:", width=14)
teamEntry = Entry(tv, width=14)
bowlTeam = Label(tv, text="BowlingTeam:", width=14)
bowlTeamEntry = Entry(tv, width=14)
MatchName.grid(row=0, column=0, padx=10, pady=10)
iMatchName.grid(row=0, column=1, padx=10, pady=10)
teamName.grid(row=1, column=0, padx=10, pady=10)
teamEntry.grid(row=1, column=1, padx=10, pady=10)
bowlTeam.grid(row=2, column=0, padx=10, pady=10)
bowlTeamEntry.grid(row=2, column=1, padx=10, pady=10)
submit = Button(tv, text='submit', command=scoreBat, width=14)
submit.grid(row=3, column=0, padx=10, pady=10, columnspan=3)


def bacc():
    tv.destroy()
    import cricket
back = Button(tv, text="Back", command=bacc, width=14)
back.grid(row=4, column=0, padx=10, pady=10, columnspan=3)
tv.mainloop()
