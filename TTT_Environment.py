import numpy as np
import pandas as pd


class TicTacToe():

    def __init__(self):
        # RL agent is currently made to be the player who uses 1 - other player uses 4.
        tmp = np.zeros((3, 3))
        self.df_state = pd.DataFrame(data=tmp)
        self.ActionSpace = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.win_loss = [3, 12]
        self.win = false
        self.lose = false
        self.tie = false
        self.moves = 0
        self.play = true

    def reset(self):
        tmp = np.zeros((3, 3))
        self.df_state = pd.DataFrame(data=tmp)
        self.ActionSpace = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.win_loss = [3, 12]
        self.win = false
        self.lose = false
        self.tie = false
        self.moves = 0
        self.play = true

    def end_condition(self):
        # Checks the rows, columns and diagonals for end conditions
        for col in range(3):
            if self.df_state[row].sum() == 3:
                self.win = true
            elif self.df_state[row].sum() == 12:
                self.lose = true
        for row in range(3):
            if self.df_state.iloc[row].sum() == 3:
                self.win = true
            elif self.df_state.iloc[row].sum() == 12:
                self.lose = true
        if np.trace(self.df_state) == 3:
            self.win = true
        elif np.trace(self.df_state) == 12:
            self.lose = true
        second_diag = self.df_state.iloc[0, 2] + self.df_state.iloc[1, 1] + self.df_state.iloc[2, 0]
        if second_diag == 3:
            self.win = true
        elif second_diag == 12:
            self.lose = true
        if self.moves == 9 and self.win == false and self.lose == false:
            self.tie = true

    def end_of_turn(self):
        # Determines if the next player can make a move
        if self.win != false or self.lose != false or self.tie != false:
            self.play = false

    def action_space(self):
        # possible moves that can be made
        self.ActionSpace = []
        i = 1
        for row in range(3):
            for col in range(3):
                if self.df_state.iloc[row, col] == 0:
                    self.ActionSpace.append(i)
                i = i + 1

    def update_environment(self, action, player_val):
        # Receives the numerical value for the action and converts it to the DataFrame index location
        move = []
        if action > 6:
            tmp = action - 7
            move = [2, tmp]
        elif action > 3:
            tmp = action - 4
            move = [1, tmp]
        else:
            tmp = action - 1
            move = [0, tmp]
        self.df_state.at[move] = player_val

    def step(self, action, player):
        # The step function is the function to simulate the agents turn. It receives the agents action, updates the environment, checks win condition and then applies rewards
        reward = 0
        if self.play == false:
            if self.win == true:
                reward = 10
            elif self.tie == true:
                reward = 5
        else:
            if player == 1:
                self.update_environment(action, 1)
            else:
                self.update_environment(action, 4)
            self.end_condition()
            self.end_of_turn()
            self.action_space()

        return reward, self.df_state

