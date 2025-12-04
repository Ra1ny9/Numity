# Number Guessing Game

A fun command-line number guessing game written in Python. Try to guess the secret number between 1 and 99 using clever hints!

## Description

This game generates a random number between 1 and 99 and challenges you to guess it. With each attempt, you receive a new hint to help narrow down the possibilities. You have 10 tries to guess correctly.

## Game Rules

1. The game picks a secret number between 1 and 99
2. You get 10 attempts to guess the number
3. Before each guess, you receive a helpful hint about the number
4. Enter your guess when prompted (must be between 1 and 99)
5. If you guess correctly, you win! Otherwise, you get another hint
6. If you use all 10 attempts without guessing correctly, the game reveals the answer

## Hints Provided

The hints progressively reveal more about the secret number:

1. Whether the number is even or odd
2. Whether it's greater or smaller than a comparison value
3. Whether it's divisible by 3 or 4
4. Whether the reversed number is even or odd
5. Whether it's a perfect cube
6. Whether it appears in the first 10 digits of Pi
7. Whether it's in the Fibonacci sequence
8. The sum of its prime factors
9. Whether it has a perfect square root
10. The sum of its digits

## How to Run

### On Replit

Simply click the **Run** button. The game will start automatically in the console.

### Locally

1. Make sure you have Python 3 installed
2. Clone this repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```
3. Run the game:
   ```bash
   python game.py
   ```

## Requirements

- Python 3.x (no external dependencies required)

## License

This project is open source and available for educational purposes.
