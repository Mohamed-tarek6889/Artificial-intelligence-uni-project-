from tkinter import *

def O_plays():
    path_cost = {
        (0, 0): 7,
        (0, 1): 4,
        (0, 2): 8,
        (1, 0): 3,
        (1, 1): 9,
        (1, 2): 2,
        (2, 0): 6,
        (2, 1): 1,
        (2, 2): 5
    }

    # Sort the path_cost dictionary by values in descending order
    sorted_path_cost = dict(sorted(path_cost.items(), key=lambda item: item[1], reverse=True))

    for row, col in sorted_path_cost:
        if buttons[row][col]['text'] == "":
            buttons[row][col]['text'] = players[1]
            break

def next_turn(row, column):
    if buttons[row][column]['text'] == "":
        buttons[row][column]['text'] = players[0]

        if not check_winner() and empty_spaces():
            O_plays()

def check_winner():
    for line in winning_lines:
        a, b, c = line
        if buttons[a // 3][a % 3]['text'] == buttons[b // 3][b % 3]['text'] == buttons[c // 3][c % 3]['text'] != "":
            return True
    return False

def empty_spaces():
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] == "":
                return True
    return False

def new_game():
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="")

window = Tk()
window.title("Tic-Tac-Toe")

players = ["x", "o"]

buttons = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

frame = Frame(window)
frame.pack()

winning_lines = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                 (0, 3, 6), (1, 4, 7), (2, 5, 8),
                 (0, 4, 8), (2, 4, 6)]

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="", font=('consolas', 40), width=5, height=2,
                                       command=lambda row=row, column=column: next_turn(row, column))
        buttons[row][column].grid(row=row, column=column)

new_game()
window.mainloop()
