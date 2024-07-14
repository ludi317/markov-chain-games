
# Chutes and Ladders

Chutes and Ladders is a children's game driven entirely by chance. The game board consists of 100 squares as pictured below, and a spinner numbered from 1 to 6. 
Players start off the board and take turns spinning the spinner. Based on the square they land on, a player will either stay on the square, move forward if they land at the bottom of a ladder, or move backward if they land at the top of a chute. 
The winner is the first player to reach the final square. If a player overshoots the last square, they remain on their current square.
![chutes_and_ladders.jpg](img/chutes_and_ladders.jpg)

The game is exactly modeled as an absorbing Markov chain, since from any square the odds of moving to any other square are fixed and independent of previous moves.
The game begins on square 0, representing the off-board state.
The final square is an absorbing state; once a player reaches it, they cannot leave.

This repository uses the properties of Markov chains to calculate various statistics of a single-player game.
* Mean number of moves to win game: 39.8592604644135
* Median (50% of games finish by this number of moves): 33
* Mode (most common number of moves that wins a game): 22
* Minimum (the smallest number of moves that can win): 6
* Standard deviation: 25.96486891240239

## Graphs
### Expected Number of Moves Per Starting Square
This graph shows the expected value of the number of moves to finish the game when starting on each square. 
If the starting square is at the bottom of a ladder or the top of a chute, the only possible next move is to take the ladder or chute.
For example, the 80 square is at the bottom of a ladder to square 100, so its expected number of moves to finish the game is 1.
![chutes_and_ladders_expected_moves.png](img/chutes_and_ladders_expected_moves.png)

### Probability of Winning At Nth Move
![chutes_and_ladders_pmf.png](img%2Fchutes_and_ladders_pmf.png?)

### Probability of Winning By Nth Move
This is just the integral of the previous graph.
![chutes_and_ladders_cmf.png](img%2Fchutes_and_ladders_cmf.png)

# Curious George

On the back cover of the children's story *Curious George Goes to the Chocolate Factory*, is another such Markov chain game, but with 11 squares and a coin toss mapping to 1 or 2 squares forward.
![curious_george.jpg](img/curious_george.jpg)
Here is its graph of the expected number of moves to win per square. Square 6 takes you back to the beginning, so its expected number of moves is 1 more than square 0's.
![curious_george_expected_moves.png](img/curious_george_expected_moves.png)
### References
* https://en.wikipedia.org/wiki/Absorbing_Markov_chain
* https://math.uchicago.edu/~may/REU2014/REUPapers/Hochman.pdf
* https://possiblywrong.wordpress.com/2015/02/20/analysis-of-chutes-and-ladders/
