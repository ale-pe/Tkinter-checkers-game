from tkinter import *
fen = Tk()

  

#### var ####
choose = ""
turn = 1
scorea = 0
scoreb = 0
fen.title('Jeu')
fen.geometry("900x600")
title = StringVar()
title.set("Blancs 0 - 0 Noirs")
fen['bg']='#34495e' # couleur de fond
# fen.wm_attributes('-fullscreen','true')
# fen.overrideredirect(True)
# fen.deiconify()
Frame1 = Frame(fen,borderwidth=2,relief=GROOVE,bg="#2c3e50",bd=0)
# Frame1.grid()
Frame1.pack(side="top", fill="x")
Label(Frame1,textvariable=title,bg="#2c3e50",fg="white",font='Helvetica 13 bold').pack(padx=10,pady=10)
Frame2 = Frame(fen,borderwidth=2,relief=GROOVE,bg="#34495e",bd=0,width=100,heigh=10,)
Frame2.pack(side="top", fill="x")


######
can = Canvas(fen,width=800,heigh=500,bg='ivory')

can.pack()
can.create_rectangle(0,0,100,100,fill="#0F80FF",tags = "azer")
can.create_rectangle(0,100,100,200,fill="#0F80FF")
can.create_rectangle(0,200,100,300,fill="#0F80FF")
can.create_rectangle(0,300,100,400,fill="#0F80FF")
can.create_rectangle(0,400,100,500,fill="#0F80FF")
########
can.create_rectangle(100,0,200,100,fill="#8000FF")
can.create_rectangle(100,100,200,200,fill="#8000FF")
can.create_rectangle(100,200,200,300,fill="#8000FF")
can.create_rectangle(100,300,200,400,fill="#8000FF")
can.create_rectangle(100,400,200,500,fill="#8000FF")
########
can.create_rectangle(200,0,300,100,fill="#FC6666")
can.create_rectangle(200,100,300,200,fill="#FFFF66")
can.create_rectangle(200,200,300,300,fill="#FC6666")
can.create_rectangle(200,300,300,400,fill="#FFFF66")
can.create_rectangle(200,400,300,500,fill="#FC6666")
########
can.create_rectangle(300,0,400,100,fill="#FFFF66")
can.create_rectangle(300,100,400,200,fill="#FC6666")
can.create_rectangle(300,200,400,300,fill="#FFFF66")
can.create_rectangle(300,300,400,400,fill="#FC6666")
can.create_rectangle(300,400,400,500,fill="#FFFF66")
########
can.create_rectangle(400,0,500,100,fill="#FC6666")
can.create_rectangle(400,100,500,200,fill="#FFFF66")
can.create_rectangle(400,200,500,300,fill="#FC6666")
can.create_rectangle(400,300,500,400,fill="#FFFF66")
can.create_rectangle(400,400,500,500,fill="#FC6666")
########
can.create_rectangle(500,0,600,100,fill="#FFFF66")
can.create_rectangle(500,100,600,200,fill="#FC6666")
can.create_rectangle(500,200,600,300,fill="#FFFF66")
can.create_rectangle(500,300,600,400,fill="#FC6666")
can.create_rectangle(500,400,600,500,fill="#FFFF66")
########
can.create_rectangle(600,0,700,100,fill="#8000FF")
can.create_rectangle(600,100,700,200,fill="#8000FF")
can.create_rectangle(600,200,700,300,fill="#8000FF")
can.create_rectangle(600,300,700,400,fill="#8000FF")
can.create_rectangle(600,400,700,500,fill="#8000FF")
########
can.create_rectangle(700,0,800,100,fill="#118040")
can.create_rectangle(700,100,800,200,fill="#118040")
can.create_rectangle(700,200,800,300,fill="#118040")
can.create_rectangle(700,300,800,400,fill="#118040")
can.create_rectangle(700,400,800,500,fill="#118040")
# can.create_line(100, 0, 200, 50)
# can.create_line(100, 100, 200, 50)
# can.create_line(50, 0, 50, 100)

can.create_polygon(100, 0, 200, 50, 100, 100,fill='red', width=2)
can.create_polygon(100, 100, 200, 150, 100, 200,fill='red', width=2)
can.create_polygon(100, 200, 200, 250, 100, 300,fill='red', width=2)
can.create_polygon(100, 300, 200, 350, 100, 400,fill='red', width=2)
can.create_polygon(100, 400, 200, 450, 100, 500,fill='red', width=2)
###
can.create_polygon(700, 0, 700, 100, 600, 50,fill='red', width=2)
can.create_polygon(700, 100, 700, 200, 600, 150,fill='red', width=2)
can.create_polygon(700, 200, 700, 300, 600, 250,fill='red', width=2)
can.create_polygon(700, 300, 700, 400, 600, 350,fill='red', width=2)
can.create_polygon(700, 400, 700, 500, 600, 450,fill='red', width=2)

a1 = can.create_oval(30, 30, 70, 70, outline="#f11",fill="white", width=2,tags="a1",)
a2 = can.create_oval(30, 130, 70, 170, outline="#f11",fill="white", width=2,tags="a2")
a3 = can.create_oval(30, 230, 70, 270, outline="#f11",fill="white", width=2,tags="a3")
a4 =can.create_oval(30, 330, 70, 370, outline="#f11",fill="white", width=2,tags="a4")
a5 = can.create_oval(30, 430, 70, 470, outline="#f11",fill="white", width=2,tags="a5")

