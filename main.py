from markov import Game

curious_george_jumps = {1: 2, 3: 2, 4: 7, 6: 0, 8: 11, 9: 7}

chutes_and_ladders_jumps = {2: 19, 4: 14, 8: 31, 16: 6, 21: 42, 28: 84, 36: 44, 48: 26, 49: 10, 51: 67, 56: 53, 62: 18,
                            64: 60, 71: 91, 80: 100, 87: 24, 93: 73, 95: 75, 98: 78}

if __name__ == '__main__':
    Chutes_And_Ladders = Game("Chutes and Ladders", 100, 6, chutes_and_ladders_jumps)
    Curious_George = Game("Curious George Chocolate Trail", 11, 2, curious_george_jumps)
    games = [Chutes_And_Ladders, Curious_George]
    for game in games:
        print(game.name)
        print("Mean:", game.expected_moves()[0])
        print("Median:", game.median_moves())
        print("Mode:", game.mode_moves())
        print("Minimum:", game.min_moves())
        print("Standard deviation:", game.std_dev()[0])
        game.plot_expected_moves()
        game.plot_pmf()
        game.plot_cmf()
        print()



