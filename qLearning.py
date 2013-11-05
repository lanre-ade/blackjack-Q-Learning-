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
alpha = 0.001
epsilon = 1
gamma = 1
Q = numpy.zeros((181, len(actions)))
for episodeNum in range(numEpisodes):
    s = blackjack.init();
    G = 0
    while (s != -1):
        i = random.uniform(0, 1)
        #do an epsilon check, random policy or else proceed to policy
        if (i <= epsilon){
            a = ramdom_policy(actions)
        }
        else{ 
            a = argmax(Q[s, :])
        }
        result = blackjack.sample (s,a)
        s_ = result[1]
        G = result[0]
        Q[s, a] = Q[s, a] + alpha * (result[0] + (gamma * max (Q[s_:])) - Q(s, a)
        s = s_
    returnSum = returnSum + G
    if (episodeNum % 10000 == 0){    
        print "Episode: ", episodeNum, "Average Return: ", returnSum/episodeNum
        }


print "Average return: ", returnSum/numEpisodes


