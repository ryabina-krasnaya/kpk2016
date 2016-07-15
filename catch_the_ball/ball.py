import tkinter
from random import choice, randint

ball_initial_number = 20
ball_min_R = 15
ball_max_R = 40
ball_available_colors = ['blue', 'red', '#FF00FF','#FFFFFF', '#FFFF00','gray']

def click_ball(event):
    """По клику мышкой на объекте - он исчезает"""
    obj = canvas.find_closest(event.x,event.y)
    x1, y1,x2, y2 = canvas.coords(obj)
    if x1 <= event.x <= x2 and y1 <= event.y <= y2:
        canvas.delete(obj)
        create_random_ball()

def move_all_balls(event):
    """Передвигает все шарики на чуть-чуть"""
    for obj in canvas.find_all():
        dx = randint(-1,1)
        dy = randint(-1,1)
        canvas.move(obj,dx,dy)

def create_random_ball():
    """Создает шарик в случайном месте игрового холста не переходя за его границы"""
    R = randint(ball_min_R, ball_max_R)
    x = randint(0, int(canvas['width'])-1-2*R)
    y = randint(0, int(canvas['height'])-1-2*R)

    canvas.create_oval(x,y,x+2*R,y+2*R, width=2, fill = random_color())

def random_color():
    """Возвращает случайный цвет из имеющегося набора цветов"""
    return choice(ball_available_colors)


def init_ball_catch_game():
    """Создает необходимое для игры количество шариков, по которым нужно кликать"""
    for i in range(ball_initial_number):
        create_random_ball()

def init_main_window():
    global root,canvas

    root = tkinter.Tk()

    canvas = tkinter.Canvas(root, background = 'green', width = 600, height = 400)
    canvas.bind("<Button>", click_ball)
    canvas.bind("<Motion>", move_all_balls)
    canvas.pack()


if __name__ == "__main__":
    init_main_window()
    init_ball_catch_game()
    root.mainloop()
    print("Приходите поиграть ещё!")