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

    def probability_of_completion(self, n_moves):
        # Compute the n-step transition matrix
        Pn = np.linalg.matrix_power(self.P, n_moves)

        # The probability of transitioning from square 0 to the absorbing state in n moves
        return Pn[0][self.n]

    def median_moves(self):
        # use binary search to find the median number of moves
        lo = 0
        hi = 1000
        while lo < hi:
            mid = (lo + hi) // 2
            if self.probability_of_completion(mid) < 0.5:
                lo = mid + 1
            else:
                hi = mid
        return lo

    def min_moves(self):
        # use binary search to find the minimum number of moves
        lo = 0
        hi = 1000
        while lo < hi:
            mid = (lo + hi) // 2
            if self.probability_of_completion(mid) == 0:
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

    def plot_variance(self):
        variance = self.variance()
        plt.plot(variance)
        plt.xlabel('Square')
        plt.ylabel('Variance of the number of moves')
        plt.title(self.name)
        plt.show()