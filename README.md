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

1. (>) greater than
2. (>=) greater than or equal to
3. (<) less than
4. (<=) less than or equal to

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
# First example
garden = ["Tomatoes", "Green Beans", "Cauliflower", "Grapes"]
garden[2] = "Strawberries"
print(garden) # it will print ["Tomatoes", "Green Beans", "Strawberries", "Grapes"]

# Second example
garden_waitlist = ["Jiho","Adam","Sonny","Alisha"]
garden_waitlist[1] = "Calla"
print(garden_waitlist)
garden_waitlist[-1] = "Alex"
print(garden_waitlist)
```

We can also remove elements from our list by using the built-in function *.remove()*. Let's see how to use the function.

```python
# First example
shopping_line = ["Cole", "Kip", "Chris", "Sylvana"]
shopping_line.remove("Chris")
print(shopping_line) # ["Cole", "Kip", "Sylvana"]

# Second example

order_list = ["Celery","Orange Juice","Orange","Flatbread"]
print(order_list)
order_list.remove("Flatbread")
print(order_list)
new_store_order_list = ["Orange", "Apple", "Mango", "Broccoli", "Mango"]
print(new_store_order_list)
new_store_order_list.remove("Mango")
print(new_store_order_list)
new_store_order_list.remove("Onions") # It will print an error. We don't have onions.
```


As we saw previously, list can be filled with number or strings. However, list can contain other lists as well. We will commonly refer to these as two-dimensional lists. Let's see an example. Noelle is 61 inches tall, Ava is 70 inches, Sam is 67 inches and Mia is 64 inches. Previously, we saw that we could create a list representing both Noelle’s name and height:

```python
noelle = ["Noelle", 61]
# We can put several of these lists into one list, such that each entry in the list represents a student and their height:
heights = [["Noelle", 61], ["Ava", 70], ["Sam", 67], ["Mia", 64]]

# Second example
heights = [["Jenny", 61], ["Alexus", 70], ["Sam", 67], ["Grace", 64],["Vik",68]]
ages = [["Aaron",15],["Dhruti",16]]
```

Two-dimensional lists can be accessed using brackets as well. However, instead of providing a single pair of brackets [ ] we will use an additional set for each dimension past the first.

```python
# Using the previous example
noelles_height = heights[0][1] 
print(noelles_height) ## It will print 61

# Second example
class_name_test = [["Jenny",90],["Alexus",85.5],["Sam",83],["Ellie",101.5]]
print(class_name_test)

sams_score = class_name_test[2][1]
print(sams_score)

ellies_score = class_name_test[-1][-1]
print(ellies_score)
```

Using this example, let's imagine that our list stores the student’s favorite hobby and one of them "Jenny" changed her hobby. Let's do that.

```python
class_name_hobbies = [["Jenny", "Breakdancing"], ["Alexus", "Photography"], ["Grace", "Soccer"]] # Original list
# "Jenny" changed their mind and is now more interested in "Meditation".
class_name_hobbies[0][1] = "Meditation"
print(class_name_hobbies) # [["Jenny", "Meditation"], ["Alexus", "Photography"], ["Grace", "Soccer"]]

# Second example
incoming_class = [["Kenny","American",9],["Tanya","Russian",9],["Madison","Indian",7]]
print(incoming_class)
incoming_class[2][2] = 8
print(incoming_class)
incoming_class[-3][-3] = "Ken"
print(incoming_class)
``` 

Now are going to explore additional ways of working with lists. Using built-in functions we can:

1. Add and remove items from a list using a specific index.
2. Create lists with continuous values.
3. Get the length of a list.
4. Select portions of a list (called slicing).
5. Count the number of times that an element appears in a list.
6. Sort a list of items.


The method .insert() allows us to add a new element to a specific index in a list. This method takes two inputs, the index and the element we want to insert. This method can also handle shifting over elements and ca be used with negative indices. Let's see an example

```python
store_line = ["Karla", "Maxium", "Martim", "Isabella"]
store_line.insert(2, "Vikor")
print(store_line)  # The output will be  ['Karla', 'Maxium', 'Vikor', 'Martim', 'Isabella']
``` 
Some important details about this method are:
1. The order and number of the inputs is important. The .insert() method expects two inputs, the first being a numerical index, followed by any value as the second input.
2. When we insert an element into a list, all elements from the specified index and up to the last index are shifted one index to the right. This does not apply to inserting an element to the very end of a list as it will simply add an additional index and no other elements will need to shift. 

Let's see an second example

```python
front_display_list = ["Mango", "Filet Mignon", "Chocolate Milk"] 
front_display_list.insert(0,"Pineapple")
print(front_display_list) # ['Pineapple', 'Mango', 'Filet Mignon', 'Chocolate Milk']
```

Python gives us a method to remove elements from a list as well. This method is quite similar to .insert(). However, the .pop() method takes an optional single input: The index for the element you want to remove. Let's see how it works

```python
# First example
cs_topics = ["Python", "Data Structures", "Balloon Making", "Algorithms", "Clowns 101"]
removed_element = cs_topics.pop() # without index means "remove the last element"
print(cs_topics)
print(removed_element) # ["Python", "Data Structures", "Balloon Making", "Algorithms"]

# Second example
data_science_topics = ["Machine Learning", "SQL", "Pandas", "Algorithms", "Statistics", "Python 3"]
data_science_topics.pop()
print(data_science_topics) # ["Machine Learning", "SQL", "Pandas", "Algorithms", "Statistics"]
data_science_topics.pop(3)
print(data_science_topics) # ['Machine Learning', 'SQL', 'Pandas', 'Statistics']
```

In Python, we can also create a list of consecutive numbers like [0,1,2,3,4,5,6]. Typing out all those numbers is overwhelming. However, Python gives us an easy way of creating these type of lists using a built-in function called *range()*. This function takes a single input and generates numbers starting at 0 and ending at the number before the input. Let's see an example:

```python
# First example
my_range = range(10)
print(my_range) # It will print range(0, 10)
print(list(my_range)) # It will print [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Second example
zero_to_seven = range(8)
print(list(zero_to_seven)) # [0, 1, 2, 3, 4, 5, 6, 7]
``` 
If we use this same method but with two inputs, we cancreate a list that starts at a different number. For example, range(2,9) would generate numbers starting at 2 and ending at 8.

```python
my_list = range(2, 9)
print(list(my_list)) # It will print [2, 3, 4, 5, 6, 7, 8]
```
If we use a third input our method, we can create a list that "skips" numbers. For example, range(2, 9, 2) will give us a list where each number is 2 greater than the previous number.

```python
my_range2 = range(2, 9, 2)
print(list(my_range2)) # It will print [2, 4, 6, 8]

