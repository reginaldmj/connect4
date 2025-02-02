# connect 4

Connect 4 in Python

The Connect Four game is a classic two-player game where players take turns dropping colored discs (usually red and yellow) into a vertically suspended grid, with the goal of getting four of their own discs in a row, either horizontally, vertically, or diagonally.

Basic Rules: Game Setup:

The game is played on a grid with 7 columns and 6 rows (7x6 board). One player is assigned an 'O,', and the other player is assigned an 'X.' Gameplay:

Players take turns dropping one of their discs into any of the 7 columns. The disc will fall to the lowest available row in the chosen column. The game ends when one player connects four discs in a row, either horizontally, vertically, or diagonally. If the grid fills up without either player connecting four, the game is a draw. Winning Condition:

A player wins if they form a continuous line of 4 discs, either: Horizontally: 4 discs in a row on the same row. Vertically: 4 discs in a column. Diagonally: 4 discs in a diagonal line, either from top-left to bottom-right or top-right to bottom-left. Ending the Game:

The game either ends when a player connects four discs or when the grid is full without a winner (in which case it’s a draw).
