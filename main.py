import random
options = ["Rock", "Paper", "Scissors"]


cpu_score = 0
player_score = 0
while True:
    player= input("Rock, Paper or Scissors? To end the game please type in End").capitalize()
    cpu = random.choice(options)
    ##The conditions of the game
    if player == cpu:
        print("DRAW!")
    elif player == "Rock":
        if cpu == "Paper":
            print("You Lose this round,Paper Eats Rock")
            cpu_score+=1
        else:
            print("You Win this round, Rock Batters Paper")
            player_score+=1
    elif player == "Paper":
        if cpu == "Scissors":
            print("You Lose this round,Scissors cuts through Paper")
            cpu_score+=1
        else:
            print("You Win this round,Paper Eats Rock")
            player_score+=1
    elif player == "Scissors":
        if cpu == "Rock":
            print("You Lose this round,Rock Batters Scissors")
            cpu_score+=1
        else:
            print("You Win this round,Scissors cuts through Paper")
            player_score+=1
    elif player == "End":
        print("Final Scores:")
        print(f"Cpu Score = {cpu_score}")
        print(f"Player Score ={player_score}")
        break



