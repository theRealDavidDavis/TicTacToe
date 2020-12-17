# TicTacToe
Reinforcement Learning Model vs Random Placement

Note: This project is currently ongoing

This repository hosts the files used to train a rienforcement learning model in how to play TicTacToe. The model plays against an opponent who makes truely random deicisions. 

In this repsoitory, the model's moves are tracked with the value '1' and it's opponents moves are tracked with the value '12'. As in traditional TicTacToe, when a player has 3 in a row, be it vertical, horizontal or diagonal, they win. This is determined by summing the 3 values representing the spaces to determine if the sum is equal to 3 or 12. If the sum equals 12 the opponent wins and if it is 3 then the model wins. 
