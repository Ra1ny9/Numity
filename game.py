import random

# Define the functions for each hint

# Hint 1: Check if number is even or odd
def even_odd(num):
    return f"The number is {'even' if num % 2 == 0 else 'odd'}"

# Hint 2: Check if number is greater or smaller than a random number
def greater_smaller(num):
    rand_choice = random.choice(["greater", "smaller"])
    
    if rand_choice == "greater":
        comparison_value = random.randint(10, 30)  # Random number between 10 and 30 for "Greater than"
        return f"The number is greater than {comparison_value}" if num > comparison_value else f"The number is smaller than or equal to {comparison_value}"
    
    elif rand_choice == "smaller":
        comparison_value = random.randint(70, 99)  # Random number between 70 and 99 for "Smaller than"
        return f"The number is smaller than {comparison_value}" if num < comparison_value else f"The number is greater than or equal to {comparison_value}"

# Hint 3: Check if number is divisible by 3 or 4 (randomly chosen), with adjustments for odd/even
def divisible_by(num, is_odd):
    if is_odd:  # If number is odd, we only check for divisibility by 3
        divisor = 3
        return f"The number is {'divisible' if num % divisor == 0 else 'not divisible'} by {divisor}"
    else:  # If number is even, randomly choose between 3 and 4
        divisor = random.choice([3, 4])
        return f"The number is {'divisible' if num % divisor == 0 else 'not divisible'} by {divisor}"

# Hint 4: Check if number reversed is even or odd
def reversed_even_odd(num):
    reversed_num = int(str(num)[::-1])
    return f"The number reversed is {'even' if reversed_num % 2 == 0 else 'odd'}"

# Hint 5: Check if number is a perfect cube
def perfect_cube(num):
    return f"The number is {'a perfect cube' if round(num ** (1/3)) ** 3 == num else 'not a perfect cube'}"

# Hint 6: Check if number is in the first 10 digits of pi
def in_first_10_digits_of_pi(num):
    pi_digits = [3, 14, 41, 15, 59, 92, 26, 65, 53, 35, 1, 4, 5, 9, 2, 6]  # Corrected digits of pi
    return f"The number is {'in' if num in pi_digits else 'not in'} the first 10 digits of pi"

# Hint 7: Check if number is in the Fibonacci sequence
def fibonacci(num):
    fib_sequence = [0, 1]
    while fib_sequence[-1] < num:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return f"The number is {'in' if num in fib_sequence else 'not in'} the Fibonacci sequence"

# Hint 8: Sum of the prime factors of the number
def sum_of_prime_factors(num):
    factors = []
    for i in range(2, num + 1):
        while num % i == 0:
            factors.append(i)
            num //= i
    prime_sum = sum(factors)
    return f"The sum of the prime factors of the number is {prime_sum}"

# Hint 9: Square root
def square_root(num):
    if (num ** 0.5).is_integer():
        return "The number has a perfect square root."
    else:
        return "The number does not have a perfect square root."

# Hint 10: Digit sum
def digit_sum(num):
    return f"The sum of the digits of the number is {sum(int(digit) for digit in str(num))}"

# List of hints
hints = [
    ("Even/Odd", even_odd),
    ("Greater/Smaller than", greater_smaller),
    ("Divisible by", divisible_by),
    ("Reversed Even/Odd", reversed_even_odd),
    ("Perfect Cube", perfect_cube),
    ("In the first 10 digits of Pi", in_first_10_digits_of_pi),
    ("Fibonacci Number", fibonacci),
    ("Sum of Prime Factors", sum_of_prime_factors),
    ("Square Root", square_root),
    ("Digit Sum", digit_sum)
]

# Function to validate user input
def get_valid_input():
    print("Please enter a number between 1 and 99.")
    while True:
        try:
            user_input = input("What is your guess? ")
            guess = int(user_input)  # Try converting input to integer
            if guess < 1 or guess > 99:
                print("The guess should be between 1 and 99. Please try again.")
            else:
                return guess
        except ValueError:
            print("Invalid input! Please enter a valid number between 1 and 99.")

# Main game loop
def start_game():
    # Generate a random number between 1 and 99
    num = random.randint(1, 99)
    
    # Get the first hint (Even/Odd)
    is_odd = num % 2 != 0  # Check if the number is odd
    print("Welcome to the number guessing game!")
    print("Try to guess the number based on the hints.")
    
    # Provide the first hint and give the user 10 tries
    attempts = 0
    while attempts < 10:
        # Choose the hint for this attempt
        hint_index = attempts
        hint_name, hint_function = hints[hint_index]

        # Provide the hint directly without the category
        if hint_name == "Divisible by":
            print(f"\nHint {hint_index + 1}: {hint_function(num, is_odd)}")  # Pass is_odd flag to handle divisibility hint
        else:
            print(f"\nHint {hint_index + 1}: {hint_function(num)}")

        # Get the user's guess
        user_guess = get_valid_input()  # Ensure valid input

        # Check if the guess is correct
        if user_guess == num:
            print(f"Congratulations! You guessed the number {num} correctly!")
            break

        # If the guess is incorrect, inform the user
        print("Incorrect guess. Let's move to the next hint.")
        attempts += 1

    if attempts == 10:
        print(f"\nSorry, you've used all 10 attempts. The correct number was {num}.")

# Start the game
if __name__ == "__main__":
    start_game()
    
    
