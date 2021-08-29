import tkinter as tk
from tkinter import messagebox
from random import random
from random import choice
from game_files.game import Game
from game_files.minmax_alpha_beta import *
from game_files.expectimax import *


class FirstMessage:
    """
    This is the main window of the game
    """

    def __init__(self, cols=7, gamma=0, ab_depth=4, exp_depth=2):
        self.cols = cols
        self.gamma = gamma
        self.ab_depth = ab_depth
        self.exp_depth = exp_depth
        self.y = tk.Tk()
        self.y.geometry('400x400')
        self.y.title('Start Menu')
        self.label_text = tk.Label(self.y, text='choose one of the options below:', font=('Helvetica', 20))
        self.label_text.pack(side=tk.TOP)
        self.button1 = tk.Button(self.y, text='Human vs Human', height=4, width=50, command=self.H_vs_H)
        self.button1.pack()
        self.button2 = tk.Button(self.y, text='Human vs AI', height=4, width=50, command=self.H_vs_AI)
        self.button2.pack()
        self.button3 = tk.Button(self.y, text='AI vs Human', height=4, width=50, command=self.AI_vs_H)
        self.button3.pack()
        self.button4 = tk.Button(self.y, text='AI vs AI', height=4, width=50, command=self.AI_vs_AI)
        self.button4.pack()
        self.y.mainloop()

    def H_vs_H(self):
        """
        This function starts a game between 2 humans
        :return:
        """
        self.y.destroy()
        gui = Gui(cols=self.cols, gamma=self.gamma, exp_depth=self.exp_depth, ab_depth=self.ab_depth)

    def AI_vs_H(self):
        """
        This function opens a window for a game between an AI player and a human (where the AI player is first).
        :return:
        """
        self.y.destroy()
        self.y = tk.Tk()
        self.y.geometry('400x400')
        self.y.title('AI Menu')
        self.label_text = tk.Label(self.y, text='choose one of the options below:', font=('Helvetica', 20))
        self.label_text.pack(side=tk.TOP)
        self.button1 = tk.Button(self.y, text='Expectimax vs Human', height=4, width=50, command=self.Exp_vs_H)
        self.button1.pack()
        self.button2 = tk.Button(self.y, text='AlphaBeta vs Human', height=4, width=50, command=self.Ab_vs_H)
        self.button2.pack()
        self.y.mainloop()

    def Exp_vs_H(self):
        """
        This function starts a game between an Expectimax player and a human (where the Expectimax player is first).
        :return:
        """
        self.y.destroy()
        gui = Gui(player1="Exp", gamma=self.gamma, cols=self.cols, exp_depth=self.exp_depth, ab_depth=self.ab_depth)

    def Ab_vs_H(self):
        """
        This function starts a game between an AlphaBeta player and a human (where the AlphaBeta player is first).
        :return:
        """
        self.y.destroy()
        gui = Gui(player1="Ab", gamma=self.gamma, cols=self.cols, exp_depth=self.exp_depth, ab_depth=self.ab_depth)

    def H_vs_AI(self):
        """
        This function opens a window for a game between an AI player and a human (where the human player is first).
        :return:
        """
        self.y.destroy()
        self.y = tk.Tk()
        self.y.geometry('400x400')
        self.y.title('AI Menu')
        self.label_text = tk.Label(self.y, text='choose one of the options below:', font=('Helvetica', 20))
        self.label_text.pack(side=tk.TOP)
        self.button1 = tk.Button(self.y, text='Human vs Expectimax', height=4, width=50, command=self.H_vs_Exp)
        self.button1.pack()
        self.button2 = tk.Button(self.y, text='Human vs AlphaBeta', height=4, width=50, command=self.H_vs_Ab)
        self.button2.pack()
        self.y.mainloop()

    def H_vs_Exp(self):
        """
        This function starts a game between an Expectimax player and a human (where the human player is first).
        :return:
        """
        self.y.destroy()
        gui = Gui(player2="Exp", gamma=self.gamma, cols=self.cols, exp_depth=self.exp_depth, ab_depth=self.ab_depth)

    def H_vs_Ab(self):
        """
        This function starts a game between an AlphaBeta player and a human (where the human player is first).
        :return:
        """
        self.y.destroy()
        gui = Gui(player2="Ab", gamma=self.gamma, cols=self.cols, exp_depth=self.exp_depth, ab_depth=self.ab_depth)

    def AI_vs_AI(self):
        """
        This function opens a window for a game between 2 AI players.
        :return:
        """
        self.y.destroy()
        self.y = tk.Tk()
        self.y.geometry('400x400')
        self.y.title('AI Menu')
        self.label_text = tk.Label(self.y, text='choose one of the options below:', font=('Helvetica', 20))
        self.label_text.pack(side=tk.TOP)
        self.button1 = tk.Button(self.y, text='Expectimax vs Expectimax', height=4, width=50, command=self.Exp_vs_Exp)
        self.button1.pack()
        self.button2 = tk.Button(self.y, text='Expectimax vs AlphaBeta', height=4, width=50, command=self.Exp_vs_Ab)
        self.button2.pack()
        self.button3 = tk.Button(self.y, text='AlphaBeta vs Expectimax', height=4, width=50, command=self.Ab_vs_Exp)
        self.button3.pack()
        self.button4 = tk.Button(self.y, text='AlphaBeta vs AlphaBeta', height=4, width=50, command=self.Ab_vs_Ab)
        self.button4.pack()
        self.y.mainloop()

    def Exp_vs_Exp(self):
        """
        This function starts a game between 2 Expectimax players.
        :return:
        """
        self.y.destroy()
        gui = Gui("Exp", "Exp", gamma=self.gamma, cols=self.cols, exp_depth=self.exp_depth, ab_depth=self.ab_depth)

    def Exp_vs_Ab(self):
        """
        This function starts a game between an AlphaBeta player and an Expectimax player (where the Expectimax
        player is first).
        :return:
        """
        self.y.destroy()
        gui = Gui("Exp", "Ab", gamma=self.gamma, cols=self.cols, exp_depth=self.exp_depth, ab_depth=self.ab_depth)

    def Ab_vs_Exp(self):
        """
        This function starts a game between an AlphaBeta player and an Expectimax player (where the AlphaBeta
        player is first).
        :return:
        """
        self.y.destroy()
        gui = Gui("Ab", "Exp", gamma=self.gamma, cols=self.cols, exp_depth=self.exp_depth, ab_depth=self.ab_depth)

    def Ab_vs_Ab(self):
        """
        This function starts a game between 2 AlphaBeta players.
        :return:
        """
        self.y.destroy()
        gui = Gui("Ab", "Ab", gamma=self.gamma, cols=self.cols, exp_depth=self.exp_depth, ab_depth=self.ab_depth)


