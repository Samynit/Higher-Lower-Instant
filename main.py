# Display art
from art import logo, vs
from game_data import data
import random
import os

def format_data(account):
  account_name = account["name"]
  account_descr = account["description"]
  account_country = account["country"]
  return (f"{account_name}, a {account_descr}, from {account_country}")

def check_answer(guess, a_followers, b_followers):
  if a_followers > b_followers:
    if guess == "a":
      return True
    else:
      return False
  else:
    return guess == "b"

def comments():
  if score == 0:
    print("You performed very bad.")
  elif score >= 1 and score <= 2:
    print("You performed bad.")
  elif score >= 3 and score <= 4:
    print("You performed good.")
  elif score >= 5 and score <= 8:
    print("You performed very good.")
  elif score >= 9:
    print("You performed extremely good.")


print(logo)
score = 0
game_continue = True
account_b = random.choice(data)

# Generate a random account to compare
while game_continue:
  # Making account at last position become the next first position
  account_a = account_b
  account_b = random.choice(data)
  
  while account_a == account_b:
    account_b = random.choice(data)
  
  print(f"Compare A: {format_data(account_a)}.")
  print(vs)
  print(f"Compare B: {format_data(account_b)}.")
  
  # Ask user for a guess
  guess = input("Who has more followers? Type 'A' or 'B': ").lower()
  
  
  a_follower_count = account_a["follower_count"]
  b_follower_count = account_b["follower_count"]
  
  is_correct = check_answer(guess, a_follower_count, b_follower_count)
  
  # Clear the screen between rounds
  os.system('cls')
  print(logo)
  # Get follower count of each account
  if is_correct:
    score += 1
    print(f"You're right! Current score: {score}.")
  else:
    game_continue = False
    print(f"Sorry, that's wrong! Final score: {score}.")
    comments()
    

