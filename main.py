import random

game = ["rock", "paper", "scissors"]
i = random.randint(0, 2)
random_pick = game[i]

while True:
    user_choice = input("Rock, paper or scissors?: ")
    if user_choice.lower() in {"rock", "paper", "scissors"}:
        break

if user_choice.lower() == "rock" and random_pick == "paper":
    print("YOU'VE LOST!")
elif user_choice.lower() == "rock" and random_pick == "scissors":
    print("YOU'VE WON!")
elif user_choice.lower() == "paper" and random_pick == "scissors":
    print("YOU'VE LOST!")
elif user_choice.lower() == "paper" and random_pick == "rock":
    print("YOU'VE WON!")
elif user_choice.lower() == "scissors" and random_pick == "rock":
    print("YOU'VE LOST!")
elif user_choice.lower() == "scissors" and random_pick == "paper":
    print("YOU'VE WON!")
else:
    print("DRAW!")