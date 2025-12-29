import random
from tkinter import *
from tkinter import ttk

choices = ["paper", "scissors", "stone"]


def random_choice() -> str:
    return random.choice(choices)


def choice_winner(first: str, second: str) -> str:
    d = {
        "paper": "scissors",
        "scissors": "stone",
        "stone": "paper"
    }

    if first in choices:
        if first == second:
            return "DRAW"
        elif d[first] == second:
            return "YOU LOSE"
        return "YOU WIN"
    return "error"


window = Tk()
window.geometry("600x700")
window.title('Paper, scissors, stone')

c_bot = Canvas(window, width=600, height=300, bg='green')
c_user = Canvas(window, width=600, height=300, bg='green')
p = Canvas(window, width=600, height=100, bg='black')

c_bot.pack(anchor=N)
c_user.pack(anchor=CENTER)
p.pack(anchor=S)

c = 0


def main() -> None:
    global c

    c_bot.delete(ALL)
    c_user.delete(ALL)
    p.delete(ALL)

    count = c_user.create_text(70, 270, text=f'Your score: {c}', font="Arial 18", fill='black')

    btn_paper = ttk.Button(text='paper', command=lambda: user_choice("paper"))
    p.create_window(100, 50, window=btn_paper, width=100, height=50)

    btn_scissors = ttk.Button(text='scissors', command=lambda: user_choice("scissors"))
    p.create_window(300, 50, window=btn_scissors, width=100, height=50)

    btn_stone = ttk.Button(text='stone', command=lambda: user_choice("stone"))
    p.create_window(500, 50, window=btn_stone, width=100, height=50)

    user_item, bot_item, btn_play_again = None, None, None

    def user_choice(choice: str):
        global c

        nonlocal user_item, bot_item, btn_play_again, count

        user_item = PhotoImage(file=f"{choice}.png")
        c_user.create_image(175, 50, anchor=NW, image=user_item)
        p.delete(ALL)

        bot_choice = random_choice()
        bot_item = PhotoImage(file=f"{bot_choice}.png")

        c_bot.create_image(190, 60, anchor=NW, image=bot_item)

        winner = choice_winner(choice, bot_choice)

        if winner == "YOU WIN":
            c += 1

        p.create_text(290, 50, text=winner, font='Arial 18', fill="red")

        c_user.delete(count)
        count = c_user.create_text(70, 270, text=f'Your score: {c}', font="Arial 18", fill='black')

        btn_play_again = ttk.Button(text='again', command=lambda: main())
        c_user.create_window(50, 50, window=btn_play_again, width=50, height=35)

    window.mainloop()


if __name__ == "__main__":
    main()