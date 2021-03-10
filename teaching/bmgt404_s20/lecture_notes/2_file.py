#!/usr/bin/python

# practice print statement
print ("hello, world!")
print ("")
print "hello, 'world!'"
print "hello\tworld"
print 'hello\nworld'

# practice assignment and type conversion
x = 3
y = 5
z = 2.5
m = '2.7'
print x+y
print x/y
print type(m)
print float(m) + y

x = raw_input('X= ')
# you will type some number, e.g., 5 during execution
y = raw_input('Y= ')
# you will type some number, e.g., 10 during execution
print "X+Y=",int(x) + int(y)
print "X/Y=",float(x)/float(y)

# practice operators and operands
print 20 + 10
print 7/3
print 7//3
print 7%3

# practice arithmetic operators
a = 10
b = 7
print 'a+b=',a + b
print 'a-b=',a - b
print 'a*b=',a * b
print 'a/b=',a / b
print 'a%b=',a % b
print 'a//b=',a // b

# practice comparison operators
print 'a is greater than b ?',a > b
print 'a is equal to b ?',a == b
print 'a is not equal to b ?', a <> b

# practice logical operators
print (a>=b) and (a>5)
print (a<=b) or (a>5)
print not a
print not True
print not not False

# practice precedence of operators
a = 10
b = 5
print (a+b)>15 or (a-b)<8
print (a+b)>15 or ((a-b)<8 and False)
print a+b>15-2*2**4/4 and (not False)

# practice modulus operator
x = raw_input('give a number (>1000):')
print "the last two digits: ",x%100
