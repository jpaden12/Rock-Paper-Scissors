import random
import easygui
from easygui import *

# Variables
Title = 'Rock Paper Scissors'
Plscore = 0
P2score = 0
Cscore = 0




# The functions that choose the winner
def GM1winner(name):
    Player1 = buttonbox(name[5:] , Title,\
    ('Rock', 'Paper', 'Scissors'))
    Choices = ['Rock', 'Paper', 'Scissors']
    CPUChoice = random.choice(Choices)
    if Player1 == CPUChoice:
        return 'Tie'
    elif Player1 == 'Rock':
        if CPUChoice == 'Scissors':
            return 'Player1'
        elif CPUChoice == 'Paper':
            return 'CPU'
    elif Player1 == 'Scissors':
        if CPUChoice == 'Rock':
            return 'CPU'
        elif CPUChoice == 'Paper':
            return 'Player1'
    elif Player1 == 'Paper': 
        if CPUChoice == 'Rock':
            return 'Player1'
        elif CPUChoice == 'Scissors':
            return 'CPU'
    
def GM2Winner(P1name, P2name):
    Player1 = buttonbox(P1name[5:], Title,\
    ('Rock', 'Paper', 'Scissors'))
    Player2 = buttonbox(P2name[5:], Title, \
    ('Rock', 'Paper', 'Scissors'))
    if Player1 == Player2:
        return 'Tie'
    elif Player1 == 'Rock':
        if Player2 == 'Paper':
            return 'Player1'
        elif Player2 == 'Scissors':
            return 'Player1'
    elif Player1 == 'Paper':
        if Player2 == 'Scissors':
            return 'Player2'
        elif Player2 == 'Rock':
            return 'Player1'
    elif Player1 == 'Scissors':
        if Player2 == 'Rock':
            return 'Player2'
        elif Player2 == 'Paper':
            return 'Player1'
    
    
        

# GameMode 1: Player 1 vs. CPU
# Number = The number of games to be played
def GM1():
    choose = buttonbox('Choose the number of games!', Title, ('Best of 3', 'Best of 5', 'Best of 7'))
    PlayerName = enterbox('Enter you name.', Title, 'Name: ')
    GM1Winner = GM1winner(PlayerName)



    ####Need to fix the winner function.######
    if GM1Winner == 'CPU':
        msgbox('Sorry! You lose.', Title,'OK','Loser_Picture.jpg')
    elif GM1Winner == 'Player1':
        #Insert "You Win" Picture here
        msgbox('Congratulations! You WIN!!', Title, ok_button = 'Go Back')
    else:
        msgbox('You tied!! Nobody won.', Title, ok_button = 'Go Back')


#GameMode 2: Player 1 vs. Player 2
def GM2():
    choose = buttonbox('Choose the number of games!', Title, ('Best of 3', 'Best of 5', 'Best of 7'))
    P1name = enterbox('Player 1, enter your name.', Title, 'Name: ')
    P2Name = enterbox('Player 2, enter your name.', Title, 'Name: ')
    #Insert Player 1 and Player 2 variables here
    GM2Winnerr = GM2Winner(P1name, P2Name)
 

    if GM2Winnerr == 'Player1':
        msgbox('Player1 wins!', Title, ok_button = 'Go Back')
    elif GM2Winnerr == 'Player2':
        msgbox('Player2 wins!', Title, ok_button = 'Go Back')
    else:
        msgbox('You both tied!! Nobody won.', Title, ok_button = 'Go Back')
        
        


##----------------------------------------
#Title Screen, Credits, and Exit Method

TitleScreen = True

while TitleScreen == True:
    a = buttonbox('Welcome to Rock Paper Scissors!!!', Title ,('Credits', 'Start', 'Exit'), 'Logo.png')
    if a == 'Credits':
        TitleScreen == False
        msgbox("This game was developed using Python 3.4 and EasyGUI \n (C) 2015 Jamal Paden",'Credits',ok_button="Back")
        TitleScreen == True
    if a == 'Exit':
        TitleScreen == False
        #Insert Exit method here
        msgbox("Insert Exit method here")
        TitleScreen == True
    if a == 'Start':
        TitleScreen == False
        b = buttonbox('Game Modes', 'Game Modes',('Player 1 vs. CPU', 'Player 1 vs. Player 2'))
        print(b)
        if b == 'Player 1 vs. CPU':
            GM1()
        else:
            GM2()



    
