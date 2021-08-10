# How to Python

## Introduction 

Python is one of the most useful programming languages due to its flexibility and speed. Currently, Python programming has become one of the most demanding professional skills. To start with this new languague, we can add our first line of code. 

```python
my_name = "New_student" ## My name
print("Hello and welcome " + my_name + "!") ## Print the result
## Hello and welcome New_student!
```

As you saw previously, the code has two elements. The function or variables and comments. Using *#*, we are telling the computer to ignore that part of a program. So we can say that text written in a program but not run by the computer is called a comment. Another element in our previous code is the *print* function. In Python, the print() function is used to tell a computer to talk. The printed words that appear as a result of the *print* function are referred to as *output* of our program. 

In programming, computers refer to block of text as strings. In Python a string is either surrounded by double quotes or single quotes like "Hello World" or 'Hellor World'.  

Using Python, we can store data for reuse. This is what we called a variable. In this programming laguangue, we assign variables by using the equal sign *=*. Let's see an example

```python
message_string = "Hello there"
# Prints "Hello there"
print(message_string)
```

If the context of a program changes, we can update a variable but perform the same logical process on it. Let's see how to update a variable. 

```python
# Greeting
message_string = "Hello there!!!"
print(message_string)
 
# Farewell
message_string = "Bye! Take care"
print(message_string)
```

When we create a program it is normal to make mistakes. Python refers to mistakes as *errors* and will point to the location where an error ocurred with a *^* character.  When programs throw errors that we didn't expect to encounter we call those *errors bugs*.  Two common errors that we encounter while writing Python are SyntaxError and NameError.

- SyntaxError: Something is wrong with the way our program is written
- NameError: Ocurrs when Python interpreter a sees a word it does not recognize.

In general, computers can understand other types of data. One of the most relevant is *Numbers* and it has multiple ways of storing numbers. Within this data type, we can fin different types of data.  

1. An integer, or int, is a whole number. It has no decimal point and contains all counting numbers (1, 2, 3, …) as well as their negative counterparts and the number 0

2. A floating-point number, or a float, is a decimal number. It can be used to represent fractional quantities as well as precise measurements.

```python
# Define the release and runtime integer variables below:
release_year = 2009
runtime = 2
# Define the rating_out_of_10 float variable below: 
rating_out_of_10 = 7.6
```

Since we've already stored some numerical variables, we can also performe some calculations using programming language. Python performs addition, substraction, multiplication and division with *+, -, *, /*.

```python
# Prints "500"
print(573 - 74 + 1)
 
# Prints "50"
print(25 * 2)
 
# Prints "2.0"
print(10 / 5)
```
It is important to be careful when dividing by 0. In thi case, Python will raise a *ZeroDivisionError*.

When performing arithmetic operations on variables does not change the variable. Two variables can be added together, divided by 2, and multiplied by a third variable without Python distinguishing between the variables and literals. Let's see an example

```python
coffee_price = 1.50
number_of_coffees = 4
 
print(coffee_price * number_of_coffees) # Prints "6.0"
print(coffee_price) # Prints "1.5"
print(number_of_coffees) # Prints "4"
 
coffee_price = 2.00 # Updating the price 
 
print(coffee_price * number_of_coffees) # Prints "8.0"
print(coffee_price) # Prints "2.0"
print(number_of_coffees) # Prints "4"
```

If we want to work with exponents, Python can also perform this operation. Typing superscript numbers isn't always easy on modern keyboards. To do this opereation, we use te notation "**".

```python
print(2 ** 10) # 2 to the 10th power, or 1024
print(8 ** 2) # 8 squared, or 64
print(9 ** 3) # 9 * 9 * 9, 9 cubed, or 729
print(4 ** 0.5) # We can even perform fractional exponents
```

In Python can also obtained the remainder of a division calculation. This is called "modulo operator". If the number is divisible, then the result of the modulo operator will be 0. 

```python
print(29 % 5) # Prints 4 because 29 / 5 is 5 with a remainder of 4
print(32 % 3) # Prints 2 because 32 / 3 is 10 with a remainder of 2
print(44 % 2) # Modulo by 2 returns 0 for even numbers and 1 for odd numbers
```
The + operator doesn’t just add two numbers, it can also “add” two strings! The process of combining two strings is called string concatenation. Performing string concatenation creates a brand new string. Let's see an example

