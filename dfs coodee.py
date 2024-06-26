from tkinter import *
import random

def O_playes(row , column , counter1  , counter2) : 
    #index = [buttons[counter1][counter2]['text']]  # I think I want this array to take the place I am going to expand form every time
    #visited = []
    if check_winner_O() is True : 
        #buttons[counter1][counter2]['text']= players[1]
        retrun
    elif counter1>2 : 
       # buttons[2][2]['text']= players[1]
        counter=0
        while counter<10: 
            i = random.randint(0,2)
            j = random.randint(0,2) 
            if buttons[i][j]['text'] == "":
                buttons[i][j]['text']=players[1]
                break
            counter=counter+1
 ## 
    else:
        
        ################################################################
        if buttons[counter1][counter2]['text'] == "" and check_winner_X() is False : 
            buttons[counter1][counter2]['text'] = players[0]
            if check_winner_X() is True:
                buttons[counter1][counter2]['text'] = ""
                buttons[counter1][counter2]['text'] = players[1]
                return 
            else:    
                buttons[counter1][counter2]['text'] = ""
            
                 
        counter2 +=1
        if counter2 ==3: 
            counter2 = 0 
            counter1 =counter1+1
        O_playes(row,column , counter1 , counter2 )
        


    #item = index.pop()
    
                

       
        #visited.append(item)







def next_turn(row, column):

    global player

    if buttons[row][column]['text'] == "" and check_winner_O() is False and check_winner_X() is False:

        if player == players[0]:

            buttons[row][column]['text'] = player
            ### here I am just going to put the first "O" randomly so I know where to search from 
           # if buttons[1][1]['text'] == "" and check_winner_O() is False and check_winner_O() is False: 
            #    buttons[1][1]['text'] = players[1] 
            #elif buttons[1][1]['text'] == players[0] and check_winner_O() is False and check_winner_X() is False: 
             #   buttons[0][1]['text']= players[1] 
            ### here I think I will start impleminting the logic 
            num1=0
            num2=0
            O_playes(row,column,num1,num2)

            if check_winner_O() is False and check_winner_O is False:
                player = players[0]
                #label.config(text=(players[1]+" turn"))


            elif check_winner_X()  is True:
                label.config(text=(players[0]+" wins"))
            
            elif check_winner_O() is True:
                label.config(text=(players[1]+" wins"))

            elif check_winner_O()=="Tie" or check_winner_X == "Tie":
                label.config(text="Tie!")


        #else:

           # buttons[row][column]['text'] = player

           # if check_winner() is False:
                #player = players[0]
               # label.config(text=(players[0]+" turn"))

           # elif check_winner() is True:
             #   label.config(text=(players[1]+" wins"))

         #   elif check_winner() == "Tie":
             #   label.config(text="Tie!")

def check_winner_O():

    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] == players[1]:
            #buttons[row][0].config(bg="green")
            #buttons[row][1].config(bg="green")
            #buttons[row][2].config(bg="green")
            return True

    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] == players[1]:
            #buttons[0][column].config(bg="green")
            #buttons[1][column].config(bg="green")
            #buttons[2][column].config(bg="green")
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] == players[1]:
        #buttons[0][0].config(bg="green")
        #buttons[1][1].config(bg="green")
        #buttons[2][2].config(bg="green")
        return True

    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] == players[1]:
        #buttons[0][2].config(bg="green")
        #buttons[1][1].config(bg="green")
        #buttons[2][0].config(bg="green")
        return True

    elif empty_spaces() is False:

        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="yellow")
        return "Tie"

    else:
        return False
def check_winner_X():

    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] == players[0]:
            #buttons[row][0].config(bg="green")
            #buttons[row][1].config(bg="green")
            #buttons[row][2].config(bg="green")
            return True

    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] == players[0]:
            #buttons[0][column].config(bg="green")
            #buttons[1][column].config(bg="green")
            #buttons[2][column].config(bg="green")
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] == players[0]:
        #buttons[0][0].config(bg="green")
        #buttons[1][1].config(bg="green")
        #buttons[2][2].config(bg="green")
        return True

    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] == players[0]:
        #buttons[0][2].config(bg="green")
        #buttons[1][1].config(bg="green")
        #buttons[2][0].config(bg="green")
        return True

    elif empty_spaces() is False:

        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="yellow")
        return "Tie"

    else:
        return False


def empty_spaces():

    spaces = 9

    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -= 1

    if spaces == 0:
        return False
    else:
        return True

def new_game():

    global player

    #player = random.choice(players)
    player=players[0]
    label.config(text=player+" turn")

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="",bg="#F0F0F0")


window = Tk()
window.title("Tic-Tac-Toe")
players = ["x","o"]
#player = random.choice(players)
player=players[0]
buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]]

label = Label(text=player + " turn", font=('consolas',40))
label.pack(side="top")

reset_button = Button(text="restart", font=('consolas',20), command=new_game)
reset_button.pack(side="top")

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="",font=('consolas',40), width=5, height=2,
                                      command= lambda row=row, column=column: next_turn(row,column))
        buttons[row][column].grid(row=row,column=column)

window.mainloop()