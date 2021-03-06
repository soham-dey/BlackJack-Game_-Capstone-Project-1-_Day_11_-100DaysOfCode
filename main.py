############### Blackjack Project #####################
import random
from replit import clear
from art import logo


def blackjack():
  print(logo)
#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
  def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

#Deal the user and computer 2 cards each using deal_card() and append().
  user_cards = []
  computer_cards=[]
  for i in range(0,2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

#Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
  def calculate_score(card_list):
    sum_cards= sum(card_list)
    #Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
    if len(card_list)==2 and (11, 10) in card_list:
      return "0"
    elif 11 in card_list and sum_cards>21:
      #Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
      card_list.remove(11)
      card_list.append(1)
      return int(sum_cards)
    else:
      return int(sum_cards)

#Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
  def check_score(user_cards, computer_cards):
    user_score= int(calculate_score(user_cards))
    computer_score= int(calculate_score(computer_cards))
    if user_score=="0" or computer_score=="0" or int(user_score)>21:
      end="Yes"
    elif int(user_score)==21:
      end="Yes"
    else:
      end="No"
    return end
    
#If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
  check_score(user_cards, computer_cards)
  end=check_score(user_cards, computer_cards)
  print("User's Initial cards: ", user_cards)
  print("Computer's Initial Card(only one): ", computer_cards[0])
  while end=="No":
    if end=="No":
      draw_another_card=input("Do you want to draw another card? Type 'y' for yes and 'n' for No: ")
      if draw_another_card=="y":
        user_cards.append(deal_card())
        #The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.
        check_score(user_cards, computer_cards)
        end=check_score(user_cards, computer_cards)
        if sum(user_cards)>=21:
          end="Yes"  
      elif draw_another_card=="n":
        end="Yes"
        #Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
        if sum(computer_cards)<17:
          while sum(computer_cards)<17:
            computer_cards.append(deal_card())
          end="Yes"

  user_total=sum(user_cards)
  computer_total=sum(computer_cards)
  
  #If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
  if (11,10) in user_cards and len(user_cards)==2:
    user_total=0
    print("You have won!")
  elif (11,10) in computer_cards and len(computer_cards)==2:
    computer_total=0
    print("Computer has won!")
  elif user_total>21:
    print("Computer has won!")
  elif computer_total>21:
    print("You have won!")
  elif computer_total>user_total:
    print("Computer has won!")
  elif computer_total==user_total:
    print("You have a draw!")
  elif user_total==21:
      print("You have won!")

  print("User's cards: ", user_cards, "\nUser's Score: ", user_total)
  print("Computer's cards: ", computer_cards, "\nComputer's Score: ", computer_total)

#Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
  new_game=input("Do you want to start a new game? type 'y' for Yes and 'n' for No: ")
  if new_game=="y":
    clear()
    blackjack()
  else:
    clear()

# call the game
blackjack()
