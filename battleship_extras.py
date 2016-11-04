import os
import time
from random import randint


def welcome():
    print("\n", "\t" * 6, "\033[1m !!WELCOME TO THE BATTLESHIP GAME!!\033[0m \n \n")
    command = input("You can start now with the 'start' command to play against a player." +
                    "Use the 'start_ai' command to play against a bot or read the how-to-play" +
                    " with the 'howto' command!" +
                    " Please specify a command [start, start_ai, howto]: ")

    if (command == "howto"):
        cls()
        print("\t" * 6, "How-TO-PLAY \n")
        print("The purpose of the game is to destroy the opposing player's battleships," +
              " and ends with a fight to the death.\n")
        print("1. In the first phases the two player can secretly arranges their ships on their primary grid." +
              "You can’t take two ship on the same coordinate and the ships cannot overlap.\n")
        print("2. After the ships have been positioned, the first player can attack and choose the coordinate" +
              "where he/she would like to shoot. The attacking player notes the hit or miss the ship." +
              "If she/he hitting the another player ship, he/she get a point.\n")
        print("3. That player win the game, who has more points :)")
        time.sleep(7)
        cls()
        return 1
    elif (command == "start"):
        cls()
        print("\n", "\t" * 6, "Let's play Battleship!")
        time.sleep(3)
        return 1
    elif (command == "start_ai"):
        cls()
        print("\n", "\t" * 6, "\033[1m\033[4m Let's play Battleship!\033[0m")
        time.sleep(3)
        return 2
    else:
        welcome()


# Function for clearing screen

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def add_nickname_ai():
    global player_one
    player_one = input("Please add your nickname: \033[92m")
    global player_two
    player_two = "AI"


def add_nickname():
    global player_one
    player_one = input("Please add your nickname - Player One: \033[92m")
    print("\033[0m")
    global player_two
    player_two = input("Please add your nickname - Player Two: \033[92m")
    # change the print color
    print("\033[0m")


# This funtcion creates the board of the game
def create_board():
    board = []
    for x in range(5):
        board.append(["0"] * 5)
    return board

# Prints the board on the console. Each element will looke like "~ "


def print_board(board):
    for row in board:
        for element in row:
            if(int(element) == 0):
                print("\033[94m| ~ | \033[0m", end="")
        print()


# Asks the row number from the user to place the ships
def row_func():
    row = 0
    while((row < 1) or (row > 5)):
        row_input = input("Select a row number (1 <= number <= 5): ")
        if (row_input.isnumeric() is True and int(row_input) <= 5 and int(row_input) != 0):
            row = int(row_input)
            return row
        else:
            print ("Please enter a valid integer (1 - 5)")
            continue


# Asks the column number from the user to place the ships
def column_func():
    column = 0
    while((column < 1) or (column > 5)):
        column_input = input("Choose column number (<= 1 number <= 5): ")
        if (column_input.isnumeric() is True and int(column_input) <= 5 and int(column_input) != 0):
            column = int(column_input)
            return column
        else:
            print ("Please enter a valid integer (1 - 5)")
            continue


# This function containts different function calls and asks the user to place the ships
def place_map1():
    map1 = create_board()
    print_board(map1)
    i = 0
    print("\n\nFirst phase - Place ships\nSelect a row number then a column number to place a ship")
    print("{0}, please place your ships!".format(player_one))
    # Each phase has 5 rounds for placing and for attacking
    while(i < 5):
        print("\nPlacement phase \n\033[92m{0}\033[0m, Round ".format(player_one), i + 1, ".", sep="")
        row_num = row_func() - 1
        column_num = column_func() - 1
        # Checks if there is a ship already
        if(map1[row_num][column_num] == 1):
            print("There is a ship already. Place it to somewhere else!")
        else:
            # If not, the user can place a ship to there
            map1[row_num][column_num] = 1
            # Prints the map using "~ " and "O " signs
            for e in map1:
                print()
                for x in e:
                    if(int(x) == 0):
                        print("\033[94m | ~ | \033[0m", end="")
                    elif(int(x) == 1):
                        print("\033[94m | 0 | \033[0m", end="")
            # Prints the last select
            print("\nIn the last round you selected the ", row_num + 1, ". row.", sep="")
            print("In the last round you selected the ", column_num + 1, ". column.", sep="")
            i += 1
    time.sleep(5)
    # Clearing the screen
    cls()
    return map1


def place_map2():
    map2 = create_board()
    print_board(map2)
    i = 0
    print("\nFirst phase - Place ships\nSelect a row number then a column number to place a ship")
    print("{0}, please place your ships!".format(player_two))
    # Each phase has 5 rounds for placing and for attacking
    while(i < 5):
        print("\nPlacement phase\n\033[92m{0}\033[0m, Round ".format(player_two), i + 1, ".", sep="")
        row_num = row_func() - 1
        column_num = column_func() - 1
        # Checks if there is a ship already
        if(map2[row_num][column_num] == 1):
            print("There is a ship already. Place it to somewhere else!")
        else:
            # If not, the user can place a ship to there
            map2[row_num][column_num] = 1
            # Prints the map using "~ " and "O " signs
            for e in map2:
                print()
                for x in e:
                    if(int(x) == 0):
                        print("\033[94m| ~ | \033[0m", end="")
                    elif(int(x) == 1):
                        print("\033[94m| 0 | \033[0m", end="")
            # Prints the last select
            print("\nIn the last round you selected the ", row_num + 1, ". row.", sep="")
            print("In the last round you selected the ", column_num + 1, ". column.", sep="")
            i += 1

    time.sleep(5)
    # Clearing the screen
    cls()
    return map2


