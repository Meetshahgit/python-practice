# This Python game is created to get an an real world idea of using if statment, Variables , While loops to create this game

# As the name suggest computer has will store a value which the user has to guess

# These are our variable which will help us use other functions
secret_word = "Learn"
user_answer = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False
score = 120

# Here we have created a small loop which allows players to guess variable entered

while user_answer != secret_word and not (out_of_guesses):
    if guess_count < guess_limit:
        user_answer = input("Enter Guess: ")
        guess_count += 1
    else:
        out_of_guesses = True
    score = score - 20

# Here we used if statement to let players know that they have won the game or lose the game
    
if out_of_guesses:
    print("You are out of Guesses, You Lose!!!")
else:
    print("you win!!!")
    print("your Score " + str(score))
