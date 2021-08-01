# Exercise 1 Part 1

#1. First, write two comments with: Your first and last name and a fun fact about yourself
#2. Output your first initial as a block letter. There are a few ways to do this! Press Save to run your program
#3. Output your second initial as a block letter by adding to the print() statements.
#4 .Press Save to run your program.

first_name = 'Hi! I am William Roberts and '
fun_fact = 'I love Harry Potter'
my_initials = ' and my initials are:'

first_initial = '''
W            w
 W    ww    w
  W  w  w  w
   Ww     w
'''

second_initial = '''
R R R R            
R     R  
R    R   
R  R
R   R 
R     R
'''
print(first_name+fun_fact+ my_initials+ first_initial+ second_initial )

# Exercise 1 Part 2
# We’ve decided to pursue the dream of small-business ownership and open up a furniture store called Lovely 
# Loveseats for Neat Suites on Fleet Street. With our newfound knowledge of Python programming, we’re going to build a 
# system to help speed up the process of creating receipts for your customers.

lovely_loveseat_description = '''
Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white.
'''
lovely_loveseat_price = 254.00

stylish_settee_description  = '''
Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black.
'''
stylish_settee_price = 180.50

luxurious_lamp_description = '''
Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade.
'''
luxurious_lamp_price = 52.15
sales_tax = 0.088

customer_one_total = 0
customer_one_itemization = ""

customer_one_total += lovely_loveseat_price
customer_one_itemization += lovely_loveseat_description

customer_one_total += luxurious_lamp_price
customer_one_itemization += luxurious_lamp_description

customer_one_tax = customer_one_total*sales_tax

customer_one_total += customer_one_tax

print("Customer One Items:")
print(customer_one_itemization)

print("Customer One Total:")
print(customer_one_total)
