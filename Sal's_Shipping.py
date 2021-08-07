# Sal runs the biggest shipping company in the tri-county area, Sal’s Shippers. 
# Sal wants to make sure that every single one of his customers has the best, and most affordable experience shipping their packages.
# In this project, you’ll build a program that will take the weight of a package and determine the cheapest way to ship that package using Sal’s Shippers.
# Sal’s Shippers has several different options for a customer to ship their package:
# 1. Ground Shipping, which is a small flat charge plus a rate based on the weight of your package.
# 2. Ground Shipping Premium, which is a much higher flat charge, but you aren’t charged for weight.
# 3. Drone Shipping (new), which has no flat charge, but the rate based on weight is triple the rate of ground shipping.

# Write a shipping.py Python program that asks the user for the weight of their package and then tells them which method of shipping is cheapest 
# and how much it will cost to ship their package using Sal’s Shippers.



print("inputs")
weight = 1.5
cost_ground_premium = 125
price = 0
print("Gound Shipping:")
if weight <= 2:
  price = weight*1.50+20
  print(price)
elif weight > 2 and weight <= 6:
  price = weight*3.0+20
  print(price)
elif weight > 6 and weight <= 10:
  price = weight*4.0+20
  print(price)
else:
  price = weight*4.75+20
  print(price)

print("Ground Shipping Premium:")
print(price + cost_ground_premium)

print("Drone Shipping:")
if weight <= 2:
  price = weight*4.50
  print(price)
elif weight > 2 and weight <= 6:
  price = weight*9.0
  print(price)
elif weight > 6 and weight <= 10:
  price = weight*12.0
  print(price)
else:
  price = weight*14.25
  print(price)
