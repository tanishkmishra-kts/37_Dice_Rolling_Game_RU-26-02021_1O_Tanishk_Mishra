# Python Dice Rolling Game 🎲

A clean, modular command-line Python script that simulates rolling a 6-sided die, calculates statistics (frequency, total, and average), handles ties for the most frequent face, and includes robust input validation.

---

## Features

- **Robust Input Validation:** Ensures users can only enter whole numbers between `1` and `1000`, gracefully handling invalid strings or out-of-range integers.
- **Statistical Analysis:** 
  - Computes the frequency count for each face (1 through 6).
  - Calculates the total sum of all rolls.
  - Computes the mathematical average of the roll outcomes.
- **Tie-Aware Mode Detection:** Automatically detects whether a single face was rolled the most or if there's a tie between multiple faces.
- **Modular Code Structure:** Organized into discrete functions adhering to single-responsibility principles for easy readability and maintenance.
- **Repeat Play:** Interactive loop allowing users to play multiple rounds.

---

## Requirements

- Python 3.x (No external libraries required; uses Python's built-in `random` module).

---

## How to Run

1. Clone or download the script (`dice_game.py`) to your local machine.
2. Open your terminal or command prompt.
3. Run the script using Python:
   ```bash
   python dice_game.py