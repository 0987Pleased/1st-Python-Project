Python 3.12.7 (tags/v3.12.7:0b05ead, Oct  1 2024, 03:06:41) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import random
import matplotlib.pyplot as plt
... 
... def random_walk(num_steps):
...     # Initialize the starting point at the origin (0, 0)
...     x = [0]
...     y = [0]
...     
...     # List of possible directions
...     directions = ['right', 'up', 'left', 'down']
... 
...     # Randomly generate or ask for user-defined steps
...     for _ in range(0, num_steps):
...         direction = input(f"Enter direction for step {_} (right/up/left/down or random): ").strip().lower()
... 
...         if direction == 'random':
...             direction = random.choice(directions)
...             print(f"Random direction chosen: {direction}")
...         elif direction not in directions:
...             print("Invalid direction! Please enter 'right', 'up', 'left', 'down', or 'random'.")
...             continue
... 
...         # Update position based on the chosen direction
...         if direction == 'right':  # Move right
...             x.append(x[-1] + 1)
...             y.append(y[-1])
...         elif direction == 'up':  # Move up
...             x.append(x[-1])
...             y.append(y[-1] + 1)
...         elif direction == 'left':  # Move left
...             x.append(x[-1] - 1)
...             y.append(y[-1])
...         elif direction == 'down':  # Move down
...             x.append(x[-1])
...             y.append(y[-1] - 1)
...     
...     return x, y
... 
... def plot_walk(x, y):
...     plt.figure(figsize=(10, 10))
...     plt.plot(x, y, marker='o', markersize=3, linestyle='-', color='b', alpha=0.6)
...     plt.title("2D Random Walk Simulation")
...     plt.xlabel("X position")
...     plt.ylabel("Y position")
...     plt.xlim(min(x) - 1, max(x) + 1)
...     plt.ylim(min(y) - 1, max(y) + 1)
...     plt.grid()
...     plt.show()
... 
... def main():
...     # Ask the user for the number of steps
...     while True:
...         try:
...             num_steps = int(input("Enter the number of steps for the random walk (positive integer): "))
...             if num_steps > 0:
...                 break
...             else:
...                 print("Please enter a positive integer.")
...         except ValueError:
...             print("Invalid input! Please enter a valid integer.")
... 
...     x, y = random_walk(num_steps)
...     plot_walk(x, y)
... 
... if __name__ == "__main__":
