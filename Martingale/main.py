import random

# Constants:
HEADS = 'heads'
TAILS = 'tails'
COIN_VALUES = [HEADS, TAILS]


def flip_coin(): # Function to flip a coin
	return random.choice(COIN_VALUES)

def play_martingale(*, starting_funds: int, min_bet: int, max_bet: int) -> int:

  steps_to_loose = 0
  current_funds = starting_funds
  current_bet = min_bet

  while current_funds > 0:
    print('==============================')
    steps_to_loose += 1
    current_funds -= current_bet
    print(f'Current funds: {current_funds}, Current bet: {current_bet}')
    flipped_coin_value = flip_coin()

    if flipped_coin_value == HEADS: # Win
      win = current_bet * 2
      print(f'Win: {win}')
      current_funds += win
      current_bet = min_bet

    else: # Loose
      print('Loose')
      current_bet *= 2

      if current_bet > max_bet:
        current_bet = min_bet

      if current_bet > current_funds:
        current_bet = current_funds

  return steps_to_loose

if __name__ == "__main__":
  print(play_martingale(starting_funds=100, min_bet=1, max_bet=1000)) # Game parameters