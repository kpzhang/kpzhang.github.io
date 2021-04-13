import os,sys
import random
import math

import numpy as np

fh = open('2015.txt','r') # activity file
lines = fh.readlines()
fh.close()

brands = []
users = []
brand_acts = {}
user_acts = {}
for line in lines:
	arr = line.strip().split(',')
	uid = arr[0].strip()
	bid = arr[1].strip()
	sent = arr[2].strip()

	if bid not in brands:
		brands.append(bid)
	if uid not in users:
		users.append(uid)
	if uid not in user_acts:
		user_acts[uid] = {}
	user_acts[uid][bid] = sent
	if bid not in brand_acts:
		brand_acts[bid] = {}
	brand_acts[bid][uid] = sent


# block-based MCMC: sample brands and users alternatively (brands first)
alpha = 0.3
beta = 0.6
delta = 0.1
gamma = 0.9

print 'block-based MCMC is starting...'
# initilization
brand_favs = {}
user_poss = {}
b_samples = []
for bid in brands:
	#n = np.random.randint(1,9)
	#b_samples.append([1]*n+[0]*(10-n))
	#brand_favs[bid] = n/10.0
	b_samples.append([1,1,1,1,0])
	brand_favs[bid] = 0.8

u_samples = []
for uid in users:
	#n = np.random.randint(1,9)
	#u_samples.append([1]*n+[0]*(10-n))
	#user_poss[uid] = n/10.0
	u_samples.append([1,1,1,1,0])
	user_poss[uid] = 0.8

for k in range(200): # 250 rounds
	print 'running...round:',k+1
	
	# sampe brands and calculate its posterior prob.
	for i in range(len(users)):
		n1 = u_samples[i].count(1)
		n0 = u_samples[i].count(0)
		p = n1 * 1.0 / (n1 + n0)
		user_poss[users[i]] = p

	for j in range(len(brands)):
		bid = brands[j]
		n1 = b_samples[j].count(1)
		n0 = b_samples[j].count(0)
		cur_fav_1 = n1 * 1.0 / (n1 + n0)
		cur_fav_0 = 1.0 - cur_fav_1

		multiplier_1 = math.log(cur_fav_1*10)
		multiplier_0 = math.log(cur_fav_0*10)
		for uid,sent in brand_acts[bid].iteritems():
			cur_pos = user_poss[uid]
			prob = 1.0
			if cur_pos <= 0.5:
				if sent == '1':
					prob = beta
				else:
					prob = 1-beta
			else:
				if sent == '1':
					prob = gamma
				else:
					prob = 1-gamma

			multiplier_1 += math.log(prob*10)

		for uid,sent in brand_acts[bid].iteritems():
			cur_pos = user_poss[uid]
			prob = 1.0
			if cur_pos <= 0.5:
				if sent == '1':
					prob = delta
				else:
					prob = 1-delta
			else:
				if sent == '1':
					prob = alpha
				else:
					prob = 1-alpha

			multiplier_0 += math.log(prob*10)

		mcmc_prob = multiplier_1 / (multiplier_1 + multiplier_0)
		sample = np.random.choice(2,1, replace=False,p=[1-mcmc_prob,mcmc_prob])[0]
		b_samples[j].append(sample)
	
	# sampe brands and calculate its posterior prob.
	for i in range(len(brands)):
		n1 = b_samples[i].count(1)
		n0 = b_samples[i].count(0)
		p = n1 * 1.0 / (n1 + n0)
		brand_favs[brands[i]] = p

	for i in range(len(users)):
		uid = users[i]
		n1 = u_samples[i].count(1)
		n0 = u_samples[i].count(0)
		cur_pos_1 = n1 * 1.0 / (n1 + n0)
		cur_pos_0 = 1.0 - cur_pos_1

		multiplier_1 = math.log(cur_pos_1*100)
		multiplier_0 = math.log(cur_pos_0*100)
		for bid,sent in user_acts[uid].iteritems():
			cur_fav = brand_favs[bid]
			prob = 1.0
			if cur_fav <= 0.5:
				if sent == '1':
					prob = alpha
				else:
					prob = 1-alpha
			else:
				if sent == '1':
					prob = gamma
				else:
					prob = 1-gamma

			multiplier_1 += math.log(prob*100)

		for bid,sent in user_acts[uid].iteritems():
			cur_fav = brand_favs[bid]
			prob = 1.0
			if cur_fav <= 0.5:
				if sent == '1':
					prob = delta
				else:
					prob = 1-delta
			else:
				if sent == '1':
					prob = beta
				else:
					prob = 1-beta

			multiplier_0 += math.log(prob*100)

		mcmc_prob = multiplier_1 / (multiplier_1 + multiplier_0)
		#print multiplier_1,',',multiplier_0
		sample = np.random.choice(2,1, replace=False,p=[1-mcmc_prob,mcmc_prob])[0]
		u_samples[i].append(sample)


# output after 250 rounds
fh = open('brand_favs_predicted_2015.txt','w')
for i in range(len(brands)):
	n1 = b_samples[i].count(1)
	n0 = b_samples[i].count(0)
	p = n1 * 1.0 / (n1 + n0)
	fh.write(brands[i]+','+str(p)+'\n')
fh.close()

fh = open('user_poss_predicted_2015.txt','w')
for i in range(len(users)):
	n1 = u_samples[i].count(1)
	n0 = u_samples[i].count(0)
	p = n1 * 1.0 / (n1 + n0)
	fh.write(users[i]+','+str(p)+'\n')
fh.close()
