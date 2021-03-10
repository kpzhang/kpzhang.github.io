#!/usr/bin/python

'''
***
*** all problems in the lab 5
***
'''
import math

# exercise 1
position = [0, 0] # original position

moves = [] # a list of tuples to store all moves

print "Enter all moves"
while True:
    one_step = raw_input().upper()
    if one_step == 'X':
        break
    # process the current move. One move consists of direction and number of steps separated by spaces
    arr = one_step.strip().split(" ")
    one_move = (arr[0], int(arr[1]))
    moves.append(one_move)

# get the final position
for move in moves:
    direction = move[0]
    steps = move[1]
    if direction == 'UP':
        position[1] += steps
    elif direction == 'DOWN':
        position[1] -= steps
    elif direction == 'LEFT':
        position[0] -= steps
    else:
        position[0] += steps

# calculate the euclidean distance
dist = math.sqrt(position[0]*position[0]+position[1]*position[1])
print "The distance is:", dist


# exercise 2
article = [] # a list of sentences

print "Enter the entire article"
while True:
    sentence = raw_input().lower()
    if sentence == 'x':
        break
    article.append(sentence)

# a frequency dictionary
freq = {}
for sentence in article:
    words = sentence.strip().split()
    for w in words:
        freq[w] = freq.get(w,0)+1

# print out the result
all_keys = freq.keys()
all_keys.sort()
for word in all_keys:
    print word,":",freq[word]
