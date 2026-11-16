import random


def get_valid_rolls_input():
  """Validates that the number of rolls is an integer between 1 and 1000."""
  while True:
    user_input = input("Number of rolls: ")
    try:
      num = int(user_input)
      if 1 <= num <= 1000:
        return num
      else:
        print("Invalid input. Enter a whole number from 1 to 1000.")
    except ValueError:
      print("Invalid input. Enter a whole number from 1 to 1000.")


def roll_dice(num_rolls):
  """Rolls a 6-sided die num_rolls times using the random module."""
  return [random.randint(1, 6) for _ in range(num_rolls)]


def calculate_statistics(rolls):
  """Calculates frequency of each face, total sum, and average."""
  # Initialize frequency dictionary for faces 1 to 6
  freq = {i: 0 for i in range(1, 7)}
  for roll in rolls:
    freq[roll] += 1

  total = sum(rolls)
  average = total / len(rolls) if rolls else 0
  return freq, total, average


def display_results(freq, total, average):
  """Displays frequency, total, average, and most frequent face(s)."""
  # Format frequency output
  freq_parts = [f"{face}:{freq[face]}" for face in range(1, 7)]
  print("Frequency: " + " | ".join(freq_parts))
  print(f"Total: {total} | Average: {average:.2f}")

  # Determine most frequent face(s) handling ties
  max_freq = max(freq.values())
  modes = [face for face, count in freq.items() if count == max_freq]

  if len(modes) == 1:
    time_str = "1 time" if max_freq == 1 else f"{max_freq} times"
    print(f"Most frequent: {modes[0]} ({time_str})")
  else:
    modes_str = " and ".join(map(str, modes))
    print(f"Most frequent: {modes_str} ({max_freq} times each)")


def main():
  print("--- Welcome to the Dice Rolling Game! ---")
  while True:
    num_rolls = get_valid_rolls_input()
    rolls = roll_dice(num_rolls)

    # Optional: print rolls if you want to see what was rolled
    # print(f"Rolls: {rolls}")

    freq, total, average = calculate_statistics(rolls)
    display_results(freq, total, average)

    play_again = input("Play again? (y/n): ").strip().lower()
    if play_again != "y":
      print("Thanks for playing!")
      break


if __name__ == "__main__":
  main()