import sys 
from PySide6.QtWidgets import QApplication , QMessageBox 
from PySide6.QtUiTools import QUiLoader
from functools import partial
import random

def check():
    global x_score , o_score , draw
    for j in range(3):
        for i in range(3):
            if buttons[i][0].text() == "X" and buttons[i][1].text() == "X" and buttons[i][2].text() =="X" :
                msg_box =  QMessageBox( text= "  🎉✨ player 1 wins ✨🎉 ")
                x_score += 1
                main_window.xscore.setText(f"X score : {x_score}")                
                msg_box.exec() 
        if buttons[0][j].text() == "X" and buttons[1][j].text() == "X" and buttons[2][j].text() =="X" :
            msg_box =  QMessageBox( text= "  🎉✨ player 1 wins ✨🎉 ")
            x_score += 1
            main_window.xscore.setText(f"X score : {x_score}") 
            msg_box.exec()
    if (buttons[0][0].text() == "X" and buttons[1][1].text() == "X" and buttons[2][2].text() =="X" ) or (buttons[0][2].text() == "X" and buttons[1][1].text() == "X" and buttons[2][0].text() =="X"):
        msg_box =  QMessageBox( text= "  🎉✨ player 1 wins ✨🎉 ")
        x_score += 1
        main_window.xscore.setText(f"X score : {x_score} ") 
        msg_box.exec()        

    for j in range(3):
        for i in range(3):
            if buttons[i][0].text() == "O" and buttons[i][1].text() == "O" and buttons[i][2].text() =="O" :
                msg_box =  QMessageBox( text= "  🎊⚡ player 2 wins ⚡🎊 ")
                o_score += 1
                main_window.oscore.setText(f"O score : {o_score}")                 
                msg_box.exec() 
        if buttons[0][j].text() == "O" and buttons[1][j].text() == "O" and buttons[2][j].text() =="O" :
            msg_box =  QMessageBox( text= "  🎊⚡ player 2 wins ⚡🎊 ")
            o_score += 1
            main_window.oscore.setText(f"O score :{o_score} ")             
            msg_box.exec()
    if (buttons[0][0].text() == "O" and buttons[1][1].text() == "O" and buttons[2][2].text() =="O" ) or (buttons[0][2].text() == "O" and buttons[1][1].text() == "O" and buttons[2][0].text() =="O"):
        msg_box =  QMessageBox( text= "  🎊⚡ player 2 wins ⚡🎊 ")
        o_score += 1
        main_window.oscore.setText(f"O score : {o_score} ")        
        msg_box.exec() 
    else :
        c = 0
        for i in range(3):
            for j in range(3):
                if buttons[i][j].text() != ""  :
                    c+=1
        if c == 9 :
            msg_box = QMessageBox(text = "❌⭕  DRAW  ⭕❌")
            draw += 1
            main_window.draw.setText(f"Draw : {draw}")
            msg_box.exec()



def play(row , col ):
    global player
    global buttons
    main_window.player2.setChecked(True)

    if player == 1 :
        buttons[row][col].setText("X")
        buttons[row][col].setStyleSheet("color : red; border-radius: 10px; ")       
        player = 2 
        check()
    elif player == 2 :
        buttons[row][col].setText("O")
        buttons[row][col].setStyleSheet("color : cyan; border-radius: 10px; ")       
        player = 1

    check()


def play_vs_cpu(row , col ):
    global player , cpu_push_button
    global buttons 
    global flag
    main_window.cpu.setChecked(True)

    if player == 1 :
        buttons[row][col].setText("X")
        buttons[row][col].setStyleSheet("color : red; border-radius: 10px; ")       
        check()
        while cpu_push_button == False :
            i = random.randint(0 , 2)
            j = random.randint(0 , 2)
            if buttons[i][j].text() != "X" and buttons[i][j].text() != "O" and buttons[i][j].text() == "" :
                buttons[i][j].setText("O")
                buttons[i][j].setStyleSheet("color : cyan; border-radius: 10px; ")       
                cpu_push_button = True
    check()
    cpu_push_button = False




def about():
    about_box = QMessageBox(text = "Game Rules : you are player 1 who play as 'X' , and your opponent plays as 'O' character .\nyou can choose between player modes  by clicking on 'new game' button \nbelow the game :\n\n    1. YOU vs CPU \n    2. YOU vs player-2 ")
    about_box.setWindowTitle("Tic Tac Toe")
    about_box.exec()


def new_game():
    global buttons
    for i in range(3):
        for j in range(3):
            buttons[i][j].setText("")
    #main_window.cpu.setChecked(False)
    #main_window.player2.setChecked(False)



app = QApplication(sys.argv)
player = 1 
flag = 0
cpu_push_button = False
x_score = 0 
o_score = 0
draw = 0
loader = QUiLoader()
main_window = loader.load("TicTacToe.ui")
main_window.show()
main_window.setWindowTitle("Tic Tac Toe")



buttons = [[main_window.btn1 , main_window.btn2 , main_window.btn3], 
           [main_window.btn4 , main_window.btn5 , main_window.btn6],
           [main_window.btn7 , main_window.btn8 , main_window.btn9]]


# if flag == 0 :
#     for i in range(3):
#         for j in range(3):
#             buttons[i][j].clicked.connect(partial(play , i , j))
# elif flag == 1 :
for i in range(3):
    for j in range(3):
        buttons[i][j].clicked.connect(partial(play_vs_cpu , i , j))    

 


#main_window.player2.clicked.connect(partial(play , i , j))
main_window.cpu.clicked.connect(partial(play_vs_cpu , i , j))
# if main_window.cpu.clicked :
#     main_window.cpu.setChecked(True)
# elif main_window.player2.clicked :
#     main_window.player2.setChecked(True)

main_window.about.clicked.connect(about)
main_window.newgame.clicked.connect(new_game)       



app.exec()

