# a simple GUI for my tic-tac-toe game
from tkinter import *
import time
from random import randint, choice
import tkinter.messagebox as message
import tkinter.simpledialog as dialog

count = 0
test_board = ["#", " ", " ", " ", " ", " ", " ", " ", " ", " "]
playername = None
rounds = None
roundcount = None
status = None
value1 = None
value2 = None
value3 = None
value4 = None
value5 = None
value6 = None
value7 = None
value8 = None
value9 = None
computer_score = None
human_score = None
root = Tk()  # parent window
outer = Frame(root, border=2, relief='sunken')
inner = Frame(outer)
outer.pack(side='top')
inner.pack()


def Menubar(root):
    def dummy():
        print('hello', 'how are you')
        message.showinfo('', 'Hello World')

    root.title('TIC-TAC-TOE-GAME')  # give window a title
    root.geometry('400x600')
    main_menu = Menu(root)  # create the file menu
    ifile = Menu(root)
    ihelp = Menu(root)
    itool = Menu(root)

    ifile.add_command(label='Resume', )
    ifile.add_command(label='Restart', command=refresh)
    ifile.add_command(label='New', command=dummy)
    ifile.add_command(label='Save', command=dummy)
    ifile.add_command(label='Load Game', command=dummy)

    ihelp.add_command(label='Help', command=dummy)
    ihelp.add_command(label='About', command=dummy)
    ihelp.add_command(label='Credits', command=dummy)

    itool.add_command(label='Get tips', command=dummy)
    itool.add_command(label='Setting', command=dummy)

    main_menu.add_cascade(label='File', menu=ifile)
    main_menu.add_cascade(label='Help', menu=ihelp)
    main_menu.add_cascade(label='Tools', menu=itool)

    root.config(menu=main_menu)  # add menu bar to the parent window


def Board(root):  # The board
    global value1
    global value2
    global value3
    global value4
    global value5
    global value6
    global value7
    global value8
    global value9
    global inner
    global outer

    value1 = StringVar()
    ibutton1 = Button(inner, height=6, width=10, textvariable=value1,
                      command=lambda x=1, y=1, p=1: button(x, y, value1, p))
    ibutton1.grid(row=1, column=1)

    value2 = StringVar()
    ibutton2 = Button(inner, height=6, width=10, textvariable=value2,
                      command=lambda x=1, y=2, p=2: button(x, y, value2, p))
    ibutton2.grid(row=1, column=2)

    value3 = StringVar()
    ibutton3 = Button(inner, height=6, width=10, textvariable=value3,
                      command=lambda x=1, y=3, p=3: button(x, y, value3, p))
    ibutton3.grid(row=1, column=3)

    value4 = StringVar()
    ibutton4 = Button(inner, height=6, width=10, textvariable=value4,
                      command=lambda x=2, y=1, p=4: button(x, y, value4, p))
    ibutton4.grid(row=2, column=1)

    value5 = StringVar()
    ibutton5 = Button(inner, height=6, width=10, textvariable=value5,
                      command=lambda x=2, y=2, p=5: button(x, y, value5, p))
    ibutton5.grid(row=2, column=2)

    value6 = StringVar()
    ibutton6 = Button(inner, height=6, width=10, textvariable=value6,
                      command=lambda x=2, y=3, p=6: button(x, y, value6, p))
    ibutton6.grid(row=2, column=3)

    value7 = StringVar()
    ibutton7 = Button(inner, height=6, width=10, textvariable=value7,
                      command=lambda x=3, y=1, p=7: button(x, y, value7, p))
    ibutton7.grid(row=3, column=1)

    value8 = StringVar()
    ibutton8 = Button(inner, height=6, width=10, textvariable=value8,
                      command=lambda x=3, y=2, p=8: button(x, y, value8, p))
    ibutton8.grid(row=3, column=2)

    value9 = StringVar()
    ibutton9 = Button(inner, height=6, width=10, textvariable=value9,
                      command=lambda x=3, y=3, p=9: button(x, y, value9, p))
    ibutton9.grid(row=3, column=3)


def Statusbar(root):
    global status
    global rounds
    global playername
    global human_score
    global computer_score
    human_score = IntVar()
    computer_score = IntVar()
    rounds = IntVar()
    human_score.set(0)
    computer_score.set(0)
    rounds.set(1)
    status = StringVar()
    status.set("Round {}.  Scores: Your score:{}  Computer score:{} ".format(rounds.get(), human_score.get(),
                                                                             computer_score.get()))
    sframe = Frame(root, border=2)
    sframe.pack(side='bottom')
    label = Label(sframe, textvariable=status, foreground='black', background='white')
    label.pack(fill='x')


def show_error(root):
    message.showinfo('Error', 'Ops, that space is already filled')


def form():
    global playername
    global roundcount
    playername = StringVar()
    roundcount = IntVar()
    playername.set(dialog.askstring("welcome", "Hello its Tic_tac_toe, your favourite game.\n\nWhat is you name"))
    roundcount.set(dialog.askinteger('No of rounds', 'How many rounds do you want to go with the computer'))


# THE BACKEND

def winner_check(mark):
    # THIS FUNCTION PERFORMS SAME FUNCTION AS THE win_check function
    global test_board
    x = test_board
    if (x[1] == mark and x[2] == mark and x[3] == mark):
        return True
    elif (x[4] == mark and x[5] == mark and x[6] == mark):
        return True
    elif (x[7] == mark and x[8] == mark and x[9] == mark):
        return True
    elif (x[7] == mark and x[5] == mark and x[3] == mark):
        return True
    elif (x[9] == mark and x[5] == mark and x[1] == mark):
        return True
    elif (x[1] == mark and x[4] == mark and x[7] == mark):
        return True
    elif (x[2] == mark and x[5] == mark and x[8] == mark):
        return True
    elif (x[3] == mark and x[6] == mark and x[9] == mark):
        return True
    else:
        return False


