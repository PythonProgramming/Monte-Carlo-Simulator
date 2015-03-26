
import random
import matplotlib
import matplotlib.pyplot as plt
import time

#lower_bust = 19.00
#higher_profit = 69.00

# back to 1,000
sampleSize = 1000
startingFunds = 100000
wagerSize = 100
wagerCount = 100



'''
def rollDice():
    roll = random.randint(1,100)

    if roll == 100:
        return False
    elif roll <= 50:
        return False
    elif 100 > roll >= 50:
        return True
'''


def rollDice():
    roll = random.randint(1,100)

    if roll <= 50:
        return False
    elif roll >= 51:
        return True







    


def multiple_bettor2(funds,initial_wager,wager_count,multiple):#,color):
    global ROI
    global multiple_busts
    global multiple_profits
    
    value = funds
    wager = initial_wager
    wX = []
    vY = []
    currentWager = 1
    previousWager = 'win'
    previousWagerAmount = initial_wager

    while currentWager <= wager_count:
        if previousWager == 'win':
            if rollDice():
                value += wager
                wX.append(currentWager)
                vY.append(value)
            else:
                value -= wager 
                previousWager = 'loss'
                previousWagerAmount = wager
                wX.append(currentWager)
                vY.append(value)
                if value <= 0:
                    multiple_busts += 1
                    break
        elif previousWager == 'loss':
            if rollDice():
                wager = previousWagerAmount * multiple
                if (value - wager) <= 0:
                    wager = value
                    
                value += wager
                wager = initial_wager
                previousWager = 'win'
                wX.append(currentWager)
                vY.append(value)
            else:
                wager = previousWagerAmount * multiple
                if (value - wager) <= 0:
                    wager = value
                value -= wager
                previousWager = 'loss'
                previousWagerAmount = wager
                wX.append(currentWager)
                vY.append(value)

                if value <= 0:
                    multiple_busts += 1
                    break

    
        currentWager += 1
    #print(('ending Value:',value 
    ROI += value

    #plt.plot(wX,vY)

    if value > funds:
        multiple_profits+=1  


multipleSampSize = 1000000
multiple_busts = 0.0
multiple_profits = 0.0
ROI = 0

counter = 1
while counter <= multipleSampSize:
    multiple_bettor2(startingFunds,wagerSize,wagerCount,1.75)
    counter += 1

print(('Total Amount Invested:', multipleSampSize * startingFunds))
print(('Total Return:',ROI))
print(('Difference:',ROI-(multipleSampSize * startingFunds)))
print(('Bust Rate:',(multiple_busts/multipleSampSize)*100.00))
print(('Profit Rate:',(multiple_profits/multipleSampSize)*100.00))
