from tkinter import *
from  random import *

window = Tk()
window.title("Projet couleur")
window.geometry("700x500")

w = 700
z = 500
temps = 30
sc = 0
go = 1
color_list = ["red","blue","green","pink","yellow","orange","white"]
color_word = choice(color_list)
text_word = choice(color_list)

def chrono () :
    global temps, go

    time.config( text ="Temps restant :" + str(temps))

    if temps > 0 and go == 1 :
        temps -= 1
        c.after(1000, chrono)
    if go == 0 :
            go =1


def ren () :
    global  temps, go, sc
    temps = 30
    sc = 0
    go = 0
    score.configure(text="score :" + str(sc))

def red () :
    global sc, color_word
    if color_word == "red" and 30>temps > 0 :
        sc += 1
        score.configure(text= "score :" + str (sc))
        color_word = choice(color_list)
        text_word = choice(color_list)
        couleur.configure(text= text_word, fg = color_word )

def blue () :
    global sc, color_word
    if color_word == "blue"  and 30>temps > 0 :
        sc += 1
        score.configure(text= "score :" + str (sc))
        color_word = choice(color_list)
        text_word = choice(color_list)
        couleur.configure(text= text_word, fg = color_word )

def green () :
    global sc, color_word
    if color_word == "green"  and 30>temps > 0 :
        sc += 1
        score.configure(text= "score :" + str (sc))
        color_word = choice(color_list)
        text_word = choice(color_list)
        couleur.configure(text= text_word, fg = color_word )



def pink () :
    global sc, color_word
    if color_word == "pink"  and 30>temps > 0  :
        sc += 1
        score.configure(text= "score :" + str (sc))
        color_word = choice(color_list)
        text_word = choice(color_list)
        couleur.configure(text= text_word, fg = color_word )

def yellow () :
    global sc, color_word
    if color_word == "yellow" and 30>temps > 0  :
        sc += 1
        score.configure(text= "score :" + str (sc))
        color_word = choice(color_list)
        text_word = choice(color_list)
        couleur.configure(text= text_word, fg = color_word )

def orange () :
    global sc, color_word
    if color_word == "orange" and 30>temps > 0  :
        sc += 1
        score.configure(text= "score :" + str (sc))
        color_word = choice(color_list)
        text_word = choice(color_list)
        couleur.configure(text= text_word, fg = color_word )

def white () :
    global sc, color_word
    if color_word == "white" and 30> temps > 0  :
        sc += 1
        score.configure(text= "score :" + str (sc))
        color_word = choice(color_list)
        text_word = choice(color_list)
        couleur.configure(text= text_word, fg = color_word )


c = Canvas(window, width=w, height=z)
start = Button(window, text= "démarrer", font=("segoe script", 16), fg = "blue", command = chrono)
reset  = Button(window, text= "réinitialiser", font=("segoe script", 16), fg = "blue", command = ren)
label = Label(window, text = "Tapez la couleur des mots, et pas le texte des mots !!!", font=("segoe script", 14))
score = Label(window, text = "score :" + str (sc), font=("segoe script", 16))
time = Label(window, text = "Temps restant :" + str(temps), font=("segoe script", 16))
couleur = Label(window, text = text_word, font=("britannic bold", 20), fg = color_word)

b_red = Button(window, text= "rouge", font=("cooper black", 16), bg = "red",bd = 0, command = red)
b_blue = Button(window, text= "bleu", font=("cooper black", 16), bg = "blue",bd = 0, command = blue)
b_green = Button(window, text= "vert", font=("cooper black", 16), bg = "green",bd = 0, command = green)
b_pink = Button(window, text= "rose", font=("cooper black", 16), bg = "pink",bd = 0, command = pink)
b_yellow= Button(window, text= "jaune", font=("cooper black", 16), bg = "yellow",bd = 0, command = yellow)
b_orange = Button(window, text= "orange", font=("cooper black", 16), bg = "orange",bd = 0, command = orange)
b_white = Button(window, text= "blanc", font=("cooper black", 16), bg = "white",bd = 0, command = white)



c.grid(column = 0, row = 0,columnspan = 2 , rowspan = 2 )
start.grid(column = 0, row = 1)
reset .grid(column = 1, row = 1)
label.place(x=70, y=20)
score.place(x=280, y=60)
time.place(x= 230, y = 100)
couleur.place(x= 300, y = 150)
b_red.place(x= 60, y = 200)
b_blue.place(x= 180, y = 200)
b_green.place(x= 280, y = 200)
b_pink.place(x= 380, y = 200)
b_yellow.place(x= 480, y = 200)
b_orange.place(x= 200, y = 280)
b_white.place(x= 350, y = 280)


window.mainloop()
#fin