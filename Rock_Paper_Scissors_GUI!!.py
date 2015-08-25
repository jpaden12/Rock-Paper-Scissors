import random
import easygui
from easygui import *

#Variables
Title = 'Rock Paper Scissors'
Plscore = 0
Cscore = 0
Choices = ['Rock', 'Paper', 'Scissors']



#The function that chooses the winner
def winner(name):
    Player1 = buttonbox(name[5:] , Title,\
    ('Rock', 'Paper', 'Scissors'))
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
        

#GameMode 1: Player 1 vs. CPU
#Number = The number of games to be played
def GM1():
    number = buttonbox('Choose the number of games!', Title, ('Best of 3', 'Best of 5', 'Best of 7'))
    PlayerName= enterbox('Enter you name.', Title, 'Name: ')
   ## Player1 = buttonbox(PN[5:] , Title,\
    #('Rock', 'Paper', 'Scissors'))
    # CPUChoice = random.choice(Choices)
    funct = winner(PlayerName)



    ####Need to fix the winner function.######
    if funct == 'CPU':
        msgbox('Sorry! You lose.', Title,'OK','Loser_Picture.jpg')
    elif funct == 'Player1':
        #Insert "You Win" Picture here
        msgbox('Congratulations! You WIN!!', Title, ok_button = 'Go Back')
    else:
        #Insert Tie Here
        pass


#GameMode 2: Player 1 vs. Player 2
#P2N = Player 2 Name
def GM2():
    choose = buttonbox('Choose the number of games!', Title, ('Best of 3', 'Best of 5', 'Best of 7'))
    PN = enterbox('Player 1, enter your name.', Title, 'Name: ')
    P2N = enterbox('Player 2, enter your name.', Title, 'Name: ')
    #Insert Player 1 and Player 2 variables here
    PlayerChoice = buttonbox('Player 1 name and Player 2 name', Title,\
    ('Rock', 'Paper', 'Scissors'))
    CPUChoice = random.choice(Choices)
    
 



##----------------------------------------
#Title Screen, Credits, and Exit Method

TitleScreen = True

while TitleScreen == True:
    a = buttonbox('Welcome to Rock Paper Scissors!!1!', Title ,('Credits', 'Start', 'Exit'), 'Logo.png')
    print(a)
    if a == 'Credits':
        TitleScreen == False
        msgbox("This game was developed and published by Jamal Paden \n Developed using Python 3.4 and EasyGUI \n (C) 2015 Jamal Paden",'Credits',ok_button="Back")
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
        #Put the finished second game mode here
        else:
            Pass



    
