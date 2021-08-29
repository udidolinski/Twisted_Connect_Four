import numpy as np
from numba import njit

"""
These functions are parts of the heuristic for the Expectimax player.
"""


@njit
def get_possible_moves(board):
    count = 0
    for column in range(len(board[0])):
        if board[0][column] == 0:
            count += 1
    avail_columns = np.zeros(count)
    for column in range(len(board[0])):
        if board[0][column] == 0:
            avail_columns[count - 1] = column
            count -= 1
    return avail_columns


@njit
def check_rows_new(board, player):
    score_counter = 0
    my_counter = 0
    for i in range(0, len(board) - 3):
        for j in range(0, len(board[0]) - 3):
            for k in range(0, 4):
                for m in range(0, 4):
                    if board[i + k][m + j] == player or board[i + k][m + j] == 4:
                        my_counter += 1
                        continue
                    if board[i + k][m + j] == (player % 2 + 1) or board[i + k][m + j] == 3:
                        my_counter = 0
                        break
                if my_counter == 4:
                    return np.inf
                else:
                    score_counter += my_counter ** 2
                my_counter = 0
    return score_counter


@njit
def check_cols_new(board, player):
    score_counter = 0
    my_counter = 0
    for i in range(0, len(board[0]) - 3):
        for j in range(0, len(board) - 3):
            for k in range(0, 4):
                for m in range(0, 4):
                    if board[m + j][k + i] == player or board[m + j][k + i] == 4:
                        my_counter += 1
                        continue
                    if board[m + j][k + i] == player % 2 + 1 or board[m + j][k + i] == 3:
                        my_counter = 0
                        break
                if my_counter == 4:
                    return np.inf
                else:
                    score_counter += my_counter ** 2
                my_counter = 0
    return score_counter


@njit
def check_diag_new(board, player):
    score_counter = 0
    for i in range(0, len(board) - 3):
        for j in range(0, len(board[0]) - 3):
            my_counter = 0
            for m in range(0, 4):
                if board[i + m][m + j] == player or board[i + m][m + j] == 4:
                    my_counter += 1
                    continue
                if board[i + m][m + j] == player % 2 + 1 or board[i + m][m + j] == 3:
                    my_counter = 0
                    break
            if my_counter == 4:
                return np.inf
            else:
                score_counter += my_counter ** 2
            my_counter = 0
            for m in range(0, 4):
                if board[i + 3 - m][m + j] == player or board[i + 3 - m][m + j] == 4:
                    my_counter += 1
                    continue
                if board[i + 3 - m][m + j] == player % 2 + 1 or board[i + 3 - m][m + j] == 3:
                    my_counter = 0
                    break
            if my_counter == 4:
                return np.inf
            else:
                score_counter += my_counter ** 2
    return score_counter


@njit
def check_score(player, board):
    score = 0
    temp_score = check_rows_new(board, player=player)
    if temp_score == np.inf:
        return temp_score
    score += temp_score
    temp_score = check_cols_new(board, player=player)
    if temp_score == np.inf:
        return temp_score
    score += temp_score
    temp_score = check_diag_new(board, player=player)
    if temp_score == np.inf:
        return temp_score
    score += temp_score
    temp_score = check_diag_new(board, player=player % 2 + 1)
    if temp_score == np.inf:
        return -temp_score
    score -= temp_score
    temp_score = check_cols_new(board, player=player % 2 + 1)
    if temp_score == np.inf:
        return -temp_score
    score -= temp_score
    temp_score = check_rows_new(board, player=player % 2 + 1)
    if temp_score == np.inf:
        return -temp_score
    score -= temp_score
    return score


@njit
def exp_check_score(player, board, inf_val):
    score = 0
    temp_score = check_rows_new(board, player=player)
    if temp_score == np.inf:
        return inf_val
    score += temp_score
    temp_score = check_cols_new(board, player=player)
    if temp_score == np.inf:
        return inf_val
    score += temp_score
    temp_score = check_diag_new(board, player=player)
    if temp_score == np.inf:
        return inf_val
    score += temp_score
    temp_score = check_diag_new(board, player=player % 2 + 1)
    if temp_score == np.inf:
        return -inf_val
    score -= temp_score
    temp_score = check_cols_new(board, player=player % 2 + 1)
    if temp_score == np.inf:
        return -inf_val
    score -= temp_score
    temp_score = check_rows_new(board, player=player % 2 + 1)
    if temp_score == np.inf:
        return -inf_val
    score -= temp_score
    return score