# Second exaxmple
range_diff_five = range(0,40,5)
print(list(range_diff_five)) # It will print [0, 5, 10, 15, 20, 25, 30, 35]
```

Sometimes, we need to find the number of times in a list. We can do this by using the .len() method.

```python
# First example
my_list = [1, 2, 3, 4, 5]
print(len(my_list)) # It will print 5

# Second example

long_list = [1, 5, 6, 7, -23, 69.5, True, "very", "long", "list", "that", "keeps", "going.", "Let's", "practice", "getting", "the", "length"]
range_list = range(2, 3000, 10)

long_list_len = len(long_list)
print(long_list_len) # It will print 18

range_list_length = len(range_list)
print(range_list_length) # It will print 300

range_list = range(2, 3000, 100)
range_list_length = len(range_list)
print(range_list_length) # It will print 30
```

If we want to extract only a portion of a lists. We can use the following sintax table[start:end]. 
```python
# First example
letters = ["a", "b", "c", "d", "e", "f", "g"]
sliced_list = letters[1:6]
print(sliced_list) # It will print ["b", "c", "d", "e", "f"]

# Second Example
suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]
beginning = suitcase[0:4]

print(beginning) # It will print ['shirt', 'shirt', 'pants', 'pants']
beginning = suitcase[0:2]
print(beginning) # ['shirt', 'shirt']
middle = suitcase[2:4]
print(middle) # ['pants', 'pants']
```

Slicing syntax in Python is very flexible. Let’s look at a few more problems we can tackle with slicing. Let's see some examples

```python
# First example

# fruits = ["apple", "cherry", "pineapple", "orange", "mango"]
# If we want to select the first n elements of a list, we could use the following code:

fruits[:n]
print(fruits[:3]) # Would output ['apple', 'cherry', 'pineapple']

# We can do something similar when we want to slice the last n elements in a list:
# fruits[-n:] For our fruits list, suppose we wanted to slice the last two elements.

print(fruits[-2:]) # Would output ['orange', 'mango']

# Negative indices can also accomplish taking all but n last elements of a list.
# fruits[:-n]
print(fruits[:-1]) # Would output ['apple', 'cherry', 'pineapple', 'orange']

# Second example

suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]

last_two_elements = suitcase[-2:]
print(last_two_elements)

slice_off_last_three = suitcase[:-3]
print(slice_off_last_three)
```

If we want to count occurrences of an item in a list. We can use the .count() method. Let's see how it works.

```python
letters = ["m", "i", "s", "s", "i", "s", "s", "i", "p", "p", "i"]
num_i = letters.count("i")
print(num_i) # Would output 4

```
We can also use this function to count elements in a two-dimensional list. 

```python
# First example
number_collection = [[100, 200], [100, 200], [475, 29], [34, 34]]
num_pairs = number_collection.count([100, 200])
print(num_pairs) # Would output 2

# Second examle
votes = ["Jake", "Jake", "Laurie", "Laurie", "Laurie", "Jake", "Jake", "Jake", "Laurie", "Cassie", "Cassie", "Jake", "Jake", "Cassie", "Laurie", "Cassie", "Jake", "Jake", "Cassie", "Laurie"]
jake_votes = votes.count("Jake")
print(jake_votes) # Would output 9
```
Often, we will want to sort a list in either numerical (1, 2, 3, …) or alphabetical (a, b, c, …) order. We can sort a list using the method .sort().

```python
# First example
names = ["Xander", "Buffy", "Angel", "Willow", "Giles"]
names.sort()
print(names) # ['Angel', 'Buffy', 'Giles', 'Willow', 'Xander']

names.sort(reverse=True)
print(names) # ['Xander', 'Willow', 'Giles', 'Buffy', 'Angel']
``` 

A second way of sorting a list in Python is to use the built-in function sorted(). The sorted() function is different from the .sort() method in two ways:

1. It comes before a list, instead of after as all built-in functions do.
2. It generates a new list rather than modifying the one that already exists.

```python
# First example
names = ["Xander", "Buffy", "Angel", "Willow", "Giles"]
sorted_names = sorted(names)
print(sorted_names) # Would output ['Angel', 'Buffy', 'Giles', 'Willow', 'Xander']

# Note that using sorted did not change names:
print(names) # Would output ['Xander', 'Buffy', 'Angel', 'Willow', 'Giles']

# Second example
games = ["Portal", "Minecraft", "Pacman", "Tetris", "The Sims", "Pokemon"]
games_sorted = sorted(games)
print(games) # Would output ['Portal', 'Minecraft', 'Pacman', 'Tetris', 'The Sims', 'Pokemon']
print(games_sorted) # Would output ['Minecraft', 'Pacman', 'Pokemon', 'Portal', 'Tetris', 'The Sims']
```

## Loops 

In programming, the process of using an initialization, repetitions, and an ending condition is called a loop. In a loop, we perform a process of iteration (repeating tasks.
Using Python there two types of iteration.

- Indefinite iteration, where the number of times the loop is executed depends on how many times a condition is met.
- Definite iteration, where the number of times the loop will be executed is defined in advance (usually based on the collection size).

In this section, we’ll learn how to use Python to implement both definite and indefinite iteration in our own programs.

Let's imagine we have a list of ingredients and we want to print out all of them.

```python
ingredients = ["milk", "sugar", "vanilla extract", "dough", "chocolate"]
#If we only use print(), our program might look like this:

print(ingredients[0])
print(ingredients[1])
print(ingredients[2])
print(ingredients[3])
print(ingredients[4])
```

This process is managable when we write 5 or 10 print() statements. However, let's imagine that our list has 100,000 elements. It would take an extremely long time and by the end, we could still end up with inconsistencies and mistakes. To do this, we can use loops. 

Let’s start with your first type of loop, a for loop, a type of definite iteration. In our examples, we will be using Python lists as our collection of elements.
With for loops, on each iteration, we will be able to perform an action on each element of the collection. Before we work with any collection, let’s examine the general structure of a for loop:

```python
for <temporary variable> in <collection>:
  <action>
Let’s break down each of these components:
```

A for keyword indicates the start of a for loop. A temporary variable that is used to represent the value of the element in the collection the loop is currently on. An in keyword separates the temporary variable from the collection used for iteration. A collection to loop over. In our examples, we will be using a list. An action to do anything on each iteration of the loop. Now, lets use our previous example to create a for loop.
 
```python
ingredients = ["milk", "sugar", "vanilla extract", "dough", "chocolate"]
for ingredient in ingredients:
  print(ingredient)
 
