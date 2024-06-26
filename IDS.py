from tkinter import *
import random

def O_plays():
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] == "":
                # Check if "O" can win in the next move
                buttons[row][column]['text'] = players[1]
                if check_winner(players[1]):
                    return
                buttons[row][column]['text'] = ""
## here I am gonna block if I found the x is winning somewhere and there are no moves that will make me win 
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] == "":
                # Check if "X" can win in the next move and block it
                buttons[row][column]['text'] = players[0]
                if check_winner(players[0]):
                    buttons[row][column]['text'] = players[1]
                    return
                buttons[row][column]['text'] = ""

    # here I am gonna put the o randomly if both the didn't cases weren't found 
    counter=0
    while counter<10: 
        i = random.randint(0,2)
        j = random.randint(0,2) 
        if buttons[i][j]['text'] == "":
            buttons[i][j]['text']=players[1]
            break
        counter=counter+1

def next_turn(row, column):
    if buttons[row][column]['text'] == "" and not check_winner(players[0]) and not check_winner(players[1]):
        buttons[row][column]['text'] = players[0]
        if not check_winner(players[0]):
            O_plays()
            if check_winner(players[1]):
                label.config(text=(players[1] + " wins"))
            elif check_winner(players[0]):
                label.config(text=(players[0] + " wins"))
            elif not any('' in row for row in buttons):
                label.config(text="x")

def check_winner(player):
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] == player:
            return True

    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] == player:
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] == player:
        return True

    if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] == player:
        return True

    return False

def empty_spaces():
    return any('' in row for row in buttons)

def new_game():
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="")
    label.config(text=players[0] + " turn")

window = Tk()
window.title("Tic-Tac-Toe")
players = ["X", "O"]
buttons = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

label = Label(text=players[0] + " turn", font=('consolas', 40))
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
