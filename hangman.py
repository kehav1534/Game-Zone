from random import randint
import os
from ascii_art import hangman , hangman_ascii
from score import game_scores
from load import loading

def Hangman(score) :
    try_again = 'y'
    loading()
    while try_again == 'y' :


        word_list = [ "hitman" , "postman" , "book" , "tree" , "laptop" , "uplift" , "apoligize" ]

        print("score :" , score)
        selected     =  word_list[randint(0 , len(word_list) - 1 )]
        space = []
        for n in range( 0 , len(selected)) :
            space.append(" __ ")

        select_list = []
        for letter in selected:
            select_list.append(letter)
        print("\n")
        life = 6
        print(hangman)
        while life > 0 and space.count(" __ ") > 0 :

            Guess = input("\nGuess a letter : ").strip(" ")
            Guess.lower()
            for n in range( len(select_list) ):
                if select_list[n] == Guess :
                    space[n] = f" {select_list[n]} "
                elif len(select_list) - 1 == n and select_list.count(Guess) == 0  :
                    life = life - 1
            os.system('cls')
            if life <= 2 :
                print("You're running out of health life...")
            print(hangman_ascii[life])

            word = ""
            for n in space:
                word += n
            print(word)
            if life == 0:
                print("\nYou loose...Try again!")
            elif space.count(" __ ") == 0 :
                print("\nYaay! You won the game.")
        score += life
        try_again = input("\nDo you want to try again? (y/n)\n? ").strip(" ")
        try_again = try_again.lower()
        os.system('cls')

    return score 

