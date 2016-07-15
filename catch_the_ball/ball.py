import tkinter

def click_ball(event):
    """По клику мышкой на объекте - он исчезает"""
   pass

def create_random_ball():
    """Создает шарик в случайном месте игрового холста не переходя за его границы"""
    canvas.create_oval(x,y,x+2*R,y+2*R, width=2, fill = random_color())

def init_ball_catch_game():
    """Создает необходимое для игры количество шариков, по которым нужно кликать"""

def init_main_window():
    global root,canvas

    root = tkinter.Tk()

    canvas = tkinter.Canvas(root, background = 'green', width = 600, height = 400)
    canvas.bind("<Motion>", paint)
    canvas.pack()

    for i in range (10):
        canvas.create_oval(2+i*40,2+i*40,i*40+30,i*40+30, width=2, fill = 'red')

root.mainloop()