@njit
def is_state_over(state, player):
    score = check_score(player, state)
    if score == np.inf or score == -np.inf:
        return True
    for i in range(len(state)):
        for j in range(len(state[0])):
            if state[i][j] == 0:
                return False
    return True


@njit
def expectimax_alpha_beta_cpp(player, state, depth, gamma=0.0, alpha=-np.inf, beta=np.inf, turn=0, inf_val=90):
    if depth == 0 or is_state_over(state, player):
        score = exp_check_score(player, state, inf_val)
        if score == np.inf:
            print("trash")
        return score
    if turn == 0:
        max_eval = -np.inf
        for move in get_possible_moves(state):
            for row in range(len(state), 0, -1):
                if int(state[int(row - 1), int(move)]) == 0:
                    state[int(row - 1), int(move)] = player
                    max_eval = max(max_eval,
                                   expectimax_alpha_beta_cpp(player, state, depth - 1, gamma=gamma, alpha=alpha,
                                                             beta=beta, turn=2, inf_val=inf_val))
                    state[int(row - 1), int(move)] = 0
                    break
                alpha = max(max_eval, alpha)
                if beta <= alpha:
                    break
        return max_eval
    if turn == 1:
        min_eval = np.inf
        for move in get_possible_moves(state):
            move = int(move)
            for row in range(len(state), 0, -1):
                if int(state[int(row - 1), int(move)]) == 0:
                    state[int(row - 1), int(move)] = player % 2 + 1
                    min_eval = min(min_eval,
                                   expectimax_alpha_beta_cpp(player, state, depth - 1, gamma=gamma, alpha=alpha,
                                                             beta=beta, turn=3, inf_val=inf_val))
                    state[int(row - 1), int(move)] = 0
                    break
            beta = min(beta, min_eval)
            if beta <= alpha:
                break
        return min_eval
    if turn == 2:  # after the player
        if gamma == 0.0:
            return expectimax_alpha_beta_cpp(player, state, depth, gamma=gamma, alpha=alpha, beta=beta, turn=1,
                                             inf_val=inf_val)
        moves = get_possible_moves(state)
        score = 0
        score += expectimax_alpha_beta_cpp(player, state, depth, gamma=gamma, alpha=alpha, beta=beta, turn=1,
                                           inf_val=inf_val)
        colour_options = np.arange(1, 5, 1)
        for colour in colour_options:
            colour = int(colour)
            for move in moves:
                move = int(move)
                for row in range(len(state), 0, -1):
                    if int(state[int(row - 1), int(move)]) == 0:
                        state[int(row - 1), int(move)] = colour
                        res = expectimax_alpha_beta_cpp(player, state, depth, gamma=gamma, alpha=alpha, beta=beta,
                                                        turn=1, inf_val=inf_val)
                        score += gamma * 1 / (len(moves) * len(colour_options)) * res
                        state[int(row - 1), int(move)] = 0
                        break
        return score
    if turn == 3:  # after the oponent
        if gamma == 0.0:
            return expectimax_alpha_beta_cpp(player, state, depth, gamma=gamma, alpha=alpha, beta=beta, turn=0,
                                             inf_val=inf_val)
        moves = get_possible_moves(state)
        score = 0.0
        score += expectimax_alpha_beta_cpp(player, state, depth, gamma=gamma, alpha=alpha, beta=beta, turn=0,
                                           inf_val=inf_val)
        colour_options = np.arange(1, 5, 1)

        for colour in colour_options:
            for move in moves:
                move = int(move)
                for row in range(len(state), 0, -1):
                    if int(state[int(row - 1), int(move)]) == 0:
                        state[int(row - 1), int(move)] = colour
                        res = expectimax_alpha_beta_cpp(player, state, depth, gamma=gamma, alpha=alpha, beta=beta,
                                                        turn=0, inf_val=inf_val)
                        score += gamma * 1 / (len(moves) * len(colour_options)) * res
                        state[int(row - 1), int(move)] = 0
                        break
        return score


