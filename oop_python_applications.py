#|------------------------- OOP Python Applications ----------------------------


#App.1

""" Write a class called BankAccount that has the following:
• A field called name that stores the name of the account holder.
• A field called amount that stores the amount of money in the account.
• A field called interest_rate that stores the account’s interest rate (as a percentage).
• A constructor that just sets the values of the three fields above.
• A method called apply_interest() that takes no arguments and applies the interest to the
account. It should just modify the amount field and not return anything.
Then test the class, by creating a new BankAccount object for a user named Juan De Hattatime who
has $1000 at 3% interest."""

class BankAccount:
    def __init__(self,name,amount,interest_rate):
        self.name=name
        self.amount=amount
        self.interest_rate=interest_rate
    def apply_interest(self):
        self.amount=self.amount*(1+float((self.interest_rate/100)))
account=BankAccount("Juan De Hattatime",1000,3)
account.apply_interest()
print("The amount of money in the account: ",account.amount)
account.interest_rate=2.4 #we modify the interest_rate
account.apply_interest()
print("The amount of money in the account: ",account.amount)

#App.2

""" Write a class called RestaurantCheck. It should have the following:
• Fields called check_number, sales_tax_percent, subtotal, table_number, and server_name
representing an identification for the check, the bill without tax added, the sales tax percentage,
the table number, and the name of the server.
• A constructor that sets the values of all four fields
• A method called calculate_total that takes no arguments (besides self) and returns the total
bill including sales tax.
• A method called print_check that writes to a file called check###.txt, where ### is the check
number and writes information about the check to that file, formatted like below:
Check Number: 443
Sales tax: 6.0%
Subtotal: $23.14
Total: $24.53
Table Number: 17
Server: Sonic the Hedgehog
Test the class by creating a RestaurantCheck object and calling the print_check() method."""

class Restaurant:
    def __init__(self,check_number,sales_tax_percent,subtotal,table_number,server_name):
        self.check_number=check_number
        self.sales_tax_percent=sales_tax_percent
        self.subtotal=subtotal
        self.table_number=table_number
        self.server_name=server_name
    def calculate_total(self):
        self.subtotal=self.subtotal*(1+self.sales_tax_percent/100)
        return self.subtotal
    def print_check(self):
        f=open('check' + str(self.check_number) + '.txt', 'w')
        print("Check Number: ",self.check_number,file=f)
        print("Sales tax: ",self.sales_tax_percent,"%",file=f)
        print("Subtotal: {:.2f}".format(self.subtotal),file=f)
        print("Total: {:.2f}".format(self.calculate_total()),file=f)
        print("Table Number: ",self.table_number,file=f)
        print("Server: ",self.server_name,file=f)
        f.close()
    
client=Restaurant(443,6,23.14,17,"Sonic the Hedgehog")
client.print_check()

#App.3

"""Write a class called Ticket that has the following:
• A field cost for the price of the ticket and a string field time for the start time of the event
(assume times are in 24-hour format, like '18:35')
• A constructor that sets those variables
• A __str__() method that returns a string of the form Ticket(<cost>, <time>), where
<cost> and <time> are replaced with the values of the cost and time fields.
• A method called is_evening_time() that returns True or False, depending on whether the
time falls in the range from 18:00 to 23:59.
• A method called bulk_discount() that takes an integer n and returns the discount for buying n
tickets. There should be a 10% discount for buying 5 to 9 tickets, and a 20% discount for buying
10 or more. Otherwise, there is no discount. Return these percentages as integers"""

class Ticket:
    def __init__(self,price,time):
        self.price=price
        self.time=time
    def __str__(self):
        return 'Ticket(' + str(self.price) + ', ' + str(self.time) + ')'
    def is_evening_time(self):
        if 18<=self.time<=23:
            return True
        else:
            return False
    def bulk_discount(self,n):
        if n<5:
            return self.price*5
        elif 5<=n<=9:
            return n*self.price*9/10
        else:
            return n*self.price*4/5

#App.4

"""        
Write a class called MovieTicket that inherits from the Ticket class of the previous problem. It
should have the following (in addition to all that it gets from the Ticket class):
• A string field called movie_name
• A constructor that sets movie_name as well as cost and time
• Override the __str__() method so that it returns a string of the form MovieTicket(<cost>, <time>, <name<),
where <cost>, <time>, and <name> are replaced with the values of the class’s fields.
• A method called afternoon_discount() that returns a discount of 10 (standing for 10%) if the
ticket time falls in the range from 12:00 to 17:59 and 0 otherwise.
Test the class by creating a MovieTicket item, printing it, and calling the afternoon_discount()
and is_evening_time() methods."""

class Movie(Ticket):
    def __init__(self,price,time,movie_name):
       self.price=price
       self.time=time
       self.movie_name=movie_name
    def __str__(self):
       return 'Ticket(' + str(self.price) + ', ' + str(self.time) + ', ' + str(self.movie_name) + ')' 
    def afternoon_discount(self):
        if 12<=self.time<=18:
            return 10
        else:
            return 0
item1=Ticket(12,19)
print(item1)
print(item1.is_evening_time())
print(item1.bulk_discount(12))
item=Movie(13,19,"Monster")
print(item)
print(item.afternoon_discount())
print(item.is_evening_time())

#|------------------------------------------------------------------------------------------------------------


