def refresh():
    # THIS FUNCTION IS USED TO REFRESH AND RESET ALL GLOBAL VARIABLES
    global count
    global test_board
    global player
    global value1
    global value2
    global value3
    global value4
    global value5
    global value6
    global value7
    global value8
    global value9

    count = 0
    test_board = ["#", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    player = ''
    value1.set('')
    value2.set('')
    value3.set('')
    value4.set('')
    value5.set('')
    value6.set('')
    value7.set('')
    value8.set('')
    value9.set('')


def computer():
    # an algorithm that helps the computer think
    # THIS FUNCTION ALLOWS THE USER OF THE GAME TO PLAY WITH THE COMPUTER. IT AUTOMATES THE SECOND PLAYER
    def identical_board(board):
        new_board = []
        for item in board:
            new_board.append(item)
        return new_board

    global test_board
    playermarker1 = 'X'
    playermarker2 = 'O'

    for num in range(1, 10):  # search through all the board to see if there a chance of winning
        x = identical_board(test_board)
        mark = playermarker2
        if x[num] == " ":
            x[num] = mark
            win = False
            if (x[1] == mark and x[2] == mark and x[3] == mark):
                win = True
            elif (x[4] == mark and x[5] == mark and x[6] == mark):
                win = True
            elif (x[7] == mark and x[8] == mark and x[9] == mark):
                win = True
            elif (x[7] == mark and x[5] == mark and x[3] == mark):
                win = True
            elif (x[9] == mark and x[5] == mark and x[1] == mark):
                win = True
            elif (x[1] == mark and x[4] == mark and x[7] == mark):
                win = True
            elif (x[2] == mark and x[5] == mark and x[8] == mark):
                win = True
            elif (x[3] == mark and x[6] == mark and x[9] == mark):
                win = True
            else:
                win = False
            if win == True:
                return int(num)
            else:
                continue
        else:
            continue

    for num in range(1,
                     10):  # search through all the board to see if there is a chance of your opponent winning. then block them
        x = identical_board(test_board)
        mark = playermarker1
        if x[num] == " ":
            x[num] = playermarker1
            lose = False
            if (x[1] == mark and x[2] == mark and x[3] == mark):
                lose = True
            elif (x[4] == mark and x[5] == mark and x[6] == mark):
                lose = True
            elif (x[7] == mark and x[8] == mark and x[9] == mark):
                lose = True
            elif (x[7] == mark and x[5] == mark and x[3] == mark):
                lose = True
            elif (x[9] == mark and x[5] == mark and x[1] == mark):
                lose = True
            elif (x[1] == mark and x[4] == mark and x[7] == mark):
                lose = True
            elif (x[2] == mark and x[5] == mark and x[8] == mark):
                lose = True
            elif (x[3] == mark and x[6] == mark and x[9] == mark):
                lose = True
            else:
                lose = False
            if lose == True:
                return int(num)
            else:
                continue
        else:
            continue

    free_corners = []
    for num in [1, 3, 7, 9, 5]:  # picks the diagonal or centre position if free
        if test_board[num] == ' ':
            free_corners.append(num)
    return choice(free_corners)

    while True:
        num = randint(1, 9)
        if test_board[num] == " ":
            return int(num)
        else:
            continue


# CONNECTING THE FRONTEND WITH THE BACKEND
def button(row, column, value, pressed_button):
    global count
    global test_board
    global root
    global status
    global playername
    global value1
    global value2
    global value3
    global value4
    global value5
    global value6
    global value7
    global value8
    global value9
    global computer_score
    global human_score
    global rounds

    marker = 'X'
    if test_board[pressed_button] != " ":
        show_error(root)
    else:
        value.set(marker)
        test_board[pressed_button] = marker
        win = winner_check(marker)
        count += 1
        if win == True:
            message.showinfo('{} wins'.format(playername.get()), '{} has won the game'.format(playername.get()))
            human_score.set(human_score.get() + 1)
            rounds.set(rounds.get() + 1)
            status.set("Round {}.  Scores: Your score:{}  Computer score:{} ".format(rounds.get(), human_score.get(),
                                                                                     computer_score.get()))
            refresh()
            return 0

        # time.sleep(2)
        if ' ' in test_board:
            marker = 'O'
            num = computer()
            if num == 1:
                value1.set(marker)
            if num == 2:
                value2.set(marker)
            if num == 3:
                value3.set(marker)
            if num == 4:
                value4.set(marker)
            if num == 5:
                value5.set(marker)
            if num == 6:
                value6.set(marker)
            if num == 7:
                value7.set(marker)
            if num == 8:
                value8.set(marker)
            if num == 9:
                value9.set(marker)
            test_board[num] = marker

            win = winner_check(marker)
            count += 1
            if win == True:
                message.showinfo('{} wins'.format('Computer'), '{} has won the game'.format('Computer'))
                computer_score.set(computer_score.get() + 1)
                rounds.set(rounds.get() + 1)
                status.set(
                    "Round {}.  Scores: Your score:{}  Computer score:{} ".format(rounds.get(), human_score.get(),
                                                                                  computer_score.get()))
                refresh()
                return 0

    if not ' ' in test_board:
        message.showinfo('Draw', 'It is a tie')
        rounds.set(rounds.get() + 1)
        status.set("Round {}.  Scores: Your score:{}  Computer score:{} ".format(rounds.get(), human_score.get(),
                                                                                 computer_score.get()))
        refresh()


Menubar(root)
Board(root)
Statusbar(root)
form()

mainloop()