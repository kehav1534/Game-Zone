import random
from time import sleep
import os
from ascii_art import Toss_ascii , head , tail
from score import game_scores

def headntails(score) :
     continu = 'y'
     while continu == 'y' or continu == "yes" :
               
          print(Toss_ascii,"\n\nScore : " , score)

          select = input("\n\nChoose Head or tail? \t").lower()
          select = select.strip(' ')

          coin = [ head , tail]

          if select == 'head' or select == '1':
               user_select = head
               print(user_select)

          elif select == 'tail' or select == '2':
               user_select = tail
               print(user_select)

          else:
               print("Choose a valid side of coin")


          random_select = coin[random.randint( 0 , len(coin)-1)]
          print("Tossing...")
          sleep(3)

          os.system('cls')

          print("You :\n" + user_select)
          print("Toss :\n")

          print(random_select)


          if random_select == user_select :
               print("Bravo! You win!!")
               score += 1
          else:
               print("You loose.")

          continu = input("\nDo want to play again?\n > ").lower()
          continu = continu.strip(" ")
          os.system('cls')
     return score
