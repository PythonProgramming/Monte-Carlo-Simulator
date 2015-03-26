

import random


# let us go ahead and change this to return a simple win/loss
def rollDice():
    roll = random.randint(1,100)

    if roll == 100:
        print roll,'roll was 100, you lose. What are the odds?! Play again!'
        return False
    elif roll <= 50:
        print roll,'roll was 1-50, you lose.'
        return False
    elif 100 > roll >= 50:
        print roll,'roll was 51-99, you win! *pretty lights flash* (play more!)'
        return True


'''
Simple bettor, betting the same amount each time.
'''
def simple_bettor(funds,initial_wager,wager_count):
    value = funds
    wager = initial_wager

    currentWager = 0

    while currentWager < wager_count:
        if rollDice():
            value += wager
        else:
            value -= wager

        currentWager += 1
        print 'Funds:', value



simple_bettor(10000,100,100)
    
    

    
    
