from tkinter import *
from random import *
import os

window = Tk()
window.title("Projet couleur")
window.geometry("700x500")
co = 0
il = 0
rep = []
k = randint(2, 6)
w = 700
z = 500
temps = 30
sc = 0
go = 1
inib = 0

color_list = ["red", "blue", "green", "pink", "yellow", "orange", "white"]


def gner():
    """Fonction génératrice de fichier de score"""
    i = 1
    if os.path.isfile("score.txt") == False:
        gner = open("score.txt", "x")
        gner.write("#############Top 10 Scores#############" + "\n")
        while i < 11:
            gner.write(str(i) + ": Score: 0" + "\n")
            i += 1
        gner.close()


def ecriscore():
    """Fonction qui a pour but d'écrire le score dans un document .txt et de l'organiser."""
    global sc
    back = 0
    inb = 0  # Inibiteur pour empécher d'avoir que le score qu'on vient d'avoir
    gner()  # Pour lancer la fonction génératrice de fichier de score
    scccrog = open("score.txt", "r")

    ligne = scccrog.readline()

    scccr = open("score.txt", "w")
    scccr.write("#############Top 10 Scores#############" + "\n")

    for ligne in scccrog:
        mots = ligne.split()
        ###################################
        if int(mots[2]) < sc:
            # La ligne que on vérifie a un score inférieur à celui qu'on viens d'avoir
            if inb == 0:
                back = mots[2]
                mots[2] = sc
                scccr.write(mots[0] + " " + mots[1] + " " + str(mots[2]) + "\n")
                inb = 1
            elif inb == 1:
                scccr.write(mots[0] + " " + mots[1] + " " + str(back) + "\n")
                back = mots[2]
            ################################################
        elif int(mots[2]) == sc or int(mots[2]) > sc:
            scccr.write(mots[0] + " " + mots[1] + " " + str(mots[2]) + "\n")
    scccrog.close()
    scccr.close()


def ezreset():
    global temps, go
    if temps == 30 or 0 and go == 1:
        chrono()
    elif temps != 0:
        pass
    else:
        ren()
        c.after(1, ezreset)
        chrono()


def chrono():
    global temps, go, inib

    time.config(text="Temps restant :" + str(temps))

    if temps > 0 and go == 1:
        temps -= 1
        c.after(1000, chrono)
    if go == 0:
        go = 1
    elif temps == 0 and inib == 0:
        ecriscore()
        inib = 1


def ren():
    global temps, go, sc, inib
    inib = 0
    temps = 30
    sc = 0
    go = 0
    score.configure(text="score :" + str(sc))


def red():
    global sc, color_word, il
    if color_word[il] == "red" and 30 > temps > 0:
        score.configure(text="score :" + str(sc))
        rep.append("red")
        il += 1
        scoree()
        rr()


def blue():
    global sc, color_word, il
    if color_word[il] == "blue" and 30 > temps > 0:
        score.configure(text="score :" + str(sc))
        rep.append("blue")
        il += 1
        scoree()
        rr()


def green():
    global sc, color_word, il
    if color_word[il] == "green" and 30 > temps > 0:
        score.configure(text="score :" + str(sc))
        rep.append("green")
        il += 1
        scoree()
        rr()


def pink():
    global sc, color_word, il
    if color_word[il] == "pink" and 30 > temps > 0:
        score.configure(text="score :" + str(sc))
        rep.append("pink")
        il += 1
        scoree()
        rr()


def yellow():
    global sc, color_word, il
    if color_word[il] == "yellow" and 30 > temps > 0:
        score.configure(text="score :" + str(sc))
        rep.append("yellow")
        il += 1
        scoree()
        rr()


def orange():
    global sc, color_word, il
    if color_word[il] == "orange" and 30 > temps > 0:
        score.configure(text="score :" + str(sc))
        rep.append("orange")
        il += 1
        scoree()
        rr()


def effacer():
    """Ca effacera tout ce qu'il y a dans le canevas"""
    frame.destroy()


def white():
    global sc, color_word, il

    if color_word[il] == "white" and 30 > temps > 0:
        score.configure(text="score :" + str(sc))
        rep.append("white")
        il += 1
        scoree()
        rr()


c = Canvas(window, width=w, height=z)

frame = Frame(window)
start = Button(window, text="démarrer", font=("segoe script", 16), fg="blue", command=ezreset)
reset = Button(window, text="réinitialiser", font=("segoe script", 16), fg="blue", command=ren)
label = Label(window, text="Tapez la couleur des mots, et pas le texte des mots !!!", font=("segoe script", 14))
score = Label(window, text="score :" + str(sc), font=("segoe script", 16))
time = Label(window, text="Temps restant :" + str(temps), font=("segoe script", 16))
b_red = Button(window, text="rouge", font=("cooper black", 16), bg="red", bd=0, command=red)
b_blue = Button(window, text="bleu", font=("cooper black", 16), bg="blue", bd=0, command=blue)
b_green = Button(window, text="vert", font=("cooper black", 16), bg="green", bd=0, command=green)
b_pink = Button(window, text="rose", font=("cooper black", 16), bg="pink", bd=0, command=pink)
b_yellow = Button(window, text="jaune", font=("cooper black", 16), bg="yellow", bd=0, command=yellow)
b_orange = Button(window, text="orange", font=("cooper black", 16), bg="orange", bd=0, command=orange)
b_white = Button(window, text="blanc", font=("cooper black", 16), bg="white", bd=0, command=white)


def r():
    global co, il, color_word, text_word, couleur, rep, frame
    frame = Frame(window)
    frame.place(x=w // k + 4, y=150)
    global co, il, color_word, text_word, couleur

    co = 0
    color_word = choices(color_list, k=k)
    text_word = choices(color_list, k=k)

    for i in range(k):
        couleur = Label(frame, text=text_word[i], font=("britannic bold", 20), fg=color_word[i])
        couleur.grid(row=0, column=co)
        co += 1
        il = 0


def scoree():
    global couleur, k, rep, sc
    if len(rep) + 1 == k:
        sc += 1


r()


def rr():
    global couleur, k, rep, text_word
    global couleur, k, rep, sc

    if len(rep) == k:
        effacer()
        couleur.destroy()
        rep = []
        k = randint(2, 6)
        r()


c.grid(column=0, row=0, columnspan=2, rowspan=2)
start.grid(column=0, row=1)
reset.grid(column=1, row=1)
label.place(x=70, y=20)
score.place(x=280, y=60)
time.place(x=230, y=100)

frame.place(x=w // k, y=150)
b_red.place(x=60, y=200)
b_blue.place(x=180, y=200)
b_green.place(x=280, y=200)
b_pink.place(x=380, y=200)
b_yellow.place(x=480, y=200)
b_orange.place(x=200, y=280)
b_white.place(x=350, y=280)
window.mainloop()
rr()