# This code outputs: milk,sugar,vanilla extract,dough, chocolate
```
 
Let's see more examples
 
 ```python
 board_games = ["Settlers of Catan", "Carcassone", "Power Grid", "Agricola", "Scrabble"]
sport_games = ["football", "hockey", "baseball", "cricket"]

for game in board_games:
  print(game)
for sport in sport_games:
  print(sport)
 ````
 
 Sometimes we won't be iterating through a specific list, but rather only want to perform a certain action multiple times. To create a for loop we can use the built-in function range(). Let's see an example
 
```python
six_steps = range(6) 
# six_steps is now a collection with 6 elements:
# 0, 1, 2, 3, 4, 5
```
 We can use the six_steps variable directly in our for loop to perfrom a six-step interation:
 
```python
for temp in range(6):
  print("Learning Loops!")
```

If we want to add additional information, we can use the same variable to track it.
 
```python
for temp in range(6):
  print("Loop is on iteration number " + str(temp + 1))
```

For loops are not the only type of loops we can use. Another type of loop is called a while loop and is a form of indefinite iteration. 
A while loop performs a set of instructions as long as a given condition is true. The structure follows this pattern:
 
```python
while <conditional statement>:
  <action>
Let’s examine this example, where we print the integers 0 through 3:
```
Let's see a simple loop using *while*
   
```python
count = 0
while count <= 3:
  # Loop Body
  print(count)
  count += 1
```
                
Lets analyze this loop: 
                
1. The first variable count is equal to 0. The conditional statement in the while loop is count <= 3, which is true at the initial iteration of the loop. With this the loop body executes. Inside the loop, it is possible to see that we want to increment to count by 1

2. When loop finish the firts iteration, Python returns to the top of the loop and check the condition again. After the first iteration count should be equal to 1. With this, the condition still evaluates to true and to the loop continues.

3. This process continues until the count variable becomes 4. At that point, the condition is false and the loop will stop. 
   
Let’s write a while loop that counts down from 10 to 0(inclusive).
 
```python
countdown = 10;

while countdown >=0:
  print(countdown)
  countdown += -1

print("We have liftoff!")
```
   
A while loop is not only for counting.  We can use this tool to iterate through a list as well.
Lets check an example.

```python
ingredients = ["milk", "sugar", "vanilla extract", "dough", "chocolate"]

length = len(ingredients)
index = 0
 
while index < length:
  print(ingredients[index])
  index += 1

# our final output wouldbe 
# milk
# sugar
# vanilla extract
# dough
# chocolate
```
                     
lets check a new example.

```python
python_topics = ["variables", "control flow", "loops", "modules", "classes"]

#Your code below: 
length = len(python_topics)
index = 0
while index < length:
  print('I am learning about ' + python_topics[index])
  index += 1
```
       
In Python, Loops are very versatile. This programming languague provides a set of control
statements that we can use to get more control.

Let's check an example that we may encounter to see a use case for loop control statements.
If we want to search a list to check if a specific value exists, we can use a if statement to check this.

```
items_on_sale = ["blue shirt", "striped socks", "knit dress", "red headband", "dinosaur onesie"]

for item in items_on_sale:
  if item == "knit dress":
    print("Found it")
```

This code goes through each item in items_on_sale and checks for a match. Once "knit_dress" is found in the list items_on_sale, we don’t need to go through the rest of the items_on_sale list. Unfortunately, our loop will keep running until we reach the end of the list. Using loops, thankfully we can stop iteration from inside the loop 
by using break loop control statement.
   
```python   
items_on_sale = ["blue shirt", "striped socks", "knit dress", "red headband", "dinosaur onesie"]
 
print("Checking the sale list!")
 
for item in items_on_sale:
  print(item)
  if item == "knit dress":
    break
 
print("End of search!")
```
Let's check a new example.
  
```python  
dog_breeds_available_for_adoption = ["french_bulldog", "dalmatian", "shihtzu", "poodle", "collie"]
dog_breed_I_want = "dalmatian"

for dog_breed in dog_breeds_available_for_adoption:
  print(dog_breed)
  if dog_breed == dog_breed_I_want:
    print("They have the dog I want!")
    break
```

In some cases, we don't want to end the loop entirely. What if we only want to skip the current iteration of the loop.
Let's see an list of integers as an example.


```python
big_number_list = [1, 2, -1, 4, -5, 5, 2, -9]
for i in big_number_list:
  if i <= 0:
    continue
  print(i)
           
# this function would output
# 1
# 2
# 4
# 5
# 2           
```
           
In this example, our control statement is paired with a conditional condition (if/elif/else). This is quite common when using this control statement. Additionally, when our loop first encountered an element (-1) that met the conditions of the if statement, it checked the code inside the block and saw the continue. When the loop then encounters a continue statement it immediately skips the current iteration and moves onto the next element in the list (4).The output of the list only printed positive integers in the list because every time our loop entered the if statement and saw the continue statement it simply moved to the next iteration of the list and thus never reached the print statement.

 ```python        
 ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]

for age in ages:
  if age < 21:
    continue
  print(age)  
 ```
If we have lists inside a list, we can use a nested loops. Suppose we are in charge of a science class, that is split into three project teams. Using a for or while loop can be useful here to get each team:

 ```python     
project_teams = [["Ava", "Samantha", "James"], ["Lucille", "Zed"], ["Edgar", "Gabriel"]]
for team in project_teams:
  print(team)

# This function will output
# ["Ava", "Samantha", "James"]
# ["Lucille", "Zed"]
# ["Edgar", "Gabriel"]
 ```
Let's see a second example. In this function, we want to calculate the total sales using a nested loop.
   
```python     
sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]

scoops_sold = 0;

for location in sales_data:
  print(location)
  for element in location:
    scoops_sold += element


print(scoops_sold)
 ```

There is another way we can write loops in our programs. In some cases, we can use append to add elements into a new list. To start, let’s say we had a list of integers and wanted to create a list where each element is doubled. 
 
```python      
numbers = [2, -1, 79, 33, -45]
doubled = []
 
for number in numbers:
  doubled.append(number * 2)
 
print(doubled)   
# This function will output [4, -2, 158, 66, -90]   
 ```
We can write this function in just one line. Let's see how to do this.

```python     
numbers = [2, -1, 79, 33, -45]
doubled = [num * 2 for num in numbers]
print(doubled)   
```

This technique is what we called List Comprehensions. They are very flexible. In fact, we can incorporate a conditional logic if we want.  Suppose we wanted to double only our negative numbers from our previous numbers list.   

