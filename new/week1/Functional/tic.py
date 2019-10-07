import os
import time
import random

board = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]


def print_b():
    print(" " + " |1| " + board[1] + " |2|" + board[2] + " |3| " + board[3])
    print(" " + " |4| " + board[4] + " |5| " + board[5] + " |6| " + board[6])
    print(" " + " |7| " + board[7] + " |8| " + board[8] + " |9| " + board[9])


while True:
    os.system("clear")
    print_b()
    ch = int(input("enter the slot for x"))

    if board[ch] == " ":
        board[ch] = "x"
    else:
        print("please select other slot")
        time.sleep(1)

    if (board[1] == "x" and board[2] == "x" and board[3] == "x") or \
            (board[4] == "x" and board[5] == "x" and board[6] == "x") or \
            (board[7] == "x" and board[8] == "x" and board[9] == "x") or \
            (board[1] == "x" and board[4] == "x" and board[7] == "x") or \
            (board[1] == "x" and board[5] == "x" and board[9] == "x") or \
            (board[3] == "x" and board[5] == "x" and board[7] == "x") or \
            (board[2] == "x" and board[5] == "x" and board[8] == "x") or \
            (board[3] == "x" and board[6] == "x" and board[9] == "x"):
        print_b()
        print("x is winner")
        break


    def com_m(board1, player):
        mo = random.randint(1, 9)
        return mo

    ch = com_m(board, "0")
    os.system("clear")
    print_b()

    if board[ch] == " ":
        board[ch] = "0"
    else:
        print("please select other slot")
        time.sleep(1)

        if (board[1] == "0" and board[2] == "0" and board[3] == "0") or \
                (board[4] == "0" and board[5] == "0" and board[6] == "0") or \
                (board[7] == "0" and board[8] == "0" and board[9] == "0") or \
                (board[1] == "0" and board[4] == "0" and board[7] == "0") or \
                (board[1] == "0" and board[5] == "0" and board[9] == "0") or \
                (board[3] == "0" and board[5] == "0" and board[7] == "0") or \
                (board[2] == "0" and board[5] == "0" and board[8] == "0") or \
                (board[3] == "0" and board[6] == "0" and board[9] == "0"):
            print_b()
            print("0 is winner")
        #    break

    isFull = True
    for i in range(1, 10):
        if board[i] == " ":
            isFull = False
        else:
            print("tie")
