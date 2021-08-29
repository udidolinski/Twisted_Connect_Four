import random


class Game:
    """
    This class is the game "Twisted Connect Four"
    """

    PLAYER_1 = 1
    PLAYER_2 = 2
    ROWS = 6
    TIE = 0
    DISCS_LST = [1, 2, 3, 4]
    winners = {"Tie": 0}

    def __init__(self, cols=7, gamma=0):
        self.columns = cols
        self.gamma = gamma
        self.board = [[None for _ in range(cols)] for _ in range(self.ROWS)]
        self.players = {1: 0, 2: 0}
        self.lastTurn = 0

    def __str__(self):
        board = ''
        for i in range(self.ROWS):
            for j in range(self.columns):
                if self.board[i][j] is None:
                    board += "* "
                else:
                    board += str(self.board[i][j]) + " "
            board += "\n"
        return board

    def set_players(self, ai1, ai2):
        """
        This function set the 2 AI players
        :param ai1:
        :param ai2:
        :return:
        """
        self.pl = [ai1, ai2]

    def make_move(self, column):
        """
        This function makes a move in the column.
        :param column:
        :return:
        """
        if not self.check_column(column) or self.get_current_player() == self.lastTurn:
            raise Exception("Illegal move.")
        turn = self.get_current_player()
        row_place = self.check_column(column)[1]
        self.board[row_place][column] = turn
        self.lastTurn = turn

    def random_move(self):
        """
        This function make a random move if a random number is less than the gamma factor.
        :return:
        """
        rand_number = random.random()
        if rand_number <= self.gamma:
            disc = random.choice(Game.DISCS_LST)
            col = self.find_random_free_col()

            row = self.check_column(col)[1]
            self.make_random_move(row, col, disc)
            self.players[self.get_current_player()] += 1
            return True
        self.players[self.get_current_player()] += 1
        return False

    def make_random_move(self, row, col, player):
        """
        This function places the player's disc at a specific location.
        :param row:
        :param col:
        :param player:
        :return:
        """
        self.board[row][col] = player

    def find_random_free_col(self):
        """
        This function check whether there is a legal move to make, if so it returns a random free column.
        :return:
        """
        avail_columns = []
        for column in range(self.columns):
            if self.get_player_at(0, column) is None:
                avail_columns.append(column)
        if not avail_columns:
            return "No possible AI moves."
        else:
            return random.choice(avail_columns)

    def find_four_winner(self, row, column, kind):
        """
        This function finds the 4 winning discs.
        :param row:
        :param column:
        :param kind:
        :return:
        """
        four_lst = []
        if kind == "row":
            for i in range(4):
                four_lst.append((row, column - i))
        elif kind == "col":
            for i in range(4):
                four_lst.append((row - i, column))
        elif kind == "down_slant":
            for i in range(4):
                four_lst.append((row - i, column - i))
        else:
            for i in range(4):
                four_lst.append((row + i, column - i))
        for point in four_lst:
            if self.board[point[0]][point[1]] != 4:
                return four_lst

    def check_new_column(self, point):
        """
        This function checks whether there is a win in any column.
        :param point:
        :return:
        """
        win_lst = []
        if point[0] > 2:
            return
        cur = self.board[point[0]][point[1]]
        if cur != 4:
            for i in range(4):
                if self.board[point[0] + i][point[1]] not in {cur, 4}:
                    return
                win_lst.append((point[0] + i, point[1]))
            return win_lst
        else:
            win_lst.append((point[0], point[1]))
            for i in range(1, 4):
                cur_disc = self.board[point[0] + i][point[1]]
                if cur_disc == 3 or (cur != 4 and cur_disc not in {cur, 4}):
                    return
                if cur == 4 and cur_disc != cur:
                    cur = cur_disc
                win_lst.append((point[0] + i, point[1]))
            if cur != 4:
                return win_lst

    def check_new_row(self, point):
        """
        This function checks whether there is a win in any row.
        :param point:
        :return:
        """
        row = point[0]
        possible_win_lst = []
        for i in range(max(point[1] - 3, 0), min(point[1] + 4, self.columns)):
            possible_win_lst.append((row, i))
        return self.go_over_possible_win_lst(possible_win_lst, "row")

    def go_over_possible_win_lst(self, possible_lst, win_type):
        """
        This function is a helper for finding a winning 4 discs.
        :param possible_lst:
        :param win_type:
        :return:
        """
        cur = None
        win_counter = 0
        neutral_counter = 0
        for point in possible_lst:
            if self.board[point[0]][point[1]] not in {None, 3}:
                if self.board[point[0]][point[1]] in {cur, 4}:
                    if self.board[point[0]][point[1]] == 4:
                        neutral_counter += 1
                    else:
                        neutral_counter = 0
                    win_counter += 1
                    if win_counter == 4:
                        four_winner = self.find_four_winner(point[0], point[1], win_type)
                        if four_winner is not None:
                            return four_winner
                        win_counter -= 1
                else:
                    win_counter = 1 + neutral_counter
                    if win_counter == 4:
                        return self.find_four_winner(point[0], point[1], win_type)
                    neutral_counter = 0
                    cur = self.board[point[0]][point[1]]
            else:
                win_counter = 0
                neutral_counter = 0
                cur = None

    def check_win_slant(self, point):
        """
        This function checks whether there is a win in any slant.
        :param point:
        :return:
        """
        win_down_slant = self.check_new_win_down_slant(point)
        if win_down_slant is not None:
            return win_down_slant
        return self.check_new_win_up_slant(point)

    def check_new_win_down_slant(self, point):
        """
        This function is a helper for finding a winning 4 discs in a slant (from left to right, up to down).
        :param point:
        :return:
        """
        possible_win_lst = []
        x = min(3, point[0], point[1])
        first_point = (point[0] - x, point[1] - x)
        y = min(3, 5 - point[0], self.columns - 1 - point[1])
        for i in range(x + y + 1):
            possible_win_lst.append((first_point[0] + i, first_point[1] + i))
        return self.go_over_possible_win_lst(possible_win_lst, "down_slant")

    def check_new_win_up_slant(self, point):
        """
        This function is a helper for finding a winning 4 discs in a slant (from left to right, down to up).
        :param point:
        :return:
        """
        possible_win_lst = []
        x = min(3, 5 - point[0], point[1])
        first_point = (point[0] + x, point[1] - x)
        y = min(3, point[0], self.columns - 1 - point[1])
        for i in range(x + y + 1):
            possible_win_lst.append((first_point[0] - i, first_point[1] + i))
        return self.go_over_possible_win_lst(possible_win_lst, "up_slant")

    def get_winner(self, row, column):
        """
        This function returns the winner of the game if someone won, if not it returns a tie (if the game ended).
        :param row:
        :param column:
        :return:
        """
        if self.board[row][column] != 3:
            win_row = self.check_new_row((row, column))
            if win_row is not None:
                return win_row
            win_col = self.check_new_column((row, column))
            if win_col is not None:
                return win_col
            win_slant = self.check_win_slant((row, column))
            if win_slant is not None:
                return win_slant
        for number in self.board[0]:
            if number is None:
                return None
        return [self.TIE]

    def get_player_at(self, row, col):
        """
        This function returns the player at the specific location.
        :param row:
        :param col:
        :return:
        """
        if (row >= self.ROWS or row < 0) or (col < 0 or col >= self.columns):
            raise Exception("Illegal location.")
        return self.board[row][col]

    def get_current_player(self):
        """
        This function returns the current player (the one which it his turn at the moment).
        :return:
        """
        if self.players[1] == self.players[2]:
            return self.PLAYER_1
        else:
            return self.PLAYER_2

    def check_column(self, column):
        """
        This function checks whether is a free place in the column to put a disc, if so it returns the specific row
        that is free, if not it returns False
        :param column:
        :return:
        """
        if column > self.columns - 1:
            return False
        if self.board[0][column] is not None:
            return False
        for row in range(self.ROWS):
            if self.board[row][column] is not None:
                return True, row - 1
        return True, self.ROWS - 1