```python      
numbers = [2, -1, 79, 33, -45]
only_negative_doubled = []
 
for num in numbers:
  if num < 0: 
    only_negative_doubled.append(num * 2)
 
print(only_negative_doubled)  # would output [-2, -90]
```             

## Introduction to Functions

In some cases, loops are not the most effective way to iterate over a list of elements. Lets imagine we have two different list and we want to iterate or make some changes in both of them. In this, and if they have different elements, we need to create two for loops to carry out all the necessary changes. We can solve this by using functions. 
             
We can describe functions as a convenient way to group our code into reusable blocks. A function can contain a sequence of steps that can be performed repeatedly throughout a program without having to repeat the process of writing the same code again. In this section, we are going to explore the idea of a function by slowly building out a Python program. 
             
To create a function, we need to add some revelent parts. The first one is what we called a function definition. A function definition has three elements. The def keyword that indicates the beginning of a function. Then, the name of the funcion which is pair of parenthesis () that can hold input values known as parameters. Finally, the last element is a colo : to mark the end of the funcion header. Letse see and example: 
             
```python
# Function 1:
def function_name():
  # functions tasks go here    
  
# Example 2:
def directions_to_timesSq():
  print("Walk 4 mins to 34th St Herald Square train station")
  print("Take the Northbound N, Q, R, or W train 1 stop")
  print("Get off the Times Square 42nd Street stop")

```
             
Having defined the name and the input of our function, we can call it by using its name followed by a pair of parentheses and no indentation.        

```python
# To call our function
directions_to_timesSq()
```

In Python, the amount of whitespace tells the computer what is part of a function and what is not part of that function. If we wanted to write another statement outside our function, we would have to unindent the new line. Lets see an example
             
```python  
def trip_welcome():
  # Indented code is part of the function body
  print("Welcome to Tripcademy!") 
  print("Let's get you to your destination.")
 
# Unindented code below is not part of the function body
print("Woah, look at the weather outside! Don't walk, take the train!")
 
trip_welcome()
# The output will be              
# Woah, look at the weather outside! Don't walk, take the train!
# Welcome to Tripcademy!
# Let's get you to your destination.
```
             
Using our previous trip_welcome () function, we can add new features to it. In general, our function does a really good job of welcoming anyone who is travelling to one specific city however it is a bit static if we want to visit a new city. In order for us to make our function a bit more dynamic, we are going to use the concept of function parameters. The parameter allows our function to accept data as an input value.
             
```python   
# Structure         
def my_function(single_parameter)
  # some code
In the context of our trip_welcome() function, it would like this:
# Example
def trip_welcome(destination):
  print("Welcome to Tripcademy!") 
  print("Looks like you're going to " + destination + " today.")

trip_welcome("Times Square")
# The output would be         
# Welcome to Tripcademy!
# Looks like youre going to Times Square today.              
```

Using functions we can pass in more than one input to our functions. Lets write a function that takes in more than on parameters by using commas.
   
```python
# Structure             
 def my_function(parameter1, parameter2, parameter3):
  # Some code
             
# Example
def trip_welcome(origin, destination):
  print("Welcome to Tripcademy")
  print("Looks like you are traveling from " + origin)
  print("And you are heading to " + destination)             
```

In our functions, we can use 3 different types of arguments:

1. Positional arguments: arguments that can be called by their position in the function definition.
2. Keyword arguments: arguments that can be called by their name.
3. Default arguments: arguments that are given default values.

Let’s look at a function called calculate_taxi_price() that allows our users to see how much a taxi would cost to their destination.

```python
def calculate_taxi_price(miles_to_travel, rate, discount):
  print(miles_to_travel * rate - discount )
```
In this example, we are using miles_to_travel is positioned as the first paremeter, rate is positioned as the second parameter, and discount is the third. If we want to call our function, we need to provide the same inputs in the same position. Let's see an example:

```python
def trip_planner(first_destination, second_destination, final_destination="Codecademy HQ"):
  print("Here is what your trip will look like!")
  print("First, we will stop in " + first_destination + ", then " + second_destination + ", and lastly " + final_destination)

trip_planner("France", "Germany", "Denmark")
trip_planner("Denmark", "France", "Germany")
trip_planner(first_destination="Iceland", final_destination="Germany", second_destination="India")
trip_planner("Brooklyn", "Queens")
```

In Python, there are two different categories of functions. So far, we have been using *Defined Functions* that are written by users. There is another category called *Built-in functions* that come built into Python for us to use. There are large number of built-in functions that we can use in our programs. Let's check some of them. 

```python
destination_name = "Venkatanarasimharajuvaripeta"
 
# Built-in function: len()
length_of_destination = len(destination_name)
 
# Built-in function: print()
print(length_of_destination) # the output would be 28
```

Let's see a second example.

```python

tshirt_price = 9.75
shorts_price = 15.50
mug_price = 5.99
poster_price = 2.00

# max price
max_price = max(tshirt_price,shorts_price,mug_price,poster_price)
print(max_price)
# min price
min_price = min(tshirt_price,shorts_price,mug_price,poster_price)
print(min_price)
# round value
rounded_price = round(tshirt_price,1)
print(rounded_price)
```

At this point, we have been using the built-in function *print* to visualize the output of our function. In general, functions can also return a value to the program so that this value can be modified or used later. We use the Python keyword *return* to do this. Let's seen an example

```python
def calculate_exchange_usd(us_dollars, exchange_rate):
  return us_dollars * exchange_rate
 
new_zealand_exchange = calculate_exchange_usd(100, 1.4)
 
print("100 dollars in US currency would give you " + str(new_zealand_exchange) + " New Zealand dollars")
```

In some cases we want to return more than one value from a function. We can return several values by separating them with a comma. Let's take some examples.

```python
def top_tourist_locations_italy():
  first = "Rome"
  second = "Venice"
  third = "Florence"
  return first,second,third

most_popular1,most_popular2,most_popular3  = top_tourist_locations_italy()

print(most_popular1) # would print out Rome
print(most_popular2) # would print out Venice
print(most_popular3) # would print out Florence
```

### Introduction to Strings

In Python, a string is a whole paragraph, sentence or word that we can store as a variable. If we think about the format, a string is a sequence of characters contained within a pair of 'single quotes' or 'double quotes'. In general, a string can be any length and can contain any letters, numbers, symbols, and spaces.

```python
favorite_word = 'Stay Positive'
print(favorite_word) # should print 'Stay Positive'
```
We can select a specific character within our string by using the same idea of list (index) Like any other list, each character in a string has an index. Consider the string:

