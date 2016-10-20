def cls():
    os.system('cls' if os.name=='nt' else 'clear')


def create_board():
    board = []
    for x in range(5):
        board.append(["0"] * 5)
    return board


def print_board(board):
    for row in board:
        print()
        for element in row:
            if(int(element) == 0):
                print ("~ ", end="")


def row_func():
    row = 0
    while((row < 1) or (row > 5)):
        row = int(input("Select a row number (1 <= number <= 5): "))
    return row


def column_func():
    column = 0
    while((column < 1) or (column > 5)):
        column = int(input("Choose column number (<= 1 number <= 5): "))
    return column


def place_map1():
    map1 = create_board()
    print_board(map1)
    i = 0
    print ("\nFirst phase - Place ships\nSelect a row number then a column number to place a ship")
    print("Player 1, please place your ships!")
    while(i < 3):
        print("\nPlacement phase\nPlayer 1, Round ", i+1 ,".", sep="")
        row_num = row_func() - 1
        column_num = column_func() - 1
        if(map1[row_num][column_num] == 1):
            print("There is a ship already. Place it to somewhere else!")
        else:
            map1[row_num][column_num] = 1
            for e in map1:
                print()
                for x in e:
                    if(int(x) == 0):
                        print ("~ ", end="")
                    elif(int(x) == 1):
                        print("O ", end="")
            print("\nIn the last round you selected the ", row_num + 1, ". row.", sep = "")
            print("In the last round you selected the ", column_num + 1, ". column.", sep = "")
            i +=1
    cls()
    return map1


def place_map2():  
    map2 = create_board()
    print_board(map2)
    i = 0
    print ("\nFirst phase - Place ships\nSelect a row number then a column number to place a ship")
    print("Player 2, please place your ships!")
    while(i < 3):
        print("\nPlacement phase\nPlayer 2, Round ", i+1 ,".", sep="")
        row_num = row_func() - 1
        column_num = column_func() - 1
        if(map2[row_num][column_num] == 1):
            print("There is a ship already. Place it to somewhere else!")
        else:
            map2[row_num][column_num] = 1
            for e in map2:
                print()
                for x in e:
                    if(int(x) == 0):
                        print ("~ ", end="")
                    elif(int(x) == 1):
                        print("O ", end="")
            print("\nIn the last round you selected the ", row_num + 1, ". row.", sep = "")
            print("In the last round you selected the ", column_num + 1, ". column.", sep = "")
            i +=1
    cls()
    return map2


def attack_map1(marked_list):
    map1 = marked_list
    i = 0
    hit_counter1 = 0
    print ("Second phase - Attack\nSelect a row number then a column number to fire")
    print("Player 1, please choose where to fire!")
    while(i < 3):
        print("\nAttack phase\nPlayer 1, Round ", i+1 ,".", sep="")
        row_num = row_func() - 1
        column_num = column_func() - 1
        if(map1[row_num][column_num] == 1):
            map1[row_num][column_num] = 2
            for e in map1:
                print()
                for x in e:
                    if(int(x) == 0):
                        print ("~ ", end="")
                    elif(int(x) == 1):
                        print("~ ", end="")
                    elif(int(x) == 2):
                        print("X ", end="")
                    elif(int(x) == 3):
                        print("Q ", end="")
            print("\nHit - You sunk a battleship")
            print("In the last round you shot the ", row_num + 1, ". row.", sep = "")
            print("In the last round you shot the ", column_num + 1, ". column.", sep = "")
            hit_counter1 += 1
            i +=1
            print("Points:", hit_counter1)
        else:
            map1[row_num][column_num] = 3
            for e in map1:
                print()
                for x in e:
                    if(int(x) == 0):
                        print ("~ ", end="")
                    elif(int(x) == 1):
                        print("~ ", end="")
                    elif(int(x) == 2):
                        print("X ", end="")
                    elif(int(x) == 3):
                        print("Q ", end="")
            print("\nYou missed it")
            print("In the last round you shot the ", row_num + 1, ". row.", sep = "")
            print("In the last round you shot the ", column_num + 1, ". column.", sep = "")
            i +=1
            print("Points:", hit_counter1)
    return hit_counter1



def attack_map2(marked_list):
    map2 = marked_list
    i = 0
    hit_counter2 = 0
    print ("\nSecond phase - Attack.\nSelect a row number then a column number to fire")
    print("Player 2, please choose where to fire!")
    while(i < 3):
        print("\nAttack phase\nPlayer 2, Round ", i+1 ,".", sep="")
        row_num = row_func() - 1
        column_num = column_func() - 1
        if(map2[row_num][column_num] == 1):
            map2[row_num][column_num] = 2
            for e in map2:
                print()
                for x in e:
                    if(int(x) == 0):
                        print ("~ ", end="")
                    elif(int(x) == 1):
                        print("~ ", end="")
                    elif(int(x) == 2):
                        print("X ", end="")
                    elif(int(x) == 3):
                        print("Q ", end="")
            print("\nHit - You sunk a battleship")
            print("In the last round you shot the ", row_num + 1, ". row.", sep = "")
            print("In the last round you shot the ", column_num + 1, ". column.", sep = "")
            hit_counter2 += 1
            i +=1
            print("Points:", hit_counter2)
        else:
            map2[row_num][column_num] = 3
            for e in map2:
                print()
                for x in e:
                    if(int(x) == 0):
                        print ("~ ", end="")
                    elif(int(x) == 1):
                        print("~ ", end="")
                    elif(int(x) == 2):
                        print("X ", end="")
                    elif(int(x) == 3):
                        print("Q ", end="")
            print("\nYou missed it")
            print("In the last round you shot the ", row_num + 1, ". row.", sep = "")
            print("In the last round you shot the ", column_num + 1, ". column.", sep = "")
            i +=1
            print("Points:", hit_counter2)
    return hit_counter2
      

def result(player1_result, player2_result):
    print("\nPoints of Player1:", player1_result)
    print("Points of Player2:", player2_result)
    print()
    if(player1_result == player2_result):
        print("\nThe result is draw!\n")
    elif(player1_result > player2_result):
        print("\nThe winner is Player1\n")
    elif(player1_result < player2_result):
        print("\nThe winner is Player2\n")


def main():
    print ("Let's play Battleship!")
    print ("First phase.\nSelect a row number then a column number to place a ship")
    placedship_map1 = place_map1()
    placedship_map2 = place_map2()
    hits1 = attack_map1(placedship_map1)
    hits2 = attack_map2(placedship_map2)
    result(hits1, hits2)


import os
main()