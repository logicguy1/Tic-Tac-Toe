import random
import numpy
import math
import os

arr = numpy.array([["1","2","3"], # Create the 2d array that keeps track of where each user put their x and o
                   ["4","5","6"],
                   ["7","8","9"]])

def check_win(array):
    for x in ("x", "o"): # We run the code below check both the "o" and "x" using this loop
        for i in range(3): # We can check the whole grid by running the lines below 3 times using the loop
            if array[i, 0] == x and array[i, 1] == x and array[i, 2] == x: # Check horozontal
                return x
            elif array[0, i] == x and array[1, i] == x and array[2, i] == x: # Check vertical
                return x

        if array[0, 0] == x and array[1, 1] == x and array[2, 2] == x: # Check diagonal
            return x
        elif array[0, 2] == x and array[1, 1] == x and array[2, 0] == x: # Chcek the other diagonal
            return x

    return None

def print_arr(array):
    os.system('cls' if os.name == 'nt' else 'clear') # Clear the screen to make it look nice and neat
    print(
f"""{arr[0, 0]} │ {array[0, 1]} │ {array[0, 2]}
──┼───┼──
{array[1, 0]} │ {array[1, 1]} │ {array[1, 2]}
──┼───┼──
{array[2, 0]} │ {array[2, 1]} │ {array[2, 2]}"""
)

print_arr(arr)

players = ["x", "o"] # Keep track of the payers and their turn
random.shuffle(players) # make a random player start

while True:
    for x in players: # Loop through the players
        while True: # We want to make sure the user inputs a valid number
            opt = input(f"{x}'s turn\n>>> ") # Ask the user for a number from 1 to 9

            try: # We will try to convert the input to an integer this will throw an error if it contains letters
                if int(opt) <= 9 and int(opt) >= 1: # Is the number between 1 - 9

                    row = math.ceil(int(opt) / 3 - 1) # Calculate the row
                    colum = ( int(opt) - 1 ) % 3 # Calculate the colum

                    if arr[row, colum] != opt: # If the spot selected is taken up by an x or an o
                        print_arr(arr) # Tell the player how the current array looks
                        print("That spot has already been taken!")
                        continue # Continue the loop and ask the user agein

                    arr[row, colum] = x # Update the array

                    break # Exit the loop

                else: # Otherwise tell the user to use something else
                    print_arr(arr) # Tell the player how the current array looks
                    print("Please input a number between 1 and 9")

            except ValueError: # If the input could not be converted to an int
                print_arr(arr) # Tell the player how the current array looks
                print("Please input a number between 1 and 9")

        print_arr(arr) # Tell the player how the current array looks

        winSate = check_win(arr) # Check the bord if there is a winner
        if winSate is not None: # Check if there was a winner or not
            print(f"And the winner is {winSate}!") # Tell the user who won the game
            exit() # Finally exit the program