@njit
def minimax_alpha_beta_cpp(player, state, depth, alpha=-np.inf, beta=np.inf, turn=0, score_huristic=check_score):
    if depth == 0 or is_state_over(state, player):
        score = score_huristic(player, state)
        return score
    if turn == 0:
        max_eval = -np.inf
        for move in get_possible_moves(state):
            for row in range(len(state), 0, -1):
                if int(state[int(row - 1), int(move)]) == 0:
                    state[int(row - 1), int(move)] = player
                    max_eval = max(max_eval,
                                   minimax_alpha_beta_cpp(player, state, depth - 1, alpha=alpha, beta=beta, turn=1,
                                                          score_huristic=score_huristic))
                    state[int(row - 1), int(move)] = 0
                    break
                alpha = max(max_eval, alpha)
                if beta <= alpha:
                    break
        return max_eval
    if turn != 0:
        min_eval = np.inf
        for move in get_possible_moves(state):
            move = int(move)
            for row in range(len(state), 0, -1):
                if int(state[int(row - 1), int(move)]) == 0:
                    state[int(row - 1), int(move)] = player % 2 + 1
                    min_eval = min(min_eval,
                                   minimax_alpha_beta_cpp(player, state, depth - 1, alpha=alpha, beta=beta, turn=0,
                                                          score_huristic=score_huristic))
                    state[int(row - 1), int(move)] = 0
                    break
            beta = min(beta, min_eval)
            if beta <= alpha:
                break
        return min_eval


class EAI:
    """
    This class is the Expectimax player.
    """

    INF_VAL = 900

    def __init__(self, game, player, depth=2, gamma=0):
        self.game = game
        self.player = player
        self.depth = depth
        self.gamma = gamma
        self.name = "EXM" + str(self.player) + " - " + str(self.depth)

    def __str__(self):
        return str(self.player)

    def get_name(self):
        """
        This function returns the player's name (shortcut for it).
        :return:
        """
        self.name = "EXM" + str(self.player) + " - " + str(self.depth)
        return self.name

    def get_winner_name(self):
        """
        This function returns the full name of this player (when the player wins).
        :return:
        """
        return "Expectimax" + str(self.player)

    def get_possible_moves(self, board):
        """
        This function returns all possible moves (all columns that are free).
        :return:
        """
        avail_columns = []
        for column in range(self.game.columns):
            if board[0][column] == 0:
                avail_columns.append(column)
        return avail_columns

    def find_best_move(self, gamma=0):
        """
        Find the best move using the gamma factor and a heuristic.
        :return:
        """
        value = EAI.INF_VAL
        new_board = np.zeros(shape=(len(self.game.board), len(self.game.board[0])))
        for a in range(len(new_board)):
            for b in range(len(new_board[0])):
                if self.game.board[a][b] is None:
                    new_board[a, b] = 0
                else:
                    new_board[a, b] = self.game.board[a][b]
        # depth = depth * 2 + 1
        moves = []
        for move in self.get_possible_moves(new_board):
            new_state = new_board
            for row in range(len(new_state), 0, -1):
                if new_state[row - 1][move] == 0:
                    new_state[row - 1][move] = self.player
                    moves.append([expectimax_alpha_beta_cpp(self.player, new_state, self.depth - 1, gamma=gamma, turn=2,
                                                            inf_val=value), move])
                    new_state[row - 1][move] = 0
                    break
        best_move = (-np.inf, 0)
        for i in range(len(moves)):
            if moves[i][0] >= best_move[0]:
                best_move = moves[i]
        return best_move[1]

    def find_legal_move(self):
        """
        This function check whether there is a legal move, if so it returns the best move possible.
        :return:
        """
        avail_columns = []
        for column in range(self.game.columns):
            if self.game.get_player_at(0, column) is None:
                avail_columns.append(column)
        if not avail_columns:
            raise Exception("No possibale AI moves.")
        else:
            return self.find_best_move(self.gamma)
