
import random
import matplotlib
import matplotlib.pyplot as plt
import time

#lower_bust = 31.235
#higher_profit = 63.208

lower_bust = 19.00
higher_profit = 69.00

# back to 1,000
sampleSize = 1000
startingFunds = 10000
wagerSize = 100
wagerCount = 100




def rollDice():
    roll = random.randint(1,100)

    if roll == 100:
        return False
    elif roll <= 50:
        return False
    elif 100 > roll >= 50:
        return True




def dAlembert(funds,initial_wager,wager_count):#,color):

    global da_busts
    global da_profits
    
    value = funds
    wager = initial_wager
    wX = []
    vY = []
    currentWager = 1
    previousWager = 'win'
    previousWagerAmount = initial_wager

    while currentWager <= wager_count:
        if previousWager == 'win':
            if wager == initial_wager:
                pass
            else:
                wager -= initial_wager

            #print 'current wager:',wager,'value:',value


            if rollDice():
                value += wager
                #print 'we won! Current Value:',value
                wX.append(currentWager)
                vY.append(value)
            else:
                value -= wager 
                previousWager = 'loss'
                #print 'we lost, current value',value
                previousWagerAmount = wager
                wX.append(currentWager)
                vY.append(value)
                if value <= 0:
                    da_busts += 1
                    break
        elif previousWager == 'loss':
            wager = previousWagerAmount + initial_wager
            if (value - wager) <= 0:
                wager = value
            #print 'Lost the last wager, current wager:',wager,'value:',value
            
            if rollDice(): 
                value += wager
                #print 'we won! Current Value:',value
                previousWager = 'win'
                wX.append(currentWager)
                vY.append(value)
            else:
                value -= wager
                previousWager = 'loss'
                #print 'we lost, current value',value
                previousWagerAmount = wager
                wX.append(currentWager)
                vY.append(value)

                if value <= 0:
                    da_busts += 1
                    break

        currentWager += 1

    #plt.plot(wX,vY)

    if value > funds:
        da_profits+=1




    



def multiple_bettor(funds,initial_wager,wager_count):#,color):

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
                wager = previousWagerAmount * random_multiple
                if (value - wager) <= 0:
                    wager = value
                    
                value += wager
                wager = initial_wager
                previousWager = 'win'
                wX.append(currentWager)
                vY.append(value)
            else:
                wager = previousWagerAmount * random_multiple
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

    #plt.plot(wX,vY)

    if value > funds:
        multiple_profits+=1



def multiple_bettor2(funds,initial_wager,wager_count,multiple):#,color):

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
                wager = previousWagerAmount * random_multiple
                if (value - wager) <= 0:
                    wager = value
                    
                value += wager
                wager = initial_wager
                previousWager = 'win'
                wX.append(currentWager)
                vY.append(value)
            else:
                wager = previousWagerAmount * 2
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

    #plt.plot(wX,vY)

    if value > funds:
        multiple_profits+=1  
    


def doubler_bettor(funds,initial_wager,wager_count,color):
    global doubler_busts
    global doubler_profits
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
                if value < 0:
                    currentWager += 10000000000000000
                    doubler_busts += 1
        elif previousWager == 'loss':
            if rollDice():
                wager = previousWagerAmount * 2
                if (value - wager) < 0:
                    wager = value
                    
                value += wager
                wager = initial_wager
                previousWager = 'win'
                wX.append(currentWager)
                vY.append(value)
            else:
                wager = previousWagerAmount * 2
                if (value - wager) < 0:
                    wager = value
                value -= wager
                previousWager = 'loss'
                previousWagerAmount = wager
                wX.append(currentWager)
                vY.append(value)

                if value <= 0:
                    currentWager += 10000000000000000
                    doubler_busts += 1

        currentWager += 1
    #plt.plot(wX,vY,color)
    if value > funds:
        doubler_profits+=1

def simple_bettor(funds,initial_wager,wager_count,color):
    global simple_busts
    global simple_profits

    value = funds
    wager = initial_wager
    wX = []
    vY = []
    currentWager = 1
    while currentWager <= wager_count:
        if rollDice():
            value += wager
            wX.append(currentWager)
            vY.append(value)
        else:
            value -= wager
            wX.append(currentWager)
            vY.append(value)

            if value <= 0:
                currentWager += 10000000000000000
                simple_busts +=1
        currentWager += 1
    plt.plot(wX,vY,color)
    if value > funds:
        simple_profits+=1
x = 0

#Doubler Bettor Bust Chances: 84.1457... so anything less than this... aaaand
#Doubler Bettor Profit Chances: 15.6355 ... aaaand better than this.

while x < 1:
    
    da_busts = 0.0
    da_profits = 0.0
    daSampSize = 10000
    currentSample = 1
    
    #random_multiple = random.uniform(0.6,2.0)
    while currentSample <= daSampSize:
        dAlembert(startingFunds,wagerSize,wagerCount)
        currentSample += 1

    if ((da_busts/daSampSize)*100.00 < lower_bust) and ((da_profits/daSampSize)*100.00 > higher_profit):
        print '#################################################'
        #print 'found a winner, the multiple was:',random_multiple
        print 'Lower Bust Rate Than:',lower_bust
        print 'Higher profit rate than:',higher_profit
        print 'Bust Rate:',(da_busts/daSampSize)*100.00
        print 'Profit Rate:',(da_profits/daSampSize)*100.00
        print '#################################################'
        time.sleep(5)
        #plt.show()
    else:
        '''
        print '####################################'
        print 'To beat:'
        print 'Lower Bust Rate Than:',lower_bust
        print 'Higher profit rate than:',higher_profit
        print 'Bust Rate:',(da_busts/daSampSize)*100.00
        print 'Profit Rate:',(da_profits/daSampSize)*100.00
        print '####################################'
        '''
        #clears the figure
        #plt.clf()
        

    x+=1

