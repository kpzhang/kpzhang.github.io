#!/usr/bin/python

'''
***
*** all functions in the lab 4
***
'''

def show_functions():
    print "*********************************************"
    print "* 1. Generate overall stats for all products (total #, avg #, min, and max)"
    print "* 2. Calculate the amount for a given product"
    print "* 3. Update the amount for a given product"
    print "*********************************************"

    choice = raw_input("Please select an operation: ")

    return choice


def gen_stats(stock):
    total_stock = 0
    avg_stock = 0.0
    min_stock = 1000000 # manually put a large number here at this moment
    max_stock = 0
    for p, num in stock.iteritems():
        total_stock += num
        if min_stock > num:
            min_stock = num
        if max_stock < num:
            max_stock = num
    avg_stock = total_stock/float(len(stock))

    return (total_stock, avg_stock, min_stock, max_stock)


def check_stock(stock):
    product_name = raw_input("Enter the product name: ")
    for p, num in stock.iteritems():
        if p == product_name:
            print p,"has", num, "in stock."
            break


def update_stock(stock):
    product_name = raw_input("Enter the product name: ")
    amount = int(raw_input("Enter the increased/decreased amount: "))
    stock[product_name] += amount

    return stock


def main():
    product_stock = {"computer":35, "chair": 100, "desk": 20, "iphone": 15}
    print "The current stock"
    print product_stock

    choice = show_functions()
    if choice == '1':
        total, avg, minimum, maximum = gen_stats(product_stock)
        print "total:",total,"\naverage:",avg,"\nminimum:",minimum,"\nmaximum:",maximum
    elif choice == '2':
        check_stock(product_stock)
    elif choice == '3':
        updated_stock = update_stock(product_stock)
        print "The updated stock:"
        print updated_stock
    else:
        print "wrong operations..."


if __name__ == '__main__':
    main()
