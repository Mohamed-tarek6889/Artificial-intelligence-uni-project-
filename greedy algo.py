from tkinter import *
import random

def O_plays(row, column):
    priority = [
        [3, 2, 3],
        [2, 4, 2],
        [3, 2, 3]
    ]

    empty_cells = []

    for i in range(3):
        for j in range(3):
            if buttons[i][j]['text'] == "":
                empty_cells.append(((i, j), priority[i][j]))

    if not empty_cells:
        return

    empty_cells.sort(key=lambda cell: cell[1], reverse=True)
    best_cell = empty_cells[0][0]
    i, j = best_cell

    buttons[i][j]['text'] = players[1]

    if check_winner(players[1]):
        buttons[i][j]['text'] = ""
        buttons[i][j]['text'] = players[0]
    else:
        buttons[i][j]['text'] = ""

def O_play_wrapper():
    if check_winner(players[1]):
        return
    O_plays(0, 0)

def next_turn(row, column):
    global player

    if buttons[row][column]['text'] == "" and not check_winner(players[0]) and not check_winner(players[1]):
        buttons[row][column]['text'] = player

        if not check_winner(player):
            if player == players[0]:
                player = players[1]
                O_play_wrapper()
            else:
                player = players[0]

def check_winner(symbol):
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] == symbol:
            return True

    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] == symbol:
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] == symbol:
        return True

    if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] == symbol:
        return True

    if not empty_spaces():
        return "Tie"

    return False

def empty_spaces():
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] == "":
                return True
    return False

def new_game():
    global player
    player = players[0]
    label.config(text=player + " turn")

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="")

window = Tk()
window.title("Tic-Tac-Toe")
players = ["X", "O"]
player = players[0]
buttons = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

label = Label(text=player + " turn", font=('consolas', 40))
label.pack(side="top")

reset_button = Button(text="Restart", font=('consolas', 20), command=new_game)
reset_button.pack(side="top")

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="", font=('consolas', 40), width=5, height=2,
                                      command=lambda row=row, column=column: next_turn(row, column))
        buttons[row][column].grid(row=row, column=column)

window.mainloop()