```python
favorite_fruit = "blueberry"
print(favorite_fruit[1]) # should print l
```

is that the first letter you expected? Notice that the letter at index 1 of "blueberry" isn’t b, it’s l. This is because the indices of a string start at 0. b is located at the zero index. Let's see a second example

```python
my_name = 'Lisa'
first_initial = my_name[0]
```
We can also select entire chunks of characters from a string. We can do this with the following syntax.

```python
string[first_index:last_index]

# Example

first_name = "Rodrigo"
last_name = "Villanueva"
new_account = last_name[:5]
temp_password = last_name[2:6]
```

We can also concatenate, or combine, two existing strings together into a new string. Consider the following two strings, we can create a new string by concatenating them together as follows.

```python
fruit_prefix = "blue"
fruit_suffix = "berries"
favorite_fruit = fruit_prefix + fruit_suffix
print(favorite_fruit)
```

One built-in function that we can use with strings is the *len()* function. This function returns the number of characters in a string. 

```python
favorite_fruit = "blueberry"
length = len(favorite_fruit)
print(length) # should print 9 
```

We can also use negatives indices. These indices count backward from the end of the string. With this, the index [-1] is the last character of the string and the index [-2] is the second last character of the string. 


```python
company_motto = "Copeland's Corporate Company helps you capably cope with the constant cacophony of daily life"

second_to_last = company_motto[-2]
print(second_to_last)

final_word = company_motto[-4:]
print(final_word)
```

In Python, strings are immutable. However, there are different ways to change strings. 

```python
first_name = "Bob"
last_name = "Daily"

#first_name[0] = "R" # should print an error

fixed_first_name = "R" + first_name[1:]
print(fixed_first_name)
```

Sometimes, using strings, we will accidentally add a new string before we wanted to by including the " character. We solve this by introducing escape characters. By adding a backslash in front of the special character we want to escape, \", we can include it in a string.

```python
 favorite_fruit_conversation = "He said, "blueberries are my favorite!""
 # We can solve by using 
 favorite_fruit_conversation = "He said, \"blueberries are my favorite!\""
```

Since we've described strings as lists of elements, we can iterate through a string by using for or while loops. This gives us a lot possibilities of ways we can manipulate and analyze strings. Let's take a look at an example. 

```python
def print_each_letter(word):
  for letter in word:
    print(letter)
    
favorite_color = "blue"
print_each_letter(favorite_color)
# 'b'
# 'l'
# 'u'
# 'e'
```

Using functions, we can explore different approaches. We can iterate through a string we do something with each character. By including conditional statements inside of these iterations, we can start to do some really cool stuff.

```python
# Example 1
favorite_fruit = "blueberry"
counter = 0
for character in favorite_fruit:
  if character == "b":
    counter = counter + 1
print(counter)

# Example 2
def contains(big_string,little_string):
  if little_string in big_string:
    return True
  else:
    return False

# Example 3
def common_letters(string_one,string_two):
  list_words = []
  for i in string_one:
    if (i in string_two) & (i not in list_words):
      list_words.append(i)
  return list_words
```

In Python, there are three built-in functions that we can change the casing of a string. These are .lower(), .upper(), and .title(). Let's check their definitions.

1. lower() returns the string with all lowercase characters.
2. upper() returns the string with all uppercase characters.
3. title() returns the string in title case, which means the first letter of each word is capitalized.

```python
# Example 1
favorite_song = 'SmOoTH'
favorite_song_lowercase = favorite_song.lower()
print(favorite_song_lowercase) # should print 'smooth'

# Example 2

poem_title = "spring storm"
poem_author = "William Carlos Williams"

poem_title_fixed = poem_title.title()
print(poem_title)

poem_author_fixed = poem_author.upper()
print(poem_author_fixed)
```

Another function is *split*. This function takes one argument and return a list of substrings. In some cases, we can provide an argument however it is not always necessary. 
If we provide an argument within the function, we can dictate the character we want our string to be split on. Let's see some examples.


```python
# Example 1
greatest_guitarist = "santana"
print(greatest_guitarist.split('n')) # should print ['sa', 'ta', 'a']

# Example 2
line_one = "The sky has given over"
line_one_words = line_one.split()
print(line_one_words)

# Example 3
authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"
author_names = authors.split(',')
print(author_names)
author_last_names = []
for name in author_names:
  author_last_names.append(name.split()[-1])
print(author_last_names)
```


We can also split strings using escape sequences. Escape sequences are used to indicate that we want to split by something in a string that is not necessarily a character. The two escape sequences we will cover here are "\n" (Newline) and "\t" (Horizontal Tab)

```python
# Example 1
smooth_chorus = \
"""And if you said, "This life ain't good enough."
I would give my world to lift you up
I could change my life to better suit your mood
Because you're so smooth"""
 
chorus_lines = smooth_chorus.split('\n')
 
print(chorus_lines)

# Example 2

spring_storm_text = \
"""The sky has given over 
its bitterness. 
Out of the dark change 
all day long 
rain falls and falls 
as if it would never end. 
Still the snow keeps 
its hold on the ground. 
But water, water 
from a thousand runnels! 
It collects swiftly, 
dappled with black 
cuts a way for itself 
through green ice in the gutters. 
Drop after drop it falls 
from the withered grass-stems 
of the overhanging embankment."""

spring_storm_lines = spring_storm_text.split('\n')
print(spring_storm_lines)
```

With the previous function, we've learned how to break a string. Now, let's learn to put a string together back using the function *join*. This function is essentially the opposite of *split*. Let's see an example

```python
my_munequita = ['My', 'Spanish', 'Harlem', 'Mona', 'Lisa']
print(' '.join(my_munequita))
# => 'My Spanish Harlem Mona Lisa'
```

We can also join a list of strings by using a comma. To do this, we have provide the comma just before the *join* function. Let's how to perform this. 

```python
santana_songs = ['Oye Como Va', 'Smooth', 'Black Magic Woman', 'Samba Pa Ti', 'Maria Maria']
santana_songs_csv = ','.join(santana_songs)
print(santana_songs_csv)
# => 'Oye Como Va,Smooth,Black Magic Woman,Samba Pa Ti,Maria Maria'
```
We can add a new line instead of a comma by just adding \n before the join function

```python
smooth_fifth_verse_lines = ['Well I\'m from the barrio', 'You hear my rhythm on your radio', 'You feel the turning of the world so soft and slow', 'Turning you \'round and \'round']
smooth_fifth_verse = '\n'.join(smooth_fifth_verse_lines)
```

Python provides a great method for cleaning strings: .strip(). Stripping a string removes all whitespace characters from the beginning and end. Consider the following example:

