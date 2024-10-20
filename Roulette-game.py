Python 3.12.7 (tags/v3.12.7:0b05ead, Oct  1 2024, 03:06:41) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import random

print('''
            32   15   19   4    21   2
        ---------------------------------
       | 26                            25  |
  3    |                                   |   17
       |                                   |
 35    |         Roulette Wheel            |   34
       |                                   |
 12    |                                   |   6
       |                                   |
       |                                   |
 28    |-----------------------------------|   27
       |    0 (Green)                      |
       |-----------------------------------|
 7     |                                   |   13
       |                                   |
 29    |                                   |   36
       |                                   |
 18    |                                   |   11
       |                                   |
       |                                   |
       |                                   |
 22    |                                   |   30
        ---------------------------------
            14   20   1    33   16   24
''')
def spin_roulette():
    # Spin the roulette wheel
    number = random.randint(0, 36)
    color = 'red' if number % 2 == 0 else 'black' if number != 0 else 'green'
    return number, color

def main():
    print("Welcome to the Roulette Game!")
    print("You can place your bet on:\n1. Number (0-36)\n2. Color (red/black)\n3. Even/Odd")
    bet_type = input("What type of bet would you like to make? (number/color/even/odd): ").strip().lower()

    if bet_type == 'number':
        bet_number = int(input("Enter a number to bet on (0-36): "))
...         if bet_number < 0 or bet_number > 36:
...             print("Invalid number! Please enter a number between 0 and 36.")
...             return
... 
...     elif bet_type == 'color':
...         bet_color = input("Enter the color to bet on (red/black): ").strip().lower()
...         if bet_color not in ['red', 'black']:
...             print("Invalid color! Please choose either 'red' or 'black'.")
...             return
... 
...     elif bet_type == 'even':
...         bet_even = 'even'
... 
...     elif bet_type == 'odd':
...         bet_odd = 'odd'
... 
...     else:
...         print("Invalid bet type! Please enter 'number' or 'color' or 'even', or 'odd'.")
...         return
... 
...     print("Spinning the roulette wheel...")
...     result_number, result_color = spin_roulette()
...     print(f"The ball landed on {result_number} ({result_color}).")
... 
...     # Check if the player has won
...     if bet_type == 'number' and result_number == bet_number:
...         print("Congratulations! You won by betting on the correct number!")
...     elif bet_type == 'color' and result_color == bet_color:
...         print("Congratulations! You won by betting on the correct color!")
...     elif bet_type == 'even' and result_number != 0 and result_number % 2 == 0:
...         print("Congratulations! You won by betting on an even number!")
...     elif bet_type == 'odd' and result_number % 2 != 0:
...         print("Congratulations! You won by betting on an odd number!")
...     else:
...         print("Sorry, you lost this time. Better luck next time!")
... 
... if __name__ == "__main__":