class Gui:
    """
    This class is the GUI of the game
    """

    BG_COLOR = '#eab560'
    OBJ_COLOR = '#8fd0d6'
    STOP_COLOR = 'yellow'
    NEUTRAL_COLOR = 'green'

    def __init__(self, player1=None, player2=None, cols=7, gamma=0, ab_depth=4, exp_depth=2):
        self.colors = {1: 'black', 2: 'blue', 3: self.STOP_COLOR, 4: self.NEUTRAL_COLOR}
        self.index = 0
        self.player1 = player1
        self.player2 = player2
        self.ab_depth = ab_depth
        self.exp_depth = exp_depth
        self.game = Game(cols, gamma)
        self.check_ai_existance()
        self.root = tk.Tk()
        self.root.geometry("1200x600")
        self.root.title('Connect Four')
        self.root.configure(background=self.BG_COLOR)
        self.title = tk.Label(self.root, text="Connect Four", font=("Helvatica", 20), background=self.BG_COLOR)
        self.title.pack(side=tk.TOP)
        self.frame = tk.Frame(self.root, width=1000, height=1200, background=self.BG_COLOR)
        self.frame.pack()
        self.left_side_list = self.draw_left_side()
        self.canvass_list = self.all_canvas()
        self.ovals_list = self.create_circles()
        self.triangles_list = self.all_triangles()
        self.canvas_bind()
        self.images = []
        self.get_images()
        self.right_side_list = self.draw_right_side()
        self.player_color = 'black'
        self.winning_way = ''
        self.root.after(500, self.ai_move)
        self.root.mainloop()

    def check_ai_existance(self):
        """
        This functions checks if there are any AI players, if so it creates them.
        :return:
        """
        if self.player1 == "Exp":
            self.player1 = EAI(self.game, 1, self.exp_depth, self.game.gamma)
        elif self.player1 == "Ab":
            self.player1 = PAI(self.game, 1, self.ab_depth, self.game.gamma)

        if self.player2 == "Exp":
            self.player2 = EAI(self.game, 2, self.exp_depth, self.game.gamma)
        elif self.player2 == "Ab":
            self.player2 = PAI(self.game, 2, self.ab_depth, self.game.gamma)

    def all_triangles(self):
        """
        This function creates and returns all the triangles above the board's columns (when the user hovers the board).
        :return:
        """
        tri = []
        for i in range(self.game.columns):
            tri.append(self.canvass_list[i].create_polygon(22, 60, 42, 60, 31, 75, fill=''))
        return tri

    def draw_left_side(self):
        """
        This function draws and return the left side of the game (where player 1's discs are left to play).
        :return:
        """
        oval_side = []
        self.canvs_side = tk.Canvas(self.frame, width=150, height=1200, highlightthickness=0, background=self.BG_COLOR)
        self.canvs_side.pack(side=tk.LEFT)
        name = "HUMAN 1"
        if self.player1:
            name = self.player1.get_name()
        self.canvs_side.create_text(75, 100, text=name, font=("Helvatica", 20))

        for i in range(7):
            for j in range(3):
                location = (7 + j * 50, 147 + 50 * i, 43 + j * 50, 186 + 50 * i)
                oval_side.append(self.canvs_side.create_oval(*location, fill="black"))
        return oval_side

    def draw_right_side(self):
        """
        This function draws and return the right side of the game (where player 2's discs are left to play).
        :return:
        """
        oval_right = []
        self.canvas_right = tk.Canvas(self.frame, width=150, height=1200, highlightthickness=0,
                                      background=self.BG_COLOR)
        self.canvas_right.pack(side=tk.LEFT)
        name = "HUMAN 2"
        if self.player2:
            name = self.player2.get_name()
        self.canvas_right.create_text(75, 100, text=name, font=("Helvatica", 20), fill='blue')
        for i in range(7):
            for j in range(3):
                location = (7 + j * 50, 147 + 50 * i, 43 + j * 50, 186 + 50 * i)
                oval_right.append(self.canvas_right.create_oval(*location, fill="blue"))
        return oval_right

    def all_canvas(self):
        """
        This function draws the main canvas of the board.
        :return:
        """
        cans = []
        for i in range(self.game.columns):
            self.canvas = tk.Canvas(self.frame, width=68, height=1200, highlightthickness=0, background=self.BG_COLOR)
            self.canvas.pack(side=tk.LEFT)
            cans.append(self.canvas)
        return cans

    def get_images(self):
        """
        This function draws the images for creating the "Connect Four" board.
        """
        for num in range(1, 8):
            img = tk.PhotoImage(file=f"game_files/pics/board_part{num}.png")
            self.images.append(img)

        self.canvass_list[0].create_image(36, 300, image=self.images[0], anchor='center')
        self.canvass_list[1].create_image(68, 300, image=self.images[1], anchor="e")

        i = -1
        for i in range(self.game.columns - 7 - int((self.game.columns - 7) / 2)):
            self.canvass_list[i + 2].create_image(68, 300, image=self.images[1], anchor="e")
        i += 2
        for j in range(1, 5):
            self.canvass_list[i + j].create_image(68, 300, image=self.images[j + 1], anchor='e')
        for k in range(int((self.game.columns - 7) / 2)):
            self.canvass_list[i + 5 + k].create_image(68, 300, image=self.images[5], anchor="e")
        self.canvass_list[self.game.columns - 1].create_image(69, 300, image=self.images[6], anchor="e")

    def create_circles(self):
        """
        This function create the white circles for the board (for the initialized empty board).
        :return:
        """
        all_ovals_list = []
        for j in range(self.game.columns):
            oval_list = []
            for i in range(6):
                location = (2.5, 88 + 65 * i, 65, 157 + 65 * i)
                oval_list.append(self.canvass_list[j].create_oval(*location, fill="white"))
            all_ovals_list.append(oval_list)
        return all_ovals_list

    def draw_circles(self, event, column):
        """
        This function draw the circles of the board and the triangles above the board's column when the user hovers
        the board.
        :param event:
        :param column:
        :return:
        """
        self.canvass_list[column].itemconfig(self.triangles_list[column], fill=self.OBJ_COLOR)
        for i in self.ovals_list[column]:
            if self.canvass_list[column].itemcget(i, "fill") == "white":
                self.canvass_list[column].itemconfig(i, fill=self.OBJ_COLOR)

    def delete_circles(self, event, column):
        """
        This function deleted the circles of the board and the triangles above the board's column when the user
        moves the mouse away from the column of the board.
        :param event:
        :param column:
        :return:
        """
        self.canvass_list[column].itemconfig(self.triangles_list[column], fill='')
        for i in self.ovals_list[column]:
            if self.canvass_list[column].itemcget(i, "fill") == self.OBJ_COLOR:
                self.canvass_list[column].itemconfig(i, fill="white")

    def draw_circles_canvas(self, i):
        """
        This function is a wrapper for the draw_circles function (bind to the user's mouse).
        :param i:
        :return:
        """
        return lambda event: self.draw_circles(event, i)

    def delete_circles_canvas(self, i):
        """
        This function is a wrapper for the delete_circles function (bind to the user's mouse).
        :param i:
        :return:
        """
        return lambda event: self.delete_circles(event, i)

    def draw_disc_canvas(self, i):
        """
        This function is a wrapper for the draw_disc function (bind to the user's mouse).
        :param i:
        :return:
        """
        return lambda event: self.draw_disc(event, i)

    def canvas_bind(self):
        """
        This function creates the canvas bind to the user's mouse, drawing the "hovers" circles, deleting them and
        drawing the discs for the game.
        :return:
        """
        for i in range(self.game.columns):
            self.canvass_list[i].bind("<Enter>", self.draw_circles_canvas(i))
            self.canvass_list[i].bind("<Leave>", self.delete_circles_canvas(i))
            self.canvass_list[i].bind('<Button-1>', self.draw_disc_canvas(i))

    def draw_disc(self, event, column):
        """
        This function draws the disc in the wanted column (where the human player clicked), checks if a player won
        and then triggers the random move.
        :param event:
        :param column:
        :return:
        """

        if self.player1 is not None and self.player2 is not None:
            return
        elif self.player1 is not None:
            if self.game.get_current_player() == self.player1.player:
                return
        elif self.player2 is not None:
            if self.game.get_current_player() == self.player2.player:
                return

        try:
            self.make_move(column)
        except:
            return

        if self.game.get_current_player() == 1:
            if self.left_side_list:
                choose = choice(self.left_side_list)
                self.canvs_side.delete(choose)
                self.left_side_list.remove(choose)
        else:
            if self.right_side_list:
                choose = choice(self.right_side_list)
                self.canvas_right.delete(choose)
                self.right_side_list.remove(choose)
        row = 5
        for i in self.ovals_list[column][::-1]:
            if self.canvass_list[column].itemcget(i, "fill") == self.OBJ_COLOR or \
                    self.canvass_list[column].itemcget(i, "fill") == "white":
                self.canvass_list[column].itemconfig(i, fill=self.player_color)
                break
            row -= 1
        winner = self.game.get_winner(row, column)
        if winner is not None:
            winning_player = self.check_winning_player(winner)
            self.game_over_message(winning_player)
            return
        self.root.after(500, self.make_human_random_move)

    def draw_disc_ai(self, column):
        """
        This function draws the disc in the wanted column (where the AI player decided)
         and then triggers the random move.
        :param column:
        :return:
        """
        try:
            self.make_move(column)
        except:
            return

        if self.game.get_current_player() == 1:
            if self.left_side_list:
                choose = choice(self.left_side_list)
                self.canvs_side.delete(choose)
                self.left_side_list.remove(choose)
        else:
            if self.right_side_list:
                choose = choice(self.right_side_list)
                self.canvas_right.delete(choose)
                self.right_side_list.remove(choose)
        row = 5
        for i in self.ovals_list[column][::-1]:
            if self.canvass_list[column].itemcget(i, "fill") == "white" or \
                    self.canvass_list[column].itemcget(i, "fill") == self.OBJ_COLOR:
                self.canvass_list[column].itemconfig(i, fill=self.player_color)
                break
            row -= 1
        winner = self.game.get_winner(row, column)
        if winner is not None:
            winning_player = self.check_winning_player(winner)
            self.game_over_message(winning_player)
            return
        self.root.after(500, self.make_random_move)

    def check_winning_player(self, winner):
        """
        This function checks and returns the winning player or a tie if there is no winner.
        :param winner:
        :return:
        """
        if winner[0] == self.game.TIE:
            return self.game.TIE
        self.draw_winning_four(winner)
        for point in winner:
            if self.game.board[point[0]][point[1]] != 4:
                return self.game.board[point[0]][point[1]]

    def draw_winning_four(self, four_lst):
        """
        This function marks the winning 4 discs in circles.
        :param four_lst:
        :return:
        """
        for point in four_lst:
            cords = self.canvass_list[point[1]].coords(self.ovals_list[point[1]][point[0]])
            self.canvass_list[point[1]].create_oval(cords[0] + 20, cords[1] + 20, cords[2] - 20, cords[3] - 20,
                                                    fill='red')

    def make_move(self, column):
        """
        This function triggers the make_move function of Game with the wanted column
        and updates the current player's color.
        :param column:
        :return:
        """
        if self.game.get_current_player() == 1:
            self.player_color = 'black'
        else:
            self.player_color = 'blue'

        self.game.make_move(column)

    def make_random_move(self):
        """
        This function makes the a random move and triggers the next move of the AI player (in a game of 2 AI players).
        :return:
        """
        self.random_move_helper()
        if self.player1 is not None and self.player2 is not None:
            self.root.after(500, self.ai_move)

    def make_human_random_move(self):
        """
        This function makes the a random move and triggers the next move of the AI player (in a game of 1 AI player).
        :return:
        """
        self.random_move_helper()
        if self.player1 is not None or self.player2 is not None:
            self.root.after(500, self.ai_move)

    def random_move_helper(self):
        """
        This function is a helper for the make random move function, where it generates a random number and makes
        a move if that number is less than (or equal) to the gamma factor.
        :return:
        """
        rand_number = random()
        if rand_number <= self.game.gamma:
            disc = choice(Game.DISCS_LST)
            col = self.game.find_random_free_col()
            self.draw_random_move(disc, col)
        self.game.players[self.game.get_current_player()] += 1

    def draw_random_move(self, disc, column):
        """
        This function draws the random move's disc.
        :param disc:
        :param column:
        :return:
        """
        row = 5
        for i in self.ovals_list[column][::-1]:
            if self.canvass_list[column].itemcget(i, "fill") == "white" or \
                    self.canvass_list[column].itemcget(i, "fill") == self.OBJ_COLOR:
                self.game.make_random_move(row, column, disc)
                self.canvass_list[column].itemconfig(i, fill=self.colors[disc])
                break
            row -= 1

        winner = self.game.get_winner(row, column)
        if winner is not None:
            winning_player = self.check_winning_player(winner)
            self.game_over_message(winning_player)

    def ai_move(self):
        """
        This function triggers the AI move after a small delay.
        :return:
        """
        if self.player1 is not None and self.game.get_current_player() == 1:
            self.root.after(200, self.make_move_ai)

        if self.player2 is not None and self.game.get_current_player() == 2:
            self.root.after(200, self.make_move_ai)

    def make_move_ai(self):
        """
        This function makes the AI move and draws the disc of the move.
        :return:
        """
        if self.game.get_current_player() == 1:
            move = self.player1.find_legal_move()
            self.draw_disc_ai(move)
        else:
            move = self.player2.find_legal_move()
            self.draw_disc_ai(move)

    def game_over_message(self, player):
        """
        This function opens the window for the game over message.
        :param player:
        :return:
        """
        if player:
            if player == 1:
                winner_name = "Human 1"
                if self.player1:
                    winner_name = self.player1.get_winner_name()
            else:
                winner_name = "Human 2"
                if self.player2:
                    winner_name = self.player2.get_winner_name()
            x = messagebox.askyesno('game over', winner_name + " won\nplay again?")
            if x:
                self.root.destroy()
                FirstMessage(self.game.columns, gamma=self.game.gamma, ab_depth=self.ab_depth, exp_depth=self.exp_depth)
            else:
                self.root.destroy()
        elif player == 0:
            x = messagebox.askyesno('game over', "I'TS A TIE!\nplay again?")
            if x:
                self.root.destroy()
                FirstMessage(self.game.columns, gamma=self.game.gamma, ab_depth=self.ab_depth, exp_depth=self.exp_depth)
            else:
                self.root.destroy()
