"""
Created by: Meto Trajkovski
Email: metot@hotmail.com
"""

import random


def get_values():
    # print explanation
    print('Program that simulates X volleyball games.\n')

    # check value for Team A probability to win a serve
    prob_a = 0
    while True:
        prob_a = input('What is the probability team A wins a serve?\nTeam A probability (0.0-1.0): ')
        try:
            prob_a = float(prob_a)
        except:
            print('The value must be a number!\n')
            continue
        
        if (prob_a < 0.0) or (prob_a > 1.0):
            print('The value must be in range 0.0 - 1.0!\n')
            continue
        
        print()
        break

    # check value for Team B probability to win a serve
    prob_b = 0
    while True:
        prob_b = input('What is the probability team B wins a serve?\nTeam B probability (0.0-1.0): ')
        try:
            prob_b = float(prob_b)
        except:
            print('The value must be a number!\n')
            continue
        
        if (prob_b < 0.0) or (prob_b > 1.0):
            print('The value must be in range 0.0 - 1.0!\n')
            continue
        
        print()
        break
    
    # check value for number of games
    num_games = 0
    while True:
        num_games = input('How many games to simulate?\nNumber of games: ')
        try:
            num_games = int(num_games)
        except:
            print('The value must be an integer!\n')
            continue
        
        if num_games <= 0:
            print('The value must be bigger than 0!\n')
            continue
        
        print()
        break

    # return those values
    return (prob_a, prob_b, num_games)


def simulate_games(prob_a, prob_b, num_games):
    wins_a = 0
    wins_b = 0

    # simulate 'num_games' games 
    for i in range(num_games):
        score_a, score_b = volleyball_game(prob_a, prob_b)
        
        if score_a > score_b:
            wins_a += 1
        else:
            wins_b += 1
    
    # return wins results
    return wins_a, wins_b


def volleyball_game(prob_a, prob_b):
    # to get play started, a team is chosen to serve by coin toss
    serves_A = random.choice([True, False])

    score_A = 0
    score_B = 0

    # play the game
    while True:
        rand = random.random()

        # check which team is serving
        if serves_A:
            # check who win the serve
            if rand < prob_a:
                score_A += 1
            else:
                score_B += 1
                serves_A = False
        else:
            # check who win the serve
            if rand < prob_b:
                score_B += 1
            else:
                score_A += 1
                serves_A = True

        # if the difference between scores is more than 2
        # and some of the team has 15 or more points
        # then the game is over, returns the score
        if (abs(score_A - score_B) >= 2) and ((score_A >= 15) or (score_B >= 15)):
            return (score_A, score_B)


def print_wins(wins_a, wins_b):
    print('Simulation ended, those are the results:')
    print('Team A won: {0}'.format(wins_a))
    print('Team B won: {0}'.format(wins_b))


def volleyball_simulation():
    # get values
    prob_a, prob_b, num_games = get_values()

    # simulate 'num_games' games
    wins_a, wins_b = simulate_games(prob_a, prob_b, num_games)

    # print results
    print_wins(wins_a, wins_b)


if __name__ == '__main__':
    volleyball_simulation()