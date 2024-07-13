import numpy as np
import matplotlib.pyplot as plt

class Game:
    def __init__(self, name, n, m, jumps):
        self.jumps = jumps
        self.name = name
        self.n = n  # number of squares
        self.m = m  # range of forward moves
        self.P = np.zeros((n + 1, n + 1))  # transition matrix
        self.N = np.eye(n)  # fundamental matrix
        self.upper_bound = 1000

        # P matrix is the full probability transition matrix, including square 0 and the final absorbing state
        # Q matrix is the transition matrix without the final absorbing state
        # N matrix is the fundamental matrix, the expected number of times the chain is in state j given that it starts in state i
        for i in range(self.n):
            if i in self.jumps:
                self.P[i][self.jumps[i]] = 1.0
                continue
            for j in range(1, self.m + 1):
                k = i if i + j > self.n else self.jumps.get(i + j, i + j)
                self.P[i][k] += 1.0 / self.m

        # Add absorbing state
        self.P[self.n][self.n] = 1

        # Q is the transition matrix without the absorbing state
        Q = self.P[:-1, :-1]

        # N, fundamental matrix, is the inverse of I - Q
        self.N = np.linalg.inv(np.eye(self.n) - Q)

        self.upper_bound = self.moves_for_3_nines()

    # Expected number of moves to reach the end of the board
    def expected_moves(self):
        # sum the rows of the N matrix
        return np.sum(self.N, axis=1)

    def plot_expected_moves(self):
        t = np.dot(self.N, np.ones(self.n))
        # append 0 to the end of the list to include the absorbing state
        t = np.append(t, 0)
        plt.plot(t)
        plt.xlabel('Square')
        plt.ylabel('Expected number of moves')
        plt.title(self.name)
        plt.show()

    # Probability of reaching the end of the board in <= n moves
    def probability_of_completion_by(self, n_moves):
        # Compute the n-step transition matrix
        Pn = np.linalg.matrix_power(self.P, n_moves)

        # The probability of transitioning from square 0 to the absorbing state in n moves
        return Pn[0][self.n]

    # Plot the cumulative mass function (cmf)
    def plot_cmf(self):
        cumulative_prob = [self.probability_of_completion_by(n) for n in range(self.upper_bound)]
        plt.bar(range(self.upper_bound), cumulative_prob)
        plt.xlabel('Number of moves')
        plt.ylabel('Probability of completion by n moves')
        plt.title("Cumulative Probability of Winning " + self.name)
        plt.show()

    # Probability of reaching the end of the board in exactly n moves
    def probability_of_completion_at(self, n_moves):
        if n_moves == 0:
            return 0
        return self.probability_of_completion_by(n_moves) - self.probability_of_completion_by(n_moves - 1)

    # Plot the probability mass function (pmf)
    def plot_pmf(self):
        prob = [self.probability_of_completion_at(n) for n in range(self.upper_bound)]
        # plot bar graph
        plt.bar(range(self.upper_bound), prob)
        median = self.median_moves()
        expected = self.expected_moves()[0]
        mode = self.mode_moves()
        plt.axvline(x=expected, color='g', linestyle='--', label='Expected')
        for m in mode:
            plt.axvline(x=m, color='b', linestyle='--', label='Mode')
        plt.axvline(x=median, color='r', linestyle='--', label='Median')
        plt.xlabel('Number of moves')
        plt.ylabel('Probability of completion at n moves')
        plt.title("Probability of Winning " + self.name)
        plt.legend()
        plt.show()

    # for discrete distributions, the median is the smallest value of X for which P(X≤m) ≥ 1/2.
    def median_moves(self):
        # use binary search
        lo = 0
        hi = self.upper_bound
        while lo < hi:
            mid = (lo + hi) // 2
            if self.probability_of_completion_by(mid) < 0.5:
                lo = mid + 1
            else:
                hi = mid
        return lo

    def mode_moves(self):
        # find the mode number of moves
        mode = [0]
        max_prob = 0
        for n_moves in range(1, self.upper_bound):
            prob = self.probability_of_completion_at(n_moves)
            if prob > max_prob:
                max_prob = prob
                mode = [n_moves]
            elif prob == max_prob:
                mode.append(n_moves)
            else:
                return mode
        return mode

    def min_moves(self):
        # use binary search to find the minimum number of moves
        lo = 0
        hi = self.upper_bound
        while lo < hi:
            mid = (lo + hi) // 2
            if self.probability_of_completion_by(mid) == 0:
                lo = mid + 1
            else:
                hi = mid
        return lo

    # Smallest number of moves such that the probability of winning is at least 99.9%
    def moves_for_3_nines(self):
        lo = 0
        hi = 1000
        while lo < hi:
            mid = (lo + hi) // 2
            if self.probability_of_completion_by(mid) < .999:
                lo = mid + 1
            else:
                hi = mid
        return lo

    def variance(self):
        # (2N - I)t - t_squared
        t = np.dot(self.N, np.ones(self.n))
        t_squared = np.multiply(t, t)
        variance = np.dot(2 * self.N - np.eye(self.n), t) - t_squared
        return variance

    def std_dev(self):
        return np.sqrt(self.variance())

    def plot_variance(self):
        variance = self.variance()
        plt.plot(variance)
        plt.xlabel('Square')
        plt.ylabel('Variance of the number of moves')
        plt.title(self.name)
        plt.show()