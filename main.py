from tkinter import *
import time

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
# TIMER PERIOD TO COVER 2:25:00, PERPETUAL RUN
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
work_sessions_done = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global timer, reps, work_sessions_done
    window.after_cancel(timer)
    reset_time = "00:00"
    reps = 0
    work_sessions_done = 0
    check_label.config(text="")
    title_label.config(text="Timer")
    canvas.itemconfig(timer_text, text=reset_time)




# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps, work_sessions_done
    if reps == 0:
        work_sessions_done = 0

    progress_label = work_sessions_done * "✅"
    check_label.config(text=progress_label)

    if reps % 2 == 0:
        countdown(WORK_MIN * 60)
        title_label.config(text="Work", fg=GREEN)
        work_sessions_done += 1
        reps += 1
    elif reps == 7:
        countdown(LONG_BREAK_MIN * 60)
        title_label.config(text="Break", fg=RED)
        reps = 0
    else:
        countdown(SHORT_BREAK_MIN * 60)
        title_label.config(text="Break", fg=PINK)
        reps += 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def countdown(count):
    global timer
    count_text = f"{str((count // 60)).zfill(2)}:{str((count % 60)).zfill(2)}"
    canvas.itemconfig(timer_text, text=count_text)
    # Recursive calls for count until 0, then rerun count with new value from start_timer
    if count > 0:
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Labels
title_label = Label(text="Timer", font=(FONT_NAME, 50), fg=GREEN, bg=YELLOW)
title_label.grid(column=1, row=0)

check_label = Label(text="", bg=YELLOW)
check_label.grid(column=1, row=3)

# Buttons
start_button = Button(text="Start", highlightbackground=YELLOW, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightbackground=YELLOW, command=reset_timer)
reset_button.grid(column=2, row=2)

window.mainloop()
