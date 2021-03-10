#!/usr/bin/python

'''
***
*** all questions in the lab 3
***
'''
# question 1
char_freq = {} # an empty dictionary defining character frequency (key: character, value: frequency)
sentence = raw_input("Please enter a sentence: ")
for i in range(len(sentence)):
    current_character = sentence[i]
    if current_character == " ":
        continue
    char_freq[current_character] = char_freq.get(current_character,0) + 1

# iterate through the dictionary
for key in char_freq.keys():
    print key,":",char_freq[key]


# question 2
d = {'x':7, 'y':2, 'a':3, 'm':2}
print d
choice = raw_input("Please select an operation: (1: sort by key, 2: sort by value) ")

if choice == '1':
    all_keys = d.keys()
    all_keys.sort() # sort all keys
    # iterate through sorted keys
    for k in all_keys:
        print k,":",d[k]
elif choice == '2':
    all_values = d.values()
    all_values.sort() # sort all values
    for v in all_values:
        for key, val in d.iteritems():
            if val == v:
                print key,":",val
                del d[key]
                break
else:
    print "wrong choice..."
