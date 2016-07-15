import tkinter

def paint(event):
    print(event.x, event.y)
    canvas.coords(line, 0, 0, event.x, event.y )

root = tkinter.Tk()

canvas = tkinter.Canvas(root, background = 'green', width = 600, height = 400)
canvas.bind("<Motion>", paint)
canvas.pack()

line = canvas.create_line(0,0,10,10)
for i in range (10):
    canvas.create_oval(2+i*40,2+i*40,i*40+30,i*40+30, width=2, fill = 'red')

root.mainloop()