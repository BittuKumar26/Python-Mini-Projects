import random

choices = ['rock', 'paper', 'scissor']
print(*choices, sep="\n")

def game():
    computer = random.choice(choices)

    user = input('Your choice: ').lower()

    if user not in choices:
        while True:
            print('Invalid input') 
            user = input('Enter a valid choice: ')
            if user in choices:
                print('its valid')
                break
            else:
                continue

    print(f'Computer\'s choice: {computer}')

    if computer == user:
        print("Draw")
    elif computer == "rock" and user == "paper":
        print("User won!!!")
    elif computer == "scissor" and user == "paper":
        print("Computer won!!!")
    elif computer == "rock" and user == "scissor":
        print("Computer won!!!")
    elif computer == "scissor" and user == "rock":
        print("User won!!!")
    elif computer == "paper" and user == "rock":
        print("Computer won!!!")
    elif computer == "paper" and user == "scissor":
        print("User won!!!")

while True:
    game()
    more = input('Want to play again?(y/n): ')
    if more == "n":
        print("Thanks for playing!")
        break











    