import os;
import time;
import random;


#Board
box = ["", " ", " ", " ", " ", " ", " ", " ", " ", " "]


def interface():
    print(" ")
    print("          TIC TAC TOE GAME          ")
    print(" ")
    print("           -------------            ")
    print("           | 1 | 2 | 3 |            ")
    print("           -------------            ")
    print("           | 4 | 5 | 6 |            ")
    print("           -------------            ")
    print("           | 7 | 8 | 9 |            ")
    print("           -------------            ")
    print(" ")
    print(" ")
    print("                BOARD                ")
    print("-------------------------------------")
    print("|     "+box[1]+"     |     "+box[2]+"     |     "+box[3]+"     |")
    print("-------------------------------------")
    print("|     "+box[4]+"     |     "+box[5]+"     |     "+box[6]+"     |")
    print("-------------------------------------")
    print("|     "+box[7]+"     |     "+box[8]+"     |     "+box[9]+"     |")
    print("-------------------------------------")


def player_x_winner():
    print(" "+player_x_name+" wins!")


def player_o_winner():
    print(" "+player_x_name+" wins!")


def draw_checker(box):
    if " " in box:
        return False
    else:
        return True


os.system('cls')
player_x_name = input('Please type your name here player X: ')
player_o_name = input('Please type your name here player O: ')


while True:
    os.system('cls')
    interface()

    #Player X
    print(" ")
    choose_box = int(input("Please choose a box "+player_x_name+": "))

    if box[choose_box] == " ":
        box[choose_box] = "X"
    else:
        print("Occupied box")
        time.sleep(1)

    if (box[1] == "X" and box[2] == "X" and box[3] == "X") or \
            (box[4] == "X" and box[5] == "X" and box[6] == "X") or \
            (box[7] == "X" and box[8] == "X" and box[9] == "X") or \
            (box[1] == "X" and box[4] == "X" and box[7] == "X") or \
            (box[2] == "X" and box[5] == "X" and box[8] == "X") or \
            (box[3] == "X" and box[6] == "X" and box[9] == "X") or \
            (box[1] == "X" and box[5] == "X" and box[9] == "X") or \
            (box[3] == "X" and box[5] == "X" and box[7] == "X"):
            os.system('cls')
            interface()
            player_x_winner()
            break

    os.system('cls')
    interface()

    if draw_checker(box):
        print("It's a draw!")
        break

    # Player O
    print(" ")
    choose_box = int(input("Please choose a box "+player_o_name+": "))

    if box[choose_box] == " ":
        box[choose_box] = "O"
    else:
        print("Occupied box")
        time.sleep(1)

    if (box[1] == "O" and box[2] == "O" and box[3] == "O") or \
            (box[4] == "O" and box[5] == "O" and box[6] == "O") or \
            (box[7] == "O" and box[8] == "O" and box[9] == "O") or \
            (box[1] == "O" and box[4] == "O" and box[7] == "O") or \
            (box[2] == "O" and box[5] == "O" and box[8] == "O") or \
            (box[3] == "O" and box[6] == "O" and box[9] == "O") or \
            (box[1] == "O" and box[5] == "O" and box[9] == "O") or \
            (box[3] == "O" and box[5] == "O" and box[7] == "O"):
            os.system('cls')
            interface()
            player_o_winner()
            break

    os.system('cls')
    interface()

    if draw_checker(box):
        print("It's a draw!")
        break