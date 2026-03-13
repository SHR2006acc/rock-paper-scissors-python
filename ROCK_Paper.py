import random
import os


def tuple_(number):
    if number == 1:
        return (-1, 1, 0)  # rock
    elif number == 2:
        return (1, 0, -1)  # paper
    else:
        return (0, -1, 1)  # ciseau


def names(number):
    if number == 1:
        return "rock"
    elif number == 2:
        return "paper"
    else:
        return "ciseau"


def result_(number, guess_human, n, guess_ai) -> bool:
    # True : Human win
    # false : ai win
    # none : Human draw
    if (number == n):
        return None
    for i in range(0, 3):
        if guess_human[i]*guess_ai[i] != 0:
            if guess_human[i] > guess_ai[i]:
                return True
            else:
                return False
    print("Error")


def main():
    paper = (1, 0, -1)
    rock = (-1, 1, 0)
    ciseau = (0, -1, 1)
    again = True
    while again == True:
        print("** Welcome To paper-rock-ciseau Game **\n\n")
        print("1-Rock\n2-paper\n3-ciseau\n_____________________________\n")
        number = int(input("Enter a number :"))
        guess_human = tuple_(number)
        n = random.randrange(1, 4)
        guess_ai = tuple_(n)
        print(
            f"\n_____________________________\n User : {names(number)}\n AI : {names(n)}")
        result = result_(number, guess_human, n, guess_ai)
        if result == None:
            print(" Result : Draw")
        elif result == True:
            print(" Result : User win ")
        else:
            print(" Result : Ai win ")
        again = bool(input("Type 1 to play again | Type 0 to disconnect "))
        os.system("cls")
    print("Good bye :)")


main()
