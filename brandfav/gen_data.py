import os, sys
import random

import numpy as np

# randomly generate 1,000 brands, 1,000,000 users
# Each user interacts with 8 brands on average
# optimal parameters based on experiments on real data: 
# alpha=0.3, beta=0.6, delta=0.1, gamma=0.9, tau=0.7

# the output format: uid,bid,1/0 (positive or nonpositive)

# brand favorability: 0.9-1: 18%, 0.8-0.9: 37%, 0.7-0.8: 25%, 0.6-0.7: 12%
#					  0.5-0.6: 6%, 0.4-0.5: 2%

# user positivity: normal distribution
'''
brands = {}
fh = open('brand_favs_truth.txt','w')
favs = np.random.uniform(low=0.9, high=1.0, size=(180*3,))
for i in range(len(favs)):
	bid = 'b_'+str(i+1)
	brands[bid] = favs[i]
	fh.write(bid+','+str(favs[i])+'\n')

n = len(brands)
favs = np.random.uniform(low=0.8, high=0.9, size=(370*3,))
for i in range(n,n+len(favs)):
	bid = 'b_'+str(i+1)
	brands[bid] = favs[i-n]
	fh.write(bid+','+str(favs[i-n])+'\n')

n = len(brands)
favs = np.random.uniform(low=0.7, high=0.8, size=(250*3,))
for i in range(n,n+len(favs)):
	bid = 'b_'+str(i+1)
	brands[bid] = favs[i-n]
	fh.write(bid+','+str(favs[i-n])+'\n')

n = len(brands)
favs = np.random.uniform(low=0.6, high=0.7, size=(120*3,))
for i in range(n,n+len(favs)):
	bid = 'b_'+str(i+1)
	brands[bid] = favs[i-n]
	fh.write(bid+','+str(favs[i-n])+'\n')

n = len(brands)
favs = np.random.uniform(low=0.5, high=0.6, size=(60*3,))
for i in range(n,n+len(favs)):
	bid = 'b_'+str(i+1)
	brands[bid] = favs[i-n]
	fh.write(bid+','+str(favs[i-n])+'\n')

n = len(brands)
favs = np.random.uniform(low=0.4, high=0.5, size=(20*3,))
for i in range(n,n+len(favs)):
	bid = 'b_'+str(i+1)
	brands[bid] = favs[i-n]
	fh.write(bid+','+str(favs[i-n])+'\n')

fh.close()	
'''
brands = {}
fh = open('brand_favs_truth.txt','w')
favs = np.random.normal(0.55, 0.1, 1000)
for i in range(len(favs)):
	bid = 'b_'+str(i+1)
	brands[bid] = favs[i]
	fh.write(bid+','+str(favs[i])+'\n')
fh.close()


# user positivity
users = {}
fh = open('user_poss_truth.txt','w')
poss = np.random.normal(0.55, 0.1, 1000000)
for i in range(len(poss)):
	uid = 'u_'+str(i+1)
	users[uid] = poss[i]
	fh.write(uid+','+str(poss[i])+'\n')
fh.close()

# user-brand interaction: each brands randomly selects 8,000 users
alpha = 0.3
beta = 0.6
delta = 0.1
gamma = 0.9

all_uids = users.keys()
for bid, fav in brands.iteritems():
	random.shuffle(all_uids)
	uids = all_uids[:2667]

	for uid in uids:
		pos = users[uid]

		if fav <= 0.5 and pos <= 0.5:
			sent = np.random.choice(2,1, replace=False,p=[1-delta,delta])[0]
		elif fav <= 0.5 and pos > 0.5:
			sent = np.random.choice(2,1, replace=False,p=[1-alpha,alpha])[0]
		elif fav > 0.5 and pos <= 0.5:
			sent = np.random.choice(2,1, replace=False,p=[1-beta,beta])[0]
		else:
			sent = np.random.choice(2,1, replace=False,p=[1-gamma,gamma])[0]


		print uid,',',bid,',',sent

