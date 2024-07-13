
# Chutes and Ladders

Chutes and Ladders is a children's game driven entirely by chance. The game board consists of 100 squares as pictured below, and a spinner numbered from 1 to 6. 
Players start off the board and take turns spinning the spinner. Based on the square they land on, a player will either stay on the square, move forward if they land at the bottom of a ladder, or move backward if they land at the top of a chute. 
The winner is the first player to reach the final square. If a player overshoots the last square, they remain on their current square.
![chutes_and_ladders.jpg](img/chutes_and_ladders.jpg)

The game is exactly modeled as an absorbing Markov chain, since from any square the odds of moving to any other square are fixed and independent of previous moves.
The game begins on square 0, representing the off-board state.
The final square is an absorbing state; once a player reaches it, they cannot leave.

This repository uses the properties of Markov chains to calculate various statistics of a single-player game.
* Expected number of moves to finish the game (39.8593 moves from square 0)
* Probability of finishing the game by a given number of moves (33 is the median)
* Variance of the number of moves to finish the game (674 moves from square 0)
* Minimum number of moves to finish the game (6 moves)

This graph shows the expected number of moves to finish the game when starting on each square. 
If the starting square is at the bottom of a ladder or the top of a chute, the only possible next move is to take the ladder or chute.
![chutes_and_ladders_expected_moves.png](img/chutes_and_ladders_expected_moves.png)

# Curious George

On the back cover of the children's story *Curious George Goes to the Chocolate Factory*, is another such Markov chain game, but with 11 squares and a coin toss mapping to 1 or 2 squares forward.
![curious_george.jpg](img/curious_george.jpg)
Here is its graph of the expected number of moves. The expected number of moves to finish the game is only 5, and the game could be finished in as few as 3 moves.
![curious_george_expected_moves.png](img/curious_george_expected_moves.png)
### References
* https://en.wikipedia.org/wiki/Absorbing_Markov_chain
* https://math.uchicago.edu/~may/REU2014/REUPapers/Hochman.pdf
* https://possiblywrong.wordpress.com/2015/02/20/analysis-of-chutes-and-ladders/
