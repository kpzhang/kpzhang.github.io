#!/usr/bin/python

'''
***
*** all questions in the lab 2
***
'''
# question 1
datalist = [1452, 11.23, 1+2j, True, 'University of Maryland', (0,-1), [5,12], {"class":'404',"section":'A'}]

for element in datalist:
    print element,":",type(element)


# question 2
print "1. Add  2. Subtract  3. Multiple  4. Divide"
while True:
    choice = raw_input("Please select an operation: ")
    first_number = raw_input("The first number is: ")
    second_number = raw_input("The second number is: ")

    if choice == '1':
        print first_number,"+",second_number,"=",int(first_number)+int(second_number)
    elif choice == '2':
        print first_number,"-",second_number,"=",int(first_number)-int(second_number)
    elif choice == '3':
        print first_number,"*",second_number,"=",int(first_number)*int(second_number)
    elif choice == '4':
        if int(second_number) == 0:
            print "can not divided by zero..."
        else:
            print first_number,"/",second_number,"=",int(first_number)/int(second_number)
    else:
        print "wrong operation..."

    again = raw_input("Do you want to do another calculation (y/n)?")
    if again.upper() == 'N':
        print "Bye..."
        break
        
# question 3
n = int(raw_input("the longest line: "))
# print out the top half
for i in range(1,n+1):
    ith_line = "" # the variable storing all stars in the ith line
    for j in range(i): # ith line has i stars
        ith_line += "*"
    print ith_line

# print out the bottom half (one line less)
for i in range(1,n):
    ith_line = ""
    for j in range(n-i): # ith line has n-i stars
        ith_line += "*"
    print ith_line