```python
# Example 1
featuring = "           rob thomas                 "
print(featuring.strip()) # => 'rob thomas'

# Example 2
love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms', '           like flowering mines    ','\n' ,'   to conquer me home.    ']

love_maybe_lines_stripped = []
for line in love_maybe_lines:
  love_maybe_lines_stripped.append(line.strip())

love_maybe_full = '\n'.join(love_maybe_lines_stripped)
print(love_maybe_full)
```

Another important function is *replace*. This function takes two arguments and replace all instances of the first argument in a string with the second argument. 

```python
with_spaces = "You got the kind of loving that can be so smooth"
with_underscores = with_spaces.replace(' ', '_')
print(with_underscores) # 'You_got_the_kind_of_loving_that_can_be_so_smooth'

```

There is another string method called *find*. find() takes a string as an argument and searching the string it was run on for that string. It then returns the first index value where that string is located.

```python
# Example 1
print('smooth'.find('t')) # => '4'
print("smooth".find('oo')) # => '2'

# Example 2

god_wills_it_line_one = "The very earth will disown you"
disown_placement = god_wills_it_line_one.find('disown')
print(disown_placement)
```

Python  provides a string method for including variables in strings. This method is format(). This function takes variables as an argument and includes them in the string that it is run on. We can include {} marks as placeholders for where those variables will be imported.

```python
# Example 1
def favorite_song_statement(song, artist):
  return "My favorite song is {} by {}.".format(song, artist)
  
# Example 2
def poem_title_card(title,poet):
  return  "The poem \"{}\" is written by {}.".format(title,poet)

print(poem_title_card("I Hear America Singing", "Walt Whitman"))

# Example 3

def poem_description(publishing_date, author, title, original_work):
  poem_desc = "The poem {title} by {author} was originally published in {original_work} in {publishing_date}.".format(publishing_date = publishing_date , author = author, title = title, original_work = original_work)
  return poem_desc


my_beard_description = poem_description("1974","Shel Silverstein","My Beard","Where the Sidewalk Ends")
print(my_beard_description)
```


### Modules Python Introduction

In this section, we will learn how to use tools other people have built in Python that are not included automatically for you when you install Python. A common concept is modules. A module is a collection of Python declarations intended broadly to be used a tool. Modules are also often referred to as "libraries" or "packages".  Let's see how to call a module in Python

```python
from datetime import datetime # calling a module
current_time = datetime.now() 
print(current_time)
```

Another famous module is *random* which allows us to generate number or select items at random. Let's check how to use this library.

```python
import random

# Create random_list below:
random_list = [random.randint(1,100) for i in range(101)]
# Create randomer_number below:
randomer_number = random.choice(random_list)
# Print randomer_number below:
print(randomer_number)
```
Python defaults to naming the namespace after the module being imported, but sometimes this name could be ambiguous or lengthy. Sometimes, the module’s name could also conflict with an object you have defined within your local namespace. Fortunately, this name can be altered by aliasing using the as keyword:

```python
# Example 1
import module_name as name_you_pick_for_the_module

# Example 2
import codecademylib3_seaborn

# Add your code below:
from matplotlib import pyplot as plt
import random
numbers_a = range(1,13)
numbers_b = random.sample(range(1000), 12)
plt.plot(numbers_a,numbers_b)
plt.show()
```

There is another module called Decimal which helps us to round decimals. This is an example:

```python
# Import Decimal below:
from decimal import Decimal

# Fix the floating point math below:
two_decimal_points = Decimal('0.2') + Decimal('0.69')
print(two_decimal_points)

four_decimal_points = Decimal('0.53') * Decimal('0.65')
print(four_decimal_points)
```

### Dictionaries

Dictionaries allow us to stored data in way that we can associate one value with another. Suppose we want to store the prices of varius item solt at cafe:

1. Avocado Toast is 6 dollars
2. Carrot Juice is 5 dollars
3. Blueberry Muffin is 2 dollars

In Python, we can use a dictionary to store this information. Let's see how it works.

```python
menu = {"avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
```
In general, a dictionary begins and ends with a curly braces { and }. Each item consiste of a key and each key is separated by a comma. When we create dictionary, we can use any type of data. That means we can use strings, lists, integers or even another dictionary as the value associated with a key. We can also mix and match key and value types. For example:
 For example.

```python
students_in_classes = {"software design": ["Aaron", "Delila", "Samson"], "cartography": ["Christopher", "Juan", "Marco"], "philosophy": ["Frederica", "Manuel"]}
subtotal_to_total = {20: 24, 10: 12, 5: 6, 15: 18}
person = {"name": "Shuri", "age": 18, "family": ["T'Chaka", "Ramonda"]}
```
When using dictionaries, we can use lists as value of an item. However, we cannot use a list as keys of the dictionary. If we try to, we will get an TypeError. 

```python
children = {"von Trapp":["Johannes", "Rosmarie", "Eleonore"], "Corleone":["Sonny", "Fredo", "Michael"]}
print(children)
```
We can add a single key by using the following syntax dictionary[key] = value. Let's see how add a new value

```python
# Example 1
menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
menu["cheesecake"] = 8

# Example 2

animals_in_zoo = {}
animals_in_zoo['zebras'] = 8
animals_in_zoo['monkeys'] = 12
animals_in_zoo['dinosaurs'] = 0
print(animals_in_zoo)
```
In we wanted to add multiple "key:value" pairs to a dictionary, we can use the .update method. 

```python
# Example 1
sensors = {"living room": 21, "kitchen": 23, "bedroom": 20}
sensors.update({"pantry": 22, "guest room": 25, "patio": 34})

# Example 2
user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}
user_ids.update({"theLooper":138475,"stringQueen":85739})
print(user_ids)
```

Imagine we have two list that we want to combine into a dictionary. We can do this by using the zip function. Here is an example.

```python
# Example 1
names = ['Jenny', 'Alexus', 'Sam', 'Grace']
heights = [61, 70, 67, 64]

students = {key:value for key, value in zip(names, heights)}
#students is now {'Jenny': 61, 'Alexus': 70, 'Sam': 67, 'Grace': 64}

# Example 2
drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]
zipped_drinks = zip(drinks,caffeine)
drinks_to_caffeine = {key:value for key,value in zipped_drinks}
print(drinks_to_caffeine)
```

When we have a dictionary, we can access to the values by using the keys. Let's see how print a value from a dictionary.

```python
# Example 1
building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}
building_heights["Burj Khalifa"] # It will print 828

# Example 2
zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}
print(zodiac_elements['earth'])
print(zodiac_elements['fire'])
```

