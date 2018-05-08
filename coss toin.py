#Simulation of Coin Toss

import random as rd
#simulation with a random number generator

#use def to change number of toss n for different results
def number_of_toss(n):
    #the inital count of heads and tails
    heads = 0
    tails = 0

    #use i to start the loop in range of n
    for i in range(n):
        toss = rd.randint(1,2) #get a random number between 1 and 2
        if toss == 1: # head
            heads += 1 #add 1 for count of heads
            print(heads, 'Heads')
        else:        # tails
            tails += 1 #add 1 for count of tails
            print(tails, 'Tails')
    print('Heads:', heads)
    print('Tails:', tails)