```python
greeting_text = "Hey there!"
question_text = "How are you doing?"
full_text = greeting_text + question_text
print(full_text) # Prints "Hey there!How are you doing?"

# To solve this, we can use " "

full_text = greeting_text + " " + question_text
print(full_text) # Prints "Hey there! How are you doing?"

# Let's see a new example

birthday_string = "I am "
age = 10
birthday_string_2 = " years old today!"
full_birthday_string = birthday_string + str(age) + birthday_string_2
# We have 2 options: 
print(full_birthday_string) # Prints "I am 10 years old today!"
# or 
print(birthday_string, age, birthday_string_2) # This also prints "I am 10 years old today!"
```
We can update variables using a shorthand called "plus equal".  When we have a number saved in a variable and want to add to the current value of the variable, we can use the += operator.

```python

number_of_miles_hiked = 12
number_of_miles_hiked += 2
print(number_of_miles_hiked) # Prints 14

#We can use this operator with strings

hike_caption = "What an amazing time to walk through nature!"
 
# Almost forgot the hashtags!
hike_caption += " #nofilter"
hike_caption += " #blessed"
```

## Boolean Expressions

When we want to built control flows into our programs, we want to be able to check if somethind is true or not. To do this, we can use boolean expression. These are statements that can either be True or False. Let's check the statement "Today is a weekday". This expression can be True if today is Tuesday, or it can be False if today is Saturday. There are no other options. However, the statement "Friday is the best day of the week" can be true or false depending on personal preferences.

Now that we understand what booleans expressions are, let's learn how to create them in Python. To do this we can use relational operators. The two relational operators we’ll cover first are:

1. Equals: ==
2. Not equals: !=

These operators compare two items and return True or False if they are equal or not. We can create boolean expressions by comparing two values using these operators:

```python
1 == 1     # True
2 != 4     # True
3 == 5     # False
'7' == 7   # False
```
If we write True or False in the code editor, they will appear in a different color than other variables.  This is because these True or False are their own sepcial type: bool. These are the only bool types that we can us in Python. There are several ways to use True or Fals. Let's check some of them. 

```python
# Set a variable equal to a boolean expression
set_to_true = True
set_to_false = False

# another option

bool_one = 5 != 7 
bool_two = 1 + 1 != 2
bool_three = 3 * 3 == 9
```
Booleans are important expression since they are relevant when building blocks of conditional statements.  Let's think about this situation. If it is raining, then bring an umbrella. Can we use a boolean expression here? Yes, we can. Right, "it is raining" is the boolean expression, and this conditional statement is checking to see if it is True. So, we can say if "it is raining" == True then the rest of the conditional statement will be executed and you will bring an umbrella.

This is the form of a conditional statement:  If [it is raining], then [bring an umbrella]

In Python, this conditiona statement looks very similar.

```python
if is_raining:
  print("bring an umbrella")
  
### A new example

user_name = "angela_catlady_87"

if user_name == "Dave":
  print("Get off my computer Dave!")

if user_name == "angela_catlady_87":
  print("I know it is you, Dave! Go away!")
```

Now that we have covered conditional statemetns, it is important to explore in more ways to use boolean expressions. In python, we can use relational operations to evaluate numbers or conditions. The commons are:

1. > greater than
2- >= greater than or equal to
3. < less than
4. <= less than or equal to

We can use them in functions or loops to evaluate if our data meet some conditions or not. We will see more them more often in the future. Now, let's concentrate in relational operations. Let's imagine that we're running a movie streaming platform and we want to check  if our users are over 13 or not. In Python, we can write a condition to evaluate this.

```python
if age <= 13:
  print("Sorry, parental control required")
```

This function will compare the age (as an input) with the condition "<=13". If this is true, then print("Sorry, parental control required"). Let's see more examples.

```python
x = 20
y = 20
if x == y:  
  print("These numbers are the same")

credits = 120
if credits >= 120:
  print("You have enough credits to graduate!")
```
In some cases, we need to check more than one conditional statement. In these cases, we can build a large boolean expression using boolean operators. These operators (also known as logical operators) combine smaller boolean expressions into larger boolean expressions. There are three boolean operators that we will cover: **and**,**or**,**not**. Now, let's use theres operators.

```python
(1 + 1 == 2) and (2 + 2 == 4)   # True
(1 > 9) and (5 != 6)            # False
(1 + 1 == 2) and (2 < 1)        # False 
(0 == 10) and (1 + 1 == 1)      # False

## Using the last example

credits = 120
gpa = 3.4
if credits >= 120 and gpa >= 2:
  print("You meet the requirements to graduate!")
```

Let's check how to se the *or* statement.

```python
True or (3 + 4 == 7)    # True
(1 - 1 == 0) or False   # True
(2 < 0) or True         # True
(3 == 8) or (3 > 4)     # False

## Using the previous example
credits = 118
gpa = 2.
if credits >= 120 or gpa >= 2.0:
  print("You have met at least one of the requirements.")
```

