import random

def roll_dice(num_rolls: int) -> dict:
    #  Initialize a dictionary to store the counts of each face
    roll_counts = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

    # Simulate rolling the dice
    for _ in range(num_rolls):
        roll = random.randint(1, 6)
        roll_counts[roll] += 1

    return roll_counts

def main():
    num_rolls = 100
    roll_counts = roll_dice(num_rolls)

    print(f"Results of {num_rolls} dice rolls:")
    for face, count in sorted(roll_counts.items()):
        print(f"Face: {face}: {count} time(s)")

if __name__ == "__main__":
    main()