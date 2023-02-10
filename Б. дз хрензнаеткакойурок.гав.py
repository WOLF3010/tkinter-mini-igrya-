from tkinter import *

screen = Tk()
screen.title("сус")
canvas = Canvas(screen, width=1000, height=500, bg="black")
canvas.pack()
light = canvas.create_oval(20, 60, 120, 150, fill="white")


def light_sus(event):
    if event.keysym == "Up":
        canvas.move(light, 0, -20)

    elif event.keysym == "Down":
        canvas.move(light, 0, 20)

    elif event.keysym == "Left":
        canvas.move(light, -20, 0)

    elif event.keysym == "Right":
        canvas.move(light, 20, 0)


canvas.bind_all("<Up>", light_sus)
canvas.bind_all("<Down>", light_sus)
canvas.bind_all("<Left>", light_sus)
canvas.bind_all("<Right>", light_sus)
canvas.create_text(675, 389, text="SUS", fill="black", font=("Arial", 66))


screen.mainloop()
