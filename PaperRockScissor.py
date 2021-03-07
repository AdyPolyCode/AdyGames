from random import randint
from sys import exit

choices = ['Paper', 'Rock', 'Scissor']


def player():
    global choices
    choice = ''
    print()
    print('Choose one: ', ', '.join([x for x in choices]))
    while choice not in choices:
        choice = input('Enter your choice: ').capitalize()
    return choice


def computer():
    global choices
    random_index = randint(0, 2)
    return choices[random_index]


def display_game(p, c):

    computer_score = 0
    player_score = 0

    play = True
    while play:
        try:
            computer_choice = c()
            player_choice = p()

            print()
            print(f'Computer: {computer_choice}')
            print(f'Player: {player_choice}')
            print()
            # print(f'Current score: Player = {player_score}, Computer = {computer_score}')
            if computer_choice == player_choice:
                print('It\'s a tie!')
            if player_choice == 'Rock' and computer_choice == 'Paper':
                computer_score += 1
                print('Computer won this round.')
            if player_choice == 'Scissor' and computer_choice == 'Paper':
                player_score += 1
                print('Player won this round.')
            if player_choice == 'Rock' and computer_choice == 'Scissor':
                player_score += 1
                print('Player won this round.')
            if player_choice == 'Paper' and computer_choice == 'Scissor':
                computer_score += 1
                print('Computer won this round.')
            if player_choice == 'Paper' and computer_choice == 'Rock':
                player_score += 1
                print('Player won this round.')
            if player_choice == 'Scissor' and computer_choice == 'Rock':
                computer_score += 1
                print('Computer won this round.')
            print(f'Current score: Player = {player_score}, Computer = {computer_score}')
        except KeyboardInterrupt:
            exit('GoodBye...')


if __name__ == '__main__':
    display_game(player, computer)