In some case we want to get access to a value that doesn't exist. If this is the case, Python will print an error. However, if we than add the value and we ask again for the same value. We will get it. Check this example:

```python
zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}
print(zodiac_elements["energy"]) # It will print an Error
zodiac_elements['energy'] = "Not a Zodiac element"
print(zodiac_elements["energy"]) # It will print "Not a Zodiac element"
```

We can do the same process by using the function *try* and *KeyError*.

```python
caffeine_level = {"espresso": 64, "chai": 40, "decaf": 0, "drip": 120}
try:
  print(caffeine_level['matcha'])
except KeyError:
  print("Unknown Caffeine Level") # It will print an Error

caffeine_level["matcha"] = 30 # 
try:
  print(caffeine_level['matcha'])
except KeyError:
  print("Unknown Caffeine Level")  # It will print 30   
```

We can access to specific values from a dictionary by using the function *get*. This functions has usually two parameters. The key we're looking for and a default value if that key doesn't exist. 

```python
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}

tc_id = user_ids.get("teraCoder",100000)
print(tc_id) # It wil print 100019

stack_id = user_ids.get("superStackSmash",100000)
print(stack_id) # It will print 100000 since superStackSmash does not exist.
```

If we want to remove a key from the dictionary we can use the *pop* function. Within this function, we need to provide 2 arguments. First of all, the value we want to remove and a default value that the functionl will return if key does not exist. 

```python
raffle = {223842: "Teddy Bear", 872921: "Concert Tickets", 320291: "Gift Basket", 412123: "Necklace", 298787: "Pasta Maker"}

raffle.pop(320291, "No Prize") # It will print "Gift Basket"
print(raffle) # It will print {223842: "Teddy Bear", 872921: "Concert Tickets", 412123: "Necklace", 298787: "Pasta Maker"}

raffle.pop(100000, "No Prize") # It will print "No Prinze
print(raffle)  # It will print {223842: "Teddy Bear", 872921: "Concert Tickets", 412123: "Necklace", 298787: "Pasta Maker"}
```

We can add values using the pop function as well. 

```python
available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
health_points = 20

health_points += available_items.pop("stamina grains", 0)
health_points += available_items.pop("power stew", 0)
health_points += available_items.pop("mystic bread", 0)

print(available_items)
print(health_points)
```

In some cases, when we work with dictionaries we need to get all the keys of values within it. We can perform this by using some built-in functions or for loops. Let's see an example.

```python
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

users = user_ids.keys() # Get the user_ids keys
lessons = num_exercises.keys() # Get the num_exercises keys

print(users)
print(lessons)
```

To obtain the value of each key, we can do something similar by using the *value* function. 

```python
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}
total_exercises = 0

for num in num_exercises.values():
  total_exercises+=num

print(total_exercises)
```

We can get both the keys and the values with the *items* method. Like *keys* and *values*, it returns a dict_list object. Each element of the dict_list returned by *items* is a tuple consisting of:

```python
pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9, "Pharmacist": 58, "Physician": 40, "Lawyer": 37, "Aerospace Engineer": 9}

for position,value in pct_women_in_occupation.items():
  print("Women make up "+ str(value)+" percent of " + position +"s.")
```

Let's see a new example

```python
tarot = { 1:	"The Magician", 2:	"The High Priestess", 3:	"The Empress", 4:	"The Emperor", 5:	"The Hierophant", 6:	"The Lovers", 7:	"The Chariot", 8:	"Strength", 9:	"The Hermit", 10:	"Wheel of Fortune", 11:	"Justice", 12:	"The Hanged Man", 13:	"Death", 14:	"Temperance", 15:	"The Devil", 16:	"The Tower", 17:	"The Star", 18:	"The Moon", 19:	"The Sun", 20:	"Judgement", 21:	"The World", 22: "The Fool"}


spread = {}

spread["past"] = tarot.pop(13)
spread["present"] = tarot.pop(22)
spread["future"] = tarot.pop(10)

for item,value in spread.items():
  print("Your " + item+" is the "+value+" card.")
  
```

## Reading a File

By using Python we can save a lot of time by developing functions that make our work easier. However, in some cases we need to work with files from other sources like excel, notepad or even pdf. In Python we can use some built-in functions to handle these files and then make all the necessary changes. 

We can use the function with to open different files. Let's see an example.

```python
with open('real_cool_document.txt') as cool_doc:
  cool_contents = cool_doc.read()
print(cool_contents)
```

This opens a file object called cool_doc and creates a new indented block where you can read the contents of the opened file. We then read the contents of the file cool_doc using cool_doc.read() and save the resulting string into the variable cool_contents. Then we print cool_contents, which outputs the statement Wowsers!. Let's see a new example

```python
with open('welcome.txt') as text_file:
  text_data = text_file.read()
  print(text_data)
```

We can also save each line of a text file by using a similar function called *readlines*. This function reads text files line by line insted of having the whole thing.

```python
with open('how_many_lines.txt') as lines_doc:
  for line in lines_doc.readlines():
    print(line)
```

If we want to print just the first line of our text, we can use the *readline* function. However, in this case the for loop is not necessary.

```python
with open('just_the_first.txt') as first_line_doc:
  first_line = first_line_doc.readline()
  print(first_line)
```
What if we want to create a file using Python?. Our *open* built-in function needs another argument to open a file to write to. We have add a second argument "W". Additionally, in this case we need the function *write*. The structure of the code is quite similar with previous one. We just need to add this new *write* function.

```python
with open('bad_bands.txt','w') as bad_bands_doc:
  bad_bands_doc.write("bad_bands")
```
We can append strings to a file by using the same *open* function by with a different argument. To do this, we just need to add *a* as a second argument within the *open* function. Let's see an example.

```python
with open('cool_dogs.txt','a') as cool_dogs_file:
  cool_dogs_file.write('Air Buddy')
```

By using the syntax * with * we can open a file and make further modifications, we can just use the open function without adding the syntax *with*. To do this it is necessary to add a new function called *close*. 

```python
fun_cities_file = open('fun_cities.txt', 'a')
# We can now append a line to "fun_cities".
fun_cities_file.write("Montréal")
# But we need to remember to close the file
fun_cities_file.close()
```

#### CSV Files

Text files aren’t the only thing that Python can read, but they’re the only thing that we don’t need any additional parsing library to understand. CSV files are an example of a text file that impose a structure to their data. CSV stands for Comma-Separated Values and CSV files are usually the way that data from spreadsheet software (like Microsoft Excel or Google Sheets) is exported into a portable format. Let's open a CSV file

