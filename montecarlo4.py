
import random
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")

def rollDice():
    roll = random.randint(1,100)

    if roll == 100:
        return False
    elif roll <= 50:
        return False
    elif 100 > roll >= 50:
        return True


'''
Simple bettor, betting the same amount each time.
'''
def simple_bettor(funds,initial_wager,wager_count):
    value = funds
    wager = initial_wager

    # wager X
    wX = []

    #value Y
    vY = []

    # change to 1, to avoid confusion so we start @ wager 1
    # instead of wager 0 and end at 100. 
    currentWager = 1

    #           change this to, less or equal.
    while currentWager <= wager_count:
        if rollDice():
            value += wager
            # append #
            wX.append(currentWager)
            vY.append(value)
            
        else:
            value -= wager
            # append #
            wX.append(currentWager)
            vY.append(value)

        currentWager += 1
        
    #print 'Funds:', value

    plt.plot(wX,vY)
    


x = 0

# start this off @ 1, then add, and increase 50 to 500, then 1000
while x < 100:
    simple_bettor(10000,100,100)
    x += 1


plt.ylabel('Account Value')
plt.xlabel('Wager Count')
plt.show()


