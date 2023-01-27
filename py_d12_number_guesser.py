import random

attempts = 0
not_guessed = True
continue_game = True

def attempt_decider(difficulty_level):
    '''Assigns number of attempts'''
    if difficulty_level == "easy":
        return 10
    elif difficulty_level == "hard":
        return 5

def guess_checker(choosen_num, guess_num):
    '''Shows if the guessed number is high/low compared to the choosen number.'''
    if choosen_num == guess_num:
        print(f"You got it! The answer was {choosen_num}.")
        global not_guessed
        not_guessed = False
    elif choosen_num < guess_num:
        return "Too High"
    else:
        return "Too Low"

while continue_game == True:
    print('''
    ██████╗ ██╗   ██╗███████╗███████╗███████╗    ████████╗██╗  ██╗███████╗    ███╗   ██╗██╗   ██╗███╗   ███╗██████╗ ███████╗██████╗ 
    ██╔════╝ ██║   ██║██╔════╝██╔════╝██╔════╝    ╚══██╔══╝██║  ██║██╔════╝    ████╗  ██║██║   ██║████╗ ████║██╔══██╗██╔════╝██╔══██╗
    ██║  ███╗██║   ██║█████╗  ███████╗███████╗       ██║   ███████║█████╗      ██╔██╗ ██║██║   ██║██╔████╔██║██████╔╝█████╗  ██████╔╝
    ██║   ██║██║   ██║██╔══╝  ╚════██║╚════██║       ██║   ██╔══██║██╔══╝      ██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗
    ╚██████╔╝╚██████╔╝███████╗███████║███████║       ██║   ██║  ██║███████╗    ██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██████╔╝███████╗██║  ██║
     ╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚══════╝       ╚═╝   ╚═╝  ╚═╝╚══════╝    ╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝
    ''')
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    attempts = attempt_decider(difficulty)
    choosen_number = random.randint(1,100)

    while not_guessed == True:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        result = guess_checker(choosen_number, guess)
        if not result == None:
            print(result)
        if not_guessed == True:
            print("Guess Again.")
        attempts -= 1

        if attempts == 0:
            print(f"Game Over. The nuber was: {choosen_number}")
            not_guessed = False

    continue_gm = input("Do you wish to play again? Type 'y' for yes, type 'n' for no.").lower()
    if continue_gm == 'n':
        continue_game = False