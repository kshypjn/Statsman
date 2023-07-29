from tkinter import *
from PIL import ImageTk, Image

board = Tk()
board.configure(bg="#121212")
board.title("Statsman")
board.geometry("450x450")
def cric():
    board.destroy()
    import cricket
def footy():
    board.destroy()
    import football
def hockey():
    board.destroy()
    import hockey

def basketb():
    board.destroy()
    import basket
heading = "Welcome To Statsman!"
sp = "Select Sport"
head = Label(board, text=heading, font=('Fira Sans', 18), fg="White", bg="#B63A3A")
head.place(x=233, y=30, anchor="center")
sport = Label(board, text=sp, font=('Fira Sans', 18), fg="#4B5EA3", bg="#A7FFB5")
sport.place(x=280, anchor="e", y=86)

canvas = Canvas(board, width = 125, height = 140)
img= (Image.open("/Users/kashyapj/Desktop/12th/pyBoard/foot.png"))
resized_image= img.resize((125,120), Image.ANTIALIAS)
new_image= ImageTk.PhotoImage(resized_image)
canvas.place(x=143, y=216, anchor='e')
canvas.create_image(0,0, anchor=NW, image=new_image)
football = Button(canvas, text="Football", command=footy, highlightbackground='#343a40')
football.place(x=100, y=134, anchor='e', width=70)

can = Canvas(board, width = 125, height = 140)
c= (Image.open("/Users/kashyapj/Desktop/12th/pyBoard/ipl.png"))
cricket_image= c.resize((125,120), Image.ANTIALIAS)
new= ImageTk.PhotoImage(cricket_image)
can.place(x=289, y=216, anchor='e')
can.create_image(0,0, anchor=NW, image=new)
cricket = Button(can, text="Cricket", command=cric, highlightbackground='#343a40')
cricket.place(x=100, y=134, anchor='e', width=70)

canvashockey = Canvas(board, width = 125, height = 140)
hock= (Image.open("/Users/kashyapj/Desktop/12th/pyBoard/hockey.png"))
h_image= hock.resize((125,120), Image.ANTIALIAS)
hockeyimage= ImageTk.PhotoImage(h_image)
canvashockey.place(x=429, y=216, anchor='e')
canvashockey.create_image(0,0, anchor=NW, image=hockeyimage)
h = Button(canvashockey, text="Hockey", command=hockey, highlightbackground='#343a40')
h.place(x=100, y=134, anchor='e', width=70)



board.mainloop()
