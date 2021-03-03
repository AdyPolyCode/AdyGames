from random import randint


class Game:

    # Init method with a single parameter
    # If false the game does not run else run
    def __init__(self, game_on=False):
        self.game_on = game_on

    # Main play method
    def play(self):
        # Waiting for player to play or not
        if self.ready_check():
            self.game_on = True
        # Main game loop
        while self.game_on:
            # Welcomes the players
            print('Lets play tic tac toe!')
            # Player and board initializing
            b = Board()
            p = Player()
            b.display_board()
            # Unpack the MARK_CHOICE function to p1 and p1
            # Basically choosing the marker for both players
            p1, p2 = p.mark_choice()
            # Make turn for player
            turn = p.turn()
            print(f'Player1 = {p1}, Player2 = {p2}')
            # Inside loop where the game begins
            while True:
                # Checks for player turn and also WIN_CHECK and BOARD_CHECK and TIE_CHECK
                if turn == 0:
                    print(f'Player1 turn.')
                    if b.tie_check(b.board):
                        print('It is a tie!')
                        break
                    player1_pos = p.mark_position()
                    if not b.board_check(player1_pos):
                        player1_pos = p.mark_position()
                    b.place_mark(p1, player1_pos)
                    b.display_board()
                    if b.win_check(b.board, p1):
                        print(f'Player1 has won the game.')
                        break
                    turn = 1
                else:
                    print(f'Player2 turn.')
                    if b.tie_check(b.board):
                        print('It is a tie!')
                        break
                    player2_pos = p.mark_position()
                    if not b.board_check(player2_pos):
                        player2_pos = p.mark_position()
                    b.place_mark(p2, player2_pos)
                    b.display_board()
                    if b.win_check(b.board, p2):
                        print(f'Player2 has won the game.')
                        break
                    turn = 0
            if self.play_again():
                self.game_on = True
            else:
                self.game_on = False

    # Player ready check method
    def ready_check(self):
        ready = False
        while not ready:
            r = input('Ready? (y/n)?: ').upper()
            if r == 'Y':
                ready = True
        return ready

    def play_again(self):
        play = False
        again = input('Do you want to play again?: ').upper()
        while again not in ['Y', 'N']:
            again = input('Do you want to play again?: ').upper()
        if again == 'Y':
            play = True
        elif again == 'N':
            play = False
        return play


class Board:

    # Init method that basically creates the board
    def __init__(self):
        self.board = [' '] * 10

    # Method for displaying the board
    def display_board(self):
        print(self.board[7] + '|' + self.board[8] + '|' + self.board[9])
        print(' | | ')
        print(self.board[4] + '|' + self.board[5] + '|' + self.board[6])
        print(' | | ')
        print(self.board[1] + '|' + self.board[2] + '|' + self.board[3])

    # Method to check if whether the player has won or not
    def win_check(self, board, mark):
        return ((board[1] == mark and board[4] == mark and board[7] == mark) or
                (board[2] == mark and board[5] == mark and board[8] == mark) or
                (board[3] == mark and board[6] == mark and board[9] == mark) or
                (board[1] == mark and board[2] == mark and board[3] == mark) or
                (board[4] == mark and board[5] == mark and board[6] == mark) or
                (board[7] == mark and board[8] == mark and board[9] == mark) or
                (board[1] == mark and board[5] == mark and board[9] == mark) or
                (board[3] == mark and board[5] == mark and board[7] == mark))

    # Method to check if its a tie or not
    def tie_check(self, board):
        if ' ' not in self.board:
            return True
        return False

    # Method to check if a marker was already placed or not
    def board_check(self, position):
        empty = True
        for i in range(1, len(self.board)):
            if self.board[position] != ' ':
                empty = False
        return empty

    # Method to place the marker to the given position
    def place_mark(self, mark, position):
        self.board[position] = mark


class Player:

    # Method to choose a marker for both players
    def mark_choice(self):
        string = ''
        while not string:
            choice = input('Enter X or O: ').upper()
            if choice == 'O':
                string = choice
            elif choice == 'X':
                string = choice
        player1 = string
        if player1 == 'X':
            player2 = 'O'
        else:
            player2 = 'X'
        return player1, player2

    # Method to give a random turn whether player 1 or player 2
    def turn(self):
        player_turn = randint(0, 1)
        if player_turn == 0:
            return player_turn
        else:
            return player_turn

    # Method to give a position to a parker
    def mark_position(self):
        choice = int(input('Enter position (1-9): '))
        if choice in range(1, 10):
            return choice
        else:
            while choice not in range(1, 10):
                choice = int(input('Enter 1-9!: '))
            return choice


if __name__ == '__main__':
    GAME = Game()
    GAME.play()
