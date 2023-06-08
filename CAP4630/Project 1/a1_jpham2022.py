# Team Me7mbers: Nicolas Uribe, Jamie Pam
# Date: 6/7/2023
# Assignment: Project 1


import math
import random
import time

class Player():
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8): ')
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again.')
        return val


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square


class SmartComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())      # If all squares are empty, choose a square
        else:
            square = self.minimax(game, self.letter)['position']    # Use the minimax algorithm to determine the best move to make
        return square

    def minimax(self, state, player):
        max_player = self.letter  # yourself
        other_player = 'X' if player == 'O' else 'O'

        # first we want to check if the previous move is a winner
        if state.current_winner == other_player:
            return {'position': None, 'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (
                        state.num_empty_squares() + 1)}
        elif not state.empty_squares():
            return {'position': None, 'score': 0}

        if player == max_player:
            best = {'position': None, 'score': -math.inf}  # each score should maximize
        else:
            best = {'position': None, 'score': math.inf}  # each score should minimize
        for possible_move in state.available_moves():
            state.make_move(possible_move, player)
            sim_score = self.minimax(state, other_player)  # simulate a game after making that move

            # undo move
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move  # this represents the move optimal next move

            if player == max_player:  # O is max player
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
        return best
    
#########################################################################################################################################################
#########################################################################################################################################################
#########################################################################################################################################################

class TicTacToe(HumanPlayer, RandomComputerPlayer, SmartComputerPlayer):
    def __init__(self):
        self.board = self.make_board()
        self.current_winner = None

    @staticmethod
    def make_board():
        return [' ' for _ in range(9)]

    def print_board(self):
        for row in [self.board[i*3:(i+1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2  Display the numbers corresponding to each square on the board
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # check the row
        row_ind = math.floor(square / 3)
        row = self.board[row_ind*3:(row_ind+1)*3]
        # print('row', row)
        if all([s == letter for s in row]):
            return True
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        # print('col', column)
        if all([s == letter for s in column]):
            return True
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            # print('diag1', diagonal1)
            if all([s == letter for s in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            # print('diag2', diagonal2)
            if all([s == letter for s in diagonal2]):
                return True
        return False

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def available_moves(self):
        return [i for i, x in enumerate(self.board) if x == " "]


def reset_game(game):
    game.board = game.make_board()          # clears the board
    game.current_winner = None              # resets the winner

def play(game, o_player, x_player, print_game=True):
    while True:
        if print_game:          # Introduction before the start of the game
            print('Welcome!\nIn this program, you will be playing against the algorithm in a game of TicTacToe.\nYou are Player X.\nHave Fun!')
            game.print_board_nums()         # display board numbers

        letter = 'O'
        while game.empty_squares():
            if letter == 'X':
                square = x_player.get_move(game)
            else:
                square = o_player.get_move(game)
            if game.make_move(square, letter):

                if print_game:
                    print(letter + ' makes a move to square {}'.format(square))
                    game.print_board()
                    print('')

                if game.current_winner:
                    if print_game:
                        print(letter + ' wins!')
                    break  # Break out of the inner while loop

                letter = 'X' if letter == 'O' else 'O'  # switches player

            time.sleep(.8)

        if not game.empty_squares():
            if print_game:
                print('It\'s a tie!')

        reply = None  
        while reply not in ['y', 'n']:
            reply = input('Would you like to replay? (y/n): ').lower()
            if reply == 'n':
                print('Thank you for playing!')
                return 
            elif reply == 'y':
                reset_game(game)
                continue  
            else:
                print('Error: reply with y or n')       # if user enters character other than y or n then it breaks out into the while loop
                                                        # which then prompts the question again until a valid answer is given


if __name__ == '__main__':
    o_player = SmartComputerPlayer('O')
    x_player = HumanPlayer('X')
    t = TicTacToe()
    play(t, o_player, x_player, print_game=True)