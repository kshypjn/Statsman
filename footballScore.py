from tkinter import *
import mysql.connector as mcon

con = mcon.connect(host="localhost", user="root", passwd="kashyap07")
myCursor = con.cursor()

tv = Tk()
tv.configure(bg="#121212")
tv.title("Football")


def score():
    home = ihome.get().upper()
    away = iaway.get().upper()
    match = home + away
    print(match)
    submit.destroy()
    hometeam.destroy()
    ihome.destroy()
    awayteam.destroy()
    iaway.destroy()
    if con.is_connected():
        print("MySql DataBase is connected Successfully.")
        myCursor.execute("use statsman")

        goals = 0
        c = 0
        i = 0
        j = "SELECT NAME,GOALS,TEAM FROM {}".format(match)
        myCursor.execute(j)
        print(j)
        tt1 = "\t" + home + "\t"
        tt2 = "\t\t\t\tVS\t\t\t\t"
        tt4 = "\t" + away + "\t"

        Whead1 = Label(tv, width=14, fg='yellow', text=tt1)
        Whead1.grid(row=i + 4, column=0)
        Whead2 = Label(tv, width=14, fg='yellow', text=tt2)
        Whead2.grid(row=i + 4, column=1)
        Whead4 = Label(tv, width=14, fg='yellow', text=tt4)
        Whead4.grid(row=i + 4, column=2)
        g = Label(tv, width=8, fg='yellow', text="name")
        t = Label(tv, width=8, fg="yellow", text="goals")
        k, lol = i, i
        g.grid(row=i + 5, column=0)
        t.grid(row=i + 5, column=1)
        g2 = Label(tv, width=10, fg='yellow', text="name")
        t2 = Label(tv, width=10, fg="yellow", text="goals")
        g2.grid(row=i + 5, column=2)
        t2.grid(row=i + 5, column=3)
        f, f2 = 0, 0
        for player in myCursor:
            c += 1
            if player[2] == home:

                if player[1] > 0:
                    for r in range(len(player) - 1):
                        w = Label(tv, width=10, text=player[r], fg='pink')
                        w.grid(row=k + 6, column=r)
                    f += int(player[1])
                    print(f)
                    k += 1
            elif player[2] == away:

                if player[1] > 0:
                    for r in range(len(player) - 1):
                        w = Label(tv, width=10, text=player[r], fg='pink')
                        w.grid(row=lol + 6, column=r + 2)
                    f2 += int(player[1])
                    lol += 1
        s = str(f) + "\t\t" + str(f2)
        print(s)
        Final = Label(tv, text=s, width=30)
        Final.grid(row=k + 7, column=0, columnspan=4)
        if f>f2:
            res = f"{home} Defeated {away}!"
        elif f<f2:
            res = f"{away} Defeated {home}!"
        else:
            res = "Match Drawn!"
        result = Label(tv,text=res,width=25,bg='#800080')
        result.grid(row=k + 8, column=0, columnspan=4)


hometeam = Label(tv, text="Home Team:", width=14, bg="#800080")
ihome = Entry(tv, width=14)
awayteam = Label(tv, text="Away Team:", width=14, bg="#800080")
iaway = Entry(tv, width=14)
hometeam.grid(row=0, column=0, padx=10, pady=10)
ihome.grid(row=0, column=1, padx=10, pady=10)
awayteam.grid(row=1, column=0, padx=10, pady=10)
iaway.grid(row=1, column=1, padx=10, pady=10)

submit = Button(tv, text='submit', command=score, width=14)
submit.grid(row=3, column=0, padx=10, pady=10, columnspan=3)

tv.mainloop()
