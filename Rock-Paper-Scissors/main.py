import random

def rock_paper_scissors(player, computer):
    if player == computer: # Draw
        return "Draw!"
    elif (player == "rock" and computer == "scissors") or \
      (player == "scissors" and computer == "paper") or \
      (player == "paper" and computer == "rock"): # Win
        return "You win!"
    else: # Lose
        return "You lose!"


def main():
  while True:
    player = input("Please, enter your choice (rock, paper, or scissors): ").lower() # Player choice
    computer = random.choice(["rock", "paper", "scissors"]) # Computer choice
    print(f"You chose: {player}")
    print(f"Computer chose: {computer}")
    print(rock_paper_scissors(player, computer))
    print('=' * 30) # Divider


if __name__ == "__main__":
  main()