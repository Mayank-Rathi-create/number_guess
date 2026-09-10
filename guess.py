import random

def number_guessing_game():
    print("Welcome to the Number guessing game.")
    print("Some Rules : \n There are 3 level in this game(Easy, Medium and Hard)." \
    "\n With each increase in level the chances will be less." \
    "\n You have to guess the number between 1 to 100." \
    "\n There will be some hint if you guessed the number wrong.")

    print("\n Please select the difficult leavel: \n" \
    "\n 1 for Easy" \
    "\n 2 for Medium" \
    "\n 3 for Hard")


    #chances code..................................................................................................
    chances = 0
    difficulty = " "
    try:
        choice_difficulty = int(input("Enter your choice (1,2,3): "))
    except ValueError:
        print("Please enter 1, 2, or 3.")
        return
    if choice_difficulty == 1:
        chances = 10
        difficulty = "Easy"
    elif choice_difficulty == 2:
        chances = 5
        difficulty = "Medium"
    elif choice_difficulty == 3:
        chances = 3
        difficulty = "Hard"
    else:
        print("invalid choice :)")
        return

    print("Great! you have selected ",difficulty ,"difficulty level.")
    print("Let's start the game. You have ",chances,"chances to guess the number between 1 to 100.")
    computer_number = random.randint(1,100)
    def guess_number():
        nonlocal chances
        while(chances > 0 ):
            try:
                user_guess = int(input("Enter your guess (1-100): "))
            except ValueError:
                print("Please enter a whole number.")
                continue

            if not 1 <= user_guess <= 100:
                print("Your guess must be between 1 and 100.")
                continue

            if user_guess == computer_number :
                print("You guessed the number right.")
                chances -=1
                print(chances,"chances were left")
                return
            elif user_guess > computer_number :
                print("Incorrect! the number is less than ",user_guess)
                chances -=1
            else :
                print("Incorrect! the number is greater than ",user_guess)
                chances -=1
        print("You have used all your chances. The correct number was ", computer_number)
    print("Game started.")
    guess_number()
number_guessing_game()

#play again codes......................................................................................................
play_again = input("Wannna play again?(y/n)")
if play_again == 'y' or play_again == 'Y':
    number_guessing_game()
else:
    print("Thanks for playing!")

