# Rodrigo Becerril Ferreyra 
# 017584071
# CECS 100 Autumn 2018
# 2018-10-03
# Project 2
# "Random-Number-Generator Game"

# Corresponds to #11 in p. 281 in the text
# Objective: make a game using randomly generated numbers without importing the "random" module.
# ---------------------------------------

# For initial seed
import time

# Main RNG. See https://en.wikipedia.org/wiki/Linear_congruential_generator
def rng(seed):
    return int((2 * seed + 0) % 6997) #range: 1 to 6997

def main():

    # Will keep track of player's winning streak.
    score = 0
    # Will keep track of player's wrong misses.
    wrong = 3

    # Numlist stores random numbers, and the game will use two random indexes
    numlist = []

    # Instructions
    print("\nSimplify the expression. Get it  three times and it's game over!\n")

    # Gives the initial seed for random number generation.
    # * 10000000 ensures a whole number while keeping precision.
    seed = (time.time() * 10000000)

    # Will keep running as long as user gets the answer right.
    while(1):
        # Will populate numlist with 100 numbers
        for i in range(100):
            seed = rng(seed)
            numlist.append(seed)

        # assign values to num variables
        num1 = numlist[rng(seed) % 100]
        seed = rng(seed)
        num2 = numlist[rng(seed) % 100]

        # The equation
        print(str(num1) + " + " + str(num2))
        
        total = num1 + num2

        # A try block is always a good idea when user input is involved.
        try:
            # The user can enter his answer here.
            ui = int(input())

            # The following will be skipped if user input is invalid.

            # Compares user input to actual sum.
            # If incorrect, wrong will be decrimented and the correct answer printed.
                # if wrong <= 0 the game will end.
                # else, the game will continue.
            # If correct, score is incremented and the problem is reset.
            if ui != total:
                wrong -= 1
                print("\nAww, you failed! The answer was " + str(total) + ".", end = "")
                if wrong != 1:
                    print(" You have " + str(wrong) + " tries left.")
                else:
                    print(" You have " + str(wrong) + " try left.")

                if wrong == 0:
                    print("Aww! You ran out of lives! Try again next time!")
                    break

            else:
                print("\nGreat job! On to the next one.")
                score += 1
        # Catches the user error if ui is invalid.
        except ValueError:
            print("\nOops! That is not a valid number. Try removing any spaces or commas.")

# Call to main function.
main()
