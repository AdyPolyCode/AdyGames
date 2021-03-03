import  random, sys

print('Paper, Rock, Scissors! ')

wins = 0
loses = 0
ties = 0
# outer game loop
while True:
    print(f'Wins: {wins}, Loses: {loses}, Ties: {ties} ...')
    # inner game loop
    while True:
        # player guess
        playerGuess = input('Enter your move: (s)cissors, (r)ock, (p)aper, (q)uit.): ').lower()

        if playerGuess:
            if playerGuess == 'q':
                sys.exit()
            elif playerGuess == 's'or playerGuess == 'p' or playerGuess == 'r':
                pass
            else:
                print('Enter a valid letter! ')
        else:
            print('Enter something! ')

        # display player move
        if playerGuess == 'r':
            print('PLAYER: Rock...')
        elif playerGuess == 's':
            print('PLAYER: Scissor...')
        elif playerGuess == 'p':
            print('PLAYER: Paper...')



        # computer guess
        computerGuess = random.randint(1, 3)

        if computerGuess == 1:
            computerGuess = 'r'
            print('COMPUTER: Rock...')
        elif computerGuess == 2:
            computerGuess = 's'
            print('COMPUTER: Scissor...')
        elif computerGuess == 3:
            computerGuess = 'p'
            print('COMPUTER: Paper...')
        else:
            pass


        if playerGuess == computerGuess:
            ties += 1
            print('It\'s a tie!')
        elif playerGuess == 's' and computerGuess == 'p':
            wins += 1
            print('It\'s a win!')
        elif playerGuess == 'p' and computerGuess == 'r':
            wins += 1
            print('It\'s a win!')
        elif playerGuess == 'r' and computerGuess == 's':
            wins += 1
            print('It\'s a win!')
        elif playerGuess == 's' and computerGuess == 'r':
            loses += 1
            print('It\'s a lose!')
        elif playerGuess == 'p' and computerGuess == 's':
            loses += 1
            print('It\'s a lose!')
        elif playerGuess == 'r' and computerGuess == 'p':
            loses += 1
            print('It\'s a lose!')
        else:
            pass
        break