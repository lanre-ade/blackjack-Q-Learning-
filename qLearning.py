
import blackjack
from random import choice
from pylab import *
from numpy import *

def random_policy (list_of_actions): #returns a random action from a list of possible actions
    return choice(list_of_actions)

def policy(s):
    return argmax(Q[s, :])

numEpisodes = 10000000
returnSum = 0.0
actions = [0,1]
alpha = 0.001
epsilon = 0.3 
gamma = 1
Q = 0.00001*rand(181,2)

print "Epsilon: ", epsilon, "Alpha: ", alpha

for episodeNum in range(numEpisodes):
    s = blackjack.init();
    G = 0
    while (s != -1):
        i = random.uniform(0, 1)
        #do an epsilon check, random policy or else proceed to policy
        if (i <= epsilon):
            a = random_policy(actions)
        else: 
            a = policy(s)
        result = blackjack.sample (s,a)
        s_ = result[1]
        G = result[0]
        Q[s, a] = Q[s, a] + alpha * (result[0] + (gamma * max(Q[s_, :])) - Q[s, a])
        s = s_
    returnSum = returnSum + G
    if (episodeNum % 10000 == 0 and episodeNum > 0):    
        print "Episode: ", episodeNum, "Average Return: ", returnSum/episodeNum

if (episodeNum > 0 ): print "Average return: ", returnSum/numEpisodes
else :print "Average return: 0"

blackjack.printPolicy(policy)
    
    
    
