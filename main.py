import os
from hangman import Hangman
import heads_or_tails , score
import rock_paper_siccors
from score import game_scores

def game() :
          
     cont = 'y'
     my_score = 0
     while cont == 'y' or cont == 'yes'  :
          temp_score = 0
          print("Game zone".center(209 , '_'))
          print(f"\nScore : {my_score}".center(380 , " "))
          print()
          game_select = input('''
                              1. hangman
                              2. Head or Tails
                              3. Rock-Paper-Scissors




             < Rule >                                                                                                 < quit >\n\n
game\\ > ''').strip(" ")
          game_select = game_select.lower()
          os.system('cls')
          if game_select == "hangman" or game_select == '1' :
               my_score = score.game_score(hangman_score = Hangman(game_scores["hangman"]) , RPS_score= 0, HeadsTails_score= 0)
      
          elif game_select == "head or tails" or game_select == '2' :
               my_score = score.game_score(hangman_score= 0 , RPS_score= 0 , HeadsTails_score= heads_or_tails.headntails(game_scores["heads_tails"]))
     
          elif game_select == "rock-paper-scissors" or game_select == '3' :
               my_score = score.game_score(hangman_score= 0 , RPS_score= rock_paper_siccors.rock_paper_n_scissors(game_scores["RPS"]) , HeadsTails_score= 0)
      
          elif game_select == "quit": 
               break
       
          cont = input("\nDo you want to continue playing? (y/n)\n > ")
          os.system('cls')

game()