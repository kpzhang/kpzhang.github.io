#!usr/bin/python

fh = open('transaction.txt','r')
lines = fh.readlines()
fh.close()

single_dict = {}
coselling_dict = {}
for line in lines:
	splits1 = line.strip().split(":")
	cid = splits1[0]
	products = splits1[1]
	splits2 = products.split(",")
	for s in splits2:
		p = str(s)
		if p in single_dict:
			single_dict[p] += 1
		else:
			single_dict[p] = 1

	for i in range(len(splits2)):
		for j in range(i+1,len(splits2)): # from i+1, because we do not want to see coselling for the same product: like i-i
			key = str(splits2[i])+"-"+str(splits2[j])
			if key in coselling_dict:
				coselling_dict[key] += 1
			else:
				coselling_dict[key] = 1

# save original dictionaires for rule generating use later
original_single_dict = single_dict
original_coselling_dict = coselling_dict

# sort two dictionaries; the results are two lists, therefore you can
# use index to access elements
sorted_single_dict = sorted(single_dict.iteritems(), key=lambda (k,v): (v, k))
sorted_coselling_dict = sorted(coselling_dict.iteritems(), key=lambda (k,v): (v, k))

print "Top selling products"
i = -1
while i>=-10:
	print sorted_single_dict[i]
	i -= 1

print "Top coselling products"
i = -1
while i >= -10:
	print sorted_coselling_dict[i]
	i -= 1

# generating rules
rules = {}
for coselling_key,coselling_val in original_coselling_dict.items():
	pair = coselling_key.split("-")
	product1 = pair[0]
	product2 = pair[1]
	# set the threshold of the individual selling for each product
	if (product1 in original_single_dict) and (original_single_dict[product1]>=1000):
		#print coselling_key,",",coselling_val,",",original_single_dict[product1]
		conf1 = float(coselling_val)/original_single_dict[product1]
		rule = product1+"->"+product2
		rules[rule] = conf1
	if (product2 in original_single_dict) and (original_single_dict[product2]>=1000):
		conf2 = float(coselling_val)/original_single_dict[product2]
		rule = product2+"->"+product1
		rules[rule] = conf2

# sort rules in terms of values
sorted_rules = sorted(rules.iteritems(), key=lambda (k,v): (v, k))
print "Top 10 rules"
i = -1
while i>=-10:
	print sorted_rules[i]
	i -= 1