```python
with open("logger.csv") as log_csv_file:
  print(log_csv_file.read())
```

Even though we can read these lines as text without a problem, there are ways to access the data in a format better suited for programming purposes. In Python we can convert that data into a dictionary using the csv library’s DictReader object. Here’s how we’d create a list of the email addresses of all of the users in the above table:

```python
import csv
 
list_of_email_addresses = []
with open('users.csv', newline='') as users_csv:
  user_reader = csv.DictReader(users_csv)
  for row in user_reader:
    list_of_email_addresses.append(row['Email'])
 ```
Let's see a new example in terms of how to read a csv files and print all the lines using a foor loop. 

```
with open("cool_csv.csv") as cool_csv_file:
  cool_csv_dict = csv.DictReader(cool_csv_file)
  for row in cool_csv_dict:
    print(row['Cool Fact']) 
```

In most cases csv files have delimiters. These are commas, semicolons, spaces or any other different delimiter. These delimiters indicate where the different values start and stop. We can use the same structure to open an read csv files. 

```python
import csv
 
with open('addresses.csv', newline='') as addresses_csv:
  address_reader = csv.DictReader(addresses_csv, delimiter=';')
  for row in address_reader:
    print(row['Address'])
```

Naturally if we have the ability to read different CSV files we might want to be able to programmatically create CSV files that save output and data that someone could load into their spreadsheet software. We can do this by using the writeheader and writerow functions. Let's see how to use them.

```python
big_list = [{'name': 'Fredrick Stein', 'userid': 6712359021, 'is_admin': False}, {'name': 'Wiltmore Denis', 'userid': 2525942, 'is_admin': False}, {'name': 'Greely Plonk', 'userid': 15890235, 'is_admin': False}, {'name': 'Dendris Stulo', 'userid': 572189563, 'is_admin': True}] 
 
import csv
 
with open('output.csv', 'w') as output_csv:
  fields = ['name', 'userid', 'is_admin']
  output_writer = csv.DictWriter(output_csv, fieldnames=fields)
 
  output_writer.writeheader()
  for item in big_list:
    output_writer.writerow(item)
``` 

Let's see a second example.

```python
access_log = [{'time': '08:39:37', 'limit': 844404, 'address': '1.227.124.181'}, {'time': '13:13:35', 'limit': 543871, 'address': '198.51.139.193'}, {'time': '19:40:45', 'limit': 3021, 'address': '172.1.254.208'}, {'time': '18:57:16', 'limit': 67031769, 'address': '172.58.247.219'}, {'time': '21:17:13', 'limit': 9083, 'address': '124.144.20.113'}, {'time': '23:34:17', 'limit': 65913, 'address': '203.236.149.220'}, {'time': '13:58:05', 'limit': 1541474, 'address': '192.52.206.76'}, {'time': '10:52:00', 'limit': 11465607, 'address': '104.47.149.93'}, {'time': '14:56:12', 'limit': 109, 'address': '192.31.185.7'}, {'time': '18:56:35', 'limit': 6207, 'address': '2.228.164.197'}]
fields = ['time', 'address', 'limit']

import csv

with open('logger.csv', 'w') as logger_csv:
  log_writer = csv.DictWriter(logger_csv, fieldnames=fields)
  log_writer.writeheader()
  for line in access_log:
    log_writer.writerow(line)
```

Naturally if we have the ability to read different CSV files we might want to be able to programmatically create CSV files that save output and data that someone could load into their spreadsheet software. Let’s say we have a big list of data that we want to save into a CSV file. We could do the following:

```python
big_list = [{'name': 'Fredrick Stein', 'userid': 6712359021, 'is_admin': False}, {'name': 'Wiltmore Denis', 'userid': 2525942, 'is_admin': False}, {'name': 'Greely Plonk', 'userid': 15890235, 'is_admin': False}, {'name': 'Dendris Stulo', 'userid': 572189563, 'is_admin': True}] 
 
import csv
 
with open('output.csv', 'w') as output_csv:
  fields = ['name', 'userid', 'is_admin']
  output_writer = csv.DictWriter(output_csv, fieldnames=fields)
 
  output_writer.writeheader()
  for item in big_list:
    output_writer.writerow(item)
```

What happend if we want to open a JSON File. We can use Python to do this but first it is importan to defined what is a JSON file. JSON, an abbreviation of JavaScript Object Notation, is a file format inspired by the programming language JavaScript. The name, like CSV is a bit of a misnomer — some JSON is not valid JavaScript (and plenty of JavaScript is not valid JSON). Python comes with a json package that will help us parse JSON files into actual Python dictionaries. Suppose we have a JSON file like the following:

```python
purchase_14781239.json

{
  'user': 'ellen_greg',
  'action': 'purchase',
  'item_id': '14781239',
}
```

if we want to open this file, we can use a function using the same *open* syntax. Let's see how to do this.

```python
import json
with open('purchase_14781239.json') as purchase_json:
  purchase_data = json.load(purchase_json)
 
print(purchase_data['user'])

```
We can do similar operations like converting a dictionary to a JSON file by using the "write" parameter within the *open* function.

```python
import json
 
with open('output.json', 'w') as json_file:
  json.dump(turn_to_json, json_file)
```

Let's see a second exampl

```python
data_payload = [
  {'interesting message': 'What is JSON? A web application\'s little pile of secrets.',
   'follow up': 'But enough talk!'}
]

import json
with open('data.json', 'w') as data_json:
  json.dump(data_payload,data_json)
```

## INTRODUCTION TO CLASSES

### Types

In Python there are different ways to store data. A float is a different kind of number from integer. A boolean is a different value from a string. We can say something similar with list and dict.  Using Python, we can check the *type* of a variable by using the *type()* function. 

```python
print(type(5)) # <class 'int'>

my_dict = {} 
print(type(my_dict)) # <class 'dict'>

my_list = []
print(type(my_list)) # <class 'list'>
```

A class is a template for a data type. It describes the kinds of information that class will hold and how a programmer will interact with that data. To create a *class* we can use a defined structure. A class, can only work if we create an instance of the class. We can defined this as Instantiating. Instantiating a class looks a lot like calling a function.


```python
# Class Structure
class Facade:
  pass

facade_1 = Facade() # creating an instance

```

A class instance is also called an object. The pattern of defining classes and creating objects to represent the responsibilities of a program is known as Object Oriented Programming or OOP. We can check by using the previous function called *type* 

```python
# Using our previous function
class Facade:
  pass

facade_1 = Facade()
facade_1_type = type(facade_1)
print(facade_1_type) # output will be <class '__main__.Facade'>
```