The final boolean operator we will cover is not. This operator is straightforward: when applied to any boolean expression it reverses the boolean value. So if we have a True statement and apply a not operator we get a False statement.

```python
not 1 + 1 == 2  # False
not 7 < 0       # True
```

 Once we start including lots of if statements in a function the code becomes a little cluttered and clunky. Luckily, there are other tools we can use to build control flow. else statements allow us to elegantly describe what we want our code to do when certain conditions are not met. else statements always appear in conjunction with if statements. Consider our waking-up example to see how this works:
 
 ```python
 if weekday:
  print("wake up at 6:30")
else:
  print("sleep in")
  
 ## Using the previous example
 
credits = 120
gpa = 1.9

if (credits >= 120) and (gpa >= 2.0):
  print("You meet the requirements to graduate!")
else:
    print("You do not meet the requirements to graduate.")
 ```

We can use elif statements to control the order we want our program to check each of our conditional statements. First, the if statement is checked, then each elif statement is checked from top to bottom, then finally the else code is executed if none of the previous conditions have been met.

```python
print("Thank you for the donation!")
 
if donation >= 1000:
  print("You've achieved platinum status")
elif donation >= 500:
  print("You've achieved gold donor status")
elif donation >= 100:
  print("You've achieved silver donor status")
else:
  print("You've achieved bronze donor status")
```

## List 

When we work with data, it is important to collect and store datapoints. In Python, a list is one of the many built-in data structures that allows us to do this. Let's imagine that we want to make a list of the heights of students in a class. Noelle is 61 inches tall, Ava is 70 inches, Sam is 67 inches and  Mia is 64 inches. Using Python, we can create a variable called **heights** to store these values. 

```python
# Create a variable called heights to store values.
heights = [61, 70, 67, 64] # A list begins and ends with square brackets [ ]
```

List can contain different data types. Using the last example, instead of storing each student's height, we can create a list that contains their names. We can even combine multiple data types in just one list as well. In general, *List* can contain any data type in Python. For example strings, intergers, booleans and float numbers. Let's check some examples.

```python
names = ["Noelle", "Ava", "Sam", "Mia"]
mixed_list_string_number = ["Noelle", 61]
mixed_list_common = ["Mia", 27, False, 0.5]
empty_list = [] # We can also create an empty list
```

There are internal built-in functions that we can use to create, manipulate, and even delete data from our list. We called them methods. For lists, methods will the form of *list_name*.method(). Some of them will require an input value that will go between the parenthesis of the method(). One of most popular methods is *.append()* and it allows us to add a new element to the end of a list. 

```python
append_example = [ 'This', 'is', 'an', 'example']
append_example.append('list')
print(append_example) # it will print ['This', 'is', 'an', 'example', 'list']

## Let's check a new example

example_list = [1, 2, 3, 4]
example_list.append(5)  #Using Append
print(example_list)

example_list.remove(5) #Using Remove
print(example_list)
```

We can add additional elements using the *+* operator to combine two list (this is aslo known as concatenation). 

```python
items_sold = ["cake", "cookie", "bread"]
items_sold_new = items_sold + ["biscuit", "tart"]
print(items_sold_new)

# A second example
my_list = [1, 2, 3]
my_list + 4 # It will print an error
my_list + [4] # It will print [1,2,3,4]
```

Let's imagine we are interviewing candidates for a job. We will call each candidate in order, represented by a Python list. 

```python
calls = ["Juan", "Zofia", "Amare", "Ezio", "Ananya"]
```


In Python, we call the location of an element in a list its index. Python lists are zero-indexed. This means that the first element in a list has index 0, rather than 1.In this example, the element with index 2 is "Amare". We can select a single element from a list by using square brackets ([]) and the index of the list item. If we wanted to select the third element from the list, we’d use calls[2]:

```python
print(calls[2]) ## The output will be Amare 
```

We can select the last element of a list by using negative index. We can use the index *-1* to select the last item of a list. Let's see the following example.

```python
pancake_recipe = ["eggs", "flour", "butter", "milk", "sugar", "love"]
print(pancake_recipe[-1]) # The ouput will be 'love'

#### A second example

hopping_list = ["eggs", "butter", "milk", "cucumbers", "juice", "cereal"]
last_element = shopping_list[-1]
index5_element = shopping_list[5]
print(last_element) # "cereal"
print(index5_element) # "cereal
```

In list, we can update or modify a value by using the index. To do this, reassing the value using the specific index of the element. 

```python
garden = ["Tomatoes", "Green Beans", "Cauliflower", "Grapes"]
garden[2] = "Strawberries"
print(garden) # it will print ["Tomatoes", "Green Beans", "Strawberries", "Grapes"]
```
