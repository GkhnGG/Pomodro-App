from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
stopwatch = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global REPS
    window.after_cancel(stopwatch)
    timer.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    REPS = 0
    tick.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global REPS
    REPS += 1
    if REPS % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        timer.config(text="Break", fg=RED)

    elif REPS % 2 == 1:
        count_down(WORK_MIN * 60)
        timer.config(text="Work", fg=GREEN)

    elif REPS % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        timer.config(text="Break", fg=PINK)

    tick.config(text="✓" * math.floor(REPS // 2))
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    minute = math.floor(count/60)
    if minute < 10:
        minute = f"0{minute}"
    second = count % 60
    if second < 10:
        second = f"0{second}"
    canvas.itemconfig(timer_text, text=f"{minute}:{second}")
    if count > 0:
        global stopwatch
        stopwatch = window.after(1000, count_down, count - 1)
    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodro")

window.config(padx=100, pady=50,bg=YELLOW)
canvas = Canvas(width=400, height=448, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(204,224, image= tomato_img)
timer_text = canvas.create_text(204, 260,text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.pack()


#Thick
tick = Label(text="",fg=GREEN, bg=YELLOW, font= (FONT_NAME, 25, "bold"))
tick.pack()
#Timer
timer = Label(text="Timer",bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"))
timer.place(x=135, y=15)
# Start
start = Button(text="Start",command= start_timer)
start.place(x=40, y=320)
# Restart
restart= Button(text="Restart", command= reset_timer)
restart.place(x=340, y=320)




window.mainloop()
