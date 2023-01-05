import random

def play_rps():
  # list of play options
  play = ["Rock", "Paper", "Scissors"]

  # assign a random play to the computer
  computer = random.choice(play)

  # get the player's play
  player = input("Enter Rock, Paper, or Scissors: ")

  # print the computer's play
  print(f"The computer played: {computer}")

  # determine the winner
  if player == computer:
    print("It's a tie!")
  elif player == "Rock":
    if computer == "Paper":
      print("The computer wins :(")
    else:
      print("You win!")
  elif player == "Paper":
    if computer == "Scissors":
      print("The computer wins :(")
    else:
      print("You win!")
  elif player == "Scissors":
    if computer == "Rock":
      print("The computer wins :(")
    else:
      print("You win!")
  else:
    print("Invalid input. Try again.")

# play the game
play_rps()