def random_row_and_col():
    return randint(1, 5)


def place_map_ai():
    map2 = create_board()
    i = 0
    print("AI is placing ships...\n\nPlease wait!")
    # Each phase has 5 rounds for placing and for attacking
    while(i < 5):
        row_num = random_row_and_col() - 1
        column_num = random_row_and_col() - 1
        # Checks if there is a ship already
        if(map2[row_num][column_num] == 1):
            row_num = random_row_and_col() - 1
            column_num = random_row_and_col() - 1
        else:
            map2[row_num][column_num] = 1
            i += 1

    time.sleep(5)
    return map2


def attack_map1(marked_list):
    map1 = marked_list
    i = 0
    hit_counter1 = 0
    print("Second phase - Attack\nSelect a row number then a column number to fire")
    print("\033[92m{0}\033[0m, please choose where to fire!".format(player_one))
    # Each phase has 5 rounds for placing and for attacking
    while(i < 5):
        print("\nAttack phase\n\033[92m{0}\033[0m, Round ".format(player_one), i + 1, ".", sep="")
        row_num = row_func() - 1
        column_num = column_func() - 1
        # Checks if there is a ship already
        if(map1[row_num][column_num] == 1):
            map1[row_num][column_num] = 2
            # Prints the map using "~ ", "X ", and "Q " signs
            for e in map1:
                print()
                for x in e:
                    if(int(x) == 0):
                        print("\033[94m| ~ | \033[0m", end="")
                    elif(int(x) == 1):
                        print("\033[94m| ~ | \033[0m", end="")
                    elif(int(x) == 2):
                        print("\033[94m|\033[91m X \033[0m\033[94m| \033[0m", end="")
                    elif(int(x) == 3):
                        print("\033[94m|\033[0m Q \033[94m| \033[0m", end="")
            # If the user hits a ship, then prints these messages
            print("\nHit - You sunk a battleship")
            print("In the last round you shot the ", row_num + 1, ". row.", sep="")
            print("In the last round you shot the ", column_num + 1, ". column.", sep="")
            hit_counter1 += 1
            i += 1
            print("Points:", hit_counter1)
        elif((map1[row_num][column_num] == 2) or (map1[row_num][column_num] == 3)):
            print("You already shoot there! Shoot to somewhere else!")
        else:
            map1[row_num][column_num] = 3
            # Prints the map using "~ ", "X ", and "Q " signs
            for e in map1:
                print()
                for x in e:
                    if(int(x) == 0):
                        print("\033[94m| ~ | \033[0m", end="")
                    elif(int(x) == 1):
                        print("\033[94m| ~ | \033[0m", end="")
                    elif(int(x) == 2):
                        print("\033[94m|\033[91m X \033[0m\033[94m| \033[0m", end="")
                    elif(int(x) == 3):
                        print("\033[94m|\033[0m Q \033[94m| \033[0m", end="")
            # Else prints these messages
            print("\nYou missed it")
            print("In the last round you shot the ", row_num + 1, ". row.", sep="")
            print("In the last round you shot the ", column_num + 1, ". column.", sep="")
            i += 1
            print("Points:", hit_counter1)
    return hit_counter1


def attack_map2(marked_list):
    map2 = marked_list
    i = 0
    hit_counter2 = 0
    print("\nSecond phase - Attack.\nSelect a row number then a column number to fire")
    print("\033[92m{0}\033[0m, please choose where to fire!".format(player_two))
    # Each phase has 5 rounds for placing and for attacking
    while(i < 5):
        print("\nAttack phase\n\033[92m{0}\033[0m, Round ".format(player_two), i + 1, ".", sep="")
        row_num = row_func() - 1
        column_num = column_func() - 1
        if(map2[row_num][column_num] == 1):
            map2[row_num][column_num] = 2
            # Prints the map using "~ ", "X ", and "Q " signs
            for e in map2:
                print()
                for x in e:
                    if(int(x) == 0):
                        print("\033[94m| ~ | \033[0m", end="")
                    elif(int(x) == 1):
                        print("\033[94m| ~ | \033[0m", end="")
                    elif(int(x) == 2):
                        print("\033[94m|\033[91m X \033[0m\033[94m| \033[0m", end="")
                    elif(int(x) == 3):
                        print("\033[94m|\033[0m Q \033[94m| \033[0m", end="")
            # If the user hits a ship, then prints these messages
            print("\nHit - You sunk a battleship")
            print("In the last round you shot the ", row_num + 1, ". row.", sep="")
            print("In the last round you shot the ", column_num + 1, ". column.", sep="")
            hit_counter2 += 1
            i += 1
            print("Points:", hit_counter2)
        elif((map2[row_num][column_num] == 2) or (map2[row_num][column_num] == 3)):
            print("You already shoot there! Shoot to somewhere else!")
        else:
            map2[row_num][column_num] = 3
            # Prints the map using "~ ", "X ", and "Q " signs
            for e in map2:
                print()
                for x in e:
                    if(int(x) == 0):
                        print("\033[94m| ~ | \033[0m", end="")
                    elif(int(x) == 1):
                        print("\033[94m| ~ | \033[0m", end="")
                    elif(int(x) == 2):
                        print("\033[94m|\033[91m X \033[0m\033[94m| \033[0m", end="")
                    elif(int(x) == 3):
                        print("\033[94m|\033[0m Q \033[94m| \033[0m", end="")
            # Else prints these messages
            print("\nYou missed it")
            print("In the last round you shot the ", row_num + 1, ". row.", sep="")
            print("In the last round you shot the ", column_num + 1, ". column.", sep="")
            i += 1
            print("Points:", hit_counter2)
    return hit_counter2


