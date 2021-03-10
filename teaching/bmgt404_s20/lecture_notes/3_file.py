#!/usr/bin/python

# practice if statement
x = 5
if x>3:
	print "x>3"
	x += 5
	print "x now is: ",x
if x>10:
	print "x>10"
print "all done"

x = 120
if x>100:
	print "x>100"
	if x<150:
		print "x<150"
print "all done"

# practice if-else statement
x = 15

if x % 2 == 0:
    print(x, "is even")
else:
	print(x, "is odd")

# nested if-else statement
x = 10
y = 10

if x < y:
	print("x is less than y")
else:
	if x > y:
		print("x is greater than y")
	else:
		print("x and y must be equal")
	
# practice if-elif-elif-...-else statement

t = raw_input("What is the time?")
x = int(t)
if x < 10:
	print "Good morning"
elif x < 12: 
	print "Soon time for lunch"
elif x < 18: 
	print "Good day"
elif x < 22:
	print "Good evening"
else: 
	print "Good night"


# practice conditional statements along with other functions (raw_input)
x = raw_input('Please select your year: (freshman,sophomore,junior,senior): ')
y = raw_input('How many courses have you taken so far? ')
n = int(y)
if x == 'freshman':
	if n < 4:
		print "take more on your sophomore year"
	else:
		print "you are taking enough for the first year"
elif x == 'sophomore':
	if n <> 8:
		print "you have taken ",n,"courses"
	else:
		print "you have taken 8 courses"
elif x == 'junior':
	if n < 12:
		print "less than 12 courses"
elif x == 'senior':
	if n >= 16:
		print "you are good to graduate"
	else:
		print "sorry, you need more courses"
else:
	print "what you typed is not in [freshman,sophomore,junior,senior]"
	print "run it again"

print "all done"
