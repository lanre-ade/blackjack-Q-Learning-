import blackjack
from random import choice
from pylab import *
from numpy import *

def random_policy (list_of_actions): #returns a random action from a list of possible actions
    next_action = choice(list_of_actions)
    #print next_action
    return next_action

numEpisodes = 10000

returnSum = 0.0
actions = [0,1]
alpha
epsilon
gamma
Q = numpy.zeros(181, len(actions))
for episodeNum in range(numEpisodes):
    s = blackjack.init();
    G = 0
    while (s != -1):
    	a = numpy
        result = blackjack.sample (s,a)
        G = G + result[0]
        s = result[1]
    print "Episode: ", episodeNum, "Return: ", G
    returnSum = returnSum + G

print "Average return: ", returnSum/numEpisodes


