import random


def start_game():
    number = random.randint(1,10)
    print("Welcome to the number game")
    name = input("What is your name: ")
    name = input(f"Would you like to play {name} [yes or no]: ").lower()
    if name == 'no':
        print('ok')
        exit()
    else:
        print("let's play")
    guess = 0
    while guess != number:
        guess = int(input('guess a number from 1 to 10 : '))
        if (guess < number):
            print('guess higher')
        elif (guess > number):
            print('guess lower')
        else:
            print('correct !!!')
            play_again = input("do you want to play again [yes or no]: ").lower()
            if play_again == 'yes':
                start_game()
            else:
                print('ok')

start_game()