def attack_map_ai(marked_list):
    map2 = marked_list
    i = 0
    hit_counter2 = 0
    print("\nNow the AI will attack")
    time.sleep(3)
    # Each phase has 5 rounds for placing and for attacking
    while(i < 5):
        print("\nAttack phase\nAI, Round ", i + 1, ".", sep="")
        row_num = random_row_and_col() - 1
        column_num = random_row_and_col() - 1
        if(map2[row_num][column_num] == 1):
            map2[row_num][column_num] = 2
            # Prints the map using "~ ", "X ", and "Q " signs
            for e in map2:
                print()
                for x in e:
                    if(int(x) == 0):
                        print("\033[94m| ~ | \033[0m", end="")
                    elif(int(x) == 1):
                        print("\033[94m| ~ | \033[0m", end="")
                    elif(int(x) == 2):
                        print("\033[94m|\033[91m X \033[0m\033[94m| \033[0m", end="")
                    elif(int(x) == 3):
                        print("\033[94m|\033[0m Q \033[94m| \033[0m", end="")
            # If the AI hits a ship, then prints these messages
            print("\nHit - AI sunk a battleship")
            print("In the last round AI shot the ", row_num + 1, ". row.", sep="")
            print("In the last round AI shot the ", column_num + 1, ". column.", sep="")
            hit_counter2 += 1
            i += 1
            print("Points:", hit_counter2)
            time.sleep(3)
        elif((map2[row_num][column_num] == 2) or (map2[row_num][column_num] == 3)):
            row_num = random_row_and_col() - 1
            column_num = random_row_and_col() - 1
        else:
            map2[row_num][column_num] = 3
            # Prints the map using "~ ", "X ", and "Q " signs
            for e in map2:
                print()
                for x in e:
                    if(int(x) == 0):
                        print("\033[94m| ~ | \033[0m", end="")
                    elif(int(x) == 1):
                        print("\033[94m| ~ | \033[0m", end="")
                    elif(int(x) == 2):
                        print("\033[94m|\033[91m X \033[0m\033[94m| \033[0m", end="")
                    elif(int(x) == 3):
                        print("\033[94m|\033[0m Q \033[94m| \033[0m", end="")
            print("\nAI missed it")
            print("In the last round AI shot the ", row_num + 1, ". row.", sep="")
            print("In the last round AI shot the ", column_num + 1, ". column.", sep="")
            i += 1
            time.sleep(3)
    return hit_counter2


# This function calculates the result according to the players's points

def result(player1_result, player2_result):
    print ("\nCalculating the result...")
    time.sleep(3)
    print("\nPoints of \033[92m{0}\033[0m:".format(player_one), player1_result)
    time.sleep(2)
    print("Points of \033[92m{0}\033[0m:".format(player_two), player2_result)
    time.sleep(2)
    print()
    if(player1_result == player2_result):
        print("\033[92m\nThe result is draw!\n \033[0m")
    elif(player1_result > player2_result):
        print("\n\033[92mThe winner is {0} \033[0m \n".format(player_one))
    elif(player1_result < player2_result):
        print("\n\033[92mThe winner is {0}\033[0m \n".format(player_two))

# The main function contains different function calls


def main():
    game_type = welcome()
    print("First phase.\nSelect a row number then a column number to place a ship")
    if(game_type == 1):
        add_nickname()
        placedship_map1 = place_map1()
        placedship_map2 = place_map2()
        hits1 = (attack_map1(placedship_map2))
        hits2 = (attack_map2(placedship_map1))
        result(hits1, hits2)
    elif(game_type == 2):
        add_nickname_ai()
        placedship_map1 = place_map1()
        placedship_map_ai = place_map_ai()
        print("\nAI placed ships! Now shoot the AI's ships!\n")
        hits1 = (attack_map1(placedship_map_ai))
        hits2 = (attack_map_ai(placedship_map1))
        result(hits1, hits2)

main()
