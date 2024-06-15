import random
CHOICES = ['rock', 'paper', 'scissors']
user_score = 0
computer_score = 0


def computer_choice():
    return random.choice(CHOICES)


def determine_winner(user_choice, computer_choice):
    global user_score, computer_score
    if user_choice == computer_choice:
        return 'tie'
    elif user_choice == 'rock' and computer_choice == 'scissors':
        user_score += 1
        return 'user'
    elif user_choice == 'paper' and computer_choice == 'rock':
        user_score += 1
        return 'user'
    elif user_choice == 'scissors' and computer_choice == 'paper':
        user_score += 1
        return 'user'
    else:
        computer_score += 1
        return 'computer'