b1 = can.create_oval(730, 30, 770, 70, outline="#f11",fill="black", width=2,tags="b1",)
b2 = can.create_oval(730, 130, 770, 170, outline="#f11",fill="black", width=2,tags="b2")
b3 = can.create_oval(730, 230, 770, 270, outline="#f11",fill="black", width=2,tags="b3")
b4 =can.create_oval(730, 330, 770, 370, outline="#f11",fill="black", width=2,tags="b4")
b5 = can.create_oval(730, 430, 770, 470, outline="#f11",fill="black", width=2,tags="b5")

def move(x):
    global scorea
    global scoreb
    global choose
    global turn
    print(choose)
    for m in ["D", "G","H","B"]:
        try:
           can.delete(m)
        except:
            pass
    if x == "B":
        can.move(choose, 0,100)
    if x == "H":
        can.move(choose, 0,-100)
    if x == "D":
        can.move(choose, 100,0)
    if x == "G":
        can.move(choose, -100,0)
    
    if turn == 1 :
        for t in [b1,b2,b3,b4,b5]:
            print(can.coords(choose))
            print(can.coords(t))
            if can.coords(choose) == can.coords(t):
                can.delete(t)
                print('ooo')
                scorea = scorea+1
                title.set("Blancs "+str(scorea)+" - "+str(scoreb)+" Noirs")
        can.itemconfig(choose, fill='white')
        turn = 2
    else :
        for t in [a1,a2,a3,a4,a5]:
            print(can.coords(choose))
            print(can.coords(t))
            if can.coords(choose) == can.coords(t):
                can.delete(t)
                print('ooo')
                scoreb = scoreb+1
                title.set("Blancs "+str(scorea)+" - "+str(scoreb)+" Noirs")
        can.itemconfig(choose, fill='black')
        turn = 1


###### MOVE P1 #######
def selectpiona(x):
    global turn
    global choose
    for m in ["D", "G","H","B"]:
        try:
           can.delete(m)
        except:
            pass
    if turn == 1 :
        namep1 = ["a1","a2","a3","a4","a5"]
    else :
        namep1 = ["b1","b2","b3","b4","b5"]
    namep1.remove(x)
    print(namep1)
    choose = x
    can.itemconfig(x, fill='pink')
    for i in namep1:
        if turn == 1 :
            can.itemconfig(i, fill='white')
        else :
            can.itemconfig(i, fill='black')
    print(can.coords(x))
    ######
    v1 = can.coords(x)[0]
    v2 = can.coords(x)[1]
    v3 = can.coords(x)[2]
    v4 = can.coords(x)[3]
    print(v1)
    print(v2)
    print(v3)
    print(v4)
    ##### ->
    v1 = v1 + 100
    v3 = v3 + 100
    result = []
    for z in namep1:
        if [v1,v2,v3,v4] == can.coords(z):
            break
        else :
            result.append("ok")
    if len(result) == 4:
        if v1 != 830 :
            print('DROITE')
            D = can.create_oval(v1, v2, v3, v4, outline="#f11",fill="blue", width=2,tags="D",)
            can.tag_bind("D","<Button-1>",lambda x: move("D"))
        #### <-
    v1 = v1 - 200
    v3 = v3 - 200
    result = []
    for z in namep1:
        if [v1,v2,v3,v4] == can.coords(z):
            break
        else :
            result.append("ok")
    if len(result) == 4:
        if v1 != -70 :
            print('GAUCHE')
            G = can.create_oval(v1, v2, v3, v4, outline="#f11",fill="blue", width=2,tags="G",)
            can.tag_bind("G","<Button-1>",lambda x: move("G"))
    ### BAS
    result = []
    v1 = v1 + 100
    v3 = v3 + 100    
    v2 = v2 + 100
    v4 = v4 + 100
    for z in namep1:
        if [v1,v2,v3,v4] == can.coords(z):
            break
        else :
            result.append("ok")
    if len(result) == 4:
        if v2 != 530 :
            print('BAS')
            H = can.create_oval(v1, v2, v3, v4, outline="#f11",fill="blue", width=2,tags="B",)
            can.tag_bind("B","<Button-1>",lambda x: move("B"))
    ### HAUT
    result = []  
    v2 = v2 - 200
    v4 = v4 - 200
    for z in namep1:
        if [v1,v2,v3,v4] == can.coords(z):
            break
        else :
            result.append("ok")
    if len(result) == 4:
        if v2 != -70.0 :
            print('HAUT')
            B = can.create_oval(v1, v2, v3, v4, outline="#f11",fill="blue", width=2,tags="H",)
            can.tag_bind("H","<Button-1>",lambda x: move("H"))




 


        

    
can.tag_bind("a1","<Button-1>",lambda x: selectpiona("a1"))
can.tag_bind("a2","<Button-1>",lambda x: selectpiona("a2"))
can.tag_bind("a3","<Button-1>",lambda x: selectpiona("a3"))
can.tag_bind("a4","<Button-1>",lambda x: selectpiona("a4"))
can.tag_bind("a5","<Button-1>",lambda x: selectpiona("a5"))

###### MOVE P2 #######
def selectpionb(x):
    global turn
    global choose
    if turn == 2:
        namep2 = ["b1","b2","b3","b4","b5"]
        namep2.remove(x)
        print(namep2)
        can.itemconfig(x, fill='yellow')
        for i in namep2:
            can.itemconfig(i, fill='#1f1')

    
can.tag_bind("b1","<Button-1>",lambda x: selectpiona("b1"))
can.tag_bind("b2","<Button-1>",lambda x: selectpiona("b2"))
can.tag_bind("b3","<Button-1>",lambda x: selectpiona("b3"))
can.tag_bind("b4","<Button-1>",lambda x: selectpiona("b4"))
can.tag_bind("b5","<Button-1>",lambda x: selectpiona("b5"))


fen.mainloop()


