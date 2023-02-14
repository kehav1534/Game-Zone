import os
import random
from score import game_scores

def rock_paper_n_scissors(score) :
     wanna_continue = 'y'
     while wanna_continue == 'y' or wanna_continue == 'yes' :
          result = ''
          print("---------------------------------------------Rock-@--Paper-#--Scissors-X-------------------------------------------------\n")
          print("Score : " , score)
          user = input(">> ").lower()

          game = ['rock' , 'paper' , 'scissors']

          game_random = game[random.randint(0,2)]

          print(f">>Computer >>> {game_random}")

          if(user[0] == "r" and game_random == "paper"):
               result = 'loose'
          elif (user[0] == "r" and game_random == "scissors"):
               result = 'win'
          elif user[0] == "p" and game_random == "rock":
               result = 'win'
          elif user[0] =='p' and game_random == "scissors":
               result = 'loose'
          elif user[0] == "s" and game_random == "rock":
               result = 'loose'
          elif user[0] == "s" and game_random == "paper":
               result = 'win'
          elif user == game_random:
               result = 'draw'


          if result == 'loose' :
               print(">>result : You loose. Better luck next time")
          elif result == 'win' :
               print(">>result : You win")
               score += 1
          elif result == 'draw' :
               print(">>result : Draw")

          wanna_continue = input("Wanna continue playing? (y/n)").strip(" ")
          wanna_continue = wanna_continue.lower()

          os.system('cls')
     return score