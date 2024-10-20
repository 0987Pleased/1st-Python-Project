Python 3.12.7 (tags/v3.12.7:0b05ead, Oct  1 2024, 03:06:41) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import random
x = input("Will you win or loose?")

dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)


print("Dice Number 1:", dice1)
print("Dice Number 2:", dice2)


def print_dice_face(dice):
    if dice == 1:
        print('''
 -----
|     |
|  o  |
|     |
 -----
''')
    elif dice == 2:
        print('''
 -----
| o   |
|     |
|   o |
 -----
''')
    elif dice == 3:
        print('''
 -----
| o   |
|  o  |
|   o |
 -----
''')
    elif dice == 4:
        print('''
 -----
| o o |
|     |
| o o |
 -----
''')
    elif dice == 5:
        print('''
 -----
| o o |
|  o  |
| o o |
 -----
''')
    elif dice == 6:
        print('''
 -----
| o o |
| o o |
| o o |
 -----
''')

# Print the faces of both dice
print("Dice Face 1:")
print_dice_face(dice1)

print("Dice Face 2:")
print_dice_face(dice2)

# Print the sum of the dice
y=dice1+dice2
print("Computer Rolled: ", y )

dice3 = random.randint(1, 6)
dice4 = random.randint(1, 6)


print("\n\nDice Number 3:", dice1)
print("Dice Number 4:", dice2)


def print_dice_face(dice):
    if dice == 1:
        print('''
 -----
|     |
|  o  |
|     |
 -----
''')
    elif dice == 2:
        print('''
 -----
| o   |
|     |
|   o |
 -----
''')
    elif dice == 3:
        print('''
 -----
| o   |
|  o  |
|   o |
 -----
''')
    elif dice == 4:
        print('''
 -----
| o o |
|     |
| o o |
...  -----
... ''')
...     elif dice == 5:
...         print('''
...  -----
... | o o |
... |  o  |
... | o o |
...  -----
... ''')
...     elif dice == 6:
...         print('''
...  -----
... | o o |
... | o o |
... | o o |
...  -----
... ''')
... 
... # Print the faces of both dice
... print("Dice Face 1:")
... print_dice_face(dice3)
... 
... print("Dice Face 2:")
... print_dice_face(dice4)
... 
... # Print the sum of the dice
... y1=dice3+dice4
... print("User Rolled:", y1)
... 
... if x == "more" or "MORE" and y1>y:
...   print("YOU WIN")
... elif y1<y:
...   print("YOU LOOSE")
... elif x == "less" or "LESS" and y1<y:
...   print("YOU WIN")
... elif y==y1:
...   print("DRAW")
... else:
