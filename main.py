import random 

options = ["rock", "paper", "scissors"]

computer_option = random.choice(options)


print("WELCOME TO ROCK/PAPER/SCISSORS GAME!!!!!")
player_options = input("choose rock paper or scissors: ")



while True:
  if computer_option == "scissors" and player_options == "paper":
    print(f"sorry you lost the computer option was scissors and you choose paper")
    break

  elif computer_option == "rock" and player_options == "paper":
     print(f"you win!! the computer option was rock and yours was paper")
     break

  elif computer_option == "scissors" and player_options == "paper":
    print(f"sorry you lost the computer option was scissors and you choose paper")
    break
    

  elif computer_option == "rock" and player_options == "scissors":
    print(f"sorry you lost the computer option was scissors and you choose paper")
    break

  elif computer_option == "paper" and player_options == "rock":
    print(f"sorry you lost the computer option was scissors and you choose paper")
    break

  elif computer_option == "scissors" and player_options == "rock":
    print(f"sorry you lost the computer option was scissors and you choose paper")
    break
    

  elif computer_option ==  player_options:
    print(f"its a tie")
    break

  else:
    print("incorrect option choosen!! :(")
    break



  


  



