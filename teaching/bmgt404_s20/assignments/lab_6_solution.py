#!/usr/bin/python

# In this code, I consider txt files are in the same folder as this python file
# If they are in different folders, you'd better use the absolute path when you
# open files

import os

# exercise 1

fh = open('customer-savings.txt','r')
lines = fh.readlines()
fh.close() # even I close the file handle, lines still stores all lines of the file

total_balance_male = 0.0
total_balance_female = 0.0
total_balance_white = 0.0
total_balance_blue = 0.0
count_balance_male = 0
count_balance_female = 0
count_balance_white = 0
count_balance_blue = 0

for line in lines:
    columns = line.strip().lower().split(",")
    gender = column[3]
    job = column[6]
    balance = float(column[8])

    if gender = 'male':
        total_balance_male += balance
        count_balance_male += 1
    else:
        total_balance_female += balance
        count_balance_female += 1

    if job == 'white collar':
        total_balance_white += balance
        count_balance_white += 1
    else:
        total_balance_blue += balance
        count_balance_blue += 1

print "Averge balance for male and female: ",total_balance_male/count_balance_male,",",total_balance_female/count_balance_female
print "Averge balance for while collar and blue collar: ",total_balance_white/count_balance_white,",",total_balance_blue/count_balance_blue


# exercise 2
fh_status = open('customer-status.txt','r')
lines_status = fh_status.readlines()
fh_status.close()

fh_sales = open('sales.txt','r')
lines_sales = fh_sales.readlines()
fh_sales.close()

# convert all sales lines into a dictionary (key: account name, value: sale line)
sales_dict = {}
for sale in lines_sales:
    acc_name = sale.strip().split(",")[0]
    sales_dict[acc_name] = sale.strip()

# convert all status lines into a dictionary (key: account name, value: status)
status_dict = {}
for status_line in lines_status:
    status = status_line.strip().split(",")[-1]
    acc_name = status_line.strip().split(",")[0]
    status_dict[acc_name] = status

# combine two files
for acc_name, sale in sales_dict.iteritems():
    if acc_name in status_dict:
        print sale,",",status_dict[acc_name]
    
